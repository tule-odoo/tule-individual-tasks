from odoo import api, models, fields

class AccountMove(models.Model):
    _inherit = "account.move"

    property_partner = fields.Many2one(comodel_name="res.partner", store=True, compute="_compute_site_address", readonly=False)

    @api.depends('partner_id')
    def _compute_site_address(self):
        for partner in self: 
            source_orders = partner.line_ids.sale_line_ids.order_id
            if len(source_orders) == 1:
                if source_orders.property_partner and not partner.property_partner:
                    partner.property_partner = source_orders.property_partner
                    return
            partner.property_partner = ""

        