# بارگذاری مدل Optical Flow

مدل جریان نوری را از پوشه `models/optical_flow/` بارگذاری می‌کند. در حال حاضر، فقط فرمت RAFT-large متعلق به torchvision پشتیبانی می‌شود که مدل مورد استفاده در گره VOIDWarpedNoise است. ComfyUI وزن‌های جریان نوری را به‌صورت خودکار دانلود نمی‌کند؛ شما باید فایل checkpoint را به‌صورت دستی در پوشه `models/optical_flow/` قرار دهید.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `model_name` | مدل جریان نوری برای بارگذاری. فایل‌ها باید در پوشه `optical_flow` قرار داده شوند. در حال حاضر فقط `raft_large.pth` از torchvision پشتیبانی می‌شود. | COMBO | بله | فهرست فایل‌های موجود در پوشه `models/optical_flow/` |

توجه: فایل checkpoint انتخابی باید یک state dict از نوع RAFT-large torchvision باشد که حاوی کلیدهایی با پیشوندهای `feature_encoder.`، `context_encoder.` و `update_block.` باشد. اگر فایل با این قالب مطابقت نداشته باشد، گره یک ValueError برمی‌انگیزد.

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `OPTICAL_FLOW` | مدل جریان نوری بارگذاری‌شده، در حالت ارزیابی و با دقت float32، که در یک ModelPatcher برای استفاده با سایر گره‌ها پوشانده شده است. | OPTICAL_FLOW |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/fa.md)

---
**Source fingerprint (SHA-256):** `5e79551545ad7ee2fd4856a47da29808a404342d1d5e57da0980058db6b11c3b`
