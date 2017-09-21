# 0x18. API advanced

## Description
The files in this repository are for tasks to gain more practice using an API. Specifically, the tasks are requesting from https://www.reddit.com/dev/api/ .

### Project Notes
#### Environment
These functions have been tested on Ubuntu 14.04.5 LTS.
Tests done in VirtualBox on Ubuntu via Vagrant(1.8.6) using `python3` (version 3.4.3).

#### Style
All files are written in the PEP 8 style.
Information about this style can be found at https://www.python.org/dev/peps/pep-0008/

## Files
All files must be executable to run. To add executable permissions to any file: `chmod u+x <file_name>`

##### [0-subs.py](0-subs.py)
Function that queries the Reddit API and returns the number of subscribers for a given subreddit.
* Prototype: `def number_of_subscribers(subreddit)`
  * @subreddit: name of the subreddit to get information about
  * Returns: 0 if the subreddit provided does not exist, the number of subscribers otherwise.

##### [1-top_ten.py](1-top_ten.py)
Function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
* Prototype: `def top_ten(subreddit)`
  * @subreddit: name of the subreddit to get information about
  * Returns: prints "None" if the subreddit is not valid, prints the top 10 hot posts if valid

##### [2-recurse.py](2-recurse.py)
Recursive function that queries the Reddit API and returns a list of titles of all hot articles for a given subreddit.
* Prototype: `def recurse(subreddit, hot_list=[])`
  * @subreddit: name of the subreddit to get information about
  * Returns: `None` if the subreddit is not valid, a list of the hot posts if valid

##### Folder [mains](mains)
Folder to hold the main files provided by Holberton School to test my functions.

## Authors
Kristen Loyd        [Github](https://github.com/KRLoyd) |  [LinkedIn](https://www.linkedin.com/in/kristen-loyd-34984a92)

## License
Public Domain, no copyright protection