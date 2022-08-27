from odoo import fields, api, _, models


class SaleOrderLineInherit(models.Model):
    _inherit = 'sale.order.line'

    taxes_product = fields.Float(string='Taxes product', compute='_total_taxes_product', digits=(16, 4))

    def _total_taxes_product(self):
        self.taxes_product = 0
        for record in self:
            if record.tax_id:
                for line in record.tax_id:
                    record.taxes_product += line.amount
            else:
                record.taxes_product = 0
