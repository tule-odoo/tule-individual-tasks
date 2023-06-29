# TULE - Stansteel & Hotmix: Add total cost to SO line and SO

[Link]([url](https://www.odoo.com/web#id=3362729&menu_id=4722&action=4665&active_id=3362708&model=project.task&view_type=form)) to task

## Steps to complete the dev
- [X] Add dependencies on SALE in __manifest__.py
- [X] Create 2 new computed fields in sale.order.line - product_cost and product-total-cost
- [X] Create 2 new computed fields in sale.order - order_margin and order_total_cost
- [X] Create the compute functions for the costs
- [X] Create the XML view file and use xpath to access specific points in the original form 

## Issues/Blocking Points
- [X] Reading the original XML file and find the appropriate positions for fields

## Topics I need clarification on
- [X] N/A
      
## Interns who helped me
- N/A

## Interns I helped
- N/A
