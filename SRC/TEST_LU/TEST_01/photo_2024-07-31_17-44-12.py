class Repeater(object):
    def __init__(self, x):
        self.repeat = x

    def __call__(self, func):
        def wrapper (*args, **kwargs):
            result = None
            for in range(self.repeat):
                result = func(*args, **kwargs)
            return result
        return wrapper

@Repeater(5)
def func():
    if not hasattr(func, 'i'):
        func.i = 0
    func.i += 1

    print(f'Выполнясь {func.i} paз')

func()

# Выполняюсь 1 раз
# Выполняюсь 2 раз
# Выполняюсь 3 раз
# Выполняюсь 4 раз
# Выполняюсь 5 раз