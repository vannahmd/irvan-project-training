from odoo import api, fields, models

class Person(models.Model):
    _name = 'tesproject.person'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    alamat = fields.Text(string='Alamat')
    tgl_lahir = fields.Datetime(string='Tanggal Lahir')


class Kasir(models.Model):
    _name = 'tesproject.kasir'
    _inherit = 'tesproject.person'
    _description = 'New Description'

    id_kasir = fields.Char(string='ID kasir')


class Teknisi(models.Model):
    _name = 'tesproject.teknisi'
    _inherit = 'tesproject.person'
    _description = 'New Description'

    id_teknisi = fields.Char(string='ID Teknisi')