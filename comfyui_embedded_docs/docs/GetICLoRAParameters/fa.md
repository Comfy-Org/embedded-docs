## مرور کلی

این گره پارامترهای IC-LoRA را از فراداده (metadata) یک مدل بارگذاری‌شده با LoRA استخراج می‌کند. با خواندن فراداده‌های safetensors، مقادیری مانند ضریب کاهش مقیاس مرجع (reference downscale factor) را پیدا کرده و به‌عنوان یک شیء پارامتر ساختاریافته خروجی می‌دهد. این خروجی می‌تواند به گره `LTXVAddGuide` برای مدیریت ویژه راهنماها متصل شود.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `iclora_model` | خروجی مستقیم از یک بارگذار LoRA برای IC-LoRA خاصی که می‌خواهید فراداده آن استخراج شود. | MODEL | بله | N/A |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `iclora_parameters` | پارامترهای IC-LoRA استخراج‌شده از فراداده LoRA (مانند reference_downscale_factor). در صورت نیاز LoRA به مدیریت ویژه راهنماها، به گره `LTXVAddGuide` متصل کنید. | IC_LORA_PARAMETERS |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetICLoRAParameters/fa.md)

---
**Source fingerprint (SHA-256):** `44673f0b06cb258014efd77f734c076865d59338ddf825598d85592f000aca50`
