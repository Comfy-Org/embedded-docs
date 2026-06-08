## مرور کلی

گره MultiGPU CFG Split کمک می‌کند بخش diffusion در یک گردش کار با چند GPU داخل یک سیستم اجرا شود. نتیجه به نوع گردش کار بستگی دارد، اما در بعضی گردش کارهای رایج افزایش سرعتی تا حدود 1.95x دیده شده است.

## نکات مهم

ترکیب GPUهای متفاوت پشتیبانی نمی‌شود. GPUهای نصب‌شده باید از یک نوع باشند؛ مثلا 2x 5090 یا 2x 5080.

ComfyUI هنگام شروع به کار، چند GPU بودن سیستم را به صورت خودکار تشخیص می‌دهد.

## GPUهای پشتیبانی‌شده

هر پیکربندی دو GPU همسان با معماری Ampere یا جدیدتر، مثل 2 x 3090 یا 2 x RTX6000 Pro.

## مدل‌های پشتیبانی‌شده

* LTX-2.3  
* WAN 2.2  
* FLUX.2 Klein \- Base Versions  
* Z-Image  
* Stable Diffusion 3.5 Large  
* Hunyuan Video  
* Qwen-Image-Edit-2511  
* Hunyuan-3D-v2.1  
* SDXL

## ورودی‌ها

| نام پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `model` | مدلی که باید پیش از نمونه‌گیری برای تقسیم CFG روی چند GPU آماده شود. | MODEL | بله | N/A |
| `max_gpus` | بیشترین تعداد GPUهای همسانی که می‌خواهید برای تقسیم کار استفاده شوند. این مقدار را برابر تعداد GPUهای مشابه نصب‌شده در سیستم قرار دهید. | INT | بله | Minimum: 1<br>Step: 1<br>Default: 2 |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `MODEL` | مدلی که برای تقسیم CFG روی چند GPU آماده شده و برای نمونه‌گیری سریع‌تر آماده است. | MODEL |

## محل قرارگیری گره و نکات گردش کار

![image1.png](./asset/image1.png)  
فیلد `max_gpus` باید روی بیشترین تعداد GPUهای همسان نصب‌شده در سیستم تنظیم شود.

**محل قرارگیری گره:** گره MultiGPU CFG Split باید بین گره بارگذاری مدل و گره نمونه‌گیری قرار بگیرد. اگر گره‌های دیگری هم به خروجی مدل از گره بارگذاری مدل وصل هستند، MultiGPU CFG Split باید آخرین گره در این زنجیره و درست قبل از گره نمونه‌گیری باشد.

![image2.png](./asset/image2.png)

**نکات گردش کار:** این گره با تقسیم فرایند diffusion در سطح CFG کار می‌کند. به همین دلیل مقدار CFG در گردش کار باید بیشتر از 1 باشد. گردش کارهای distilled که به `CFG=1` نیاز دارند، معمولا با استفاده از MultiGPU CFG Split روی چند GPU افزایش کارایی محسوسی نشان نمی‌دهند.

## بررسی استفاده از چند GPU

وقتی یک گردش کار را با MultiGPU CFG Split اجرا می‌کنید، می‌توانید Windows Task Manager را باز کرده و بخش Performance را انتخاب کنید.  
![image3.png](./asset/image3.webp)  
![image4.png](./asset/image4.webp)  
در زمانی که نمونه گیر در گردش کار در حال اجرا است، باید روی هر دو GPU نصب‌شده فعالیت ببینید.

## لینک workflow نمونه

[گردش کار نمونه (Wan 2.2 FP8)](https://raw.githubusercontent.com/Comfy-Org/embedded-docs/refs/heads/main/comfyui_embedded_docs/docs/MultiGPU_WorkUnits/asset/video_wan2_2_14B_t2v_mGPU.json)

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MultiGPU_WorkUnits/fa.md)

---
**Source fingerprint (SHA-256):** `7293ee785e29aea9a1a70a10444b99e89fb23c866505628ec57c209a2b8aaee0`
