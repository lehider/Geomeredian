# Goemeredian
Setup your sources.list
-----------------------

sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'


Set up your keys
----------------
sudo apt install curl # if you haven't already installed curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -


Installation
------------

sudo apt-get update

sudo apt-get install ros-kinetic-desktop-full

sudo apt-get install ros-kinetic-desktop

sudo apt-get install ros-kinetic-ros-base

Environment setup
-----------------
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
source ~/.bashrc


Dependencies for building packages
-----------------------------------
sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential


Initialize rosdep


sudo apt install python-rosdep

rosdep update

Create ROS Space
----------------
$ mkdir -p ~/catkin_ws/src
 
$ cd ~/catkin_ws/

$ catkin_make


Hesai Lidar SDK Installation
----------------------------
$ sudo apt-get update

$ sudo apt-get install python-catkin-tools

$ mkdir -p rosworkspace/src

$ cd rosworkspace/src

$ git clone https://github.com/HesaiTechnology/HesaiLidar_General_ROS.git --recursive

Step 1:- Network configuration
 change the ip address of hesao to 192.168.1.201

Step 2:-
 roslaunch hesai_lidar hesai_lidar.launch lidar_type:="PandarXTM" frame_id:="PandarXTM"

Novatel pwrpak7 gnss installation
---------------------------------

To install:
  git clone https://github.com/novatel/novatel_oem7_driver
  
  rosdep install --from-paths src --ignore-src -r -y
  
  cd catkin/src
  
  catkin_make
  
To launch:

  roslaunch novatel_oem7_driver oem7_net.launch oem7_ip_addr:=192.168.1.10


WebUI to record lidar/gnss/slam data
---------------------------------
Steps to launch webUI/rosboard:-

Step1: roscore

Step2:  roslaunch rosbridge_server rosbridge_websocket.launch

Step3: ./rosboard/run

Step4: Launch the hesai and gnss nodes

Step5: Add the display in UI by topic name

Step6: Press "Record" to store rosbag data(lidar,gnss,slam)

Step7: Press "Stop" to save the rosbag.


![alt text](https://github.com/lehider/Geomeredian/blob/main/images/Screenshot%20from%202022-01-30%2023-53-42.png)


To Play rosbag on ros
---------------------

Step1: To play

rosbag play *filename* 

Step2: To View 

launch rviz by "rosrun rviz rviz"

Converting rosbag file to PCD file
-----------------------------------

rosrun pcl_ros bag_to_pcd file.bag hesai/pandar /

Converting PCD to las
----------------------

**pending**

Improvements to do
------------------

1.Specify the path to store.

2.Automate PCD conversation from WebUI.

3.Converting PCD to lsa with out help of other software .

