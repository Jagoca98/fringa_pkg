# Frontiered Information Gain (fringa)


## Ejecución

`robmov.launch` carga gazebo, el turtlebot3 waffle_pi con las transformaciones corregidas, el rviz configurado guay, el gmapping y el move_base para poder al bixo. Los archivos de configuracion del move_base (los de la carpeta param) estan modificados para el laser del robot tome las medidas infinitas como válidas (GRACIAS MANUSANCHE POR DESCUBRIRME ESTO <3). Mas adelante habra que configurar el rviz y el launch para hacer octomapping.

```bash
roslaunch fringa_pkg robmov.launch
```

`explore.launch` Este es el nodo de exploracion que combina la estrategia de exploracion de fronteras con la ganancia de informacion. Tiene algunos parametros modificables. Los mas interesantes son los pesos que se les da a la funcion de coste y el radio de expectativas.
    
- `potential_scale`. Peso de la distancia euclidea.
- `gain_entropy`. Peso de la ganancia de informacion.
- `gain_obstacle`. Penalizacion por los obstáculos.
- `min_frontier_size`. Tamaño de frontera minimo para que se considere frontera (Esto sirve para purgar ruido).
- `expected_radius`. Radio de expectativas

```bash
roslaunch fringa_pkg explore.launch
```

## Instalación


Importante estas mierdas
```bash 
export TURTLEBOT3_MODEL=waffle_pi
export GAZEBO_RESOURCE_PATH=$GAZEBO_MODEL_PATH:~/RUTA_AL_WS/src/robots_moviles/worlds
```

A mi me furula con esto instalao 

- `navigation`
- `turtlebot3`
- `turtlebot3_simulations`
- `slam_gmapping`
- `robots_moviles`

Si con estos paquetes no furula, tiramos de magia prohibida antigua. En la ruta del workspace:

``` bash
rosdep install --from-paths src --ignore-src -r -y
```

Esto es brujeria de verdad, no lo digo yo, lo dice la wiki. "This command magically installs all the packages that the packages in your `catkin workspace` depend upon but are missing on your computer".


## Futuro (keaceres vaya)

- `Octomapping`. Esto lo veo como un plus.