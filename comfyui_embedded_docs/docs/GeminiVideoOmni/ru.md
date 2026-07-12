# Google Gemini Omni (Video)

Генерируйте видео со звуком по текстовому промпту с помощью модели Google Gemini Omni Flash. Дополнительно можно добавить референсные изображения и/или видео для направления или редактирования результата. Опишите желаемую длительность (3-10 сек) и соотношение сторон (16:9 или 9:16) прямо в промпте.

## Входы

| Параметр | Описание | Тип данных | Обязательный | Диапазон |
|-----------|-------------|-----------|----------|-------|
| `model` | Модель Gemini video, используемая для генерации видео. | MODEL | Yes | "Omni Flash" |
| `seed` | Seed управляет тем, будет ли узел перезапущен; результат всегда недетерминированный независимо от seed. | INT | Yes | 0 to 2147483647 |
| `prompt` | The text prompt describing the video to generate. Must be at least one non-whitespace character after stripping leading/trailing whitespace. | STRING | Yes | Minimum 1 character after stripping whitespace |
| `images` | Optional reference images to guide the video generation. Maximum of 14 images total. | IMAGE | No | Multiple images allowed (max 14) |
| `videos` | Optional reference videos to guide or edit the video generation. Maximum of 3 videos, each up to 10 seconds. | VIDEO | No | Multiple videos allowed (max 3, each max 10s) |
| `temperature` | Controls randomness in generation (default: 1.0). | FLOAT | No | 0.0 to 2.0 |
| `top_p` | Nucleus sampling parameter (default: 0.95). | FLOAT | No | 0.0 to 1.0 |

## Выходы

| Имя выхода | Описание | Тип данных |
|-------------|-------------|-----------|
| `VIDEO` | The generated video with audio from the Gemini model. | VIDEO |
| `STRING` | Any text response from the model, such as reasoning or explanations. | STRING |

> Эта документация была создана с помощью ИИ. Если вы обнаружите ошибки или у вас есть предложения по улучшению, пожалуйста, внесите свой вклад! [Редактировать на GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/ru.md)

---
**Source fingerprint (SHA-256):** `046842b7ec736283bba355aaa038b02fcf2416020f5f7aee7b0150d2a05bcbe6`
