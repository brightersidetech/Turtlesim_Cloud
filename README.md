# Turtlesim_Cloud
This implementation controls the motion of the turtlesim via cloud. The implementation uses FIROS to connect the turtlesim to the cloud. Together with the FIWARE context Brocker, turtlesim topics ca be subscribed to and data stored on the cloud. Data can as well be downoaded from the cloud and use to update turtlesim parameters by publishing to certain topics to them


## Installing the required services
### 1. Instal and configure ROS
his application needs a ROS installation. For the full tutorial on how to install ROS [use the link here](http://wiki.ros.org/noetic/Installation)

### 2. Install Turtlesim
To install and run Turtlesim, [follow thw tutorial here](http://wiki.ros.org/turtlesim)

### 3. Install docker 
FIROS support services (Fiware Orion Context Broker and the Supporting MongoDB database) would normally run on the Cloud. So, we shall need Docker for deveoping and testing. To install docker, [follow the tutorial here](https://docs.docker.com/engine/install/ubuntu/)

### 4. Setup the Orion Contect Broker
After docker has been successfully installed, 2 docker containers must be created. The mongoDB container is used by the Orion context Brocker to store context data. The Orion container is a Fiware REST API service used to store, retrive and update contect information on the cloud.

To create the two containers, the following docker commands are used.

```
docker run -d --name=mongodb mongo:4.4
docker run -d --name=orion --link mongodb:mongodb -p 1026:1026 fiware/orion -dbhost mongodb

```

### 5. Clone the FOROS Package

FIROS is a tool that helpst to connect Robots and other ROS nodes to the Cloud. It interfaces the ROS world with the cloud world by subscribing to and publising to ROS topics. ROS messages are published to the cloud and topics can be updated buy retrieving ROS messages from the cloud and publishing then to topics.

### Clone Repository
```
cd "catkin_workspace_base_directory"/src
git clone --recursive https://github.com/iml130/firos.git
cd "catkin_workspace_base_directory"/src/firos
```

### Install Dependencies
```
pip install -r requirements.txt
```

### Make Node
```
cd "catkin_workspace_base_directory"
catkin_make
```

For a detailed tutorial on how to Install FOROS, [visist the website here](https://firos.readthedocs.io/en/latest/install/install.html)

## Setting up things

```
python3 src/firos/firos/core.py --conf src/firos/config_1
```

** This is a bold text **
_ This is an italics text _
- This is a bulet