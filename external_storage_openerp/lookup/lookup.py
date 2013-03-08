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

class lookup(osv.osv):
    _name = 'lookup'
    _rec_name = 'file_name'
    _columns = {
                'file_name': fields.char('File Name', size=512),
                'en_file_name': fields.char('Encrypted File Name', size=512),
                'model_id': fields.char('Resource Model',size=256),
                'res_id': fields.integer('Resource ID')
                }
lookup()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: