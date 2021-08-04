"""
Checking version:

Windows:
    python -m pip --version
Linux/MacOS:
    python3 -m pip --version


Making sure pip is up to date:

Windows:
    python -m pip install --upgrade pip
Linux/MacOs:
    python3 -m pip install --user --upgrade pip

Installing virtualenv:

Windows:
    python -m pip install --user virtualenv
Linux:
    python3 -m pip install --user virtualenv

Using virtual environment:

Windows:
    python -m venv env
Linux/MacOS:
    python3 -m venv env

!!! Note You should exclude your virtual environment directory
 from your version control system using .gitignore or similar.

Before you can start installing or using packages in your virtual
environment you’ll need to activate it. Activating a virtual environment
will put the virtual environment-specific python and pip executables into your shell’s PATH.

Activating virtual environment:

Windows:
    .\env\Scripts\activate
Linux/MacOs:
    source env/bin/activate

Checking location of your python interpreter:

Windows:
    where python
Linux/MacOs:
    which python

As long as your virtual environment is activated pip will install packages
into that specific environment and you’ll be able to import and use packages
in your Python application.

Leaving virtual environment
    deactivate

Installing packages:
    pip install package_name

pip allows you to specify which version of a package to install
using version specifiers. For example, to install a specific version of requests:

    pip install requests==2.18.4

To install the latest 2.x release of requests:

    pip install requests>=2.0.0,<3.0.0

To install pre-release versions of packages, use the --pre flag:

    pip install --pre requests

Installing extras:

Some packages have optional extras.
You can tell pip to install these by specifying the extra in brackets:

    pip install requests[security]

Upgrading packages:

pip can upgrade packages in-place using the --upgrade flag. For example,
to install the latest version of requests and all of its dependencies:

    pip install --upgrade requests

Using requirements files

Instead of installing packages individually, pip allows you to declare all
dependencies in a Requirements File. For example you could create a requirements.txt file containing:

    requests==2.18.4
    google-auth==1.1.0

And tell pip to install all of the packages in this file using the -r flag:

    pip install -r requirements.txt

Freezing dependencies

Pip can export a list of all installed packages and their versions using the freeze command:

    pip freeze

Requirements files are used to hold the result from pip freeze
for the purpose of achieving repeatable installations.
In this case, your requirement file contains a pinned version of everything that was installed when pip freeze was run.

    pip freeze > requirements.txt
    pip install -r requirements.txt



"""
