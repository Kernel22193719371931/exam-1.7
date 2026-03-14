# Exam Robot - Контрольная работа по ROS 2

## Архитектура системы
[battery_node] ── /battery_level ──┐
├── [status_display] ── /robot_status ── [robot_controller] ── /cmd_vel
[distance_sensor] ── /distance ────┘ |
└── [robot_state_publisher] ── /robot_description, /tf
|
└── [joint_state_publisher] ── /joint_states

text

### Узлы и топики

| Узел | Публикует | Подписывается | Описание |
|------|-----------|---------------|----------|
| `battery_node` | `/battery_level` (Float32) | - | Симуляция разряда батареи (1%/сек) |
| `distance_sensor` | `/distance` (Float32) | `/cmd_vel` (Twist) | Измерение расстояния до препятствия |
| `status_display` | `/robot_status` (String) | `/battery_level`, `/distance` | Определяет статус робота |
| `robot_controller` | `/cmd_vel` (Twist) | `/robot_status` | Управление движением |
| `robot_state_publisher` | `/robot_description`, `/tf` | - | Публикация URDF и трансформаций |
| `joint_state_publisher` | `/joint_states` | - | Публикация состояний суставов |

### Статусы робота

| Статус | Условие | Команда движения |
|--------|---------|------------------|
| `ALL OK` | battery ≥ 20% AND distance ≥ 1.0м | linear.x = 0.3 м/с |
| `WARNING: Low battery` | battery < 20% | linear.x = 0.1 м/с |
| `WARNING: Obstacle close` | distance < 1.0м | angular.z = 0.5 рад/с |
| `CRITICAL` | battery < 10% OR distance < 0.7м | полная остановка |

## Запуск системы

```bash
# Сборка пакета
cd ~/ros2_ws
colcon build --packages-select exam_robot
source install/setup.bash

# Запуск
ros2 launch exam_robot robot_system.launch.py
Тестирование
Проверка топиков
bash
# Список всех топиков
ros2 topic list

# Просмотр данных
ros2 topic echo /battery_level
ros2 topic echo /distance
ros2 topic echo /robot_status
ros2 topic echo /cmd_vel

# Частота публикации
ros2 topic hz /battery_level
ros2 topic hz /distance
Проверка TF дерева
bash
ros2 run tf2_tools view_frames
# Открыть полученный PDF
Проверка узлов
bash
ros2 node list
ros2 node info /robot_controller
Параметры
Узел	Параметр	По умолчанию	Описание
battery_node	discharge_rate	1.0	Скорость разряда (%/сек)
robot_controller	max_speed	0.3	Максимальная скорость (м/сек)
text
