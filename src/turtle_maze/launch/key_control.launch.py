import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

"""
※ 終了の際は gazebo の x ボタンを押して終了すること．
"""

def generate_launch_description():
    # turtlebot3_gazebo empty_world.launch.py
    empty_world = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('turtlebot3_gazebo'),
                'launch',
                'empty_world.launch.py'
            )
        ),
        launch_arguments={
            'use_sim_time': 'true',
        }.items()
    )

    # rviz2 rviz2
    rviz2 = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        parameters=[{
            'use_sim_time': True
        }]
    )

    # turtlebot3_teleop teleop_keyboard
    teleop_keyboard = Node(
        package='turtlebot3_teleop',
        executable='teleop_keyboard',
        name='teleop_keyboard',
        parameters=[{
            'stamped': 'true',         # Jazzyに合わせたタイムスタンプ付きモード
            'use_sim_time': True    # 時間同期
        }],
        output='screen',
        prefix='xterm -e'          # キーボード入力を受け付けるために別ウィンドウで開く
    )


    return LaunchDescription([
        empty_world,
        rviz2,
        teleop_keyboard
    ])
