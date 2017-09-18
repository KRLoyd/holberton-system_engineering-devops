# 0x16. API

## Description
The files in this repository correlate with Holberton School tasks to access and work with information from [this Fake Online REST API for Testing and Prototyping](https://jsonplaceholder.typicode.com/).

### Project Notes
#### Environment
These functions have been tested on Ubuntu 14.04.5 LTS.
Tests done in VirtualBox on Ubuntu via Vagrant(1.8.6) using `python3` (version 3.4.3).

#### Style
All files are written in the PEP 8 style.
Information about this style can be found at https://www.python.org/dev/peps/pep-0008/

## Files
All files must be executable to run. To add executable permissions to any file: `chmod u+x file_name`

##### [0-gather_data_from_an_API.py](0-gather_data_from_an_API.py)
Python script to return information about an employee's TODO list progress.
* Arguments: script uses one argument, the employee's ID
* Return: The string "Employee <Employee name> is done with tasks(<number of done tasks>/<total number of tasks>):" followed by a list of completed tasks.
* Usage: `0-gather_data_from_an_API.py <employee ID>`

##### [1-export_to_CSV.py](1-export_to_CSV.py)
Using task 0, extend Python script to export task data for one employee in the CSV format.
* Arguments: script uses one argument, the employee's ID
* Creates a CSV file named `<employee id>.csv`

##### [2-export_to_JSON.py](2-export_to_JSON.py)
Using task 0, extend Python script to export task data for one employee in the JSON format.
* Arguments: script uses one argument, the employee's ID
* Creates a JSON file named `<employee id>.json`

##### [3-dictionary_of_list_of_dictionaries.py](3-dictionary_of_list_of_dictionaries.py)
Using task 0, extend Python script to export task data for all employees in the JSON format.
* Creates a JSON file named `todo_all_employees.json`


## Authors
Kristen Loyd        [Github](https://github.com/KRLoyd) |  [LinkedIn](https://www.linkedin.com/in/kristen-loyd-34984a92)

## License
Public Domain, no copyright protection