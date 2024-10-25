# Порівняння алгоритмів

## 1. Жадібний алгоритм (find_coins_greedy)

Цей алгоритм починає з найбільшого номіналу монет і намагається використовувати якомога більше монет цього номіналу, перш ніж перейти до наступного меншого. 

- **Складність**: O(k), де `k` — кількість номіналів монет.
- **Приклад використання**: Для суми 9999, жадібний алгоритм дав результат `{50: 199, 25: 1, 10: 2, 2: 2}`.
- **Час виконання**: ~4.05e-06 секунд.

## 2. Алгоритм динамічного програмування (find_min_coins)

Цей алгоритм використовує таблицю, щоб обчислити мінімальну кількість монет для кожного можливого значення суми від 0 до необхідної суми.

- **Складність**: O(n * k), де `n` — сума, що підлягає видачі, а `k` — кількість номіналів монет.
- **Приклад використання**: Для суми 9999, алгоритм динамічного програмування дав той же результат: `{50: 199, 25: 1, 10: 2, 2: 2}`.
- **Час виконання**: ~0.012 секунд.

## Висновки

- **Жадібний алгоритм**:
  - **Переваги**: Швидкість виконання та простота реалізації. Відмінно працює з класичним набором монет.
  - **Недоліки**: Не завжди гарантує оптимальне рішення для складніших наборів монет.

- **Алгоритм динамічного програмування**:
  - **Переваги**: Гарантує мінімальну кількість монет, що використовуються.
  - **Недоліки**: Значно повільніше для великих сум, особливо при великій кількості номіналів.

## Загальний висновок

Для стандартного набору монет жадібний алгоритм є більш ефективним, оскільки він швидший і в більшості випадків надає оптимальне рішення. Однак алгоритм динамічного програмування може бути кращим вибором у випадках, коли потрібно знайти мінімальну кількість монет, особливо для складніших наборів.