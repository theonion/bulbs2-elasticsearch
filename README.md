# bulbs2-elasticsearch

> your search is over

`bulbs2-elasticsearch` is a companion app to [bulbs2](https://github.com/theonion/bulbs2) that enables multi-mapping 
searches.


## Getting the Code

You can clone the code via _git_:

```bash
$ git clone https://github.com/theonion/bulbs2-elasticsearch.git
```

Alternatively, if you just want to use it in a Django application, you can install it via _pip_:

```bash
$ pip install -e git+https://github.com/theonion/bulbs2-elasticsearch.git#egg=bulbs2-elasticsearch
```

__Note:__ since this is a far-afield project that may or may not be brought to production, I am refraining from adding 
it to the PyPI index.


## Testing the Code

To run the tests, clone the repository from GitHub (see steps above). You should then create a virtual environment with 
Python 3 and install the project to that:

```bash
$ cd /path/to/virtualenvs
$ virtualenv -p python3 bulbs2-elasticsearch
$ source bulbs2/bin/activate
$ cd /path/to/bulbs2-elasticsearch
$ python setup.py install
$ pip install -r requirements-dev.txt
$ py.test tests
```

If you don't have Python 3 on your system, you can _brew_ install it:

```bash
$ brew install python3
$ brew linkapps
```

If you don't have _virtualenv_ on you system, you can _pip_ install that:

```bash
$ pip install virtualenv
```

If you don't have _brew_ installed, you can get that via:

```bash
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

If you don't have _pip_, install Python 2 and Python 3 via _brew_:

```bash
$ brew install python2 python3
$ brew linkapps
```
