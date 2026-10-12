# UnetLoader

The UNETLoader node is designed for loading U-Net models by name, facilitating the use of pre-trained U-Net architectures within the system.

This node will detect models located in the `ComfyUI/models/diffusion_models` folder.

## קלטים

| פרמטר | תיאור | סוג נתונים |
| --- | --- | --- |
| `unet_name` | מציין את שמו של מודל U-Net שיש לטעון. השם משמש לאיתור המודל בתוך מבנה תיקיות מוגדר מראש, ומאפשר טעינה דינמית של מודלים שונים של U-Net. | COMBO[STRING] |
| `weight_dtype` | 🚧  fp8_e4m3fn fp9_e5m2 | ... |

## פלטים

| פרמטר | תיאור | סוג נתונים |
| --- | --- | --- |
| `model` | מחזיר את מודל U-Net שנטען, ומאפשר להשתמש בו לעיבוד נוסף או להסקה בתוך המערכת. | MODEL |

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UnetLoader/he.md)
