from datetime import datetime
from keyboard import is_pressed


def current_date_and_time() -> str:
    """Выводит текущие дату и время по нажатию кнопки Enter."""

    cur_date_and_time = str(datetime.now())
    while True:

        if is_pressed("Enter"):

            date = f"Сейчас {cur_date_and_time[8:10]} month {cur_date_and_time[0:4]} года"
            
            time = f"{cur_date_and_time[11:13]} часов, {cur_date_and_time[14:16]} минут, {cur_date_and_time[17:19]} секунд"

            return date, time


def main() -> None:
    """Вывод результата."""

    d, t = current_date_and_time()
    print(d, t, sep="\n")


if __name__ == "__main__":
    main()

