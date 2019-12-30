# Threaded Task Executor
Allows functions to be called in a seperate thread and executed in FIFO order.

[Click Here For Full Documentation](https://github.com/enchant97/python-threadedtaskexecutor/wiki)

## Possible Uses:
- For serial communication where send/recv order matters
- Run background tasks in tkinter easily, without freezing gui
- Any application where background tasks are required to be executed in order
## Gettings Started:
### Installing
From PyPi:
```
pip install threaded-task-executor
```
From GitHub repo:
```
pip install git+https://github.com/enchant97/python-threadedtaskexecutor.git
```
### Importing
```python
from threaded_task_executor import Task_Queue, Task
```
### How To Use
```python
tasks = Task_Queue()
tasks.add_task(Task(print, args=("test 1")))
tasks.add_task(Task(print, args=("test 2")))
```
When this is run it should start the thread
and execute the tasks in FIFO order.

## Updates:
### 1.2
- New global callback that can be given to Task_Queue obj
### 1.1
- New decorator method that allows for adding to a Task_Queue obj
### 1.0
First version
