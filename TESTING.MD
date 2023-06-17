# Testing

Return back to the [README.md](README.md) file.

## Code Validation
### Python

I have used the recommended [CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| run.py | [CI PEP8](https://pep8ci.herokuapp.com/) | ![screenshot](documentation/linter1.png) | One line length error, given that this is a complex lambda function it has been marked NOQA. |
| rooms.py | [CI PEP8](https://pep8ci.herokuapp.com/) | ![screenshot](documentation/linter2.png) | Some errors found with line length, however there is no effect on gameplay. |


## Lighthouse Audit


I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | Desktop | ![screenshot](documentation/lighthouse1.png) | No warnings |
| Home | Mobile | ![screenshot](documentation/lighthouse2.png) | Minor performance warning |

## Defensive Programming

- Users must enter a valid letter/word/string when prompted otherwise one of the things underneath will happen.

| Screenshot | Notes |
| --- | --- |
| ![screenshot](documentation/error1.png) | You cannot enter anything other than directions (dependent on location, directions will change). |
| ![screenshot](documentation/error2.png) | You cannot insert numbers in the name field.|
| ![screenshot](documentation/error3.png) | You cannot include special characters in the name field.|
| ![screenshot](documentation/unlucky.png) | Players cannot continue at this point|

- The application has been tested numerous times to ensure that the user cannot break it by inputting the wrong commands.


## Bugs

No known bugs

---