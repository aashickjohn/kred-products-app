# kred-products-app
Online product purchasing app

1. Clone kred-products-app repo to your local machine.

2. Create your virtual environment inside the kred-products-app folder 
	e.g. python -m venv kred_env.
	
3. Now activate your virtual environment.

4. Now install the dependencies (requirement.txt)
	pip install -r requirement.txt
	
5. Go to kredily folder.
	cd kredily
	
6. Now run django server. and open the url in brower.
	e.g. http://127.0.0.1:8000

7. Use postman to test the following API end points.
	* Customers may exchange their username and password for an authentication token
		login/ 					-	To Login - POST Call
		
			Required:
				{
				"username": [
					"This field is required."
				],
				"password": [
					"This field is required."
				]
				}
	
	
	* Customers may see a paginated list of products. Each product in the list should have the following details: `id`, `name`, `price`, and `quantity in stock`	
		product/				-	To get products list - GET Call
									To add products to the Inventory - POST Call
									
		product/<int:pid>/		-	To check a specific product details from inventory - POST Call
	
	* Customers may see their history of orders.
		history/				-	To see customers history of orders [Login users]. - GET Call
	
	* Customers may order the products they need
	* Number of products in stock should decrease after an order is made
		order/<int:pid>/		-	To place an order - POST Call
	




