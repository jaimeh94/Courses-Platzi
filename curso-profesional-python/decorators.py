from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Pasaron {time_elapsed.total_seconds()} segundos')
    return wrapper


@execution_time
def random_func():
    for _ in range(1, 10000000):
        pass


@execution_time
def suma(a: int, b: int) -> int:
    return a + b

@execution_time
def saludo(nombre="Cesar"):
    print("Hola " + nombre)

random_func()
suma(5,5)
saludo('Jaime')