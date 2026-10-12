# RecraftTextToVectorNode

יוצר איורי וקטור SVG באופן סינכרוני על בסיס פרומפט טקסט ורזולוציה. צומת זה שולח את הפרומפט שלך אל Recraft API ומחזיר את תוכן ה-SVG שנוצר.

## קלטים

| פרמטר | תיאור | סוג נתונים | חובה | טווח |
|-----------|-------------|-----------|----------|-------|
| `prompt` | פרומפט ליצירת התמונה. (ברירת מחדל: "", מקסימום 1000 תווים) | STRING | כן | - |
| `substyle` | סגנון איור וקטורי ספציפי לשימוש ביצירה. | COMBO | כן | `"2d_character"`<br>`"2d_gradient"`<br>`"2d_illustration"`<br>`"2d_flat_character"`<br>`"2d_flat_illustration"`<br>`"2d_art"`<br>`"2d_art_character"`<br>`"2d_pattern"`<br>`"2d_pixel_art"`<br>`"2d_cyberpunk"`<br>`"2d_engraving"`<br>`"2d_black_and_white"`<br>`"2d_ink"`<br>`"2d_sketch"`<br>`"2d_watercolor"`<br>`"2d_animation"`<br>`"2d_comic"`<br>`"2d_children_illustration"`<br>`"2d_vintage"`<br>`"2d_retro"`<br>`"2d_hand_drawn"`<br>`"2d_psychedelic"`<br>`"2d_graffiti"`<br>`"2d_ukiyo_e"`<br>`"2d_woodcut"`<br>`"2d_art_deco"`<br>`"2d_art_nouveau"`<br>`"2d_bauhaus"`<br>`"2d_constructivism"`<br>`"2d_cubism"`<br>`"2d_futurism"`<br>`"2d_glitch"`<br>`"2d_impressionism"`<br>`"2d_naive"`<br>`"2d_pointillism"`<br>`"2d_pop_art"`<br>`"2d_realism"`<br>`"2d_renaissance"`<br>`"2d_rococo"`<br>`"2d_romanticism"`<br>`"2d_surrealism"`<br>`"2d_suprematism"`<br>`"2d_symbolism"`<br>`"2d_expressionism"`<br>`"2d_abstract"`<br>`"2d_minimalism"`<br>`"2d_contemporary"`<br>`"2d_modern"`<br>`"2d_brutalism"`<br>`"2d_metaphysical"`<br>`"2d_mannerism"`<br>`"2d_baroque"`<br>`"2d_neoclassicism"`<br>`"2d_orientalism"`<br>`"2d_primitivism"`<br>`"2d_fauvism"`<br>`"2d_rayonism"`<br>`"2d_orphism"`<br>`"2d_vorticism"`<br>`"2d_dadaism"`<br>`"2d_neo_expressionism"`<br>`"2d_transavantgarde"`<br>`"2d_new_wild"`<br>`"2d_graffiti_classic"`<br>`"2d_graffiti_modern"`<br>`"2d_graffiti_wildstyle"`<br>`"2d_graffiti_bubble"`<br>`"2d_graffiti_throwup"`<br>`"2d_graffiti_tag"`<br>`"2d_graffiti_blockbuster"`<br>`"2d_graffiti_mural"`<br>`"2d_graffiti_stencil"`<br>`"2d_graffiti_3d"`<br>`"2d_graffiti_character"`<br>`"2d_graffiti_abstract"`<br>`"2d_graffiti_urban"`<br>`"2d_graffiti_neo_muralism"`<br>`"2d_graffiti_post_graffiti"`<br>`"2d_graffiti_street_art"` |
| `size` | גודל התמונה שנוצרה. (ברירת מחדל: "1024x1024") | COMBO | כן | `"1024x1024"`<br>`"1024x2048"`<br>`"2048x1024"`<br>`"2048x2048"`<br>`"512x512"`<br>`"512x1024"`<br>`"1024x512"`<br>`"2048x512"`<br>`"512x2048"` |
| `n` | מספר התמונות ליצירה. (ברירת מחדל: 1, מינ': 1, מקס': 6) | INT | כן | 1-6 |
| `seed` | Seed לקביעה אם הצומת צריך לרוץ מחדש; התוצאות בפועל אינן דטרמיניסטיות ללא תלות ב-seed. (ברירת מחדל: 0, מינ': 0, מקס': 18446744073709551615) | INT | כן | 0-18446744073709551615 |
| `negative_prompt` | תיאור טקסטואלי אופציונלי של אלמנטים לא רצויים בתמונה. (ברירת מחדל: "", כשהוא ריק לא נעשה שימוש בפרומפט שלילי) | STRING | לא | - |
| `recraft_controls` | בקרות נוספות אופציונליות על היצירה באמצעות צומת Recraft Controls. | CONTROLS | לא | - |

**הערה:** הפרמטר `seed` קובע רק מתי הצומת יופעל מחדש, אך אינו הופך את תוצאות היצירה לדטרמיניסטיות.

## פלטים

| שם פלט | תיאור | סוג נתונים |
|-------------|-------------|-----------|
| `SVG` | האיור הווקטורי שנוצר בפורמט SVG | SVG |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftTextToVectorNode/he.md)

---
**Source fingerprint (SHA-256):** `aec7e96e339047e75dfe419d94d23a613595bc22e7f187895c52b143780fcbf3`
