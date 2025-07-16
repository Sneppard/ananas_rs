Smoketesting of ananas.rs 
Using selenium, tkinter, pytest on Python.

In current form it's doing:
- open main page of online shop ananas.rs
- navigate through menus to Graphic cards page
- checking few checkbox filters and sorting by price
- getting lowest price of sorted items and name of product with lowest price into variables for farther comparison in the cart
- going to lowest price product page
- adding this product to cart
- going to cart
- comparing variables which we got from graphic cards page with item in the cart

For now it's not making order and not logging in account on this shop. I've decided it's unnecessary to create impact on real business with fake accounts and orders. Yet, it's possible, ofc.
