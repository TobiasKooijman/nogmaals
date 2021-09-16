# name of student: Tobias Kooijman
# number of student: 99068704
# purpose of program: idfk school ofzo
# function of program: iets met geld
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) # vraagt met een input wat je moet betalen
payed = int(float(input('Payed amount: ')) * 100) # vraagt hoeveel je al hebt betaald met een input
change = payed - toPay # doet de betaald - hetgene wat je nog moet betalen

if change > 0: # als het contant geld groter is dan 0
  coinValue = 50 # maakt de coinvalue 50 als het contant groter is dan 0
  
  while change > 0 and coinValue > 0: # als het contant groter is dan 0 en de coinvalue groter is dan 0
    nrCoins = change // coinValue # 

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # zegt hoeveel coins je terugkrijgt
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # vraagt hoeveel muntjes je terug gaf
      change -= nrCoinsReturned * coinValue #doet de muntjes die je terug gaf X de coinvalue

# comment on code below:  dit zijn de coinvalues
    if coinValue == 50:
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
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')