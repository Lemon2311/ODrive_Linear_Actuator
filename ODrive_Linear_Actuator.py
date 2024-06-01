import odrive
from odrive.enums import AxisState, ControlMode
import time

def init(odrive):
    odrive.axis0.requested_state = AxisState.CLOSED_LOOP_CONTROL
    return odrive

def setup_velocity_control(odrive):
    odrive.axis0.controller.config.control_mode = ControlMode.VELOCITY_CONTROL
    return odrive

def check_position_delta(odrive, position_delta_margin, delta_time):
    initial_position = odrive.axis0.pos_estimate
    time.sleep(delta_time)
    return abs(odrive.axis0.pos_estimate - initial_position) < position_delta_margin

bounds = {}

def bounds_detection_routine(odrive, delta_time=1):
    
    bound_left = None
    bound_right = None

    vel = 2
    odrive.axis0.controller.input_vel = vel

    while True:

        print(f"pos:{odrive.axis0.pos_estimate};")

        if(bound_right is None and check_position_delta(odrive, 0.1, delta_time)):
            odrive.axis0.controller.input_vel = 0
            bound_right = odrive.axis0.pos_estimate
            odrive.axis0.controller.input_vel = -vel

        if(bound_right is not None and check_position_delta(odrive, 0.1, delta_time)):
            odrive.axis0.controller.input_vel = 0
            bound_left = odrive.axis0.pos_estimate
            print(f"bound_left: {bound_left}; bound_right: {bound_right}")
            bounds[odrive.serial_number] = (bound_left, bound_right)
            print(f"bounds: {bounds}")
            return odrive

def setup_position_control(odrive):
    odrive.axis0.controller.config.control_mode = ControlMode.POSITION_CONTROL
    print("Position control set")
    return odrive

def move_in_procents(odrive, procent_from_start, await_position_reach=True, position_delta_margin=0.1):
    print("Moving in procents...")
    bound_left, bound_right = bounds[odrive.serial_number]
    commanded_position = bound_left + (bound_right - bound_left) * procent_from_start / 100
    odrive.axis0.controller.input_pos = commanded_position
    
    if( not await_position_reach ):
        return commanded_position

    while await_position_reach:
        current_position = odrive.axis0.pos_estimate
        if abs(current_position - commanded_position) < position_delta_margin:
            print(f"commanded_position {commanded_position} reached")
            break

def setup(odrive, bounds_detection_routine_delta_time = 1):
    odrive = bounds_detection_routine(
            setup_velocity_control(
                init(odrive)), bounds_detection_routine_delta_time)
    setup_position_control(odrive)
    return odrive

__all__ = ['odrive', 'setup', 'move_in_procents']
