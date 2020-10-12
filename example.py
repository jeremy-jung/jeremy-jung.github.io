from spike import PrimeHub, LightMatrix, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer

hub = PrimeHub()

hub.status_light.on('blue')
doAWhile = True
while doAWhile:
    hub.light_matrix.off()
    for x in range(0, 4):
        wait_for_seconds(3)
        hub.light_matrix.set_pixel(0, x)
        doAWhile = False