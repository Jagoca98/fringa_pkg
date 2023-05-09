# Frontiered Information Gain (fringa)

## Execution

The `robmov.launch` file loads gazebo, the turtlebot3 waffle with corrected transformations, a configured rviz, gmapping, and move_base to allow the robot to move. The move_base configuration files (in the param folder) are modified to allow the robot's laser to consider infinite measurements as valid (THANKS MANUSANCHE FOR SHOWING ME THIS <3). In addition, it runs the terrorist and trajectory nodes, which are responsible for post-processing the exploration.

```bash
roslaunch fringa_pkg robmov.launch
```

By default, it loads `escenario1.world`. To run different maps:

```bash
roslaunch fringa_pkg robmov.launch world_name:=escenario1
roslaunch fringa_pkg robmov.launch world_name:=escenario2
roslaunch fringa_pkg robmov.launch world_name:=escenario3
roslaunch fringa_pkg robmov.launch world_name:=estudio
```

The `explore.launch` file runs the exploration node that combines the border exploration strategy with information gain [[1]](#1). It has some modifiable parameters. The most interesting ones are the weights given to the cost function and the expectation radius. Once the exploration is finished, a message with the exploration time is published.

- `potential_scale:` Weight of the Euclidean distance $k_d$.
- `gain_entropy:` Weight of the information gain $k_i$.
- `gain_obstacle:` Penalty for obstacles $k_f$.
- `min_frontier_size:` Minimum frontier size for it to be considered a frontier (this is used to purge noise).
- `expected_radius:` Expectation radius.

The exploration cost function is as follows:
$$U_{health} = k_d \cdot d - k_i \cdot f(k_f) \cdot IG$$

```bash
roslaunch fringa_pkg explore.launch
```

The `terrorista` node is responsible for moving the robot to the starting position of the exploration, as well as for saving the explored map and comparing it with another one generated previously and considered ground truth. The metrics used to evaluate the exploration [[2]](#2) contain both the time and distance traveled during the exploration, as well as the mean squared error (`MSE`), K-nearest base normalized error (`NE`), and the Structure Similarity Index (`SSIM`).

The `trajectory` node calculates the distance traveled during the exploration. The distance traveled is calculated by integrating the linear velocities in the local X axis. In addition to this, it is also responsible for publishing the message containing all the evaluated metrics.

## Messages

`Errores.` This message contains the following fields.
    
- **`nearest`** `float64.` K-nearest base normalized error (`NE`).
- **`mse`** `float64.` Mean Squared Error (`MSE`).
- **`issim`** `float64.` Structure Similarity Index (SSIM).

`Metricas.`
- **`distance`** `float64.` Distance traveled during the exploration.
- **`exploration_time`** `float64.` Time spent during the exploration.
- **`errors`** `Errores.` Exploration metrics.


## Instalation

Important configurations:

```bash 
export TURTLEBOT3_MODEL=waffle_pi
export GAZEBO_RESOURCE_PATH=$GAZEBO_MODEL_PATH:~/RUTA_AL_WS/src/robots_moviles/worlds
```

I got it working with these packages installed:

- `navigation`
- `turtlebot3`
- `turtlebot3_simulations`
- `slam_gmapping`
- `robots_moviles`

If it doesn't work with these packages, we'll resort to ancient forbidden magic. In the workspace directory:

```bash
rosdep install --from-paths src --ignore-src -r -y
```

This is real magic, I'm not saying it, the wiki says it. "This command magically installs all the packages that the packages in your catkin workspace depend upon but are missing on your computer"."


## References

<a id="1">[1]</a> 
J. Godoy-Calvo, D. Lin-Yang, R. Vázquez-Martín, and A. García-Cerezo, ‘Exploración dinámica de fronteras en entornos desconocidos basada en la entropía’, Rev. Iberoam. Autom. Inform. Ind. RIAI, vol. 20, no. 2, pp. 213–223, Feb. 2023. [https://doi.org/10.4995/riai.2023.18740](https://doi.org/10.4995/riai.2023.18740).

<a id="2">[2]</a> 
Sang, Xuan and Fabresse, Luc and Bouraqadi, Noury and Lozenguez, Guillaume, (2018). 
Evaluation of Out-of-the-box ROS 2D SLAMs for Autonomous Exploration of Unknown Indoor Environments.
The 11th International Conference on Intelligent Robotics and Applications, Newcastle, Australia.