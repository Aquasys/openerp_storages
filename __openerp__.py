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
{
    'name': 'External Storage',
    'version': '0.3.1',
    'category': 'Interface',
    'summary': 'AWS S3 and FTP storage for attachment files',
    'description': """
Manage attachments
==================================================

It design for store attachments in external storage
---------------------------------------------------
* Amazone web service (S3)
* FTP
    """,
    'author': 'Aquasys G.K.',
    'website': 'http://www.aquasys.co.jp/',
    'depends': ['base', 'product', 'document'],
    'data': [
        'attachment/attachment_view.xml',
        'company/company_view.xml',
        'lookup/lookup_view.xml',
        'security/ir.model.access.csv',
        'report/external_storage_reports.xml',
        'wizard/wiz_s3_report_view.xml',
        'wizard/wiz_export_view.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
