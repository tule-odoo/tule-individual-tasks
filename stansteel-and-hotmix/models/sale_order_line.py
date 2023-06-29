from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_cost = fields.Float(string="Cost", readonly=True, compute="_compute_cost")
    product_total_cost = fields.Float(string="Ext. Cost", readonly=True, compute="_compute_cost")

    @api.depends('product_id', 'product_uom_qty')
    def _compute_cost(self):
        for product in self:
            product.product_cost = product.product_id.standard_price
            product.product_total_cost = product.product_uom_qty * product.product_cost