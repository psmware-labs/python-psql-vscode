#!/usr/bin/env python
import fileinput
from pathlib import Path


#  Start the application
def main():
    the_app = input('Please enter the name of the GitHub Repository '
                    'for this application (excluding your github id):\n')
    Description = input('\nPlease enter the brief description '
                        'that was  the GitHub Repository'
                        ' to the nature of the application:\n')
    Application = 'This script will now configure the cloned template ' \
                  'for your application: \n\n' \
                  'App-Name:      {}\n' \
                  'Description:   {}\n'
    print(Application.format(the_app, Description))

    continueSetup = input('Would you like to proceed with the setup '
                          ' using the provided info?\n'
                          'Yes/Y or No/N: ').lower()

    if continueSetup == 'yes' or continueSetup == 'y':
        # Now opening the devcontainer definition file to start renaming the
        # Template services to the name of the application.
        modfile = Path(".devcontainer/devcontainer.json")
        ModifyFile(modfile, 'My Dev Env', the_app.upper())
        ModifyFile(modfile, 'template-app', the_app + '-app')
        # Now opening the devcontainer environment file to start renaming the
        # Template services to the name of the application.
        modfile = Path(".devcontainer/devcontainer.env")
        ModifyFile(modfile, 'template', the_app)
        # Now opening the devcontainer docker-compose file to start
        # Template services to the name of the application.
        modfile = Path(".devcontainer/docker-compose.yml")
        ModifyFile(modfile, 'template-app', the_app + '-app')
        ModifyFile(modfile, 'template-dbadmin', the_app + '-dbadmin')
        ModifyFile(modfile, 'template-db', the_app + '-db')

        # Now opening the README.md file to create a stub
        # for the application.
        readmeHandle = open("README.md", "w")
        title = "# {}"
        readmeHandle.writelines([title.format(the_app),
                                 '\n\n',
                                 Description,
                                 '\n'])
        readmeHandle.close()


def ModifyFile(filename, text_to_search, replacement_text):
    """ This function opens a file and replaces found text\
        with the replacment text"""
    with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(text_to_search, replacement_text), end='')


# |
# |
# The Main Entry point of the setup file
# |
if __name__ == "__main__":
    main()
