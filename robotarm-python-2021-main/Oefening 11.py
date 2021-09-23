## Oefening 11
from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
# Jouw python instructies zet je vanaf hier:
color = robotArm.scan()
## Nou, Nu kan je hem zelf besturen dus je kan het lekker zelf doen!
for n in range(9):
    robotArm.moveRight()
for n in range(9):
    robotArm.moveLeft()
    robotArm.grab()
    robotArm.scan()
    if (color.lower() == "white"):
        robotArm.moveRight()
    robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
robotArm.speed = 5