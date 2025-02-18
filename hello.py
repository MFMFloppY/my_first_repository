from datetime import datetime
from keyboard import is_pressed


def current_date():
    """Выводит текущее время по нажатию кнопки Enter."""

    while True:

        if is_pressed("Enter"):
            print(str(datetime.now().time())[:-7])
            
            break


if __name__ == "__main__":
    current_date()







