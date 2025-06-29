# ros_ws

This Repository contains the ROS Workspace. To properly clone this repository, make sure to load the submodules by running
```bash
git submodule init
git submodule update
```
after cloning.

# How to build and run the Traffic Light Assistant

## Build
First, navigate to the top level of the given Folder structure. Then, run 
```bash
colcon build
```
in the top level of the given Folder structure. Next, source the executables by running
```bash
source install/setup.bash
```

## Run
Finally, run
```bash
ros2 launch launch/launch.py
```
to start all needed executables for the traffic light assistant. You can now access the Web server on Port 5000.