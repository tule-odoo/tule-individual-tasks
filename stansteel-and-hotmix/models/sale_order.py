from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order'

    order_margin = fields.Float(string="Margin", readonly=True, compute="_compute_total_cost")
    order_total_cost = fields.Float(string="Total Cost", readonly=True, compute="_compute_total_cost")

    @api.depends('order_line')
    def _compute_total_cost(self):
        for sale_order in self:
            for order_line in sale_order.order_line:
                sale_order.order_total_cost += order_line.product_total_cost
            sale_order.order_margin = sale_order.amount_total - sale_order.order_total_cost