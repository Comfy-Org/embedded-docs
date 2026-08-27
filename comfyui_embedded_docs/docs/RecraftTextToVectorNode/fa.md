# تبدیل متن به وکتور Recraft

تصویرسازی‌های برداری SVG را به‌صورت هم‌زمان بر اساس یک پرامپت متنی و وضوح تصویر تولید می‌کند. این گره پرامپت شما را به Recraft API ارسال کرده و محتوای SVG تولیدشده را بازمی‌گرداند.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
|-----------|-------------|-----------|----------|-------|
| `پرامپت` | پرامپت برای تولید تصویر. (پیش‌فرض: ""، حداکثر ۱۰۰۰ کاراکتر) | STRING | بله | - |
| `زیرسبک` | سبک خاص تصویرسازی برداری که برای تولید استفاده می‌شود. | COMBO | بله | `"2d_character"`<br>`"2d_gradient"`<br>`"2d_illustration"`<br>`"2d_flat_character"`<br>`"2d_flat_illustration"`<br>`"2d_art"`<br>`"2d_art_character"`<br>`"2d_pattern"`<br>`"2d_pixel_art"`<br>`"2d_cyberpunk"`<br>`"2d_engraving"`<br>`"2d_black_and_white"`<br>`"2d_ink"`<br>`"2d_sketch"`<br>`"2d_watercolor"`<br>`"2d_animation"`<br>`"2d_comic"`<br>`"2d_children_illustration"`<br>`"2d_vintage"`<br>`"2d_retro"`<br>`"2d_hand_drawn"`<br>`"2d_psychedelic"`<br>`"2d_graffiti"`<br>`"2d_ukiyo_e"`<br>`"2d_woodcut"`<br>`"2d_art_deco"`<br>`"2d_art_nouveau"`<br>`"2d_bauhaus"`<br>`"2d_constructivism"`<br>`"2d_cubism"`<br>`"2d_futurism"`<br>`"2d_glitch"`<br>`"2d_impressionism"`<br>`"2d_naive"`<br>`"2d_pointillism"`<br>`"2d_pop_art"`<br>`"2d_realism"`<br>`"2d_renaissance"`<br>`"2d_rococo"`<br>`"2d_romanticism"`<br>`"2d_surrealism"`<br>`"2d_suprematism"`<br>`"2d_symbolism"`<br>`"2d_expressionism"`<br>`"2d_abstract"`<br>`"2d_minimalism"`<br>`"2d_contemporary"`<br>`"2d_modern"`<br>`"2d_brutalism"`<br>`"2d_metaphysical"`<br>`"2d_mannerism"`<br>`"2d_baroque"`<br>`"2d_neoclassicism"`<br>`"2d_orientalism"`<br>`"2d_primitivism"`<br>`"2d_fauvism"`<br>`"2d_rayonism"`<br>`"2d_orphism"`<br>`"2d_vorticism"`<br>`"2d_dadaism"`<br>`"2d_neo_expressionism"`<br>`"2d_transavantgarde"`<br>`"2d_new_wild"`<br>`"2d_graffiti_classic"`<br>`"2d_graffiti_modern"`<br>`"2d_graffiti_wildstyle"`<br>`"2d_graffiti_bubble"`<br>`"2d_graffiti_throwup"`<br>`"2d_graffiti_tag"`<br>`"2d_graffiti_blockbuster"`<br>`"2d_graffiti_mural"`<br>`"2d_graffiti_stencil"`<br>`"2d_graffiti_3d"`<br>`"2d_graffiti_character"`<br>`"2d_graffiti_abstract"`<br>`"2d_graffiti_urban"`<br>`"2d_graffiti_neo_muralism"`<br>`"2d_graffiti_post_graffiti"`<br>`"2d_graffiti_street_art"` |
| `اندازه` | اندازه تصویر تولیدشده. (پیش‌فرض: "1024x1024") | COMBO | بله | `"1024x1024"`<br>`"1024x2048"`<br>`"2048x1024"`<br>`"2048x2048"`<br>`"512x512"`<br>`"512x1024"`<br>`"1024x512"`<br>`"2048x512"`<br>`"512x2048"` |
| `تعداد` | تعداد تصاویری که تولید می‌شود. (پیش‌فرض: ۱، حداقل: ۱، حداکثر: ۶) | INT | بله | 1-6 |
| `seed` | مقدار seed برای تعیین اینکه آیا گره باید دوباره اجرا شود؛ نتایج واقعی بدون توجه به seed غیرقطعی هستند. (پیش‌فرض: ۰، حداقل: ۰، حداکثر: 18446744073709551615) | INT | بله | 0-18446744073709551615 |
| `پرامپت منفی` | یک توصیف متنی اختیاری از عناصر ناخواسته در تصویر. (پیش‌فرض: ""، در صورت خالی بودن، هیچ پرامپت منفی استفاده نمی‌شود) | STRING | خیر | - |
| `recraft_controls` | کنترل‌های اضافی اختیاری بر تولید از طریق گره Recraft Controls. | CONTROLS | خیر | - |

**نکته:** پارامتر `seed` فقط کنترل می‌کند که گره چه زمانی دوباره اجرا شود، اما نتایج تولید را قطعی نمی‌کند.

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
|-------------|-------------|-----------|
| `SVG` | تصویرسازی برداری تولیدشده در قالب SVG | SVG |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftTextToVectorNode/fa.md)

---
**Source fingerprint (SHA-256):** `aec7e96e339047e75dfe419d94d23a613595bc22e7f187895c52b143780fcbf3`
