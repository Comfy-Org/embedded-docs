# BriaEraser

Bu düğüm, Bria silgi hizmetini kullanarak bir görüntüden istenmeyen nesneleri veya alanları kaldırır. Kaldırılacak bölgeleri belirten bir görüntü ve bir maske sağlarsınız; düğüm, bu bölgeler silinmiş yeni bir görüntü döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Maskeyle işaretlenen alanların silindiği giriş görüntüsü. | IMAGE | Evet | — |
| `mask` | Beyaz alanlar silinir, siyah alanlar korunur. Maske gönderilmeden önce ikilileştirilir, bu nedenle kısmen boyanmış alanlar beyaz sayılır. Görüntüyle aynı en-boy oranına sahip olmalıdır. | MASK | Evet | — |
| `mask_type` | manual: elle çizilmiş veya fırça maskeleri için; automatic: SAM gibi bölütleme modelleri tarafından üretilen maskeler için. | COMBO | Evet | `"manual"`<br>`"automatic"` |
| `moderation` | Denetim ayarları. `"true"` olarak ayarlandığında, görsel giriş ve çıkış denetimi için iki ek boole anahtarı görünür. | DYNAMIC_COMBO | Evet | `"false"`<br>`"true"` |

Not: `moderation` `"true"` olarak ayarlandığında, `visual_input_moderation` (varsayılan: False) ve `visual_output_moderation` (varsayılan: False) ek ayarları kullanılabilir; bunlar sırasıyla giriş ve çıkış görüntülerinde görsel içerik denetimini etkinleştirir. Maske, görüntüyle aynı en-boy oranına sahip değilse veya maske ikilileştirmeden sonra hiçbir beyaz alan içermiyorsa düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Maskeyle işaretlenen alanların silindiği sonuç görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraser/tr.md)

---
**Source fingerprint (SHA-256):** `557272ecb0e6487796184ce88217ff318de4a5728a82e903aeb3fa3a0d24a664`
