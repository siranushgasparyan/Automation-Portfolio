"I have performed automated testing on an e-commerce webpage using Python and Selenium. To create a scalable and maintainable testing framework, I utilized the Page Object Model (POM) and Object-Oriented Programming (OOP) principles."


--------------------------------------------------------------------------------------------------------
-- The login.py file - defines a class named LogIn that inherits from the GeneralHelpers class. It is a Selenium test automation script that logs into a webpage.

The class contains three class-level variables username_input, password_input, and login_button, which represent the HTML elements on the login page that the script interacts with.

The class also contains two variables email and password that store the login credentials of the user.

The login function performs the login process by filling in the username_input and password_input fields with the email and password credentials using the find_and_send_keys method defined in the GeneralHelpers class. Then, it clicks the login_button using the find_and_click method.

If any exception occurs during the login process, the function prints out an error message.


--------------------------------------------------------------------------------------------------------
-- The home.py file - defines a class called HomePage which inherits from a class called GeneralHelpers. This class contains locators for three different elements on a web page: two "add to cart" buttons, a "shopping cart" link, and a "shopping cart" badge. There is also an empty list called items_list and a locator for a list of product titles.

The HomePage class has a method called add_to_cart, which clicks on both "add to cart" buttons and updates the items_list based on the current list of product titles on the page. If the "shopping cart" badge is present, it prints "Added to cart!" and then clicks on the "shopping cart" link to navigate to the shopping cart page. If there is an exception while clicking the "add to cart" buttons, it prints an error message.


--------------------------------------------------------------------------------------------------------
-- The your_card.py file - defines a Python class named YourCart which extends the GeneralHelpers class. This class has various methods that define actions that can be performed on a shopping cart. The class also contains various locators that define the elements on the webpage to be interacted with.

The click_checkout method clicks on the Checkout button, click_continue_shopping method clicks on the Continue Shopping button, and click_remove_button method clicks on the Remove button.

The check_price method checks the total price of the products in the shopping cart by finding the element that contains the price, extracting the price from it, converting it to a floating-point number, and adding it to a list. The function then returns the list of prices.


--------------------------------------------------------------------------------------------------------
-- The checkout_your_info.py file - defines a class called CheckoutPage that inherits from another class called GeneralHelpers. The class includes several class-level attributes that define element locators for web elements that the class interacts with. The fill_checkout_form method is used to fill out a form by sending input data to three different form fields and then clicking a "continue" button. The leave_form_empty method is used to click the "continue" button without filling out the form. The close_the_error method is used to click a "close" button that appears in the event of an error message being displayed. Overall, this code appears to define functionality for interacting with a checkout page on a website.


--------------------------------------------------------------------------------------------------------
--The checkout_overview.py file - defines a class called CheckoutOverviewPage that inherits from a class called GeneralHelpers. The class defines some locators, including XPATHs for elements such as product prices, tax, total, and the finish button.

The class also includes two methods. The first method is called "find_price_num" and is used to find the price of products on the page. This method finds all elements with the locator defined for prices, extracts the text from those elements, and converts the text to a list of numbers (i.e., the price of each product on the page).

The second method is called "click_finish_button" and simply clicks the Finish button. If it fails to find the Finish button, an error message is printed.

--------------------------------------------------------------------------------------------------------
--The checkout_complete.py file - efines a class called CheckoutCompletePage which inherits from a class called GeneralHelpers.

It contains a few locator constants defined using By.XPATH and stored in variables. These locators are used to find specific elements on a web page.

The class has three methods:

click_back_button(): This function clicks the "Back Home" button on the checkout complete page. It uses the find_and_click() function inherited from the GeneralHelpers class to find and click the button.

complete_header: This function returns the text of the complete header element on the page. It uses the find() function inherited from the GeneralHelpers class to find the element and get its text.

page_title: This function returns the text of the page title element on the page. It uses the find() function inherited from the GeneralHelpers class to find the element and get its text.


--------------------------------------------------------------------------------------------------------
The Tests folder contains a set of test scripts that are designed to validate different aspects of the overall logic, login, and checkout flow of a web application. These tests are written in Python using the Pytest framework, and they leverage the Selenium WebDriver to interact with the web application under test.

The tests cover a range of scenarios, including positive and negative test cases, to ensure that the web application is functioning correctly and meets the specified requirements.

--------------------------------------------------------------------------------------------------------
test_login.py - This is a test case that checks if the user is able to login and if they are redirected to the inventory page. The test is marked with @pytest.mark.order(1) which implies that it is the first test that will be executed.

The test starts by navigating to the login page URL specified in the test_data module. Then, it creates an instance of the LogIn class passing in the driver object, and calls the login method to perform the login action.

After the login action is completed, the test waits for the inventory page to load by using the WebDriverWait method from the selenium.webdriver.support.ui module, and checks if the current URL contains the string "inventory.html". If the URL does not contain "inventory.html", the test fails.

--------------------------------------------------------------------------------------------------------
test_add_to_card.py - This test case is for adding products to the cart.

First, it navigates to the login page and logs in using the login() method from the LogIn class. Then, it creates an instance of the HomePage class and uses its add_to_cart() method to add products to the cart.

After that, it creates an instance of the YourCart class and uses its check_price() method to get the prices of the products in the cart. It also checks if the total price of the products in the cart is correct and if the shopping cart badge is visible.

Finally, it checks if the page URL contains the "cart" keyword, indicating that the cart page has been opened.

--------------------------------------------------------------------------------------------------------
test_checkout_form.py - This test case checks if a user can add products to the cart, go to the checkout page, and fill out the checkout form correctly.

The test starts by logging in, adding products to the cart, and clicking the checkout button. Then, it checks if the URL contains "checkout-step-one" and if the user can fill out the checkout form on that page. After filling out the form, it checks if the URL contains "checkout-step-two". If the URL contains "checkout-step-two", the test passes, and if it does not, the test fails.

--------------------------------------------------------------------------------------------------------
test_empty_checkout_form_error.py - The test case aims to check whether an error message appears when the checkout form is left empty. It first opens the login page and logs in, then adds a product to the cart and proceeds to the checkout page. It then leaves the form empty, submits it, and checks whether the expected error message appears. If the error message matches the expected message, the test case passes.

--------------------------------------------------------------------------------------------------------
test_checkout_overview.py - This test case is the fifth in a test suite and checks if the final total price of the products is correct.

The test begins by setting up the webdriver and navigating to the login page. The user logs in, adds products to the cart, and proceeds to checkout. On the checkout overview page, the test retrieves the price of the products, calculates the total price, and compares it to the expected value.

The expected total price is calculated by adding the two product prices and the tax value, which is retrieved from the checkout overview page. If the actual and expected total prices do not match, an assertion error is raised.

--------------------------------------------------------------------------------------------------------
test_complete_checkout.py - This is a test case to check the checkout completion. The test navigates to the login page, logs in, adds products to the cart, proceeds to checkout, fills the checkout form, clicks on the finish button, and checks if the URL contains "checkout-complete". Then it checks if the page header text is "Thank you for your order!" and clicks on the back button. Finally, it checks if the URL contains "inventory.html".

--------------------------------------------------------------------------------------------------------
test_remove_product_from_cart.py - This test case checks the products count in the shopping cart after removing one of them.

The test first navigates to the login page and logs in with the user credentials. Then, it adds two products to the shopping cart and checks if the shopping cart badge is visible and has a value of 2, which corresponds to the number of items added to the cart.

Next, the test clicks on the remove button to remove one of the items and checks if the shopping cart badge value changes to 1, which corresponds to the number of items left in the cart.

--------------------------------------------------------------------------------------------------------
test_check_added_items_titles.py - The test case aims to check whether the titles of the added items in the cart match the titles of the corresponding items in the home page. The test initializes a Chrome driver and navigates to the login page. Then, the test logs in and adds two items to the cart. The test then retrieves the titles of the two items from the home page and the titles of the items from the cart page. Finally, the test checks whether the titles of the added items are the same in both pages.


--------------------------------------------------------------------------------------------------------
The conftest.py file - contains a Pytest fixture that provides a Selenium WebDriver instance with Chrome browser. The fixture uses ChromeDriverManager from the webdriver_manager library to automatically download the appropriate ChromeDriver binary and set it up for use with Selenium.

The fixture also maximizes the browser window when it starts and closes it when the test is complete using the yield statement.

The autouse=True argument specifies that this fixture should be used automatically by any test that requires it.

-----------------------------------------------------------------------------------------------------
In the allure_reports folder you can find allure repogitrts, to generate them you should use "allure serve allure_reports" command in terminal