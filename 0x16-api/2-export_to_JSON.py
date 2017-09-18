#!/usr/bin/python3
"""
Python script find todo list progress about a specific employee and
export it into a JSON formatted file.
File created: <employee_id>.json
"""
if __name__ == "__main__":
    # Import modules
    import requests
    from sys import argv

    # Set variables
    employee_id = argv[1]
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id)
    employee_url = "https://jsonplaceholder.typicode.com/users?id={}".format(
        employee_id)
    file_name = employee_id + ".json"

    # Make requests
    todo_request = requests.get(todo_url)
    employee_request = requests.get(employee_url)

    # Get JSON results of both requests
    employee_json = employee_request.json()
    todo_json = todo_request.json()

    # Save information from requests in variables
    employee_username = employee_json[0].get('username')

    # write info into JSON file
    with open(file_name, "w") as json_file:
        employee_tasks = {}
        task_list = []
        # Add individual tasks to task_list
        for task in todo_json:
            task_dict = {}
            task_dict["task"] = task.get("title")
            task_dict["completed"] = task.get("completed")
            task_dict["username"] = employee_username
            task_list.append(task_dict)
        # Add the task_list as value to employee_id in employee_tasks dict
        employee_tasks[employee_id] = task_list
        # Write the emplpyee_tasks dict to the file
        json_file.write(str(employee_tasks))
