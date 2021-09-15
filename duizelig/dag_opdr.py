import time
xy=0
dag = input('kies de dag: ')
day = 0
if dag == "maandag":
    day = 1
if dag == "dinsdag":
    day = 2
if dag == "woensdag":
    day = 3
if dag == "donderdag":
    day = 4
if dag == "vrijdag":
    day = 5
if dag == "zaterdag":
    day = 6
if dag == "zondag":
    day = 7
while xy < 1:
    xy = (xy+1)
    if day >= 1:
        character = "Maandag"
        print(character)
        time.sleep(1)
        if day >= 2:
            print("Dinsdag")
            time.sleep(1)
            if day >= 3:
                print("Woensdag")
                time.sleep(1)
                if day >= 4:
                    print("Donderdag")
                    time.sleep(1)
                    if day >= 5:
                        print("vrijdag")
                        time.sleep(1)
                        if day >= 6:
                            print("Zaterdag")
                            time.sleep(1)
                            if day >= 7:
                                print("Zondag")
                                time.sleep(1)
    else:
        print("This is an unvalid awnser!!")

                    

