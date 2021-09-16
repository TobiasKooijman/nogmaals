# name of student: Tobias Kooijman
# number of student: 99068704
# purpose of program: idfk school ofzo
# function of program: iets met geld
# structure of program: python

toPay = int(float(input('Amount to pay: '))* 100) # vraagt met een input wat je moet betalen
payed = int(float(input('Payed amount: ')) * 100) # vraagt hoeveel je al hebt betaald met een input
change = payed - toPay # doet de betaald - hetgene wat je nog moet betalen

if change > 0: # als het contant geld groter is dan 0
  coinValue = 500 # maakt de coinvalue 50 als het contant groter is dan 0
  
  while change > 0 and coinValue > 0: # als het contant groter is dan 0 en de coinvalue groter is dan 0
    nrCoins = change // coinValue # deelt change door met coinvalue

    if nrCoins > 0: # als nrCoins groter = als 0
      if coinValue < 200:
        print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # zegt hoeveel coins je terugkrijgt
      else:
        print('return maximal ', nrCoins, ' coins of ', coinValue // 100, ' euros!' )
      if coinValue < 200:
        nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? '))
        change -= nrCoinsReturned * coinValue #doet de muntjes die je terug gaf X de coinvalue
      else:
        nrCoinsReturned = int(input('How many coins of ' + str(coinValue // 100) +  ' euros did you return? ')) # vraagt hoeveel muntjes je terug gaf
        change -= nrCoinsReturned * coinValue

# comment on code below:  dit zijn de coinvalues, en die veranderen elke keer :)
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: # als change groter is dan 0 print hij de text hieronder en anders print hij "done"
  if coinValue > 200:
    print('Change not returned: ', str(change // 100)+' euros')
  else:
    print('Change not returned: ', str(change) + ' cents')
else:
  print("done")





# De code hierboven zorgt voor het programma...