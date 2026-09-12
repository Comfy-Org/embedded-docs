# Bria Silgi

Bria Eraser, Bria API'sini kullanarak bir görüntüden nesneleri veya alanları kaldırır. Kaldırılacak bölgeleri ana hatlarıyla belirten bir maske ve bir görüntü sağlarsınız; düğüm her ikisini de Bria'ya yükler, silme işini çalıştırır, tamamlanmasını bekler ve maskelenen alanların silindiği düzenlenmiş görüntüyü döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Kaldırılacak nesneleri veya alanları içeren girdi görüntüsü. | IMAGE | Evet | - |
| `mask` | Beyaz alanlar silinir, siyah alanlar korunur. Maske gönderilmeden önce ikili hale getirilir, bu nedenle kısmen boyanmış alanlar beyaz sayılır. Görüntüyle aynı en-boy oranına sahip olmalıdır. | MASK | Evet | - |
| `mask_type` | Maske kaynak türü. "manual" elle çizilen veya fırça maskeleri içindir; "automatic" SAM gibi segmentasyon modelleri tarafından üretilen maskeler içindir. | COMBO | Evet | "manual"<br>"automatic" |
| `moderation` | Moderasyon ayarları. Girdi ve/veya çıktı görüntülerinde görsel içerik moderasyonunu etkinleştirmek için "true" olarak ayarlayın. | DYNAMIC_COMBO | Evet | "false"<br>"true" |

`moderation` "true" olarak ayarlandığında, iki ek boolean ayarı kullanılabilir hale gelir:

- `visual_input_moderation` — girdi görüntüsüne görsel içerik moderasyonu uygular (varsayılan: false)
- `visual_output_moderation` — çıktı görüntüsüne görsel içerik moderasyonu uygular (varsayılan: false)

Not: Maske, görüntünün en-boy oranıyla eşleşmelidir, aksi takdirde istek başarısız olur. Maske API'ye gönderilmeden önce ikili (siyah beyaz) bir maskeye dönüştürülür: yarıdan daha az opaklıkta boyanmış alanlar yok sayılır ve kısmen boyanmış alanlar beyaz olarak değerlendirilir ve silinir. Maske en azından bir miktar beyaz alan içermelidir; boş bir maske, silinecek bir şey olmadığı için isteğin başarısız olmasına neden olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Maskelenen nesnelerin veya alanların kaldırıldığı düzenlenmiş görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraser/tr.md)

---
**Source fingerprint (SHA-256):** `5528b7a3cb4d0a7b1b28acbc642a8bd21e2eacf5aa225403d6344c29f0cdba80`
