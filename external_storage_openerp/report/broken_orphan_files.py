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
import time
from openerp.report import report_sxw
import boto


class broken_orphan_files(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(broken_orphan_files, self).__init__(cr, uid, name,
                                                  context=context)
        self.localcontext.update({
            'time': time,
            'get_broken_orphan': self.get_broken_orphan,
            'get_bucket': self.get_bucket
        })

    def get_bucket(self, company_id):
        company_pool = self.pool.get('res.company')
        company_obj = company_pool.browse(self.cr, self.uid, company_id)
        s3 = boto.connect_s3(company_obj.aws_access_key_id,
                             company_obj.aws_secret_access_key)
        bucket = s3.get_bucket(company_obj.bucket)
        return bucket.list()

    def get_broken_orphan(self):
        result = []
        self_pool = self.pool.get('lookup')
        company_id = self.pool.get('res.users').read(self.cr,
                                                self.uid, self.uid, ['id'])
        s3_files = [x.name.encode('utf-8') for x in\
                    self.get_bucket(company_id['id'])]
        lookup_ids = self_pool.search(self.cr, self.uid, [])
        lookup_files = [x.en_file_name for x in self_pool.browse(self.cr,
                                                         self.uid, lookup_ids)]
        for obj in self_pool.browse(self.cr, self.uid, lookup_ids):
            if obj.en_file_name not in s3_files:
                result.append({'type': 'Broken Pipe',
                            'file_name': obj.file_name,
                            'company': obj.company_id and obj.company_id.name,
                            'model': obj.model_id,
                            'field_name': obj.field_name
                            })
        for s3_file in s3_files:
            if s3_file not in lookup_files:
                result.append({'type': 'Orphan',
                               'file_name': s3_file,
                               'company': '',
                               'model': '',
                               'field_name': ''
                               })
        return result

report_sxw.report_sxw('report.broken.orphan.files', 'lookup',
  'openobject-addons/external_storage_openerp/report/broken_orphan_files.rml',
  parser=broken_orphan_files)
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
