# Порівняння алгоритмів

## Жадібний алгоритм
Жадібний алгоритм вибирає найбільші монети, які можна використовувати для даної суми. Він швидкий і працює за O(n), де n — кількість номіналів монет. Проте цей алгоритм не завжди знаходить оптимальне рішення, якщо набір монет складний (наприклад, монети 9, 6, 1).

## Алгоритм динамічного програмування
Алгоритм динамічного програмування використовує табличку для зберігання мінімальної кількості монет для кожної суми від 0 до потрібної суми. Це дозволяє гарантувати оптимальне рішення, але алгоритм повільніший — його складність O(amount * k), де amount — сума, яку треба видати, а k — кількість номіналів монет.

## Висновки
Жадібний алгоритм підходить для простих наборів монет і швидкого розрахунку, але не завжди дає оптимальне рішення. Алгоритм динамічного програмування є більш повільним, але гарантує мінімальну кількість монет. Він ефективніший для складних наборів монет і великих сум.