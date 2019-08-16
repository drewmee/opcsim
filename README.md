[![PyPI version](https://badge.fury.io/py/opcsim.svg)](https://badge.fury.io/py/opcsim)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/dhhagan/opcsim/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/dhhagan/opcsim.svg?branch=master)](https://travis-ci.org/dhhagan/opcsim)
[![codecov](https://codecov.io/gh/dhhagan/opcsim/branch/master/graph/badge.svg)](https://codecov.io/gh/dhhagan/opcsim)
![Docker Pulls](https://img.shields.io/docker/pulls/dhhagan/opcsim)
![Docker Stars](https://img.shields.io/docker/stars/dhhagan/opcsim)

# opcsim

opcsim is a Python library for simulating low-cost Optical Particle Sensors (both Optical Particle Counters and Nephelometers) and
their response to various aerosol distributions.

## Documentation

Full online documentation can be found [here][1].

The docs include a [tutorial][2], an [example gallery][3], and an [API Reference][4].

In addition, documentation can be built locally for development purposes. To do so, please check out the complete details in the *contributing to opcsim* section of the documentation.

## Docker

If you are familiar with Docker, there is a Docker image available to get up and running with OPCSIM with ease. To get started 
with an ephemeral container with a jupyter lab interface, navigate to your preferred working directory and execute:

```sh
$ docker run --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v "$PWD":/home/joyvan/work dhhagan/opcsim:latest
```

Once executed, you should see the url with token in your terminal that will allow you to bring up the jupyter lab instance.


## Dependencies

Opcsim is supported for python3.5+.

Installation requires [scipy][5], [numpy][6], [pandas][7], [matplotlib][8],
and [seaborn][9].


## Installation

To install (or upgrade to) the latest stable release:

```sh

$ pip install opcsim [--upgrade]
```

To install the development version directly from GitHub using pip:

```sh

$ pip install git+https://github.com/dhhagan/opcsim.git
```

In addition, you can either clone the repository and install from source or download/unzip the zip file and install from source:

```sh

$ git clone https://github.com/dhhagan/opcsim.git
$ cd /opcsim
$ python setup.py install
```

## Testing

All tests are run via Travis.ci pre-merge. For results of these tests, please click on the link in the above travis badge. In addition, you can run tests locally.

To run tests locally:

```sh

$ python setup.py test
```

To run the tests locally using coverage (adds `coverage` as a dependency):

```sh

$ coverage run --source opcsim setup.py test

# View the report
$ coverage report -m
```


## Development

**opcsim** development takes place on GitHub. Issues and bugs can be submitted and tracked via the [GitHub Issue Tracker][10] for this repository. Versioning is done via the python [versioneer][11] library.


[1]: https://dhhagan.github.io/opcsim/
[2]: https://dhhagan.github.io/opcsim/tutorial.html
[3]: https://dhhagan.github.io/opcsim/examples/index.html
[4]: https://dhhagan.github.io/opcsim/api.html
[5]: https://www.scipy.org/
[6]: http://www.numpy.org/
[7]: http://pandas.pydata.org/
[8]: http://matplotlib.org/
[9]: https://seaborn.pydata.org/
[10]: https://github.com/dhhagan/opcsim/issues
[11]: https://github.com/warner/python-versioneer
