# SeedVR2 Çıktısını Sonradan İşle

Bu düğüm, üretilen görüntüyü orijinal yeniden boyutlandırılmış görüntüyle hizalar ve isteğe bağlı renk düzeltmesi uygular. SeedVR2 yükseltme sürecinden çıkan çıktıyı alır ve orijinal referans görüntünün renkleri ve boyutlarıyla eşleşecek şekilde ayarlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | İşlenecek üretilen görüntü. | IMAGE | Evet | - |
| `original_resized_images` | Ön işleme öncesindeki orijinal yeniden boyutlandırılmış görüntü, referans olarak kullanılır. | IMAGE | Evet | - |
| `color_correction_method` | Üretilen görüntü renklerini orijinal görüntüyle eşleştirme yöntemi. lab: CIELAB uzayında renk aktarımı yapar, ayrıntıları korur (en sadık). wavelet: düşük frekanslı rengi aktarır, yükseltilmiş yüksek frekanslı ayrıntıları korur. adain: kanal başına ortalama/std eşleştirir (en hızlı, genel renk tonu). none: renk aktarımını atlar (yalnızca geometri hizalaması). (varsayılan: "lab") | COMBO | Evet | `"lab"`<br>`"wavelet"`<br>`"adain"`<br>`"none"` |

**Not:** Her iki girdi de 4-B (batch, height, width, channels) veya 5-B (batch, frames, height, width, channels) tensörler olabilir. Düğüm, en küçük batch, kare sayısı, yükseklik ve genişliğe göre her ikisini de kırpar, bu nedenle tam olarak eşleşmeleri gerekmez. Çıktı yüksekliği ve genişliği çift sayılara yuvarlanır. Referans görüntüde bir alfa kanalı (4 kanal) varsa, bu alfa kanalı korunur ve çıktıya uygulanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `images` | Hizalanmış, renk düzeltmesi yapılmış görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2PostProcessing/tr.md)

---
**Source fingerprint (SHA-256):** `00a3a3ef06edc7e0eca8f67a96095920a3e0e885dac3fb676d081e4c4c30bec5`
