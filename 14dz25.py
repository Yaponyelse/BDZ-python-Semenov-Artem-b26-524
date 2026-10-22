from contextlib import contextmanager
@contextmanager
def log_operation(path, name):
    with open(path, "a") as f:
        f.write(f"START: {name}\n")
        try:
            yield
        except:
            f.write(f"ERROR: {name}\n")
            raise
        else:
            f.write(f"END: {name}\n")