from odoo import api, models, fields
import random

class ProjectTask(models.Model):
    _inherit = "project.task"

    invoice_number = fields.Many2one(readonly=True, comodel_name="account.move", compute="_generate_invoice")

    @api.depends('sale_line_id')
    def _generate_invoice(self):
        print("kjhkjhkjh")
        for task in self:
            print(task.sale_line_id.invoice_lines.id)
            task.invoice_number = task.sale_line_id.invoice_lines[0].move_id

    @api.model
    def create(self, vals):
        # Checking for the sale orders id and delivery date
        if vals.get('sale_line_id') != False and vals.get('x_studio_delivery_date') != False:
            # Incrementing delivered quantity
            sale_order_line = self.env['sale.order.line'].search([('id', '=', vals.get('sale_line_id'))])
            sale_order_line.write({'qty_delivered': 1.0})

            # Creating the invoice
            sale_order = sale_order_line.order_id
            sale_order._create_invoices(grouped=True)
            
        return super(ProjectTask, self).create(vals)
            

            