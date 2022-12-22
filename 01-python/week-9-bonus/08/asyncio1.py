import time
import asyncio

async def main():
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} Goodbye!')
    loop.stop()

# 1. Прежде всего необходим экземпляр цикла событий. Если он уже запущен, мы можем его получить
#    с помощью get_event_loop. Если нет - нужно создать новый
def get_or_create_loop():
    loop = asyncio.get_event_loop()
    if loop.is_closed():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    return loop

loop = get_or_create_loop()
print("Created loop")
# 2. Создаем задание. Этот код пока не исполняет корутину main, 
#    но регистрирует ее в цикле событий
loop.create_task(main())
print("Created task main and now run loop")
# 3. Запускаем цикл событий на исполнение без критериев остановки цикла
loop.run_forever()
# 4. Выберем все задания, относящиеся к данному циклу
pending = asyncio.all_tasks(loop=loop)
# 5. Функция gather собирает все пока еще не законченные задания и оборачивает их в футуры
group = asyncio.gather(*pending, return_exceptions=True)
print("Gathered tasks")
# 6. run_until_complete завершает все поданные задания
loop.run_until_complete(group)
# 7. останавливаем цикл событий
loop.close()