# FLL 2026 Robot Code

Programs for a LEGO SPIKE Prime robot used for the FIRST LEGO League 2026 missions. The code is written in Python for [Pybricks](https://pybricks.com/), with a color-sensor launcher that selects a mission based on the attachment color.

## What this project does

The main launcher reads the color of the attachment under the color sensor and runs the corresponding mission program:

| Detected color | Mission program |
| --- | --- |
| Green | `Bhagat_Ladybug_Leafcutter_Windowtopast.py` |
| Red | `Advik_Mission.py` |
| Blue | `big_tree_Triangle.py` |
| Black | `RomitHumoungusFungus.py` |
| White | `RomitOldTreeSeed.py` |
| Yellow | `Abhirvey_run.py` |

If no color is detected, the hub displays an icon and waits. The color-detection thresholds and test observations are documented in `color_sensor.txt`.

## Project goals

- Use one consistent drive-base configuration across mission programs.
- Select missions automatically using colored attachments.
- Use gyro-assisted driving for consistent straight paths and turns.
- Keep each mission in its own function for independent testing and tuning.
- Record sensor observations and field adjustments for future runs.

## Hardware configuration

The mission programs use the following standard port layout. Check each program before running it because some experimental programs use different motor directions or ports.

| Port | Device | Typical use |
| --- | --- | --- |
| A | Motor | Right drive motor or attachment motor |
| B | Motor | Left drive motor |
| C | Color Sensor | Attachment/color identification |
| E | Motor | Right-side attachment |
| F | Motor | Left-side attachment |

Common robot dimensions in the programs are:

- Wheel diameter: `56 mm`
- Axle track: `114 mm`
- Gyro-assisted driving: enabled with `robot.use_gyro(True)`

## Main program

Run `Main program for bioglow` on the hub to use automatic color-based mission selection. It imports the mission functions, reads the color sensor on Port C, and launches the matching routine.

The launcher expects the robot and attachment to be positioned consistently before starting. Run each mission independently during testing before using the color-based launcher.

## Program flow

1. Initialize the SPIKE Prime hub and color sensor.
2. Read the attachment color, reflection, and HSV values.
3. Apply additional HSV checks for colors that the sensor may report as `Color.NONE` or `Color.WHITE`.
4. Match the detected color to a mission function.
5. Run the mission routine using the drive motors and attachment motors.

Each mission function creates its own `DriveBase`, enables the gyro, and performs measured movements such as `straight()`, `turn()`, `run()`, or `run_angle()`.

## Running the programs

1. Install Pybricks firmware and the Pybricks Code editor for the SPIKE Prime hub.
2. Open this project in Pybricks Code, or copy the required `.py` files to the hub.
3. Confirm the motor and sensor ports match the physical robot.
4. Place the robot at the mission start position.
5. Reset the hub heading when needed and run the selected program.
6. Test at low speed first, then tune distances, angles, motor directions, and timing for the current field setup.

These programs control real motors and can move the robot immediately. Keep hands, cables, and loose objects clear of the robot during testing.

## Recommended development workflow

1. Test the drive base and confirm both wheels move in the expected direction.
2. Confirm the color sensor returns stable readings for every attachment.
3. Test one mission function at a time without the automatic launcher.
4. Tune distance, angle, speed, acceleration, and attachment timing.
5. Test the complete route repeatedly from the same starting position.
6. Use the automatic launcher only after the selected mission routines work independently.

When tuning a route, change small groups of related values and record the result. This makes it easier to identify whether an error comes from wheel calibration, gyro drift, field placement, or attachment timing.

## File reference

- `Main program for bioglow` — automatic color-based mission launcher.
- `Bhagat_Ladybug_Leafcutter_Windowtopast.py` — Ladybug and Leaf Cutter mission routine.
- `Advik_Mission.py` — Advik mission routine.
- `Advik_Mission_Test.py` — test variant of the Advik routine.
- `big_tree_Triangle.py` — Jungle Tree lift routine and drive-base helpers.
- `RomitHumoungusFungus.py` — Humongous Fungus mission routine.
- `RomitOldTreeSeed.py` — Old Tree Seed mission routine.
- `Abhirvey_run.py` — Abhirvey mission routine.
- `color_senor_code.py` — continuously prints color-sensor readings for calibration.
- `color_sensor.txt` — recorded color and HSV observations.
- `X-box & PS controller code.py` — experimental manual controller using an Xbox-compatible controller.

## Calibration and troubleshooting

- If the robot drives backward, reverse the affected motor direction or swap the motor wiring.
- If turns are inaccurate, verify the wheel diameter and axle track, then recalibrate the gyro and adjust the turn values.
- If attachments are misidentified, run `color_senor_code.py` and compare readings with `color_sensor.txt`.
- Black and some brown/no-attachment readings may be returned as `Color.NONE`; the launcher uses HSV values to distinguish some cases.
- Lighting, battery level, tire grip, attachment position, and field conditions can change results. Re-test after changing the robot or field setup.

## Known limitations

- The launcher depends on the attachment being positioned consistently over the color sensor.
- Some colors can be confused under different lighting conditions.
- Mission routines use fixed distances, turns, and delays rather than closed-loop position feedback.
- The controller program is experimental and separate from the automatic mission launcher.
- Physical testing on the current robot and competition table is required; a syntax check alone cannot validate robot behavior.

## Project status

This is an actively tuned competition project. Mission programs are independent routines and may require field-specific calibration before a tournament run. There are no software-only automated tests; validation is performed on the physical robot and field.
