# MeshSmoothNormals

Compute smooth per-vertex normals for a mesh and attach them. Meshes without normals are shaded flat (per-face) by glTF viewers; this node makes them shade smoothly. With a crease angle below 180, edges sharper than the threshold are kept hard by splitting vertices along them.

## ورودی‌ها

| پارامتر | توضیحات | نوع داده | الزامی | محدوده |
|---------|----------|----------|--------|--------|
| `مش` | مش ورودی برای پردازش. | MESH | بله | - |
| `crease_angle` | یال‌هایی که زاویه دووجهی آن‌ها از این مقدار (بر حسب درجه) بیشتر باشد، سخت می‌مانند (رأس‌ها شکسته می‌شوند). ۱۸۰ = کاملاً هموار؛ مقدار کمتر لبه‌های تیز را حفظ می‌کند (مثلاً ~۳۰-۶۰ برای سطوح سخت). پیش‌فرض: 180.0. | FLOAT | بله | 0.0 تا 180.0 (گام 1.0) |

هنگامی که `crease_angle` برابر یا بیشتر از ۱۸۰ باشد، توپولوژی مش تغییر نمی‌کند. وقتی زیر ۱۸۰ تنظیم شود، رأس‌ها در امتداد یال‌های سخت شکسته می‌شوند که ممکن است تعداد رأس‌ها را افزایش دهد.

## خروجی‌ها

| نام خروجی | توضیحات | نوع داده |
|------------|----------|----------|
| `مش` | مش ورودی با داده‌های نرمال هموار متصل‌شده، یا با رأس‌ها و نرمال‌های شکسته‌شده هنگامی که زاویه تاخوردگی تنظیم شده است. | MESH |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshSmoothNormals/fa.md)

---
**Source fingerprint (SHA-256):** `bbe9c0fba68369d8e9d3fb68e635869233804f3aac458e7c217d94977e77b9be`
