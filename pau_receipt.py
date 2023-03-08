

def computeNetPrice(price):
    netPrice = price - (price * 0.18)
    return netPrice

customerName = input('Please enter customer name: ')
commodityName = input ('Please enter commodity name: ')
price = int(input('Enter item Price: '))
transactionDate = input('Enter Date: ')
cashierName = input('Enter Cashier name: ')

def printingOut():
    print('*********************Your Receipt******************')
    print('Customer Name: ', customerName)
    print('Net Price: ', computeNetPrice(price))

    print('Transaction Date: ', transactionDate)
    print('Cashier Name: ', cashierName)
    print('Malik and Pauline copyright')
    #print(copyright)
""

