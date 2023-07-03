from odoo import api, models, fields
from odoo.exceptions import ValidationError

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.constrains("product_uom_qty")
    def _verify_product_quantity(self):
        for product in self:
            if product.product_uom_qty != 1:
                raise ValidationError("Tasks are ONLY ordered in quantities of 1")