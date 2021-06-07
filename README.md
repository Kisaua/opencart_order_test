# opencart_order_test
Test project to create an order from demo opencart shop. 
To make an order we do not use login option. 

In data.json we use ist of products ["product id", "amount"]

We do not check the avaliability of the product on the store. 
In Json file there is all fileds like usermane, etc, we need to POST request of the order. 

run python main.py and it will create and order of two products
id = 46 amount 2 (Sony VAIO)
id = 48 amount 2 (iPod Classic)
at the end you'll recieve confirmation email to adress in data.json file (yourmail@gmail.com) 

