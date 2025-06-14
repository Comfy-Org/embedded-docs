Извлекает все линии краёв с фотографий, как если бы вы использовали ручку для обводки фотографии, рисуя контуры и границы деталей объектов.

## Принцип работы

Представьте, что вы художник, которому нужно использовать ручку для обводки фотографии. Узел Canny действует как интеллектуальный помощник, помогая вам решить, где рисовать линии (края), а где нет.

Этот процесс похож на работу по отбору:

- **Верхний порог** — это "стандарт обязательной линии": будут нарисованы только очень очевидные и чёткие контурные линии, такие как контуры лиц людей и рамы зданий
- **Нижний порог** — это "стандарт определённо не рисовать линию": слишком слабые края будут игнорироваться, чтобы избежать рисования шума и бессмысленных линий
- **Промежуточная область**: края между двумя стандартами будут нарисованы вместе, если они соединяются с "обязательными линиями", но не будут нарисованы, если они изолированы

Конечный результат — чёрно-белое изображение, где белые части — это обнаруженные линии краёв, а чёрные части — области без краёв.

## Входные параметры

| Имя параметра | Тип данных | Метод ввода | Значение по умолчанию | Диапазон значений | Описание функции |
|---------------|------------|-------------|----------------------|-------------------|------------------|
| изображение | IMAGE | Подключение | - | - | Исходная фотография, требующая извлечения краёв |
| нижний_порог | FLOAT | Ручной ввод | 0.4 | 0.01-0.99 | Нижний порог, определяет, какие слабые края игнорировать. Более низкие значения сохраняют больше деталей, но могут производить шум |
| верхний_порог | FLOAT | Ручной ввод | 0.8 | 0.01-0.99 | Верхний порог, определяет, какие сильные края сохранить. Более высокие значения сохраняют только самые очевидные контурные линии |

## Результаты вывода

| Имя вывода | Тип данных | Описание |
|------------|------------|----------|
| изображение | IMAGE | Чёрно-белое изображение краёв, белые линии — обнаруженные края, чёрные области — части без краёв |

## Сравнение параметров

![Исходное изображение](./asset/input.webp)

![Сравнение параметров](./asset/compare.webp)

**Распространённые проблемы:**

- Разорванные края: попробуйте снизить верхний порог
- Слишком много шума: повысьте нижний порог
- Пропущены важные детали: снизьте нижний порог
- Края слишком грубые: проверьте качество и разрешение входного изображения
