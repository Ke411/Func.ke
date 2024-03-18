def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    
    else:
        return price
    

    original_price = float(input("Enter the original price: Ksh"))
    discount = float(input ("Enter the dicount percentage:"))

    #Calculating the final price using the calculate_discount function
    final_price = calculate_discount("original_price, discount percent")

    #printing the final price
    if final_price != original_price:
        print(f"After a {discount}% discount, the final price is: Ksh{final_price: .2f}")
    else:
        print("No discount applied. The original price remains: Ksh" + str(final_price))
