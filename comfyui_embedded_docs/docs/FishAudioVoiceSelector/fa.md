# FishAudioVoiceSelector

## ورودی‌ها

### ورودی‌های عمومی

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
|-----------|-------------|-----------|----------|-------|
| `voice` | یک صدا انتخاب کنید، یا «custom» را برای وارد کردن هر شناسه مدل صوتی fish.audio انتخاب کنید. | DYNAMIC_COMBO | بله | "Energetic Male (en)"<br>"Friendly Women (en)"<br>"Sarah (en)"<br>"Verity (en)"<br>"Polo (en)"<br>"Adrian (en)"<br>"E-girl (en)"<br>"Narrator (en)"<br>"Warm Conversational Voice (en)"<br>"Warm Storyteller (en)"<br>"Dramatic Character Male (en)"<br>"News Narrator (zh)"<br>"Lively Female (zh)"<br>"Gentle Female (zh)"<br>"Energetic Female (ja)"<br>"Calm Female (ja)"<br>"Calm Male (ja)"<br>"custom" |

گزینه‌های صوتی پیش‌تنظیم شامل صداهای انگلیسی (en)، چینی (zh) و ژاپنی (ja) هستند و به هیچ ورودی اضافی نیاز ندارند.

### ورودی‌های سفارشی

این ورودی‌ها زمانی ظاهر می‌شوند که `voice` روی «custom» تنظیم شده باشد.

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
|-----------|-------------|-----------|----------|-------|
| `voice_id` | شناسه مدل صوتی از fish.audio، مثلاً شناسه در https://fish.audio/m/<id>/. پیش‌فرض: رشته خالی. | STRING | بله | هر شناسه مدل صوتی معتبر Fish Audio |

توجه: وقتی `voice` روی «custom» تنظیم می‌شود، `voice_id` نباید پس از حذف فاصله‌های خالی خالی باشد؛ در غیر این صورت گره خطای «Custom voice ID is empty.» را صادر می‌کند. اگر یک گزینه صوتی ناشناخته ارسال شود، گره خطای «Unknown voice» را صادر می‌کند.

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
|-------------|-------------|-----------|
| `voice` | شناسه مدل صوتی انتخاب‌شده Fish Audio. برای صدای پیش‌تنظیم، شناسه صوتی متناظر از کتابخانه Fish Audio برگردانده می‌شود؛ برای «custom»، مقدار `voice_id` واردشده برگردانده می‌شود. | FISHAUDIO_VOICE |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioVoiceSelector/fa.md)

---
**Source fingerprint (SHA-256):** `4f99a58aa7e6054f58fe84e61e4e1008b17828bd97d71ef0a4009c4de4052bbd`
