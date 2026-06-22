# LumaRay32VideoEditNode

Bu düğüm, Luma Ray 3.2 kullanarak mevcut bir videoyu yeni bir istem altında yeniden işler; orijinal hareketi korurken yeniden stil vermenize, yeniden aydınlatmanıza, öğe eklemenize veya kaldırmanıza olanak tanır. Kaynak video en fazla 18 saniye olabilir ve düzenlenmiş video, kaynağın orijinal uzunluğunu korur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | Düzenlenecek kaynak video. En fazla 18 saniye. | VIDEO | Evet | - |
| `prompt` | İstenen düzenlemeyi açıklar. | STRING | Evet | - |
| `resolution` | Düzenlenmiş video için çıktı çözünürlüğü. | COMBO | Evet | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` |
| `strength` | Kaynağı koruma ile yeniden hayal etme arasındaki güç. "auto", Ray 3.2'nin seçmesini sağlar; adhere_* en çok korur, flex_* dengelidir, reimagine_* en çok değiştirir. (varsayılan: "auto") | COMBO | Evet | `"auto"`<br>`"adhere_1"`<br>`"adhere_2"`<br>`"adhere_3"`<br>`"flex_1"`<br>`"flex_2"`<br>`"flex_3"`<br>`"reimagine_1"`<br>`"reimagine_2"`<br>`"reimagine_3"` |
| `seed` | Tekrarlanabilirlik için tohum değeri. | INT | Evet | - |

**Not:** `prompt` 1 ile 6000 karakter arasında olmalıdır. Kaynak video 18 saniyeden uzun olmamalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Düzenlenmiş video çıktısı. | VIDEO |
| `generation_id` | Oluşturma isteği için benzersiz tanımlayıcı. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32VideoEditNode/tr.md)

---
**Source fingerprint (SHA-256):** `936d9d7da3fdee9b0b468781fd470751db01f772f3c5c20582da7fb1ff85e6e6`
