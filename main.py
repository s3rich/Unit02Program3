print( "RECEIPT" )
print("---------------------")
name1 = input("What is the name of the first item? ") 
price1 = float (input("What is the price of the first item? "))
print()
name2 = input("What is the name of the second item? ")
price2 = float (input("What is the price of the second item? "))
print()
taxRate = float(input("What is the tax rate? "))
print()
print("RECEIPT") 
print( name1 + " \t" + "${:,.2f}".format( price1 ) )
print( name2 + " \t" + "${:,.2f}".format( price2 ) ) 
subtotal = price1 + price2
print( "Subtotal" + " \t" + "${:,.2f}".format( subtotal ) )
tax = subtotal*taxRate
print( "Tax" + " \t\t" + "${:,.2f}".format( tax ) )
total = subtotal + tax
print( "Total" + " \t\t" + "${:,.2f}".format( total ) )