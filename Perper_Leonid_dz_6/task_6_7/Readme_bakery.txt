Задание 7
Реализовать простую систему хранения данных о суммах продаж булочной. Данные хранить в файле bakery.csv в кодировке
utf-8. Нумерация записей начинается с 1.

Должно быть три скрипта с интерфейсом командной строки:
 - для записи данных (add_sale.py);
 - для вывода на экран записанных данных (view_sales.py);
 - для редактирования записи (edit_sale.py).

При записи передавать из командной строки значение суммы продаж.

Для чтения данных реализовать в командной строке следующую логику:
 - просто запуск скрипта — выводить все записи;
 - запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
 - запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный второму
   числу, включительно.

При редактировании передаём из командной строки номер записи и новое значение. При этом файл не должен читаться
целиком — обязательное требование. Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не
существует.
