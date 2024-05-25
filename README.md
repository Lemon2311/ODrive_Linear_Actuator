# ODrive_Linear_Actuator
This library is meant for controlling Linear Actuators powered by the ODrive controller. This automatically sets the bounds of the linear actuator by checking position change and then the move_in_procents function can be used to move in procents betwen the self established bounds.

**Note:** Library is actively being developed and doesn`t represents a finished product and will be updated as tests progress.

## Use

Import the library into your Python script:

```python
from ODrive_Linear_Actuator import odrive, setup, move_in_procents
```

### Functions

- `odrive`: Is the official python tool used to control a connected ODrive motor controller.
- `setup()`: Runs the automatic bounds detection routine and assignes them to the odrive that was given as argument.
- `move_in_procents()`: Moves the ODrive between the bounds established by running the setup function, in percents.

## Example

Here is a simple example of how to use the library:

```python
from ODrive_Linear_Actuator import odrive, setup, move_in_procents

odrives = [odrive.find_any()] # find all connected odrives and make an array of odrives

odrv0 = setup(odrives[0], 1) # setup first odrive, with automatic bounds detection and position control
# with position check delta time of 1s / checking the position change over the period of 1s

time.sleep(2) # can be used to wait before moving if needed

move_in_procents(odrv0, 12.5, True, 0.01)
# move first odrive to 12.5% of its bounds,
# wait for position to be reached set to True, with 0.01 margin
# wait for position to be reached set to True makes the function wait until the position is reached,
# and then the function returns, and the code continues to execute
# with 0.01 margin makes the function wait until the position is reached with 0.01 margin
```
## 3d models

The 2 Axis Linear Actuator folder contains the 3d models used to compose a 2 axis linear actuator system using a trapezoidal screw and linear bearings on smooth circular slider rods as the drive shafts, being powered by two ODrive S1 and M8325s Motor Kits. The linear bearings, nuts, trapezoidal screw and slider rods and ODrive motor kits are missing from the FullSystemAssembly, and will be included in the short future, as well as stl versions of all the files, the motor mounts for the cornerPieceForXY (cornerPieceXY1WithMotorMount, cornerPieceForXY4withMotorMount) models are sized to fit the ODrive S1 and M8325s Motor Kit.

The All 3d models and variants & etcs folder is basically like a brain dump of most of the files and versions of the components I created while designing the system, and don't necessarily represent working optimal and/or working components.

## Testing

Library is actively tested and on the 2 Axis Linear Actuator System, and will be updated as tests progress.

## License
This project is licensed under the [MIT License](link-to-license).
