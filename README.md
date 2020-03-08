# flake8-os-walk

Checks for uses of os.walk() without passing the onerror param.

## Why

The [os.walk()](https://docs.python.org/3/library/os.html#os.walk) function has a [major-gotcha](https://blog.toolchain.com/os-walk-has-a-major-gotcha/) which means it will silently fail (yield nothing) if the path passed to it is invalid (doesn't exits).

Also, this is an excuse for me to write my first flake8 plugin.
