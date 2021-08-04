try:
    from packages.some_package.some_module import A, some_function, GLOBAL_VAR
except ImportError as e:
    print(e)

if __name__ == "__main__":
    some_function()
