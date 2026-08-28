# BriaEraser

Bria Eraser, Bria API'sini kullanarak bir görüntüden nesneleri veya alanları siler. Silinecek bölgeleri belirten bir görüntü ve maske sağlarsınız; düğüm her ikisini de Bria'ya yükler, silme işini çalıştırır, tamamlanmasını bekler ve maskelenen alanların silinmiş olduğu düzenlenmiş görüntüyü döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Silinecek nesneleri veya alanları içeren girdi görüntüsü. | IMAGE | Evet | - |
| `mask` | Beyaz alanlar silinir, siyah alanlar korunur. Maske gönderilmeden önce ikili hale getirilir, bu nedenle kısmen boyanmış alanlar beyaz sayılır. Görüntüyle aynı en-boy oranına sahip olmalıdır. | MASK | Evet | - |
| `mask_type` | Maskenin nasıl oluşturulduğunu seçer. "manual" el ile çizilmiş veya fırça maskeleri içindir; "automatic" ise SAM gibi bölütleme modelleri tarafından üretilen maskeler içindir. | COMBO | Evet | "manual"<br>"automatic" |
| `moderation` | Moderasyon ayarları. Girdi ve/veya çıktı görüntülerinde görsel içerik moderasyonunu etkinleştirmek için "true" olarak ayarlayın. | DYNAMIC_COMBO | Evet | "false"<br>"true" |

Not: `moderation` "true" olarak ayarlandığında, iki ek boole ayarı kullanılabilir hale gelir:

- `visual_input_moderation` — girdi görüntüsüne görsel içerik moderasyonu uygular (varsayılan: false)
- `visual_output_moderation` — çıktı görüntüsüne görsel içerik moderasyonu uygular (varsayılan: false)

Maske, görüntünün en-boy oranıyla eşleşmelidir, aksi takdirde istek başarısız olur. Maske, API'ye gönderilmeden önce ikili (siyah ve beyaz) bir maskeye dönüştürülür: yarı opaklıktan daha az boyanmış alanlar yok sayılır ve kısmen boyanmış alanlar beyaz olarak kabul edilir ve silinir. Maske en azından bir miktar beyaz alan içermelidir; boş bir maske, silinecek bir şey olmadığı için isteğin başarısız olmasına neden olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Maskelenen nesnelerin veya alanların silindiği düzenlenmiş görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraser/tr.md)

---
**Source fingerprint (SHA-256):** `557272ecb0e6487796184ce88217ff318de4a5728a82e903aeb3fa3a0d24a664`
