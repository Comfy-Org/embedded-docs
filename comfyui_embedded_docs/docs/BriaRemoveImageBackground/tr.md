# Bria Görsel Arka Planı Kaldır

Bu düğüm, Bria RMBG 2.0 hizmetini kullanarak bir görüntüden arka planı kaldırır. Görüntüyü harici bir API'ye işlenmek üzere gönderir ve arka planı kaldırılmış sonucu döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Arka planı kaldırılacak girdi görüntüsü. | IMAGE | Evet | - |
| `moderation` | Moderasyon ayarları. `"true"` olarak ayarlandığında ek moderasyon seçenekleri kullanılabilir hale gelir. | COMBO | Hayır | `"false"`<br>`"true"` |
| `visual_input_moderation` | Girdi görüntüsünde görsel içerik moderasyonunu etkinleştirir. Bu parametre yalnızca `moderation` `"true"` olarak ayarlandığında kullanılabilir. Varsayılan: `False`. | BOOLEAN | Hayır | - |
| `visual_output_moderation` | Çıktı görüntüsünde görsel içerik moderasyonunu etkinleştirir. Bu parametre yalnızca `moderation` `"true"` olarak ayarlandığında kullanılabilir. Varsayılan: `True`. | BOOLEAN | Hayır | - |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. Varsayılan: `0`. | INT | Hayır | 0 ile 2147483647 arası |

**Not:** `visual_input_moderation` ve `visual_output_moderation` parametreleri `moderation` parametresine bağlıdır. Bu parametreler yalnızca `moderation` `"true"` olarak ayarlandığında etkindir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Arka planı kaldırılmış işlenmiş görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/tr.md)

---
**Source fingerprint (SHA-256):** `f62dcd5c9406ec09f5aab44585dd7f25ae0f7d9a934faa10a58e46ef116df110`
