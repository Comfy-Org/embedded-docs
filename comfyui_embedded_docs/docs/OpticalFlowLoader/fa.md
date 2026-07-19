# بارگذاری مدل Optical Flow

## نمای کلی

یک مدل جریان نوری (optical flow) را از پوشه `models/optical_flow/` بارگذاری می‌کند. در حال حاضر، تنها فرمت RAFT-large متعلق به کتابخانه torchvision پشتیبانی می‌شود که همان مدل استفاده‌شده در گره VOIDWarpedNoise است. ComfyUI به‌طور خودکار وزن‌های جریان نوری را دانلود نمی‌کند؛ شما باید فایل checkpoint را به‌صورت دستی در دایرکتوری `models/optical_flow/` قرار دهید.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | ضروری | محدوده |
| --- | --- | --- | --- | --- |
| `model_name` | مدل جریان نوری برای بارگذاری. فایل‌ها باید در پوشه `optical_flow` قرار داده شوند. امروزه تنها فایل `raft_large.pth` از کتابخانه torchvision پشتیبانی می‌شود. | STRING | بله | فهرست فایل‌های موجود در پوشه `models/optical_flow/` |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `OPTICAL_FLOW` | مدل جریان نوری بارگذاری‌شده، که در یک ModelPatcher برای استفاده با سایر گره‌ها پیچیده شده است. | MODEL |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/fa.md)

---
**Source fingerprint (SHA-256):** `94bab0bb7e2b9d9b3f343337799eccc744f79275b72a6fad9681b408b4a0820b`
