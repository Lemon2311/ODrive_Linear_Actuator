from ODrive_Linear_Actuator import odrive, setup, move_in_procents
from odrive.enums import AxisState
import time

odrives = [odrive.find_any()] # find all connected odrives and make an array of odrives

odrv0 = setup(odrives[0], 0.5) # setup first odrive, with automatic bounds detection and position control
# with position check delta time of 0.5s

move_in_procents(odrv0, 50, True, 0.01) # move first odrive to 50% of its bounds,
# wait for position to be reached set to True, with 0.01 margin
# wait for position to be reached set to True makes the function wait until the position is reached,
# and then the function returns, and the code continues to execute
# with 0.01 margin makes the function wait until the position is reached with 0.01 margin

# the fallowing code will execute after the position is reached
# a time.sleep(X) can be added here to make sure the position is reached before
# executing the fallowing code

print(odrv0.axis0.pos_estimate) # odrive position right now in turns
odrv0.axis0.requested_state = AxisState.IDLE # set odrive to idle state
