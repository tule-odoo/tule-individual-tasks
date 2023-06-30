# TULE - Luxer: Copy property from subscription to invoice delivery address

[Link to task](https://www.odoo.com/web#id=3362726&menu_id=4722&action=4665&active_id=3362708&model=project.task&view_type=form) 

## Steps to complete the dev
- [X] Add dependencies on SALE in __manifest__.py
- [X] Create a Many2one field in sale.order with comodel_name=res.partner
- [X] Create the view for that new field in the sale order quotation page
- [X] Create a computed Many2one field in account.move with comodel_name=res.partner
- [X] Add a compute function for the field in account.move that originally fetch the site address from the related sale order
- [X] Add the view for the new field on the invoice page

## Issues/Blocking Points
- [X] Create a computed field instead of using the related tag because changes in site address on the invoice should not affect the site address on the sale order, and vice versa (unless creating a new invoice)

## Topics I need clarification on
- [X] N/A
      
## Interns who helped me
- N/A

## Interns I helped
- N/A
