try:
	choice = input("Pick a number between 1 to 10.")
	print(100 / int(choice))

except ValueError as err:
	# if there's an error, run this instead.
	print("No good.  That's not a number!")

except ZeroDivisionError as err2:
	print("You can't divide by zero!")

except Exception as err3:
	print("This is a catch-all for any other kind of error that occurs!")
    
except IndexError as err4:
    print("You can't go over 10.")
finally:
    print("Always have a nice day!")