from odoo import api, models, fields

class SaleOrder(models.Model):
    _inherit = "sale.order"

    property_partner = fields.Many2one(comodel_name="res.partner")
