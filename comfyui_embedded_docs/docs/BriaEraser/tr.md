# BriaEraser

Bria Eraser, Bria API'sini kullanarak bir görüntüdeki nesneleri veya alanları kaldırır. Kaldırılacak bölgeleri belirten bir görüntü ve bir maske sağlarsınız; düğüm her ikisini de Bria'ya yükler, silme işini çalıştırır, tamamlanmasını bekler ve maskelenmiş alanlar silinmiş düzenlenmiş görüntüyü döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|---------|
| `image` | Kaldırılacak nesneleri veya alanları içeren giriş görüntüsü. | IMAGE | Evet | - |
| `mask` | Beyaz alanlar silinir, siyah alanlar korunur. Maske gönderilmeden önce ikili hale getirilir, bu nedenle kısmen boyanmış alanlar beyaz sayılır. Görüntüyle aynı en-boy oranına sahip olmalıdır. | MASK | Evet | - |
| `mask_type` | Maskenin nasıl oluşturulduğunu seçer. "manual", elle çizilmiş veya fırça maskeleri içindir; "automatic", SAM gibi segmentasyon modelleri tarafından üretilen maskeler içindir. | STRING | Evet | "manual"<br>"automatic" |
| `moderation` | Moderasyon ayarları. Giriş ve/veya çıkış görüntülerinde içerik moderasyonunu etkinleştirmek için "true" olarak ayarlayın. | STRING | Evet | "false"<br>"true" |

Not: `moderation` "true" olarak ayarlandığında, iki ek boolean ayar kullanılabilir hale gelir:

- `visual_input_moderation` — giriş görüntüsüne görsel içerik moderasyonu uygular (varsayılan: false)
- `visual_output_moderation` — çıkış görüntüsüne görsel içerik moderasyonu uygular (varsayılan: false)

Maske, görüntünün en-boy oranıyla eşleşmelidir, aksi takdirde istek başarısız olur. Maske, API'ye gönderilmeden önce ikili (siyah ve beyaz) bir maskeye dönüştürülür, bu nedenle kısmen boyanmış alanlar beyaz olarak kabul edilir ve silinir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Maskelenmiş nesnelerin veya alanların kaldırıldığı düzenlenmiş görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraser/tr.md)

---
**Source fingerprint (SHA-256):** `557272ecb0e6487796184ce88217ff318de4a5728a82e903aeb3fa3a0d24a664`
