# VOIDSampler

VOIDSampler یک نمونه‌بردار تخصصی DDIM است که برای مدل‌های inpainting VOID طراحی شده است. این گره فرایند نویززدایی دقیقی را که VOID با آن آموزش دیده است بازتولید می‌کند و مقیاس‌بندی نویزی را که KSamplerهای استاندارد اعمال می‌کنند نادیده می‌گیرد. از این گره همراه با SamplerCustom یا SamplerCustomAdvanced و در کنار RandomNoise یا VOIDWarpedNoiseSource استفاده کنید.

## ورودی‌ها

این گره هیچ پارامتر ورودی قابل‌تنظیمی ندارد. یک نمونه‌بردار خودکفا است که الگوریتم نمونه‌برداری DDIM ثابتی را اعمال می‌کند.

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| *بدون ورودی* | این گره هیچ پارامتر ورودی نمی‌پذیرد. | - | - | - |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `SAMPLER` | یک شیء نمونه‌بردار که الگوریتم DDIM VOID را پیاده‌سازی می‌کند و آماده اتصال به گره‌های SamplerCustom یا SamplerCustomAdvanced است. | SAMPLER |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/fa.md)

---
**Source fingerprint (SHA-256):** `b8bb6d3d7220cca4a6dd252efe9c92953b1c5c67c14365e5e0583bc9bdb133be`
