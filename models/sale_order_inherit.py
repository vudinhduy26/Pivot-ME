from odoo import fields, api, models, _


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
