""" Todo:
        - Alter the complete_tasks method so that it only calls 'complete' on
            non-completed task.
        - Add a remove_task method that removes only one task by id

        - Upon calling complete() on a task, set _value of that task object to the number of occurrences of the
            string "CCN" (case in-sensitive) that appears in the task's name.

        - Fix the Task object id, so that it is unique for each new task. (please consider scalability and
            what else the Id could be used for)

        - Fix other bugs and make improvements where you see fit
        - Add error handling where you see fit

    Note:
        - You cannot edit/change the TaskManager class directly. Think of it as a 3rd party library
        - You can create new objects, etc
"""
import uuid

class Task(object):

    def __init__(self, name):
		# Solution to ---> Fix the Task object id, so that it is unique for each new task
        self._id = uuid.uuid4()
		# Note this uniqueness method can run into scalability issues at very large volumes, in which
		# case if we are using an SQL database, we can use the _id to be the a database key
		# (ie. primary key), which would guarantee uniqueness but for the purpose of this assignment
		# I chose to use UUID.
        self._name = name
        self._value = None
        self._completed = False

    def complete(self):
        _completed = True

    @property
    def is_completed(self):
        return self._completed

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def value(self):
        return self._value


# This class cannot be edited directly
class TaskManager(object):

    def __init__(self):
        self._tasks = []

    def import_task(self, task):
        self._tasks.append(task)

    def complete_tasks(self):
		if len(self._tasks) > 0:
			if not all([task.is_completed for task in self._tasks]):
				for task in self._tasks:
					# Solution to ---> Alter the complete_tasks method so that it only calls 'complete' on
			        # non-completed task.
					if task.is_completed is False:
						task.complete()
						# Solution to ---> Upon calling complete() on a task, set _value of that task object
						# to the number of occurrences of the string "CCN" (case in-sensitive) that appears
						# in the task's name.
						lower_case_name = task._name.lower()
						task._value = lower_case_name.count("ccn")
					print('task {name} completed'.format(name=task.name))
					print('task ID is {id}'.format(id=task.id))
					print('ccn occurences is {occurences}'.format(occurences=task._value))


    def remove_tasks(self):
        while len(self._tasks) > 0:
            self._tasks.pop()

	# Solution to ---> Add a remove_task method that removes only one task by id
	def remove_task(self, id):
		for item in self._tasks[:]:
			if item._id == id:
				self._tasks.remove(item)
