
# import datetime
import datetime

# 1. create the store inventory
products = {
    "Grip Socks": 20,
    "Size 5 Ball": 30,
    "Barcelona Jersey": 100,
    "Sock Tape": 10,
    "Mercurials Size 9": 200
}

# 2. create an empty shopping cart
shopping_cart = {}


# function to display money with two decimal places
def money(amount):
    amount = round(amount, 2)
    whole_number = int(amount)
    decimal_number = round((amount - whole_number) * 100)

    if decimal_number < 10:
        return "$" + str(whole_number) + ".0" + str(decimal_number)

    return "$" + str(whole_number) + "." + str(decimal_number)


# 3. function to display available products
def display_products(products):

    print("\n========== AVAILABLE PRODUCTS ==========")

    # display products using a for loop
    number = 1

    for name, price in products.items():
        print(str(number) + ". " + name + " - " + money(price))
        number += 1


# function to validate customer selections
def get_valid_choice(prompt, minimum, maximum):

    choice = int(input(prompt))

    while choice < minimum or choice > maximum:
        print("Invalid choice. Please try again.")
        choice = int(input(prompt))

    return choice


# 4. function to add products to the cart
def add_product(products, shopping_cart):

    display_products(products)

    choice = get_valid_choice("Enter product number: ", 1, 5)

    product_names = list(products.keys())
    selected_product = product_names[choice - 1]

    quantity = int(input("How many " + selected_product + " would you like to add? "))

    while quantity <= 0:
        print("Quantity must be greater than 0.")
        quantity = int(input("Enter quantity: "))

    if selected_product in shopping_cart:

        shopping_cart[selected_product] += quantity

    else:

        # add a new product to the cart
        shopping_cart[selected_product] = quantity

    print("Added " + str(quantity) + " " + selected_product + " to your cart!")
    print(selected_product + " quantity is now " + str(shopping_cart[selected_product]) + ".")


# 5. function to remove one unit from the cart
def remove_product(shopping_cart):

    if len(shopping_cart) == 0:
        print("\nYour shopping cart is empty!")
        return

    print("\n========== YOUR SHOPPING CART ==========")

    number = 1

    for name, quantity in shopping_cart.items():
        print(str(number) + ". " + name + " - Quantity: " + str(quantity))
        number += 1

    choice = get_valid_choice(
        "Enter item number to remove: ", 1, len(shopping_cart)
    )

    cart_names = list(shopping_cart.keys())
    selected_product = cart_names[choice - 1]

    shopping_cart[selected_product] -= 1

    print("Removed 1 " + selected_product + " from your cart!")

    if shopping_cart[selected_product] == 0:
        del shopping_cart[selected_product]
        print(selected_product + " has been removed from your cart.")

    else:
        print(selected_product + " quantity is now " + str(shopping_cart[selected_product]) + ".")


# 6. function to calculate the subtotal and total items
def calculate_total(products, shopping_cart):

    subtotal = 0
    total_items = 0

    for name, quantity in shopping_cart.items():

        price = products[name]
        line_total = price * quantity

        subtotal += line_total
        total_items += quantity

    return subtotal, total_items


# 7. function to display the shopping cart
def display_cart(products, shopping_cart):

    if len(shopping_cart) == 0:
        print("\nYour shopping cart is empty!")
        return

    print("\n========== YOUR SHOPPING CART ==========")
    print("Product             Unit Price    Quantity    Line Total")

    for name, quantity in shopping_cart.items():

        price = products[name]
        line_total = price * quantity

        print(name + " - " + money(price) + " - " + str(quantity) + " - " + money(line_total))

    subtotal, total_items = calculate_total(products, shopping_cart)

    print("-----------------------------------------------")
    print("Total Items: " + str(total_items))
    print("Subtotal: " + money(subtotal))


# 8. function to calculate discounts
def calculate_discount(subtotal):

    if subtotal < 10:
        discount_rate = 0

    elif subtotal < 20:
        discount_rate = 0.05

    elif subtotal < 40:
        discount_rate = 0.10

    else:
        discount_rate = 0.15

    amount_saved = round(subtotal * discount_rate, 2)
    final_total = round(subtotal - amount_saved, 2)

    return discount_rate, amount_saved, final_total


# 9. function to print the final receipt
def print_receipt(products, shopping_cart):

    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%m/%d/%Y")

    subtotal, total_items = calculate_total(products, shopping_cart)

    discount_rate, amount_saved, final_total = calculate_discount(subtotal)

    print("\n========== RECEIPT ==========")
    print("Date: " + formatted_date)

    print("\nProduct             Unit Price    Quantity    Line Total")

    for name, quantity in shopping_cart.items():

        price = products[name]
        line_total = price * quantity

        print(name + " - " + money(price) + " - " + str(quantity) + " - " + money(line_total))

    # display receipt totals
    print("-----------------------------------------------")
    print("Total Items: " + str(total_items))
    print("Subtotal: " + money(subtotal))
    print("Discount: " + str(int(discount_rate * 100)) + "%")
    print("Amount Saved: " + money(amount_saved))
    print("Final Total: " + money(final_total))

    print("\nThank you for shopping!")


# 10. main menu
running = True

while running:

    print("\n========== SMART SHOPPING CART ==========")
    print("1. View Available Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Shopping Cart")
    print("5. View Current Total")
    print("6. Checkout")

    choice = get_valid_choice("Enter your choice: ", 1, 6)

    # OPTION 1: view available products
    if choice == 1:
        display_products(products)

    # OPTION 2: add a product
    elif choice == 2:
        add_product(products, shopping_cart)

    # OPTION 3: remove a product
    elif choice == 3:
        remove_product(shopping_cart)

    # OPTION 4: view shopping cart
    elif choice == 4:
        display_cart(products, shopping_cart)

    # OPTION 5: view current total
    elif choice == 5:

        subtotal, total_items = calculate_total(products, shopping_cart)

        print("\nCurrent Subtotal: " + money(subtotal))

    # OPTION 6: checkout
    elif choice == 6:

        if len(shopping_cart) == 0:
            print("\nYour shopping cart is empty!")
            print("Please add products before checking out.")

        else:

            # print receipt
            print_receipt(products, shopping_cart)

            # end the program
            running = False
