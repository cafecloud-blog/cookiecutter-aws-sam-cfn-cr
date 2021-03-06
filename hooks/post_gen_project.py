from __future__ import print_function

import os

TERMINATOR = "\x1b[0m"
INFO = "\x1b[1;33m [INFO]: "
SUCCESS = "\x1b[1;32m [SUCCESS]: "
HINT = "\x1b[3;33m"


def main():

    project_name = '{{ cookiecutter.project_name }}'

    print(SUCCESS +
          "Project initialization complete! Your new project folder is here: {}".
          format(project_name) + TERMINATOR)
    print(INFO +
          "{}/README.md contains information to get you started.".
          format(project_name) + TERMINATOR)
    print(INFO +
          "Author: Jonathan Pelletier (info@cafecloud.ca). For more AWS related content, visit https://cafecloud.ca" + TERMINATOR)

if __name__ == '__main__':
    main()