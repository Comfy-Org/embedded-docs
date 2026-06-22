# RecraftStyleV3VectorIllustrationNode

این گره یک سبک را برای استفاده با API Recraft پیکربندی می‌کند و به‌طور خاص سبک `vector_illustration` را انتخاب می‌کند. به شما امکان می‌دهد در صورت تمایل، زیرسبک دقیق‌تری را در آن دسته انتخاب کنید. خروجی این گره یک شیء پیکربندی سبک است که می‌تواند به سایر گره‌های API Recraft ارسال شود.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | ضروری | محدوده |
| --- | --- | --- | --- | --- |
| `substyle` | یک زیرسبک اختیاری و دقیق‌تر در دسته `vector_illustration`. در صورت عدم انتخاب، از سبک پایه `vector_illustration` استفاده می‌شود. | STRING | خیر | `"vector_illustration"`<br>`"vector_illustration_flat"`<br>`"vector_illustration_3d"`<br>`"vector_illustration_hand_drawn"`<br>`"vector_illustration_retro"`<br>`"vector_illustration_modern"`<br>`"vector_illustration_abstract"`<br>`"vector_illustration_geometric"`<br>`"vector_illustration_organic"`<br>`"vector_illustration_minimalist"`<br>`"vector_illustration_detailed"`<br>`"vector_illustration_colorful"`<br>`"vector_illustration_monochrome"`<br>`"vector_illustration_grayscale"`<br>`"vector_illustration_pastel"`<br>`"vector_illustration_vibrant"`<br>`"vector_illustration_muted"`<br>`"vector_illustration_warm"`<br>`"vector_illustration_cool"`<br>`"vector_illustration_neutral"`<br>`"vector_illustration_bold"`<br>`"vector_illustration_subtle"`<br>`"vector_illustration_playful"`<br>`"vector_illustration_serious"`<br>`"vector_illustration_elegant"`<br>`"vector_illustration_rustic"`<br>`"vector_illustration_urban"`<br>`"vector_illustration_nature"`<br>`"vector_illustration_fantasy"`<br>`"vector_illustration_sci_fi"`<br>`"vector_illustration_historical"`<br>`"vector_illustration_futuristic"`<br>`"vector_illustration_whimsical"`<br>`"vector_illustration_surreal"`<br>`"vector_illustration_realistic"`<br>`"vector_illustration_stylized"`<br>`"vector_illustration_cartoony"`<br>`"vector_illustration_anime"`<br>`"vector_illustration_comic"`<br>`"vector_illustration_pixel"`<br>`"vector_illustration_low_poly"`<br>`"vector_illustration_high_poly"`<br>`"vector_illustration_isometric"`<br>`"vector_illustration_orthographic"`<br>`"vector_illustration_perspective"`<br>`"vector_illustration_2d"`<br>`"vector_illustration_2.5d"`<br>`"vector_illustration_3d"`<br>`"vector_illustration_4d"` |

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `recraft_style` | یک شیء پیکربندی سبک API Recraft شامل سبک `vector_illustration` انتخاب‌شده و زیرسبک اختیاری. این خروجی می‌تواند به سایر گره‌های Recraft متصل شود. | STYLEV3 |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3VectorIllustrationNode/fa.md)

---
**Source fingerprint (SHA-256):** `acd7a6decfdd052a0ff3c01a66dfdd4aa37a711ed6e2e123cc9a424b738b1346`
