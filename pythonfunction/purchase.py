# python function to aggregate market items
def purchase():
    
    #list of items purchased in the market with the price
    print('enter your firstitem')
    
    pencil = input()
    print('enter pencil amount')
    pencilamount = float(input())
    print('enter your second item')
    cutlery = input()
    print('enter cutlery amount')
    cutleryamount = float(input())
    print('enter your third item')

    stationery = input()
    print('enter stationery amount')
    stationeryamount = float(input())
    print('these are my purchase items: ' + pencil + ': ' + str(pencilamount) + ' , ' + cutlery + ' : ' + str(cutleryamount) + ' , ' +  stationery + ' : ' + str(stationeryamount))
    
purchase()
