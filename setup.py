try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__version__ = '0.2.0-dev'

DISTNAME = 'opcsim'
AUTHOR = 'David H Hagan'
AUTHOR_EMAIL = 'dhagan@mit.edu'
DESCRIPTION = "OPCSIM: simulating low-cost optical particle counters"
URL = 'https://dhhagan.github.io/opcsim/'
DOWNLOAD_URL = 'https://github.com/dhhagan/opcsim'

# Check dependencies
def check_dependencies():
    install_requires = []
    try:
        import numpy
    except ImportError:
        install_requires.append('numpy')

    try:
        import scipy
    except ImportError:
        install_requires.append('scipy')

    try:
        import matplotlib
    except ImportError:
        install_requires.append('matplotlib')

    try:
        import pandas
    except ImportError:
        install_requires.append('pandas')

    try:
        import seaborn
    except ImportError:
        install_requires.append('seaborn')

    return install_requires

if __name__ == '__main__':

    _install_requires = check_dependencies()

    setup(
        name=DISTNAME,
        version=__version__,
        packages=['opcsim', 'opcsim.equations'],
        description=DESCRIPTION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        maintainer=AUTHOR,
        maintainer_email=AUTHOR_EMAIL,
        license='MIT',
        url=URL,
        download_url=DOWNLOAD_URL,
        keywords=['atmospheric chemistry'],
        test_suite='tests',
        install_requires=_install_requires,
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Operating System :: OS Independent',
            'Intended Audience :: Science/Research',
            'Intended Audience :: Developers',
    		'Intended Audience :: Education',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
    		'Topic :: Scientific/Engineering :: Atmospheric Science',
    		'Topic :: Software Development',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ]
    )