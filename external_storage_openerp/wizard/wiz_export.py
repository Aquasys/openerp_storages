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
from openerp.addons.external_storage_openerp import s3_interface
import logging


class wiz_export(osv.osv_memory):
    '''
    Export of attachments existing in openerp
    Useful for initial export of existing database and
    binary fields which are not storing on S3 and requirement to upload some
    docs to export
    '''
    _name = 'wiz.export'
    _rec_name = 'export_to'
    _columns = {
        'export_to': fields.selection([('s3', 'S3'), ('ftp', 'FTP')],
                                      'Export To')
    }
    _defaults = {
        'export_to': lambda *a: 's3'
    }

    def action_external_export(self, cr, uid, ids, context={}):
        '''
        Export to attachment to AWS S3
        '''
        if not ids:
            return False
        for att_id in context['active_ids']:
            attach_pool = self.pool.get('ir.attachment')
            #user_obj = self.pool.get('res.users').browse(cr, uid, uid)
            export_to = self.read(cr, uid, ids and ids[0], ['export_to'])
            if export_to['export_to'] == 's3':
                attach_obj = attach_pool.browse(cr, uid, att_id)
                connection_check = s3_interface.connection_test(
                    cr, attach_pool, att_id, 'db_datas', user=uid,
                    context=context)
                try:
                    if connection_check:
                        s3_interface.s3_set_file(cr, attach_pool, att_id,
                                                 'db_datas',
                                                 attach_obj.db_datas,
                                                 user=uid, context=context)
                    logging.info("Exported Succesfully")
                except Exception as details:
                    logging.error(details)
        return True
wiz_export()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
