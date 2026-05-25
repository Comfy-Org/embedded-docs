> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAnimation/fa.md)

### مرور کلی

گره Preview3DAnimation عمدتاً برای پیش‌نمایش خروجی‌های مدل سه‌بعدی استفاده می‌شود. این گره دو ورودی دریافت می‌کند: یکی `camera_info` از گره Load3D و دیگری مسیر فایل مدل سه‌بعدی. مسیر فایل مدل باید در پوشه `ComfyUI/output` قرار داشته باشد.

**فرمت‌های پشتیبانی‌شده**
در حال حاضر، این گره از چندین فرمت فایل سه‌بعدی از جمله `.gltf`، `.glb`، `.obj`، `.fbx` و `.stl` پشتیبانی می‌کند.

**تنظیمات برگزیده گره‌های سه‌بعدی**
برخی تنظیمات برگزیده مرتبط با گره‌های سه‌بعدی را می‌توان در منوی تنظیمات ComfyUI پیکربندی کرد. لطفاً برای تنظیمات مربوطه به مستندات زیر مراجعه کنید:
[منوی تنظیمات](https://docs.comfy.org/interface/settings/3d)

## ورودی‌ها

| نام پارامتر | نوع          | توضیحات                                   |
| ----------- | ------------ | ----------------------------------------- |
| camera_info | LOAD3D_CAMERA | اطلاعات دوربین                            |
| model_file  | STRING       | مسیر فایل مدل در مسیر `ComfyUI/output/`   |

## توضیحات ناحیه بوم

در حال حاضر، گره‌های مرتبط با سه‌بعدی در فرانت‌اند ComfyUI از یک مؤلفه بوم مشترک استفاده می‌کنند، بنابراین عملیات پایه آن‌ها به جز برخی تفاوت‌های عملکردی، عمدتاً یکسان است.

> محتوا و رابط زیر عمدتاً بر اساس گره Load3D است. لطفاً برای ویژگی‌های خاص به رابط واقعی گره مراجعه کنید.

ناحیه بوم شامل عملیات مختلف نمایشی است، از جمله:

- تنظیمات نمای پیش‌نمایش (شبکه، رنگ پس‌زمینه، نمای پیش‌نمایش)
- کنترل دوربین: FOV، نوع دوربین
- شدت نور سراسری: تنظیم نورپردازی
- خروجی مدل: پشتیبانی از فرمت‌های `GLB`، `OBJ`، `STL`
- و غیره.

![رابط کاربری گره Load 3D](../Preview3D/asset/preview3d_canvas.jpg)

1. شامل چندین منو و منوهای پنهان گره Load 3D
2. محور عملیات نمای سه‌بعدی

### 1. عملیات نمایشی

<video controls width="640" height="360">
  <source src="https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3D/asset/view_operations.mp4" type="video/mp4">
  مرورگر شما از پخش ویدیو پشتیبانی نمی‌کند.
</video>

عملیات کنترل نمایش:

- کلیک چپ + کشیدن: چرخاندن نما
- کلیک راست + کشیدن: جابجایی نما
- چرخاندن چرخ میانی یا کلیک میانی + کشیدن: بزرگنمایی/کوچکنمایی
- محور مختصات: تغییر نماها

### 2. عملکردهای منوی چپ

![منو](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu.webp)

در ناحیه پیش‌نمایش، برخی منوهای عملیات نمایشی در منو پنهان شده‌اند. برای باز کردن منوهای مختلف، دکمه منو را کلیک کنید.

- 1. صحنه: شامل تنظیمات شبکه پنجره پیش‌نمایش، رنگ پس‌زمینه، تصویر بندانگشتی
- 2. مدل: حالت رندر مدل، جنس بافت، تنظیمات جهت بالا
- 3. دوربین: جابجایی بین نمای متعامد و پرسپکتیو، تنظیم زاویه پرسپکتیو
- 4. نور: شدت نور سراسری صحنه
- 5. خروجی: خروجی مدل به فرمت‌های دیگر (GLB، OBJ، STL)

#### صحنه

![منوی صحنه](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_scene.webp)

منوی صحنه برخی عملکردهای پایه تنظیمات صحنه را فراهم می‌کند:

1. نمایش/مخفی‌سازی شبکه
2. تنظیم رنگ پس‌زمینه
3. کلیک برای بارگذاری تصویر پس‌زمینه
4. مخفی‌سازی تصویر بندانگشتی پیش‌نمایش

#### مدل

![منوی_صحنه](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_model.webp)

منوی مدل برخی عملکردهای مرتبط با مدل را فراهم می‌کند:

1. **جهت بالا**: تعیین می‌کند کدام محور جهت بالای مدل است
2. **حالت متریال**: جابجایی بین حالت‌های رندر مدل - اصلی، نرمال، وایرفریم، لاین‌آرت

#### دوربین

![منوی_دوربین](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_camera.webp)

این منو جابجایی بین نمای متعامد و پرسپکتیو و تنظیم اندازه زاویه پرسپکتیو را فراهم می‌کند:

1. **دوربین**: جابجایی سریع بین نمای متعامد و پرسپکتیو
2. **FOV**: تنظیم زاویه FOV

#### نور

![منوی_نور](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_light.webp)

از طریق این منو می‌توانید به سرعت شدت نور سراسری صحنه را تنظیم کنید

#### خروجی

![منوی_خروجی](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/Load3d/asset/menu_export.webp)

این منو قابلیت تبدیل و خروجی سریع فرمت مدل را فراهم می‌کند