# بارگذاری مدل Optical Flow

## بررسی اجمالی

یک مدل جریان نوری را از پوشه `models/optical_flow/` بارگذاری می‌کند. در حال حاضر، فقط فرمت RAFT-large متعلق به torchvision پشتیبانی می‌شود که مدلی است که توسط گره VOIDWarpedNoise استفاده می‌شود. ComfyUI وزن‌های جریان نوری را به‌طور خودکار دانلود نمی‌کند؛ شما باید فایل checkpoint را به صورت دستی در پوشه `models/optical_flow/` قرار دهید.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `model_name` | مدل جریان نوری برای بارگذاری. فایل‌ها باید در پوشه `optical_flow` قرار گیرند. امروزه فقط `raft_large.pth` متعلق به torchvision پشتیبانی می‌شود. | COMBO | بله | فهرست فایل‌های موجود در پوشه `models/optical_flow/` |

فایل انتخابی باید یک checkpoint RAFT-large از torchvision باشد. گره بررسی می‌کند که فایل حاوی کلیدهای RAFT مورد انتظار (`feature_encoder.*`، `context_encoder.*` و `update_block.*`) باشد و در صورت عدم تشخیص فرمت، یک ValueError ایجاد می‌کند.

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `OPTICAL_FLOW` | مدل جریان نوری بارگذاری‌شده، که برای استفاده با سایر گره‌ها در یک ModelPatcher قرار گرفته است. | OPTICAL_FLOW |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/fa.md)

---
**Source fingerprint (SHA-256):** `5e79551545ad7ee2fd4856a47da29808a404342d1d5e57da0980058db6b11c3b`
