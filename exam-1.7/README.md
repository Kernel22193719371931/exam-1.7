# Exam Robot

## Запуск 
```bash
cd ~/ros2_ws
colcon build --packages-select exam_robot
source install/setup.bash
ros2 launch exam_robot robot_system.launch.py
```

## Тестирование

```bash
# Проверка топиков
ros2 topic list

# Проверка данных
ros2 topic echo /battery_level
ros2 topic echo /distance
ros2 topic echo /robot_status

# Проверка TF дерева
ros2 run tf2_tools view_frames
```

## Архитектура

    /battery_level - симулятор батареи

    /distance - симулятор дальномера

    /robot_status - объединяет данные

    /cmd_vel - команды движения

    /robot_description - URDF модель

    /joint_states - состояние суставов
