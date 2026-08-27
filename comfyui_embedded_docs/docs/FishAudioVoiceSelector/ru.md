# FishAudioVoiceSelector

Узел Fish Audio Voice Selector выбирает голос из библиотеки Fish Audio для генерации речи (text-to-speech). Вы можете выбрать один из встроенных предустановленных голосов или выбрать «custom», чтобы ввести любой ID модели голоса с fish.audio.

## Входы

### Общие входы

| Параметр | Описание | Тип данных | Обязательный | Диапазон |
|-----------|-------------|-----------|----------|-------|
| `voice` | Выберите голос или «custom», чтобы ввести любой ID модели голоса fish.audio. | DYNAMIC_COMBO | Да | "Energetic Male (en)"<br>"Friendly Women (en)"<br>"Sarah (en)"<br>"Verity (en)"<br>"Polo (en)"<br>"Adrian (en)"<br>"E-girl (en)"<br>"Narrator (en)"<br>"Warm Conversational Voice (en)"<br>"Warm Storyteller (en)"<br>"Dramatic Character Male (en)"<br>"News Narrator (zh)"<br>"Lively Female (zh)"<br>"Gentle Female (zh)"<br>"Energetic Female (ja)"<br>"Calm Female (ja)"<br>"Calm Male (ja)"<br>"custom" |

Предустановленные голоса охватывают английский (en), китайский (zh) и японский (ja) и не требуют дополнительных входных данных.

### Пользовательские входы

Эти входы появляются, когда параметр `voice` установлен в «custom».

| Параметр | Описание | Тип данных | Обязательный | Диапазон |
|-----------|-------------|-----------|----------|-------|
| `voice_id` | ID модели голоса с fish.audio, например ID из https://fish.audio/m/<id>/. По умолчанию: пустая строка. | STRING | Да | Любой допустимый ID модели голоса Fish Audio |

Примечание: когда параметр `voice` установлен в «custom», `voice_id` не должна быть пустой после удаления пробельных символов; в противном случае узел вызывает ошибку «Custom voice ID is empty.». Если передана нераспознанная опция голоса, узел вызывает ошибку «Unknown voice».

## Выходы

| Имя выхода | Описание | Тип данных |
|-------------|-------------|-----------|
| `voice` | Выбранный ID модели голоса Fish Audio. Для предустановленного голоса возвращается соответствующий ID голоса из библиотеки Fish Audio; для «custom» возвращается введённое значение `voice_id`. | FISHAUDIO_VOICE |

> Эта документация была создана с помощью ИИ. Если вы обнаружите ошибки или у вас есть предложения по улучшению, пожалуйста, внесите свой вклад! [Редактировать на GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioVoiceSelector/ru.md)

---
**Source fingerprint (SHA-256):** `4f99a58aa7e6054f58fe84e61e4e1008b17828bd97d71ef0a4009c4de4052bbd`
