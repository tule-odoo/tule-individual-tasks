# TULE - Luxer: Copy property from subscription to invoice delivery address

[Link to task](https://www.odoo.com/web#id=3362720&menu_id=4722&cids=3&action=4665&active_id=3362708&model=project.task&view_type=form)

## Steps to complete the dev
- [X] Add dependencies on SALE and PROJECT in __manifest__.py
- [X] Add the Delivery Date on the task page using Studio
- [X] Creat a Many2one field invoice_number field in project.task
- [X] Compute this field based on sale_line_id and the Delivery Date
- [X] Creat a view for it
- [X] Override the CREATE function in project.task to generate a draft invoice and set the delivered quantity to be 1 whenever the task is saved
- [ ] Set sales order to automatically generate tasks  

## Issues/Blocking Points
- [X] Override the CREATE function in project.task
- [X] Connect the invoice_number field to the correct invoice automatically when the invoice is created
- [ ] Set sales order to automatically generate tasks

## Topics I need clarification on
- [X] When can I assign values using self.[field_name] and when should I use self.env.write. When I overrode the create function, self.[field_name] did not work. Was it because the record has not been created, therefore there is no self? Because from my understanding, self is a recordset.
      
## Interns who helped me
- N/A

## Interns I helped
- N/A
