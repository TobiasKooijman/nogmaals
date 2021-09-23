#Oefening 10
from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
p=9
# Jouw python instructies zet je vanaf hier:
while p > 0:
    robotArm.grab()
    for n in range(p):
        robotArm.moveRight()
    robotArm.drop()
    for n in range(p - 1):
        robotArm.moveLeft()
    robotArm.grab()
    p= p-2
    if p <= 0:
        robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()