## Oefening 9
from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
i=1
# Jouw python instructies zet je vanaf hier:
while i < 5:
    for n in range(3):
        robotArm.moveRight()
    robotArm.grab()
    for n in range(4):
        for n in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for n in range(6):
            robotArm.moveLeft()
        robotArm.grab()
    i += 1
    if i == 7:
        break
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()