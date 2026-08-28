# FishAudioVoiceSelector

گره «انتخاب صدا Fish Audio» صدایی را از کتابخانه Fish Audio برای تولید گفتار (text-to-speech) انتخاب می‌کند. می‌توانید یکی از صداهای از پیش‌تنظیم‌شده را انتخاب کنید یا گزینه «custom» را برگزینید تا هر شناسه مدل صوتی دلخواهی از fish.audio وارد کنید.

## ورودی‌ها

### ورودی‌های مشترک

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
|-----------|-------------|-----------|----------|-------|
| `voice` | یک صدا انتخاب کنید، یا «custom» را برای وارد کردن هر شناسه مدل صدای fish.audio انتخاب کنید. | DYNAMIC_COMBO | بله | "Energetic Male (en)"<br>"Friendly Women (en)"<br>"Sarah (en)"<br>"Verity (en)"<br>"Polo (en)"<br>"Adrian (en)"<br>"E-girl (en)"<br>"Narrator (en)"<br>"Warm Conversational Voice (en)"<br>"Warm Storyteller (en)"<br>"Dramatic Character Male (en)"<br>"News Narrator (zh)"<br>"Lively Female (zh)"<br>"Gentle Female (zh)"<br>"Energetic Female (ja)"<br>"Calm Female (ja)"<br>"Calm Male (ja)"<br>"custom" |

گزینه‌های صدای از پیش‌تنظیم‌شده شامل صداهای انگلیسی (en)، چینی (zh) و ژاپنی (ja) هستند و به هیچ ورودی اضافی نیاز ندارند.

### ورودی‌های سفارشی

این ورودی‌ها زمانی ظاهر می‌شوند که `voice` روی «custom» تنظیم شده باشد.

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
|-----------|-------------|-----------|----------|-------|
| `voice_id` | شناسه مدل صدا از fish.audio، به عنوان مثال شناسه در https://fish.audio/m/<id>/ . پیش‌فرض: رشته خالی. | STRING | بله | هر شناسه مدل صدای معتبر Fish Audio |

توجه: وقتی `voice` روی «custom» تنظیم شود، `voice_id` پس از حذف فاصله‌های ابتدا و انتها نباید خالی باشد؛ در غیر این صورت گره خطای «Custom voice ID is empty.» صادر می‌کند. اگر گزینه صدای ناشناخته‌ای ارسال شود، گره خطای «Unknown voice» صادر می‌کند.

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
|-------------|-------------|-----------|
| `voice` | شناسه مدل صدای انتخاب‌شده Fish Audio. برای صداهای از پیش‌تنظیم‌شده، شناسه صدای متناظر از کتابخانه Fish Audio بازگردانده می‌شود؛ برای «custom»، مقدار واردشده `voice_id` بازگردانده می‌شود. | FISHAUDIO_VOICE |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioVoiceSelector/fa.md)

---
**Source fingerprint (SHA-256):** `4f99a58aa7e6054f58fe84e61e4e1008b17828bd97d71ef0a4009c4de4052bbd`
