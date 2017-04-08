# speedplot ![Travis CI Build Status](https://travis-ci.org/JacobHeater/speedplot.svg?branch=master)
A visualization tool that shows historical trends of your internet speeds.

## Setup

### Prerequisites

This is a Python application that leverages MongoDB. Therefore, you
must have Python 2 and MongoDB installed to continue with the rest of
the setup process. If you are not familiar with MongoDB, it would be
a good idea to read some of the documentation first, if you intend on
making any modifications to the code.

[Get Python 2](https://www.python.org/downloads/)

[Get MongoDB Community Edition](https://docs.mongodb.com/manual/administration/install-community/)

### Next Steps

1. Clone the repository.
1. From the command line run the following commands:
    1. `pip install -r packages.txt`
    1. Set `FLASK_APP` Environment Variable
        1. Windows `$env:FLASK_APP = 'server.py'`
        1. Bash `export FLASK_APP = 'server.py'`
    1. `flask run`
1. Open browser to `http://localhost:5000/`

## Preparing MongoDB

This application uses MongoDB to store the results of the speedtests for later
lookup. You ***must*** [install](https://docs.mongodb.com/getting-started/shell/installation/) 
MongoDB before running any of the test scripts.

1. Install MongoDB
2. Start the MongoDB background service
    1. Depending on your environment this may vary.
3. To ensure things are working correctly, run the `test` script.
    1. From the command line run `python scripts/test.py`

## Running Tests

**STOP!!!**

**Please read the following notes!**

When running commands in the command line, you must be run the
commands from the root folder of the project. See the example
below before running the following steps.

```sh
cd C:/Projects/Python/speedplot
```

Now that I have changed my path to the project root, I can continue
following the steps below.

---

You have the option to run all test cases conveniently using
the `test.py` script in the `scripts` directory. That is useful
for when you want to make sure that changes you have made have not
broken anything across the board. You can run all tests by executing the
following command in the command line.

```sh
python scripts/test.py
```

To run an individual test case in the `tests` directory, you can run
a command similar to the one below.

```sh
cd tests && python -m unittest entitytests
```

## Continuous Integration & Pull Requests

All pull requests that are submitted must pass the CI build, which runs
our test suite, at present. Pushing directly to `master` is forbidden, 
and has been disabled. All pull requests require at least one review.

## Concerns/Issues

If you have any issues, please use the issue tracker to raise any concerns
you may have.

## License

---

MIT License

Copyright (c) 2017 Jacob Heater

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
