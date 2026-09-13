# Bria Görsel Arka Planı Kaldır

Bu düğüm, Bria RMBG 2.0 hizmetini kullanarak bir görüntünün arka planını kaldırır. İşlenmek üzere görüntüyü harici bir API'ye gönderir ve arka planı kaldırılmış sonucu döndürür.

## Girdiler

`moderation` seçicisi `"true"` olarak ayarlandığında ek moderasyon seçeneklerini gösterir.

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görsel` | Arka planın kaldırılacağı giriş görüntüsü. | IMAGE | Evet | - |
| `moderasyon` | Moderasyon ayarları. `"true"` olarak ayarlandığında ek moderasyon seçenekleri kullanılabilir hale gelir. | DYNAMIC_COMBO | Evet | `"false"`<br>`"true"` |
| `tohum` | `seed`, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. Varsayılan: `0`. | INT | Evet | 0 - 2147483647 |

### Moderasyon "true" Girdileri

Bu parametreler yalnızca `moderation` `"true"` olarak ayarlandığında görünür. `"false"` seçeneği ek giriş eklemez.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | Giriş görüntüsünde görsel içerik moderasyonunu etkinleştirir. Varsayılan: `False`. | BOOLEAN | Hayır | - |
| `visual_output_moderation` | Çıkış görüntüsünde görsel içerik moderasyonunu etkinleştirir. Varsayılan: `True`. | BOOLEAN | Hayır | - |

**Not:** `visual_input_moderation` ve `visual_output_moderation` parametreleri `moderation` parametresine bağlıdır. Yalnızca `moderation` `"true"` olarak ayarlandığında etkindirler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Arka planı kaldırılmış işlenmiş görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/tr.md)

---
**Source fingerprint (SHA-256):** `f62dcd5c9406ec09f5aab44585dd7f25ae0f7d9a934faa10a58e46ef116df110`
