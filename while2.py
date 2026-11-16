def buying (name , *prices , **options):
    total_price = sum(prices)
    print(f"store's name is: {name}")
    print(f"total price is : {total_price}")
    if 'discount' in options:
        total_price = total_price * (1- options["discount"])
        print (f"total price with discount is : {total_price}")
    elif 'tax' in options:
        total_price = total_price * (1+ options["tax"])
        print(f"total price with tax is : {total_price}")
    return total_price
final = buying('snapp' , 698 , 98 , 3839 ,821 , discount=0)
print(final)
