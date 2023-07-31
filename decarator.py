from time import perf_counter, sleep


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        res = func(*args, **kwargs)
        print(f'время выполнения:{perf_counter() - start_time}')
        return res

    return wrapper

class Timer:
    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = perf_counter()
        res = self.func(*args,**kwargs)
        finish_time = perf_counter() - start_time
        print(f'class timer время выполнения:{finish_time}')
        return res
@Timer
@timer
def doing():
    print('.')
    sleep(0.5)
    print('..')
    sleep(0.5)
    print('...')
doing()





