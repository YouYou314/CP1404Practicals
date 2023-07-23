DISCOUNT = 0.9
item_number = int(input("Number of items: "))
total_price = 0
while item_number <= 0:
    print("Invalid numer of the items!")
    item_number = int(input("Number of items: "))
for i in range(int(item_number)):
    item_price = float(input("Price of item: "))
    total_price = total_price + item_price
if total_price > 100:
    total_price = total_price * DISCOUNT
print(f"Total price for {item_number} items is $ {total_price:.2f}")
