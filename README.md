# Code Review Grader
Name is a work in progress

## Description
This software is the API backend for a code review grader. It features the ability for students to submit repositories of code, and for moderators/graders to score them. It will (eventually) be coupled with a frontend that centers on ease of use and responsiveness.

## Getting Started
If you want to work on the project, you need to do a couple things for setup first!

### Make a VirtualEnv
If you are new to Python development, you'll want to read up on [Virtual Environments.](https://docs.python-guide.org/dev/virtualenvs/) Basically, it's a way of containing all of your Python dependencies for a project without leaking them into the system Python modules. I like using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) for this task, but you are free to use whatever you'd like.

Once you have created a virtual environment for this project, change directory to the project root and install the dependencies by running:

``` bash
pip install -r requirements.txt
```

You'll also want to install `pylint` through either pip, or your system's package manager. Do us a favor and **don't** install it to your virtualenv. Instead, create your virtualenv with the `--system-site-packages` flag, so you can inherit it.
