import view
import model
import logging


# вывод ошибок уровня инфо в консоль
# logging.basicConfig(level=logging.INFO)


# # Вывод ошибок в файл
logging.basicConfig(filename='Seminars/Seminar_7/log.txt', filemode='a', format='%(asctime)s, %(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S', level=logging.INFO, encoding='utf-8')


def main():
    select = view.show_menu()
    if select == '1':
        logging.info('Выбран режим калькулятора')
        x = view.get_example()
        res = model.calc(x)
        view.show_res(res)
        logging.info('Выполнено корректно')
    if select == '2':
        logging.info('Выбран режим конвертера')
        x = view.get_convert()
        res = model.convert(x)
        view.show_res_m(res)
        logging.info('Выполнено корректно')
