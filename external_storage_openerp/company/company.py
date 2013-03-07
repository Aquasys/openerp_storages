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
import boto
import logging
from openerp.tools.translate import _
from ftplib import FTP

class res_company(osv.osv):
    ''' AWS(A3) and FTP credentials store in admin level configuration '''
    _inherit = 'res.company'
    _columns = {
                'aws_access_key_id':fields.char('AWS_ACCESS_KEY_ID',size=128),
                'aws_secret_access_key':fields.char('AWS_SECRET_ACCESS_KEY',size=128),
                'bucket':fields.char('Bucket',size=128),
                'ftp_host':fields.char('FTP Host',size=128),
                'ftp_user':fields.char('FTP User',size=128),
                'ftp_password':fields.char('FTP Password',size=128),
               }

    def test_s3_connection(self, cr, uid, ids, context={}):
        ''' method to test credentials and connection '''
        if not ids:
            return False
        try:
            company_obj = self.browse(cr, uid, ids[0])
            s3 = boto.connect_s3(company_obj.aws_access_key_id, company_obj.aws_secret_access_key)
            bucket = s3.get_bucket(company_obj.bucket)
            logging.info("Connection successful to AWS S3")
        except Exception as detail:
            logging.error(detail)
            raise osv.except_osv(_('Connection unsuccessful'), _('Credential are invalid'))
        raise osv.except_osv(_('Successful'), _('Connection test Sucessful'))
        return True

    def test_ftp_connection(self, cr, uid, ids, context={}):
        '''test connection to ftp server'''
        if not ids:
            return False
        try:
            company_obj = self.browse(cr, uid, ids[0])
            ftp = FTP(company_obj.ftp_host, company_obj.ftp_user, company_obj.ftp_password)       # connect to host, default port
            logging.info("Connection successful to FTP")
        except Exception as detail:
            logging.error(detail)
            raise osv.except_osv(_('Connection unsuccessful'), _('Credential are invalid'))
        raise osv.except_osv(_('Successful'), _('Connection test Sucessful'))
        return True

res_company()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: