from odoo import api, fields, models


class InputBarang(models.TransientModel):
    _name = 'tesproject.inputbarang'

    barang_id = fields.Many2one(
        comodel_name='tesproject.barang', 
        string='Nama Barang',
        required=True)

    jumlah = fields.Integer(
        string='Jumlah',
        required=False)

    def button_inputbarang(self):
        for rec in self:
            self.env["tesproject.barang"].search([('id','=', rec.barang_id.id)]).write({'stok' : rec.barang_id.stok + rec.jumlah})
