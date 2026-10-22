import time
class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc, tb):
        print(time.perf_counter() - self.start)
with Timer():
    sum(range(10**6))








#import time
#from contextlib import contextmanager

#@contextmanager
#def timer():
#    start = time.perf_counter()
#    yield
#    print(time.perf_counter() - start)

#with timer():
#   sum(range(10**6))