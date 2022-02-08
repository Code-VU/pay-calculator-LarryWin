def calculatePay():
    # Implement your solution in between the two comment blocks
    print("calculating pay")
    # This first line is provided for you
    try:
        sHours = input("Enter Hours: ")
        fHours = float(sHours)
        sRate = input("Enter Rate: ")
        fRate = float(sRate)
        fBaseHours = 40.0
        fOvertimeHours = fHours - fBaseHours
        fOvertimePay = 0
        fBasePay = 0
        if (fOvertimeHours > 0):
            fOvertimePay = fOvertimeHours * 1.5 * fRate
        if (fHours > 40):
            fBasePay = 40 * fRate
        else:
            fBasePay = fHours * fRate
        
        pay = fBasePay + fOvertimePay
        print(round(pay, 1))
    except:
        print('Error, please enter numeric input')

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculatePay()