## Oefening 8
from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')
# Jouw python instructies zet je vanaf hier:
i=1
while i < 5:
    robotArm.moveRight()
    robotArm.grab()
    for n in range (8):
        for n in range(8):
            robotArm.moveRight()
        robotArm.drop()
        for n in range (8):
            robotArm.moveLeft()
        robotArm.grab()       
        i += 1
        if i == 8:
            break
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()