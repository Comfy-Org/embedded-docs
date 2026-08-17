# SeedVR2 Çıktısını Sonradan İşle

Bu düğüm, üretilen görüntüyü orijinal yeniden boyutlandırılmış görüntüyle hizalar ve isteğe bağlı renk düzeltmesi uygular. SeedVR2 büyütme işleminin çıktısını alır ve orijinal referans görüntüsünün renkleri ve boyutlarıyla eşleşecek şekilde ayarlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | İşlenecek üretilen görüntü. | IMAGE | Evet | - |
| `original_resized_images` | Ön işleme öncesindeki orijinal yeniden boyutlandırılmış görüntü; referans olarak kullanılır. | IMAGE | Evet | - |
| `color_correction_method` | Üretilen görüntü renklerini orijinal görüntüyle eşleştirme yöntemi. lab: CIELAB uzayında renk transferi yapar, ayrıntıları korur (en sadık). wavelet: düşük frekanslı rengi aktarır, büyütülmüş yüksek frekanslı ayrıntıları korur. adain: kanal başına ortalama/std eşleştirmesi yapar (en hızlı, genel renk tonu). none: renk transferini atlar (yalnızca geometri hizalaması). (varsayılan: "lab") | COMBO | Evet | `"lab"`<br>`"wavelet"`<br>`"adain"`<br>`"none"` |

**Not:** Çıktı, üretilen ve referans görüntülerin daha küçük yükseklik ve genişliğine göre kırpılır ve nihai boyutlar çift sayılara aşağı yuvarlanır. Referans görüntüde alfa kanalı (4 kanal) varsa korunur ve çıktıya uygulanır. Her iki girdi de 4B veya 5B görüntü tensörü olabilir ve çıktı, üretilen görüntü girdisiyle aynı boyutsallığı kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `images` | Hizalanmış, renk düzeltmesi yapılmış görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2PostProcessing/tr.md)

---
**Source fingerprint (SHA-256):** `00a3a3ef06edc7e0eca8f67a96095920a3e0e885dac3fb676d081e4c4c30bec5`
