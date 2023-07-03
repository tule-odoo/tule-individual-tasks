from odoo import api, models, fields
import random

class ProjectTask(models.Model):
    _inherit = "project.task"

    invoice_number = fields.Many2one(comodel_name="account.move", readonly=True, compute="_generate_invoice")

    @api.onchange("x_studio_delivery_date")
    def _generate_invoice(self):
        for task in self:
            task.invoice_number = random.randint(0, 100)