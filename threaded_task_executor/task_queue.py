"""
Allows for executing thread when a Task objects are added to the queue
"""
from .queue_peek import Queue_Peek as _Queue_Peek
from .task import Task as _Task
from threading import Thread as _Thread
from functools import wraps as _wraps

__all__ = ["Task_Queue"]

class Task_Queue:
    """
    executes threads that will run Task objects

    args:
        daemon : used in threading.Thread
        global_callback : used when there is no callback given when adding a task (can be None)
    """
    def __init__(self, daemon=None, global_callback=None):
        self.__tasks = _Queue_Peek()
        self.__daemon = daemon
        self.__global_callback = global_callback

    def __execute_tasks(self):
        """
        Executes all of the tasks, and
        removes them from the queue when
        they are completed
        """
        while not self.__tasks.empty():
            task = self.__tasks.peek()
            task.execute()
            self.__tasks.pop()

    def get_current_task(self):
        """
        Allows for the current task that is executing to be returned
        """
        return self.__tasks.peek()

    def tasks_left(self):
        """
        Returns the number of tasks left to be completed,
        includes currently executing task if any.
        """
        return self.__tasks.size

    def add_task(self, new_task):
        """
        Adds a new task, if there is no
        threads running will start one,
        if no callback was given it will use global_callback if it was set
        , unless a int 0 was provided which means no use of global callback
        """
        if isinstance(new_task, _Task):
            if new_task.callback == None:
                new_task.callback = self.__global_callback
            elif new_task.callback == 0:
                new_task.callback = None
            if self.__tasks.empty():
                self.__tasks.push(new_task)
                the_thread = _Thread(target=self.__execute_tasks, daemon=self.__daemon)
                the_thread.start()
            else:
                self.__tasks.push(new_task)
        else:
            raise TypeError("Must be a Task class instance")

    def add_from_func(self, callback=None, task_name=""):
        """
        Decorator to add a function which will use add_task()
        args:
            callback : used for Task()
            task_name : used for Task()
        """
        def decorator(func):
            def wrapper(*args, **kw):
                self.add_task(_Task(func, callback, task_name, args, kw))
            return wrapper
        return decorator
