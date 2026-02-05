new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']
completed_tasks.append(new_tasks.pop())

print(new_tasks)
print(completed_tasks)

new_tasks.remove('task_007')
print(new_tasks)

new_tasks.insert(0, new_tasks.pop(2))
last_task = new_tasks[0]  # task_015
print('Задача с повышенным приоритетом (следующая в работе): ' + last_task)