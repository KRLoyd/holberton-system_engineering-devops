# 0x14. Regular expression

## Description
These files are Ruby scripts to practice using regular expressions to match specific patterns.


### Project Notes
#### Environment
These Ruby scripts have been tested on Ubuntu 14.04.5 LTS.
Tests and development are done in VirtualBox on Ubuntu via Vagrant(1.8.1).
#### Style
These regular expressions were built with Oniguruma, a regular expression library used by Ruby by defalt.


## Files
All files must be executable to run. To add executable permissions to any file: `chmod u+x file_name`

##### [0-simply_match_holberton.rb](0-simply_match_holberton.rb)
Ruby script that accepts one argument and passes it to a regular expression matching method to match `Holberton`.
* Usage: `./0-simply_match_holberton.rb <argument>`
  * If no argument is passed, an empty line is printed

##### [1-repetition_token_0.rb](1-repetition_token_0.rb)
Ruby script that accepts one argument and pass it to a regular expression matching method to match specific cases.
* Cases to match:
  * `hbttn`
  * `hbtttn`
  * `hbttttn`
  * `hbtttttn`
* Usage: `./1-repetition_token_0.rb <argument>`

##### [2-repetition_token_1.rb](2-repetition_token_1.rb)
Ruby script that accepts one argument and pass it to a regular expression matching method to match specific cases.
* Cases to match:
  * `htn`
  * `hbtn`
* Usage: `./2-repetition_token_1.rb <argument>`

##### [3-repetition_token_2.rb](3-repetition_token_2.rb)
Ruby script that accepts one argument and pass it to a regular expression matching method to match specific cases.
* Cases to match:
  * `hbtn`
  * `hbttn`
  * `hbtttn`
  * `hbttttn`
* Usage: `./3-repetition_token_2.rb <argument>`

##### [4-repetition_token_3.rb](4-repetition_token_3.rb)
Ruby script that accepts one argument and pass it to a regular expression matching method to match specific cases.
* Cases to match:
  * `hbn`
  * `hbtn`
  * `hbttn`
  * `hbtttn`
  * `hbttttn`
* Usage: `./4-repetition_token_3.rb <argument>`

##### [5-beginning_and_end.rb](5-beginning_and_end.rb)
Ruby script that accepts one argument and pass it to a regular expression matching method to match a string that starts with `b`, ends with `n`, and can have any character in between.
* Usage: `./5-beginning_and_end.rb <argument>`

##### [6-phone_number.rb](6-phone_number.rb)
Ruby script that accepts one argument and pass it to a regular expression matching method to match a 10 digit phone number. (This task was given to us by Naha Jain, Senior Software Engineer at LinkedIn).
* Usage:
  ```
  $ ./6-phone_number.rb 4155049898 | cat -e
  4155049898$
  $ ./6-phone_number.rb " 4155049898" | cat -e
  $
  $ ./6-phone_number.rb "415 504 9898" | cat -e
  $
  $ ./6-phone_number.rb "415-504-9898" | cat -e
  $
  $
  ```

##### [7-OMG_WHY_ARE_YOU_SHOUTING.rb](7-OMG_WHY_ARE_YOU_SHOUTING.rb)
Ruby script that accepts one argument and pass it to a regular expression matching method to match only capital letters.
* Usage:
  ```
  $ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e
  ILOVESYSADMIN$
  $ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
  WHATSAY$
  $ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
  $
  $
  ```


## Authors
Kristen Loyd        [Github](https://github.com/KRLoyd) |  [LinkedIn](https://www.linkedin.com/in/kristen-loyd-34984a92)

## License
Public Domain, no copyright protection