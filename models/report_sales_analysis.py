from odoo import fields, models, api, _
from odoo import tools


class ReportSalesAnalysis(models.Model):
    _name = "report.sales.analysis"
    _description = "Sales Analysis Report"
    _auto = False
    _rec_name = 'date'
    _order = 'date desc'

    name = fields.Char('Order Reference', readonly=True)
    date = fields.Datetime('Order Date', readonly=True)
    partner_id = fields.Many2one('res.partner', 'Customer', readonly=True)
    product_id = fields.Many2one('product.product', 'Product Variant', readonly=True)
    qty_delivered = fields.Float('Qty Delivered', readonly=True)
    product_uom_qty = fields.Float('Qty Ordered', readonly=True)
    price_total = fields.Float('Total', readonly=True)
    order_id = fields.Many2one('sale.order', string='Order', readonly=True)
    qty_invoiced = fields.Float('Qty Invoiced', readonly=True)
    total_in_invoiced = fields.Float('Money In Invoiced', readonly=True)
    total_in_paid = fields.Float('Money In Paid', readonly=True)

    def init(self):
        tools.drop_view_if_exists(self.env.cr, 'report_sales_analysis')
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW report_sales_analysis AS (
                SELECT 
                    row_number() OVER () AS id,
                    line.partner_id,
                    line.product_id,
                    line.product_uom_qty,
                    line.price_total,
                    line.order_id,
                    line.qty_invoiced
                    FROM (
                    SELECT 
                        res_partner.id as partner_id,
                        product_product.id as product_id,
                        sale_order_line.product_uom_qty as product_uom_qty,
                        sale_order_line.product_uom_qty*sale_order_line.price_unit as price_total,
                        sale_order.id as order_id,
                        account_move_line.quantity as qty_invoiced
                        FROM sale_order_line
                        LEFT JOIN sale_order_line_invoice_rel ON sale_order_line_invoice_rel.order_line_id = sale_order_line.id
                        LEFT JOIN sale_order ON sale_order.id = sale_order_line.order_id
                        LEFT JOIN res_partner ON res_partner.id = sale_order.partner_id
                        LEFT JOIN product_product ON product_product.id = sale_order_line.product_id
                        LEFT JOIN account_move_line ON account_move_line.id = sale_order_line_invoice_rel.invoice_line_id
                        LEFT JOIN account_move ON account_move.id = account_move_line.move_id
                         
                    ) as line
            )
        """)
