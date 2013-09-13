# -*- coding: utf-8 -*-
##########################################################################
# Aquasys G.K.

# Copyright (C) 20012-2013.

#

# This program is free software: you can redistribute it and/or modify

# it under the terms of the GNU Affero General Public License as

# published by the Free Software Foundation, either version 3 of the

# License, or (at your option) any later version.

#

# This program is distributed in the hope that it will be useful,

# but WITHOUT ANY WARRANTY; without even the implied warranty of

# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

# GNU Affero General Public License for more details.

#

# You should have received a copy of the GNU Affero General Public License

# along with this program. If not, see <http://www.gnu.org/licenses/>.
#########################################################################
from openerp.osv import osv, fields
import logging
import boto
from boto.s3.key import Key
#import hashlib
#import base64


class lookup(osv.osv):
    _name = 'lookup'
    _rec_name = 'file_name'
    _columns = {'file_name': fields.char('File Name', size=512),
                'en_file_name': fields.char('Encrypted File Name', size=512),
                'model_id': fields.char('Resource Model', size=256),
                'res_id': fields.integer('Resource ID'),
                'company_id': fields.many2one('res.company', 'Company'),
                'field_name': fields.char('Field Name', size=256),
                }

    #Unlink method to delete the records from Openerp S3 lookup instance
    #and delteing respective records with same file_name from AWS S3 Bucket
    def unlink(self, cr, uid, ids, context=None):
        """
        Unlink Method to delete the record from lookup table and also deleting
        respecive records with same name from AWS S3 bucket
        @param cr: DB Cusrsor
        @param uid: current user id
        @param ids: ids of records we want to delete
        @return: osv.osv.unlink method; Responsible to delete records
                 from lookup instance
        """
        #Connecting to AWS S3 Object
        user_obj = self.pool.get('res.users')
        company_id = user_obj.read(cr, uid, uid, ['company_id'],
                                   context=context)['company_id']
        s3_connection_info = self.pool.get('res.company').read(
            cr, uid, [company_id[0]],
            ['aws_access_key_id', 'aws_secret_access_key', 'bucket'])[0]
        try:
            s3 = boto.connect_s3(s3_connection_info['aws_access_key_id'],
                                 s3_connection_info['aws_secret_access_key'])
            bucket = s3.get_bucket(s3_connection_info['bucket'])
            logging.info("Connection successful to AWS S3 for deleting file")
            k = Key(bucket)
            for r in self.read(cr, uid, ids, ['en_file_name']):
            #Check if OpenERP S3 Lookup filename exist in bucket
                if bucket.get_key(r['en_file_name']):
                    k.key = r['en_file_name']
                    bucket.delete_key(k)
        except Exception as detail:
            logging.error(detail)
        return super(lookup, self).unlink(cr, uid, ids, context=context)
lookup()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
