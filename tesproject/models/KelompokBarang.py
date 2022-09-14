from odoo import api, fields, models


class KelompokBarang(models.Model):
    _name = 'tesproject.kelompokbarang'
    _description = 'New Description'

    name = fields.Selection([
    ('acc', 'Accesoris'), ('komputer', 'Perangkat Komputer'), ('laptop', 'Perangkat Laptop')], string='Nama Kelompok Barang')
    kode_kelompok = fields.Char(string='Kode kelompok Barang')

    @api.onchange('name')
    def _onchange_kode_kelompok(self):
        if (self.name == 'acc'):
            self.kode_kelompok = 'ACC'
        elif (self.name == 'komputer'):
            self.kode_kelompok = 'KOMP'
        elif (self.name == 'laptop'):
            self.kode_kelompok = 'LAPT'

    kode_rak = fields.Char(string='Kode Rak')

    barang_ids = fields.One2many(comodel_name='tesproject.barang',
                                inverse_name='kelompokbarang_id', 
                                string='Daftar Barang')

    jml_item = fields.Char(compute='_compute_jml_item', string='Jml Item')

    @api.depends('barang_ids')
    def _compute_jml_item(self):
        for record in self:
            a = self.env['tesproject.barang'].search([('kelompokbarang_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.jml_item = b
            record.daftar = a
    
    daftar = fields.Char(string='Daftar isi')