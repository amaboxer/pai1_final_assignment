FROM ros:jazzy

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-colcon-common-extensions \
    ros-jazzy-turtlebot3 \
    ros-jazzy-turtlebot3-simulations \
    xterm \
    
    && rm -rf /var/lib/apt/lists/*


ENV TURTLEBOT3_MODEL=burger

WORKDIR /ros2_ws

RUN echo "source /opt/ros/jazzy/setup.bash" >> /home/ubuntu/.bashrc

CMD ["bash"]