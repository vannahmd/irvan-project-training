from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'New Description'

    is_pelanggan = fields.Boolean(string='Is Pelanggan')
    is_owner = fields.Boolean(string='Is Owner')