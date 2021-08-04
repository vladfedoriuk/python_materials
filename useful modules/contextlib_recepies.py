import contextlib
from contextlib import contextmanager
from io import StringIO

"""Supporting a variable number of context managers"""
try:

    with contextlib.ExitStack() as stack:
        for resource in resources:
            stack.enter_context(resource)
        if need_special_resource():
            special = acquire_special_resource()
            stack.callback(release_special_resource, special)
            # Perform operations that use the acquired resources

except NameError:
    pass

"""Catching exceptions from __enter__ methods"""
try:

    stack = contextlib.ExitStack()
    try:
        x = stack.enter_context(cm)
    except Exception:
        # handle __enter__ exception
        pass
    else:
        with stack:
            pass
        # Handle normal case

except NameError:
    pass

"""Replacing any use of try-finally and flag variables"""
try:

    with contextlib.ExitStack() as stack:
        stack.callback(cleanup_resources)
        result = perform_operation()
        if result:
            stack.pop_all()  # we don't need to clean up a resource if it doesn't exist

except NameError:
    pass

try:

    class Callback(contextlib.ExitStack):
        def __init__(self, callback, *args, **kwds):
            super(Callback, self).__init__()
            self.callback(callback, *args, **kwds)

        def cancel(self):
            self.pop_all()

    with Callback(cleanup_resources) as cb:
        result = perform_operation()
        if result:
            cb.cancel()

except NameError:
    pass

try:
    from contextlib import ExitStack

    with ExitStack() as stack:

        @stack.callback
        def cleanup_resources():
            ...

        result = perform_operation()
        if result:
            stack.pop_all()

except NameError:
    pass

"""Single use, reusable and reentrant context managers"""


# single use
@contextmanager
def singleuse():
    print("before")
    yield
    print("after")


cm = singleuse()

with cm:
    print("in")
try:
    with cm:
        print("would not be printed")
except Exception:
    pass


# reentrant
stream = StringIO()
context = contextlib.redirect_stdout(stream)
with context:
    print("this will be in stream")
with context:
    print("this also will be in stream")

print("this will be in stdout")
print(stream.getvalue())

"""
Reusable context managers
Distinct from both single use and reentrant context managers are “reusable” context managers 
(or, to be completely explicit, “reusable, but not reentrant” context managers, 
since reentrant context managers are also reusable). 
These context managers support being used multiple times, but will fail 
(or otherwise not work correctly) 
if the specific context manager instance has already been used in a containing with statement.
"""

stack = contextlib.ExitStack()
with stack:
    stack.callback(print, "in the first context")
    print("leaving the first context")

with stack:
    stack.callback(print, "in the second")
    print("leaving the second context")

with stack:
    stack.callback(print, "outer context")
    with stack:
        stack.callback(print, "inner callback")
        print("leaving inner context")
    print("leaving the outer context")

with ExitStack() as stack:
    stack.callback(print, "callback from outer context")
    with ExitStack() as stack:
        stack.callback(print, "callback from inner context")
        print("leaving inner context")
    print("leaving outer context")


with ExitStack() as stack:

    @stack.callback
    def clean_up():
        print("clean up was made")

    resource = None
    if resource:
        stack.pop_all()
