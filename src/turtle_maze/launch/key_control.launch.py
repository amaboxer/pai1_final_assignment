import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # turtlebot3_gazebo empty_world.launch.py
    empty_world = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('turtlebot3_gazebo'),
                'launch',
                'empty_world.launch.py'
            )
        )
    )

    # rviz2 rviz2
    rviz2 = Node(
        package='rviz2',
        executable='rviz2'
    )

    return LaunchDescription([
        empty_world,
        rviz2
    ])
