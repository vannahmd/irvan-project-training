from odoo import api, fields, models


class Pengajuan(models.Model):
    _name = 'tesproject.pengajuan'
    _description = 'New Description'

    tgl_pengser = fields.Datetime(string='Tanggal Pengajuan', default=fields.Datetime.now())
    kode_pengser = fields.Char(string='Kode Pengajuan')
    name = fields.Char(string='Nama Pelanggan')
    no_telp = fields.Char(string='No Telepon')
    barang = fields.Char(string='Nama Barang')
    keluhan = fields.Text(string='Keluhan')

    # _sql_constraints = [
    #     ('kode_pengser', 'unique (kode_pengser)', 'Kode PengajuanPada training day 18 kali ini, mempelajari tentang lanjutan menggunakan state dan menambahkan fitur wizzard pada report penjualan. Serta menggunakan filter untuk menentukan rentang tanggal pada report penjualan agar dapat terlihat ketika dicetak nantinya.Pada training day 18 kali ini, mempelajari tentang lanjutan menggunakan state dan menambahkan fitur wizzard pada report penjualan. Serta menggunakan filter untuk menentukan rentang tanggal pada report penjualan agar dapat terlihat ketika dicetak nantinya. tidak boleh sama !!!!')
    # ]
    