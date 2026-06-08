# SeedVR2 Çıktısını Son İşleme

Bu düğüm, oluşturulan görüntüyü orijinal yeniden boyutlandırılmış görüntüyle hizalar ve isteğe bağlı renk düzeltmesi uygular. SeedVR2 yükseltme işleminden gelen çıktıyı alır ve orijinal referans görüntünün renkleri ve boyutlarıyla eşleşecek şekilde ayarlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|---------|--------|
| `images` | İşlenecek oluşturulan görüntü. | IMAGE | Evet | - |
| `original_resized_images` | Ön işleme öncesi orijinal yeniden boyutlandırılmış görüntü, referans olarak kullanılır. | IMAGE | Evet | - |
| `color_correction_method` | Oluşturulan görüntü renklerini orijinal görüntüyle eşleştirme yöntemi. lab: CIELAB uzayında renk aktarımı, detayı korur (en sadık). wavelet: düşük frekanslı rengi aktarır, yükseltilmiş yüksek frekanslı detayı korur. adain: kanal başına ortalama/std eşlemesi (en hızlı, genel renk tonu). none: renk aktarımını atla (yalnızca geometri hizalaması). (varsayılan: "lab") | COMBO | Evet | `"lab"`<br>`"wavelet"`<br>`"adain"`<br>`"none"` |

**Not:** `images` ve `original_resized_images` girişleri eşleşen boyutlara sahip olmalıdır. Orijinal görüntüde alfa kanalı varsa (4 kanal), bu kanal korunur ve çıktıya uygulanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `images` | Renk düzeltmesi uygulanmış ve boyutları referans görüntüyle hizalanmış işlenmiş görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2PostProcessing/tr.md)

---
**Source fingerprint (SHA-256):** `befbe8ccd591c8064a07ae4bb8df853c7ce10f3de83ebfa9214755c22faf28b0`
