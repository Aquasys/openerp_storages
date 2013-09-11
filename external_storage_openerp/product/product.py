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
from openerp import tools


class product_product(osv.osv):
    _inherit = 'product.product'

    def _get_image(self, cr, uid, ids, name, args, context=None):
        result = dict.fromkeys(ids, False)
        for obj in self.browse(cr, uid, ids, context=context):
            result[obj.id] = tools.image_get_resized_images(
                obj.image, avoid_resize_medium=True)
        return result

    def _set_image(self, cr, uid, id, name, value, args, context=None):
        return self.write(cr, uid, [id],
                          {'image': tools.image_resize_image_big(value)},
                          context=context)

    _columns = {
        'image': fields.binary("Image", store='s3',
                               help="This field holds the image used as \
                               image for the product, limited \
                               to 1024x1024px."),
        'image_medium': fields.function(_get_image, fnct_inv=_set_image,
                                        string="Medium-sized image",
                                        type="binary",
                                        multi="_get_image",
                                        help="Medium-sized image of the \
                                        product. It is automatically resized \
                                        as a 128x128px image, with aspect \
                                        ratio preserved, only when the image \
                                        exceeds one of those sizes. Use this \
                                        field in form views or some kanban \
                                        views."),
        'image_small': fields.function(_get_image, fnct_inv=_set_image,
                                       string="Small-sized image",
                                       type="binary", multi="_get_image",
                                       help="Small-sized image of the \
                                       product It is automatically resized \
                                       as a 64x64px image, with aspect ratio \
                                       preserved. Use this field anywhere a \
                                       small image is required."),
    }
product_product()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
