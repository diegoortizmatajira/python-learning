# Python Types and Variables
from fractions import Fraction

confirmation_message = "Your account has been created"
customer_name = "Diego Ortiz"
cart_item_count = 8
item_price = 10.53
item_taxes = 1.3
premium_user = True
sliced_name = customer_name[6:9]
sliced_name_to_end = customer_name[6:]

print("Confirmation message: ", confirmation_message, type(confirmation_message))
print("Customer name: ", customer_name, type(customer_name))
print("Customer name (initial): ", customer_name[0], type(customer_name[0]))
print("Customer name (slice): ", sliced_name, type(sliced_name))
print("Customer name (slice to end): ", sliced_name_to_end, type(sliced_name_to_end))
print("Cart items count", cart_item_count, type(cart_item_count))
print("Item price: ", item_price, type(item_price))
print("User is premium: ", premium_user, type(premium_user))

item_total_price = item_price + item_taxes
print("Total Price: ", item_total_price, type(item_total_price))

fraction1 = Fraction(6, 10)
print("Fraction: ", fraction1, type(fraction1))
fraction2 = Fraction(0.5)
print("Fraction: ", fraction2, type(fraction2))
fraction3 = Fraction(0.33333333333333)
print("Fraction: ", fraction3, type(fraction3))
fraction_sum = fraction1 + fraction2
print("Sum of Fraction1 and Fraction2: ", fraction_sum, type(fraction_sum))
