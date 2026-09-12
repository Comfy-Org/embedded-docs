# Загрузить CLIP

Узел CLIPLoader загружает модель текстового энкодера (CLIP, T5 или аналогичную) из файла, делая её доступной для использования в других узлах, которым требуется преобразование текстовых подсказок в числовые представления. Он поддерживает множество архитектур моделей, каждая из которых требует определённого типа энкодера.

## Входы

| Параметр | Описание | Тип данных | Обязательный | Диапазон |
|-----------|-------------|-----------|----------|-------|
| `название_clip` | Имя файла модели текстового энкодера для загрузки. Это должен быть файл, расположенный в каталоге `ComfyUI/models/text_encoders/`. | STRING | Да | Список файлов, найденных в папке `text_encoders` |
| `тип` | Тип архитектуры загружаемой модели. Определяет, какой именно вариант энкодера использовать (по умолчанию: `"stable_diffusion"`). | COMBO | Да | `"stable_diffusion"`<br>`"stable_cascade"`<br>`"sd3"`<br>`"stable_audio"`<br>`"mochi"`<br>`"ltxv"`<br>`"pixart"`<br>`"cosmos"`<br>`"lumina2"`<br>`"wan"`<br>`"hidream"`<br>`"chroma"`<br>`"ace"`<br>`"omnigen2"`<br>`"qwen_image"`<br>`"hunyuan_image"`<br>`"flux2"`<br>`"ovis"`<br>`"longcat_image"`<br>`"cogvideox"`<br>`"lens"`<br>`"pixeldit"`<br>`"ideogram4"`<br>`"boogu"`<br>`"krea2"`<br>`"joyimage"`<br>`"mage"`<br>`"minimax"`<br>`"yue2"` |
| `устройство` | Устройство, на которое загружается модель. `"default"` использует GPU, если он доступен, а `"cpu"` принудительно загружает на CPU. Это расширенная опция (по умолчанию: `"default"`). | COMBO | Нет | `"default"`<br>`"cpu"` |

### Поддерживаемые соответствия типов и энкодеров

Параметр `type` выбирает правильный энкодер для заданной архитектуры модели. Ниже приведены основные соответствия:

| Тип | Энкодер |
|------|---------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl / clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cogvideox | t5 xxl (дополнение до 226 токенов) |
| cosmos | old t5 xxl |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |
| hidream | llama-3.1 (рекомендуется) или t5 |
| omnigen2 | qwen vl 2.5 3B |
| joyimage | qwen3-vl 8B |
| lens | gpt-oss-20b |
| pixeldit | gemma 2 2B elm |
| minimax | MiniMax H3 Qwen3-VL или Music3 Qwen/RVQ |

## Выходы

| Имя выхода | Описание | Тип данных |
|-------------|-------------|-----------|
| `CLIP` | Загруженная модель текстового энкодера, готовая к подключению к другим узлам для кодирования текста и кондиционирования. | CLIP |

> Эта документация была создана с помощью ИИ. Если вы обнаружите ошибки или у вас есть предложения по улучшению, пожалуйста, внесите свой вклад! [Редактировать на GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPLoader/ru.md)

---
**Source fingerprint (SHA-256):** `6df608d500520d9414acd82d9fd509b1e211a8385202cefd5579e8a8f397bc64`
