# Bria Görsel Arka Planı Kaldır

Bu düğüm, Bria RMBG 2.0 veya RMBG 3.0 hizmetini kullanarak bir görüntünün arka planını kaldırır. İşlenmek üzere görüntüyü harici bir API'ye gönderir ve arka planı kaldırılmış sonucu döndürür.

## Girdiler

`moderation` seçicisi `"true"` olarak ayarlandığında ek moderasyon seçeneklerini gösterir.

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görsel` | Arka planın kaldırılacağı giriş görüntüsü. | IMAGE | Evet | - |
| `moderasyon` | Moderasyon ayarları. `"true"` olarak ayarlandığında ek moderasyon seçenekleri kullanılabilir hale gelir. | DYNAMIC_COMBO | Evet | `"false"`<br>`"true"` |
| `tohum` | `seed`, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; aynı görüntü seed değerinden bağımsız olarak her zaman aynı sonucu verir. Varsayılan: `0`. | INT | Evet | 0 - 2147483647 |
| `model` | Arka plan kaldırma modeli. Varsayılan `"RMBG2"`; `"RMBG3"` daha yeni Bria RMBG 3.0 modelini kullanır. | COMBO | Hayır | `"RMBG2"`<br>`"RMBG3"` |

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
**Source fingerprint (SHA-256):** `82f7ec2ac2d1579a3da009b464bce7c56fa2d7b1f599744d6158177ecd462cb2`
