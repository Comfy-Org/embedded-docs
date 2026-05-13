> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetPropertiesAndCombine/fa.md)

## ورودی‌ها

| پارامتر | نوع داده | ضروری | محدوده | توضیحات |
|---------|----------|-------|--------|----------|
| `positive` | CONDITIONING | بله | - | ورودی شرطی‌سازی مثبت اصلی |
| `negative` | CONDITIONING | بله | - | ورودی شرطی‌سازی منفی اصلی |
| `positive_NEW` | CONDITIONING | بله | - | شرطی‌سازی مثبت جدید برای اعمال |
| `negative_NEW` | CONDITIONING | بله | - | شرطی‌سازی منفی جدید برای اعمال |
| `strength` | FLOAT | بله | 0.0 تا 10.0 | ضریب شدت برای اعمال شرطی‌سازی جدید (پیش‌فرض: 1.0) |
| `set_cond_area` | STRING | بله | "default"<br>"mask bounds" | نحوه اعمال ناحیه شرطی‌سازی را کنترل می‌کند (پیش‌فرض: "default") |
| `mask` | MASK | خیر | - | ماسک اختیاری برای محدود کردن ناحیه اعمال شرطی‌سازی |
| `hooks` | HOOKS | خیر | - | گروه هوک اختیاری برای کنترل پیشرفته |
| `timesteps` | TIMESTEPS_RANGE | خیر | - | مشخصات محدوده گام زمانی اختیاری |

## خروجی‌ها

| نام خروجی | نوع داده | توضیحات |
|-----------|----------|---------|
| `positive` | CONDITIONING | خروجی شرطی‌سازی مثبت ترکیب‌شده |
| `negative` | CONDITIONING | خروجی شرطی‌سازی منفی ترکیب‌شده |

---
**Source fingerprint (SHA-256):** `d434fdc1ccbe3ddee6293a6300cc55d30cb5bf357025b26777791746f51e755e`
