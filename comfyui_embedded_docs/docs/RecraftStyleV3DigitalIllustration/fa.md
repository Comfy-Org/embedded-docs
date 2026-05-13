> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3DigitalIllustration/fa.md)

این گره یک سبک را برای استفاده با API ریکرفت (Recraft) پیکربندی می‌کند و به‌طور خاص سبک "digital_illustration" (تصویرسازی دیجیتال) را انتخاب می‌کند. به شما امکان می‌دهد یک زیرسبک اختیاری برای تنظیم دقیق‌تر جهت هنری تصویر تولیدشده انتخاب کنید.

## ورودی‌ها

| پارامتر | نوع داده | الزامی | محدوده | توضیحات |
|---------|----------|--------|--------|---------|
| `زیرسبک` | STRING | خیر | `"digital_illustration"`<br>`"digital_illustration_anime"`<br>`"digital_illustration_cartoon"`<br>`"digital_illustration_comic"`<br>`"digital_illustration_concept_art"`<br>`"digital_illustration_fantasy"`<br>`"digital_illustration_futuristic"`<br>`"digital_illustration_graffiti"`<br>`"digital_illustration_graphic_novel"`<br>`"digital_illustration_hyperrealistic"`<br>`"digital_illustration_ink"`<br>`"digital_illustration_manga"`<br>`"digital_illustration_minimalist"`<br>`"digital_illustration_pixel_art"`<br>`"digital_illustration_pop_art"`<br>`"digital_illustration_retro"`<br>`"digital_illustration_sci_fi"`<br>`"digital_illustration_sticker"`<br>`"digital_illustration_street_art"`<br>`"digital_illustration_surreal"`<br>`"digital_illustration_vector"` | یک زیرسبک اختیاری برای مشخص کردن نوع خاصی از تصویرسازی دیجیتال. در صورت عدم انتخاب، سبک پایه "digital_illustration" استفاده می‌شود. |

## خروجی‌ها

| نام خروجی | نوع داده | توضیحات |
|-----------|----------|---------|
| `recraft_style` | STYLEV3 | یک شیء سبک پیکربندی‌شده شامل سبک انتخاب‌شده "digital_illustration" و زیرسبک اختیاری، آماده برای ارسال به سایر گره‌های API ریکرفت. |

---
**Source fingerprint (SHA-256):** `e52790a670839608ee1cb576e802a54d3bf2ca879ec288a24acd4ac7db27021a`
