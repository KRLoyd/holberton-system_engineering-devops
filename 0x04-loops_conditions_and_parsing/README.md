# 0x04. Loops, conditions and parsing

## Description
To be able to explain the following:
* How to create SSH keys
* What is the advantage of using #!/usr/bin/env bash over #!/bin/bash
* How to use while, until and for loops
* How to use if, else, elif and case condition statements
* How to use the cut command
* What are files and other comparison operators, and how to use them

### Project Notes
#### Environment
These functions have been tested on Ubuntu 14.04.5 LTS.
Tests and development are done in VirtualBox on Ubuntu via Vagrant(1.8.1).

#### Style
All Bash scripts have been checked with `Shellcheck` (version 0.3.3). To install `Shellcheck` run `apt-get install shellcheck`
 
## Files

[0-RSA_public_key.pub](0-RSA_public_key.pub) : File that stores my public key.

[1-for_holberton_school](1-for_holberton_school) : Bash script that displays `Holberton School` 10 times using a `for` loop.

[2-while_holberton_school](2-while_holberton_school) : Bash script that displays `Holberton School` 10 times using a `while` loop.

[3-until_holberton_school](3-until_holberton_school) : Bash script that displays `Holberton School` 10 times using an `until` loop.

[4-if_9_say_hi](4-if_9_say_hi) : Bash script that displays `Holberton School` 10 times, but on 9th iteration: also displays `hi`.

[5-4_bad_luck_8_is_your_chance](5-4_bad_luck_8_is_your_chance) : Bash script that loops from 1 to 10 and prints per the following instructions:
* 4th loop iteration: displays `bad luck`
* 8th loop iteration: displays `good luck`
* all other iterations: displays `Holberton School`

[6-superstitious_numbers](6-superstitious_numbers) : Bash script that prints from 1 to 20 and prints per the following instructions:
* 4th loop iteration: also displays `bad luck from China`
* 9th loop iteration: also displays `bad luck from Japan`
* 17th loop iteration: also displays `bad luck from Italy`

[7-clock](7-clock) : Bash script that displays the time for 12 hours and 59 minutes.
* Notes:
    * Hours are displayed from 0 to 12
    * Minutes are displayed from 1 to 59

[8-for_ls](8-for_ls) : Bash sript that displays content of the current director in list format.
* Notes:
    * For loop is used
    * Hidden files are not displayed

[9-to_file_or_not_to_file](9-to_file_or_not_to_file) : Bash script that gives you information about the `holbertonschool` file.
* Notes:
    * If the file does not exist:
        * Displays `holbertonschool file does not exist`
    * If the file exists:
        * Displays `holbertonschool file exists`
        * If the file is empty:
            * Displays `holbertonschool file is empty`
        * If the file is not empty:
            * Displays `holbertonschool file is not empty`
        * If the file is a regular file:
            * Displays `holbertonschool is a regular file`

[10-fizzbuzz](10-fizzbuzz) : Bash script that displays numbers from 1 to 100 with the following conditions:
* If the number is a multiple of 3 and 5, displays `FizzBuzz`
* If the number is a multiple of 3, displays `Fizz`
* If the number is a multiple of 5, displays `Buzz`

## Authors
Kristen Loyd        [Github](https://github.com/KRLoyd) |  [LinkedIn](https://www.linkedin.com/in/kristen-loyd-34984a92)

## License
Public Domain, no copyright protection
