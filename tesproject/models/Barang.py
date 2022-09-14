from odoo import api, fields, models


class Barang(models.Model):
    _name = 'tesproject.barang'
    _description = 'New Description'

    name = fields.Char(string='Nama Barang')
    harga_beli = fields.Integer(string='Harga Beli', required=True)
    harga_jual = fields.Integer(string='Harga Jual', required=True)
    stok = fields.Integer(string='Stok')

    kelompokbarang_id = fields.Many2one(comodel_name='tesproject.kelompokbarang', 
                                        string='Kelompok Barang',
                                        ondelete='cascade')

    supplier_id = fields.Many2many(comodel_name='tesproject.supplier', 
                                   string='Supplier')
    