# minirhizpreprocessing



## Installing the module

We recommend installing this module into a dedicated Python virtual environment to avoid dependency
conflicts or polluting the global Python distribution.

### From a wheel

First, it is recommended to install the version of the dependencies known to work with the
``requirements.txt`` file with pip:

```shell
pip install -r requirements.txt
```

Then, simply install the wheel with pip:

```shell
pip install minirhizpreprocessing-X.Y.Z-py3-none-any.whl
```

### From source

For this install to work, **you need to have the git command available in your terminal**.

First, install the version of the dependencies known to work with the ``requirements.txt`` file
with pip, then install the module from the local source with pip:

```shell
pip install -r requirements.txt
pip install .
```

### Checking the installation

Now, you should have a new command ``minirhizpreprocessing`` available in your terminal
and in any directory when the corresponding vitual environment is activated. You can test it with
the following command to display the help:

```shell
minirhizpreprocessing --help
```

## Installing for development

If you need to work on the module for maintenance or updates, always use a dedicated Python virtual
environment. First install the dependencies with pip, then install the module in development mode
with pip. As for the source installation, the git command must be available in your terminal.

```shell
pip install -r requirements.txt
pip install -e .[dev]
```

The ``[dev]`` part corresponds to the extra dependencies used during development. In this case, it
will also install [Pylint](https://pylint.readthedocs.io/en/latest/) for doing static code analysis.

Pylint can analyze the entire source code with the following command:

```shell
pylint src/minirhizpreprocessing
```

In development mode, pip will install a reference to the source code instead of doing a full install.
This will allow to update the source code and directly see the modified behavior with the installed
``minirhizpreprocessing`` command.

## Building the Docker image

First, create a directory named ``wheels`` into the root directory. Place any needed private wheels
inside it before building the image.

This project contains a ``Makefile`` to build the Docker image on **Linux**:

```shell
make build
```

Once done, you should have a new Docker image called ``minirhizpreprocessing`` that you can
directly use to run the module. For example:

```shell
docker run --rm minirhizpreprocessing --help
```
