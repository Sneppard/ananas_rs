Smoketesting of ananas.rs 
Using selenium, tkinter, pytest on Python.

In current form it's doing:
- open main page of online shop ananas.rs
- navigate through menus to Graphic cards page
- check few checkbox filters and sort by price
- get lowest price of sorted items and name of product with lowest price into variables for farther comparison in the cart
- go to lowest price product page
- add this product to cart
- go to cart
- compare variables which we got from graphic cards page with item in the cart

For now it's not making order and not logging in account on this shop. I've decided it's unnecessary to create impact on real business with fake accounts and orders.
