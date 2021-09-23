## Oefening 12
from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
# Jouw python instructies zet je vanaf hier:
for n in range(9):
    robotArm.moveRight()
for n in range(15):
    robotArm.moveLeft()
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        for n in range(9):
            robotArm.moveRight()
    robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()