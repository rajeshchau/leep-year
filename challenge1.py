# finding the leep year by coding logic

# for making the logic we have given :
    # every year that divisible by 4
    # every yera evely divisible by 100
    # year also divisible by 400
# let's start

year =int(input("Enter the year :"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"yes it is a leep year.")
        else:
            print(f"no,it is not a leep year!")
    else:
        print(f"no,it is not a leep year !")
else:
    print(f"no,it is not a leep year !")
