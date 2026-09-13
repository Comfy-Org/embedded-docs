# Luma Ray 3.2 Video Düzenle

## Genel Bakış

Bu düğüm, Luma Ray 3.2 kullanarak mevcut bir videoyu yeni bir istem altında yeniden oluşturur; özgün hareketi korurken öğeleri yeniden biçimlendirmenize, ışıklandırmayı değiştirmenize, öğe eklemenize veya kaldırmanıza olanak tanır. Kaynak video en fazla 18 saniye olabilir ve düzenlenen video kaynağın özgün uzunluğunu korur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | Düzenlenecek kaynak video. En fazla 18 saniye. | VIDEO | Evet | - |
| `prompt` | İstenen düzenlemeyi açıklar. | STRING | Evet | - |
| `resolution` | Düzenlenen video için çıktı çözünürlüğü. (varsayılan: "720p") | COMBO | Evet | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` |
| `strength` | Kaynağın ne kadar güçlü korunacağına karşı yeniden hayal edileceğini belirler. "auto" Ray 3.2'nin seçmesini sağlar; adhere_* en çok korur, flex_* dengelidir, reimagine_* en çok değiştirir. (varsayılan: "auto") | COMBO | Evet | `"auto"`<br>`"adhere_1"`<br>`"adhere_2"`<br>`"adhere_3"`<br>`"flex_1"`<br>`"flex_2"`<br>`"flex_3"`<br>`"reimagine_1"`<br>`"reimagine_2"`<br>`"reimagine_3"` |
| `seed` | Tekrarlanabilirlik için tohum. | INT | Evet | - |

**Not:** `prompt` 1 ile 6000 karakter arasında olmalıdır. Kaynak video süresi 18 saniyeyi aşmamalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Düzenlenen video çıktısı. | VIDEO |
| `generation_id` | Oluşturma isteği için benzersiz tanımlayıcı. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32VideoEditNode/tr.md)

---
**Source fingerprint (SHA-256):** `936d9d7da3fdee9b0b468781fd470751db01f772f3c5c20582da7fb1ff85e6e6`
