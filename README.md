# Solar System Simulator
---
A basic Solar System Simulator.

## Input

To add objects in the `user_config.yml` file, add the block given below separated by `---` from the previous block:
```yaml
type: "planet"
name: "Earth" # optional
mass: 1.0
position: [1.0, 0.0]
velocity: [0.0, 0.17]
```

* `type:` Type of the object, either `planet` or `sun` for now
* `name:` Custom name of the object. It is optional
* `mass:` Mass of the object in units of Earth's mass.
* `position: [pos_x, pos_y]` Initial X and Y positions of the object in the solar system plane in _AU_ units.
* `velocity: [vel_x, vel_y]` Initial X and Y velocities of the object in the plane in _AU/day_ units.

## Execution

To run the simulation, run the command `make run` in the terminal. To visualize, run the command `make visualize`.

Remember to clean the directory by running `make clean` before running a fresh simulation.

> If you can't be bothered by typing so much everytime, just run `make`. It will do everything for you.

## Output

The outputs for the position and velocities are generated and stored in the `output` folder. The outputs for the visualization is stored in the `output/graphs` folder.