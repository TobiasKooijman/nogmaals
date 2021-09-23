## Oefening 7
from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
i=1
# Jouw python instructies zet je vanaf hier:
while i < 5:
    for n in range(6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    robotArm.moveRight()
    robotArm.moveRight()
    i += 1
    if i == 7:
        break
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
robotArm.speed = 5