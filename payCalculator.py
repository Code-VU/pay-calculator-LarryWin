def calculatePay():
    # Implement your solution in between the two comment blocks
    print("calculating pay")
    # This first line is provided for you
    sHours = input("Enter Hours: ")
    sRate = input("Enter Rate: ")
    fHours = int(sHours)
    fRate = int(sRate)
    pay = fHours * fRate
    print(pay)
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculatePay()