from openerp.tests.common import TransactionCase
import base64

#set absolute path for your input attachement file
FILE = '/tmp/thingstodo.txt'


class TestS3Interface(TransactionCase):
    """
    Tests Case:  To Check for Unique file name
    1.Create Partner
    2.Check for partner created
    3.Attach new file with newly created partners
    4.Check 2 new record has been created in Attachement
    5.Check 2 related records for attachements are created in
    lookup table with different name.
    6.Check for Unique filename
    """
    def setUp(self):
        super(TestS3Interface, self).setUp()
        self.lookup_model = self.registry('lookup')
        self.attachment_model = self.registry('ir.attachment')
        self.partner_model = self.registry('res.partner')

    def test_programmatic_attachment(self):
        cr, uid = self.cr, self.uid
        # 1.Partner Records Created
        self.registry('res.partner').create(
            cr, uid, {'name': 'test_per_class_teardown_partner'})
        self.registry('res.partner').create(
            cr, uid, {'name': 'test_per_class_teardown_partner_123'})
        # 2.Search for created parnter Records
        res_id1 = self.registry('res.partner').search(
            cr, uid, [('name', '=', 'test_per_class_teardown_partner')])
        self.assertEqual(1, len(res_id1), "Test partner1 not found.")
        res_id2 = self.registry('res.partner').search(
            cr, uid, [('name', '=', 'test_per_class_teardown_partner_123')])
        self.assertEqual(1, len(res_id2), "Test partner2 not found.")
        #Reading File
        f = open(FILE, 'rw')
        data = base64.encodestring(f.read())
        fname = FILE.split('/')[-1]
        # 3.creating record with file data for newly created parnters in
            #ir_attachement
        # Attaching same file to both newly created Partner Records
        self.attachment_model.create(cr, uid, {
            'name': fname,
            'db_datas': data,
            'datas_fname': fname,
            'res_model': 'res.partner',
            'res_id': res_id1[0],
        })
        self.attachment_model.create(cr, uid, {
            'name': fname,
            'db_datas': data,
            'datas_fname': fname,
            'res_model': 'res.partner',
            'res_id': res_id2[0],
        })
        # 4. Check: 2 reacords are created for same file attached to different
            #partners in ir_attachment
        att_id1 = self.attachment_model.search(
            cr, uid, [('res_id', '=', res_id1[0]),
                      ('res_model', '=', 'res.partner'),
                      ('name', '=', fname)])
        self.assertEqual(1, len(att_id1), "Test attachement1 Notefound.")
        att_id2 = self.attachment_model.search(
            cr, uid, [('res_id', '=', res_id2[0]),
                      ('res_model', '=', 'res.partner'),
                      ('name', '=', fname)])
        self.assertEqual(1, len(att_id2), "Test attachement2 Not found.")
        # 5. Check: 2 records with differnt names are created in lookup table
        look_id1 = self.lookup_model.search(
            cr, uid, [('res_id', '=', att_id1[0]),
                      ('model_id', '=', 'ir_attachment')])
        self.assertEqual(1, len(look_id1), "Test Lookup Notefound.")
        look_id2 = self.lookup_model.search(
            cr, uid, [('res_id', '=', att_id2[0]),
                      ('model_id', '=', 'ir_attachment')])
        self.assertEqual(1, len(look_id2), "Test Lookup Not found.")
        # 6. Check for unique file name
        look_data = self.lookup_model.read(
            cr, uid, look_id1, ['en_file_name'])[0]
        look_data1 = self.lookup_model.read(
            cr, uid, look_id2, ['en_file_name'])[0]
        self.assertNotEqual(look_data, look_data1, 'Filename is not unique')
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
