# https://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation
# to install a virtualenvwrapper:
"""
    pip install --user virtualenvwrapper
"""

# find a virtualenvwrapper.sh executable:
"""
    find . -name virtualenvwrapper.sh
"""

# add to a ~/.bashrc file the following:
"""
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python
    export WORKON_HOME=$HOME/.virtualenvs
    source ./.local/bin/virtualenvwrapper.sh
""" # the path to virtualenvwrapper.sh might be different

# in the case of path resolution problems:
"""
    sudo cp ./.local/bin/virtualenvwrapper.sh /usr/bin/
"""

# create a virtualenv:
"""
    mkvirtualenv --python=<path to python> <name of venv>
"""

# remove virtualenv:
"""
    deactvate
    rmvirtualenv <name of venv>
"""

# some settings:
'''
    echo "export DJANGO_SETTINGS_MODULE='<path to settings>'" >> ~/.virtualenvs/<name of venv>/bin/postactivate
    echo "cd $(pwd)" >> ~/.virtualenvs/<name of venv>/bin/postactivate
'''

# to start working on in a virtualenv:
"""
    workon <name of virtualenv>
"""

# pip install virtualenvwrapper
# mkvirtualenv inprogress -p python3.8
# git clone git@gitlab.deployed.pl:inprogress/inprogress.git
# cd inprogress
# cp inprogress/settings/local.py inprogress/settings/local_settings.py
# echo "cd $(pwd)" >> ~/.virtualenvs/inprogress/bin/postactivate
# pip install -r requirements/local.txt
# pre-commit install
# pre-commit install --hook-type commit-msg



