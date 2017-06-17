# ToDo list app
# This program can be used to keep track of your tasks
# so that you don't have to yourself
# ToDo list app supports the following commands:
# create
# show
# select taskname
# edit

from datetime import date
from helper_functions import get_date
import pickle

class Task():
	def __init__(self, task_name = "task" , due_date = "tomorrow"):
		self.task_name = task_name
		self.due_date = due_date

	def get_task_details(self):
		print "Task Name: %s" % (self.task_name)
		print "Due Date: %s" % (self.due_date)


def create_task():
	task_name = raw_input('Task name: ')
	due_date_raw = raw_input('Due Date: ')
	due_date = get_date(due_date_raw)
	try:
		task = Task(task_name, due_date)
		task.get_task_details()
		print "Task created successfully"
	except Exception as e:
		print(str(e))
		print "Task could not be created"

def process_query(query):
	query_primary = query.split(" ")[0]
	if query_primary == "create":
		create_task()

def main():
	print "___________ToDoApp__________________\n\n"
	while(True):
		query = raw_input('>')
		process_query(query)



if __name__ == '__main__':
	main()
