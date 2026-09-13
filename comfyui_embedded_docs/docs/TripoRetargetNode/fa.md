# Tripo: هدف‌گذاری مجدد مدل ریگ‌شده

TripoRetargetNode یک انیمیشن پیش‌تنظیم را روی یک مدل سه‌بعدی ریگ‌شده موجود اعمال می‌کند. شناسه وظیفه (task ID) مدلی را می‌گیرد که قبلاً ریگ شده است، یک درخواست ری‌تارگت به API Tripo می‌فرستد و فایل انیمیشن‌دار حاصل را دانلود می‌کند. مدل انیمیشن‌دار می‌تواند به‌صورت GLB یا FBX برگردانده شود، همراه با هندسه مش اختیاری و پخش درجای اختیاری.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | بازه |
|-----------|-------------|-----------|----------|-------|
| `original_model_task_id` | شناسه وظیفه مدل سه‌بعدی ریگ‌شده قبلی برای ری‌تارگت. وظیفه ارجاع‌شده باید یک وظیفه rig باشد. | RIG_TASK_ID | بله | - |
| `animation` | پیش‌تنظیم انیمیشنی که باید روی مدل ریگ‌شده اعمال شود. انیمیشن‌های `preset:*` با هر دو مدل ریگ کار می‌کنند. انیمیشن‌های `preset:biped:*` برای ریگ‌های مدل v1.0-20240301 ساخته شده‌اند؛ یک ریگ v2.5 فقط chop، climb، dive، fall، hurt، idle، jump، run، shoot، slash، turn و walk را می‌پذیرد. | COMBO | بله | `"preset:idle"`<br>`"preset:walk"`<br>`"preset:run"`<br>`"preset:dive"`<br>`"preset:climb"`<br>`"preset:jump"`<br>`"preset:slash"`<br>`"preset:shoot"`<br>`"preset:hurt"`<br>`"preset:fall"`<br>`"preset:turn"`<br>`"preset:quadruped:walk"`<br>`"preset:hexapod:walk"`<br>`"preset:octopod:walk"`<br>`"preset:serpentine:march"`<br>`"preset:aquatic:march"`<br>به‌علاوه گزینه‌های اضافی `"preset:biped:*"` که در رابط کاربری نمایش داده می‌شوند |
| `out_format` | قالب فایل خروجی؛ نتیجه در خروجی متناظر می‌آید. (پیش‌فرض: glb) | COMBO | خیر | `"glb"`<br>`"fbx"` |
| `export_with_geometry` | هندسه مش را در خروجی بگنجان؛ وقتی خاموش باشد فقط اسکلت انیمیشن‌دار صادر می‌شود. (پیش‌فرض: True) | BOOLEAN | خیر | True<br>False |
| `animate_in_place` | انیمیشن را درجا پخش کن، بدون جابه‌جایی ریشه. (پیش‌فرض: False) | BOOLEAN | خیر | True<br>False |
| `auth_token_comfy_org` | توکن احراز هویت برای دسترسی به API Comfy.org (پارامتر پنهان). | AUTH_TOKEN_COMFY_ORG | خیر | - |
| `api_key_comfy_org` | کلید API برای دسترسی به سرویس Comfy.org (پارامتر پنهان). | API_KEY_COMFY_ORG | خیر | - |
| `unique_id` | شناسه یکتا برای رهگیری عملیات (پارامتر پنهان). | UNIQUE_ID | خیر | - |

توجه: انیمیشن‌های گروه `preset:*` با هر دو مدل ریگ کار می‌کنند. انیمیشن‌های گروه `preset:biped:*` برای ریگ‌های مدل v1.0-20240301 ساخته شده‌اند؛ یک ریگ v2.5 فقط chop، climb، dive، fall، hurt، idle، jump، run، shoot، slash، turn و walk را می‌پذیرد. اگر ریگ ارجاع‌شده با مشخصات Mixamo و نسخه مدلی که با `v1.0` شروع می‌شود ساخته شده باشد، فراخوانی ری‌تارگت با خطا شکست می‌خورد. قالب خروجی درخواستی باید GLB یا FBX باشد؛ اگر سرویس هر نوع فایل دیگری برگرداند، گره خطا می‌دهد.

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
|-------------|-------------|-----------|
| `model_file` | فایل مدل سه‌بعدی انیمیشن‌دار تولیدشده (فقط برای سازگاری با نسخه‌های قبلی). | STRING |
| `retarget task_id` | شناسه وظیفه برای رهگیری عملیات ری‌تارگت. | RETARGET_TASK_ID |
| `GLB` | مدل سه‌بعدی انیمیشن‌دار در قالب GLB. زمانی پر می‌شود که `out_format` برابر glb باشد. | FILE3DGLB |
| `FBX` | مدل سه‌بعدی انیمیشن‌دار در قالب FBX. زمانی پر می‌شود که `out_format` برابر fbx باشد. | FILE3DFBX |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/fa.md)

---
**Source fingerprint (SHA-256):** `4814858b940ece13f85010ff81fcdac0258fe8550aebd914be2613e8f40c0e5a`
