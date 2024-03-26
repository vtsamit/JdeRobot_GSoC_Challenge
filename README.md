<h1 align="center"> JdeRobot_GSoC_Challenge </h1>
<br>
<h2 align="left"> ROS2 Challenge (NAVIGATION 2) </h2>

*   Install ROS Navigation2 and Turtlebot3 package

```
sudo apt install ros-humble-navigation2
sudo apt install ros-humble-turtlebot3*
```

*  Clone the repository and build the package
```
mkdir -p ~/navigation_ws/src
cd ~/navigation_ws/src
git clone https://github.com/ros-planning/navigation2.git
cd ..
rosdep install -y -r -q --from-paths src --ignore-src --rosdistro humble
colcon build --symlink-install
```
*  Open .bashrc file and export the path variables
  
```
gedit ~/.bashrc
source ~/nav2_ws/install/setup.bash
export TURTLEBOT3_MODEL=waffle
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/opt/ros/foxy/share/turtlebot3_gazebo/models
source /usr/share/gazebo/setup.sh
```
* Open a new terminal and launch
  
```
cd ~/navigation_ws/
ros2 launch nav2_bringup tb3_simulation_launch.py
```
*  Visualize using rviz2, set position using 2d_Pose Estimate and give waypoints using Nav2_Goal

### Video Simulation - 
(https://youtu.be/eOtf-TjvbB4)
<br>
<h2 align="left"> NAVIGATION Challenge using ROS-Noetic </h2>

### Source Code - 
(https://github.com/vtsamit/Labyrinth_Ros_Navigation)
### Visuals - 
(https://drive.google.com/file/d/1CFbJVxbLxP4gabwmcAitaT45VJuusIf-/view?usp=sharing)
<p align="center" style="background-color: rgb(250,250,250)">
<img src="https://github.com/vtsamit/Labyrinth_Ros_Navigation/blob/main/Screenshot from 2024-03-25 23-50-31.png"/>
</p>

<br>
<h2 align="left"> ROS2 Challenge (Introduction) </h2>

*  Clone the repository and build the package
```
git clone https://github.com/vtsamit/JdeRobot_GSoC_Challenge.git
cd ~/GSoC_ros2_ws/
colcon build --symlink-install
```
* Make the python files as executable

```
cd src/intro_package/intro_package/
chmod +x publisher_gsoc.py
chmod +x subscriber_gsoc.py
cd ~/GSoC_ros2_ws/
colcon build
```

* Open a new terminal and run publisher node
```
source ~/GSoC_ros2_ws/install/setup.bash
ros2 run intro_package publisher_gsoc
```

* Open a new terminal and run subscriber node
```
source ~/GSoC_ros2_ws/install/setup.bash
ros2 run intro_package subscriber_gsoc
```
### Video -
(https://drive.google.com/file/d/14KpZ3r1GuRKpksgicKbEMZ0hcO5t_ap4/view?usp=sharing)
<br>
<h2 align="left"> Python Challenge </h2>

* Clone the Repository and create virtual environment

```
git clone https://github.com/vtsamit/JdeRobot_GSoC_Challenge.git
cd ~/JdeRobot_Challenge_Python/
python3 -m venv venv
source venv/bin/activate

```

* Install requirements
```
pip install -r requirements.txt
```
* Run the Brownian Motion Simulation
```
python3 run_motion.py
```
### Video Simulation -
(https://drive.google.com/file/d/1VYAs145_QpA66lpBWDDVRfCc5mj_sQK8/view?usp=sharing)

<br>
<h2 align="left"> Robotics Academy Challenge (Obstacle Avoidance) </h2>

### Youtube Video - 
(https://youtu.be/FQ8J4lkrk74)











  
