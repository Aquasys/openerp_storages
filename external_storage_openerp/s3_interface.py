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
'''
To store attachment to Amezone web service
This methods to be call to connect amezone web service S3
This functions should be called from openerp's class binary.
Import this package in fields.py and see the patch
'''
import openerp.tools as tools
from openerp import SUPERUSER_ID
import logging
import boto
from boto.s3.key import Key
import hashlib
import base64


def sha_file_naming(filename):
    ''' Encrypted file name using sha algoritham
    to achive uniqueness of files on AWS S3'''
    sha_object = hashlib.sha256(filename)
    return sha_object.hexdigest()


def s3_set_file(cr, obj, id, name, filename,
                value, user=SUPERUSER_ID, context={}):
    '''Upload file to AWS S3 using boto
    Track log in lookup table for mapping of external
    file name to openerp record'''
    encrypt_filename = ''
    cr.execute('select company_id from res_users where id = %s' %
               (user))
    company_id = cr.fetchall()
    company_id = tools.misc.flatten(company_id)
    cr.execute('select aws_access_key_id,aws_secret_access_key,bucket from \
            res_company where id = %s' % (company_id[0]))
    s3_connection_info = tools.misc.flatten(cr.fetchall())
#    try:
    s3 = boto.connect_s3(s3_connection_info[0], s3_connection_info[1])
    bucket = s3.get_bucket(s3_connection_info[2])
    logging.info("Connection successful to AWS S3")
    k = Key(bucket)
    #Check for existing file in lookup and delete it on AWS S3
    cr.execute("select en_file_name from lookup where model_id='%s' \
            and res_id=%s and company_id=%s and field_name='%s'"%(obj._table,
                                                      id, company_id[0], name))
    file_exist = tools.misc.flatten(cr.fetchall())
    if file_exist:
        k.key = file_exist[0]
        bucket.delete_key(k)
        cr.execute("delete from lookup where en_file_name='%s'"
                   % (file_exist[0]))
    #create file name from it content for unique file name
    encrypt_filename = sha_file_naming(value)
    k.key = encrypt_filename
    k.set_contents_from_string(base64.decodestring(value), encrypt_key=True)
    logging.info("File stored to AWS S3")
#    except Exception as detail:
#        logging.error(detail)

    try:
        query = "insert into lookup (file_name,en_file_name,model_id,res_id,\
        company_id,field_name) values('%s','%s','%s','%s',%s,'%s')"%('',
                         encrypt_filename, obj._table, id, company_id[0], name)
        cr.execute(query)
    except Exception as detail:
        logging.error(detail)
    return encrypt_filename


def s3_get_file(cr, obj, i, name, user=SUPERUSER_ID, context={}, values=[]):
    ''' Download file from AWS S3 '''
    data = ''
    cr.execute('select company_id from res_users where id = %s' %
               (user))
    company_id = cr.fetchall()
    company_id = tools.misc.flatten(company_id)
    try:
        cr.execute('select aws_access_key_id,aws_secret_access_key,bucket from \
        res_company where id = %s' % (company_id[0]))
        s3_connection_info = tools.misc.flatten(cr.fetchall())
        cr.execute("select en_file_name from lookup where res_id=%s and \
        model_id='%s' and company_id=%s and field_name='%s'"%(i,obj._table,
                                                      company_id[0], name))
        encrypt_filename = tools.misc.flatten(cr.fetchall())
    except Exception as detail:
        logging.error(detail)

    try:
        s3 = boto.connect_s3(s3_connection_info[0], s3_connection_info[1])
        bucket = s3.get_bucket(s3_connection_info[2])
        logging.info("Connection successful to AWS S3")
        k = Key(bucket)
        k.key = encrypt_filename[0]
        data = k.get_contents_as_string()
        logging.info("File read from AWS S3")
    except Exception as detail:
        logging.error(detail)

    return data