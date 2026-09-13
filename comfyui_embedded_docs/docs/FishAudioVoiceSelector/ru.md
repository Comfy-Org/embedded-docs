# Выбор голоса Fish Audio

Узел Fish Audio Voice Selector выбирает голос из библиотеки Fish Audio для синтеза речи. Вы можете выбрать один из встроенных предустановленных голосов или выбрать "custom", чтобы ввести любой ID голосовой модели из fish.audio.

## Входы

### Общие входы

| Параметр | Описание | Тип данных | Обязательный | Диапазон |
|-----------|-------------|-----------|----------|-------|
| `voice` | Выберите голос или 'custom', чтобы ввести любой ID голосовой модели fish.audio. | DYNAMIC_COMBO | Да | "Energetic Male (en)"<br>"Friendly Women (en)"<br>"Sarah (en)"<br>"Verity (en)"<br>"Polo (en)"<br>"Adrian (en)"<br>"E-girl (en)"<br>"Narrator (en)"<br>"Warm Conversational Voice (en)"<br>"Warm Storyteller (en)"<br>"Dramatic Character Male (en)"<br>"News Narrator (zh)"<br>"Lively Female (zh)"<br>"Gentle Female (zh)"<br>"Energetic Female (ja)"<br>"Calm Female (ja)"<br>"Calm Male (ja)"<br>"custom" |

Предустановленные варианты голосов охватывают английские (en), китайские (zh) и японские (ja) голоса и не требуют дополнительных входов.

### Пользовательские входы

Эти входы появляются, когда для `voice` установлено значение "custom".

| Параметр | Описание | Тип данных | Обязательный | Диапазон |
|-----------|-------------|-----------|----------|-------|
| `voice_id` | ID голосовой модели из fish.audio, например ID в https://fish.audio/m/<id>/. По умолчанию: пустая строка. | STRING | Да | Любой допустимый ID голосовой модели Fish Audio |

Примечание. Когда для `voice` установлено значение "custom", `voice_id` не должен быть пустым после удаления пробелов; иначе узел выдаёт ошибку "Custom voice ID is empty." Если передан нераспознанный вариант голоса, узел выдаёт ошибку "Unknown voice".

## Выходы

| Имя выхода | Описание | Тип данных |
|-------------|-----------|-----------|
| `voice` | ID выбранной голосовой модели Fish Audio. Для предустановленного голоса возвращается соответствующий ID голоса из библиотеки Fish Audio; для "custom" возвращается введённое значение `voice_id`. | FISHAUDIO_VOICE |

> Эта документация была создана с помощью ИИ. Если вы обнаружите ошибки или у вас есть предложения по улучшению, пожалуйста, внесите свой вклад! [Редактировать на GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioVoiceSelector/ru.md)

---
**Source fingerprint (SHA-256):** `4f99a58aa7e6054f58fe84e61e4e1008b17828bd97d71ef0a4009c4de4052bbd`
