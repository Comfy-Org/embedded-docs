# SaveGaussianSplat

این گره یک فایل سه‌بعدی Gaussian splat را در دایرکتوری خروجی ذخیره می‌کند. فرآیند ذخیره‌سازی فایل را مدیریت کرده و داده‌های پیش‌نمایش را برای نمای سه‌بعدی فراهم می‌کند.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | ضروری | محدوده |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | یک فایل سه‌بعدی Gaussian splat. | FILE3D | بله | SplatAny<br>PLY<br>SPLAT<br>SPZ<br>KSPLAT |
| `filename_prefix` | پیشوند نام فایل ذخیره‌شده (پیش‌فرض: "3d/ComfyUI"). | STRING | بله | هر پیشوند نام فایل معتبر |
| `viewport_state` | وضعیت فعلی نمای دید شامل اطلاعات دوربین و مدل. | LOAD3D | بله | - |
| `model_3d_info` | اطلاعات اضافی مدل سه‌بعدی برای نمای دید. | LOAD3DMODELINFO | خیر | - |
| `camera_info` | اطلاعات دوربین برای پیش‌نمایش نمای دید. | LOAD3DCAMERA | خیر | - |
| `width` | عرض پیش‌نمایش (پیش‌فرض: 1024). | INT | بله | 1 تا 4096 |
| `height` | ارتفاع پیش‌نمایش (پیش‌فرض: 1024). | INT | بله | 1 تا 4096 |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
|-------------|-------------|-----------|
| `model_3d` | فایل سه‌بعدی Gaussian splat ذخیره‌شده. | FILE3D |
| `model_3d_info` | اطلاعات مدل سه‌بعدی برای نمای دید. | LOAD3DMODELINFO |
| `camera_info` | اطلاعات دوربین برای پیش‌نمایش نمای دید. | LOAD3DCAMERA |
| `width` | عرض پیش‌نمایش. | INT |
| `height` | ارتفاع پیش‌نمایش. | INT |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGaussianSplat/fa.md)

---
**Source fingerprint (SHA-256):** `f2d6b98d2ce1fe11df8ba440b7f46a21e2308966c15daa5ca0bdca7dab1726cc`
