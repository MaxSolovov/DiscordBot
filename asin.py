import asyncio
import random


async def task(name):
    print(f'{name} задача началась')
    a = random.randint(1,8)
    await asyncio.sleep(a)
    print(f'Прошло {a} секунд. {name} задача завершилась')


async def main():
    await asyncio.gather(
        task('Первая'),
        task('Вторая'),
    )
    print("Все задачи выполнены ")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())