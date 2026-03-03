from collections import deque
import copy


def bfs_plan(user, tasks):
    # Доступные часы по дням
    availability = {day["day"]: day["hours_available"] for day in user["availability"]}

    # Начальное состояние
    initial_state = {
        "schedule": {day: [] for day in availability},
        "remaining_tasks": {task["task_id"]: task["estimated_hours"] for task in tasks}
    }

    queue = deque([initial_state])

    while queue:
        state = queue.popleft()

        # Проверяем цель
        if all(hours == 0 for hours in state["remaining_tasks"].values()):
            return state["schedule"]

        # Перебираем задачи
        for task_id, remaining in state["remaining_tasks"].items():
            if remaining > 0:
                # Перебираем дни
                for day in availability:
                    # Проверяем, есть ли свободное место
                    if len(state["schedule"][day]) < availability[day]:

                        new_state = copy.deepcopy(state)

                        # Назначаем 1 час задачи
                        new_state["schedule"][day].append(task_id)
                        new_state["remaining_tasks"][task_id] -= 1

                        queue.append(new_state)

                break  # Берём только одну задачу за шаг

    return None