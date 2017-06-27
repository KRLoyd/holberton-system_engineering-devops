# 0x05. Processes and signals

## Description
To be able to explain the following:
* What is a PID
* What is a process
* How to find a process PID
* How to kill a process
* What is a signal
* What are the 2 signals that cannot be ignored

### Project Notes
#### Environment
These functions have been tested on Ubuntu 14.04.5 LTS.
Tests and development are done in VirtualBox on Ubuntu via Vagrant(1.8.1).
#### Compilation
All `.c` programs and functions are compiled with `gcc -Wall -Werror -Wextra -pedantic` version 4.8.4.
#### Style
All C code is written in Betty style. Information about this style can be found [here](https://github.com/holbertonschool/Betty/wiki).

All Bash scripts pass `Shellcheck` (version 0.3.3).


## Files
All files must be executable to run. To add executable permissions to any file: `chmod u+x file_name`

[0-what-is-my-pid](0-what-is-my-pid) : Bash script that displays its PID

[1-list_your_processes](1-list_your_processes) : Bash Script to display a list of currently running processes.
* Notes:
    * Shows all processes, for all users, including those without a TTY
    * Displays a user-oriented format
    * Shows process hierarchy

[2-show_your_bash_pid](2-show_your_bash_pid) : Bash script that displays a linee containing the word `bash`.

[3-show_your_bash_pid_made_easy](3-show_your_bash_pid_made_easy) : Bash script to display the PID and process name of the processes whose names contain the word `bash`.

[4-to_infinity_and_beyond](4-to_infinity_and_beyond) : Bash script that displays `To infinity and beyond` indefinitely.

[5-kill_me_now](5-kill_me_now) : Bash script to kill a `4-to_infinity_and_beyond` process.
* Note: uses `kill` command.

[6-kill_me_now_made_easy](6-kill_me_now_made_easy) : Bash script to kill `4-to_infinity_and_beyond` processes without using `kill` or `killall` commands.

[7-highlander](7-highlander) : Bash script that displays a string indefinitely and traps the `SIGTERM` signal.
* Notes:
    * String to display: `To infinity and beyond`
    * When a `SIGTERM` trapped, prints `I am invincible!!!`
    * [67-kill_me_now_made_easy](67-kill_mew_now_made_easy) : kills the `7-highlander` process

[8-beheaded_process](8-beheaded_process) : Bash script to kill the process `7-highlander`

[9-process_and_pid_file](9-process_and_pid_file) : Bash script that does many things!
* Notes:
    * Saves its PID in file `/var/run/holbertonscript.pid`
    * Displays `To infinity and beyond` indefinitely
    * Traps `SIGTERM` signals
        * Displays `I hate the kill command`
        * Deletes file `/var/run/holbertonscript.pid`
        * Terminates itself
    * Traps `SIGINT` signals
        * Displays `Y U no love me?!`
    * Traps `SIGQUIT` signals
        * Deletes file `/var/run/holbertonscript.pid`
        * Terminates itself

[10-manage_my_process](10-manage_my_process) : Bash (init) script to manage `manage_my_process`
* Notes:
    * When passed the argument `start`: starts `manage_my_process`, creates a file containint its PID in `/var/run/my_process.pid`, displays `manage_my_process started`
    * When passed the argument `stop`: stops `manage_my_process`, deletes the file `/var/run/my_process.pid`, displays `manage_my_process stopped`
    * When passed the argument `restart`: stops `manage_my_process`, deletes the file `/var/run/my_process.pid`, starts `manage_my_process`, creates a file containint its PID in `/var/run/my_process.pid`, displays `manage_my_process restarted`
    * When passed nothing or something that was not listed above: displays `Usage: manage_my_process {start|stop|restart}`
* [manage_my_process](manage_my_process) : Bash script to write `I am alive!` to file `/tmp/my_process`.

[11-zombie.c](11-zombie.c) : C program that creates 5 zombie processes.
* Notes:
    * For every zobie process created, displays `Zombie process created, PID: <ZOMBIE_PID>`
    * To see a list of the zombies created, open a new Terminal window and run `ps aux | grep -e 'Z+.*<defunct>'`

## Authors
Kristen Loyd        [Github](https://github.com/KRLoyd) |  [LinkedIn](https://www.linkedin.com/in/kristen-loyd-34984a92)

## License
Public Domain, no copyright protection
