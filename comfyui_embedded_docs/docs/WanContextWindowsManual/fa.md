# پنجره‌های زمینه WAN (دستی)

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
| --- | --- | --- | --- | --- |
| `model` | مدلی که در طول نمونه‌برداری، پنجره‌های زمینه روی آن اعمال می‌شود. | MODEL | بله | - |
| `context_length` | طول پنجره زمینه بر حسب فریم‌های واقعی. باید به شکل 4*n + 1 باشد. (پیش‌فرض: 81) | INT | بله | 1 تا 16384 (گام 4) |
| `context_overlap` | میزان هم‌پوشانی پنجره زمینه بر حسب فریم‌های واقعی. (پیش‌فرض: 30) | INT | بله | 0 یا بیشتر |
| `context_schedule` | الگوریتم زمان‌بندی وابسته به گام برای پنجره‌های زمینه. (پیش‌فرض: "uniform_standard") | COMBO | بله | `"static_standard"`<br>`"uniform_standard"`<br>`"uniform_looped"`<br>`"batched"` |
| `context_stride` | گام پنجره زمینه؛ فقط برای زمان‌بندی‌های یکنواخت قابل استفاده است. (پیش‌فرض: 1) | INT | بله | 1 یا بیشتر |
| `closed_loop` | بستن حلقه پنجره زمینه؛ فقط برای زمان‌بندی‌های حلقه‌ای قابل استفاده است. (پیش‌فرض: False) | BOOLEAN | بله | True یا False |
| `fuse_method` | روش مورد استفاده برای ادغام پنجره‌های زمینه. (پیش‌فرض: "pyramid") | COMBO | بله | `"pyramid"`<br>`"gaussian"`<br>`"average"<br>`"overlap"` |
| `freenoise` | اعمال جابجایی نویز FreeNoise که ترکیب پنجره‌ها را بهبود می‌بخشد. (پیش‌فرض: True) | BOOLEAN | بله | True یا False |
| `retain_first_frame` | حفظ اولین فریم I2V در هر پنجره زمینه (ممکن است به حفظ مرجع اولیه کمک کند). (پیش‌فرض: False) | BOOLEAN | بله | True یا False |
| `split_conds_to_windows` | تقسیم چندین شرط‌ساز (ایجادشده توسط ConditionCombine) به هر پنجره بر اساس شاخص ناحیه. (پیش‌فرض: False) | BOOLEAN | بله | True یا False |

**توجه:** `context_stride` فقط بر زمان‌بندی‌های یکنواخت اثر می‌گذارد و `closed_loop` فقط برای زمان‌بندی‌های حلقه‌ای کاربرد دارد. `context_length` باید الگوی 4n + 1 را دنبال کند. این گره `context_length` و `context_overlap` را قبل از اعمال، از فریم‌های واقعی به واحدهای مدل تبدیل می‌کند و حداقل ۱ را برای `context_length` و ۰ را برای `context_overlap` الزامی می‌کند. ورودی‌های `context_stride`، `closed_loop`، `freenoise` و `split_conds_to_windows` گزینه‌های پیشرفته هستند.

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
| --- | --- | --- |
| `model` | مدل با پیکربندی پنجره زمینه اعمال‌شده. | MODEL |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/fa.md)

---
**Source fingerprint (SHA-256):** `cf4927371e9d4b509f2e6e5319cd6109e3ef36da6b3faee278bcf8c906672857`
