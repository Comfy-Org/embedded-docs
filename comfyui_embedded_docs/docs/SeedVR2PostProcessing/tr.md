# SeedVR2 Çıktısını Sonradan İşle

Bu düğüm, oluşturulan görüntüyü orijinal yeniden boyutlandırılmış görüntüyle hizalar ve isteğe bağlı renk düzeltmesi uygular. Bir SeedVR2 büyütme işleminden çıktı alır ve bunu orijinal referans görüntünün renkleri ve boyutlarıyla eşleşecek şekilde ayarlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | İşlenecek oluşturulan görüntü. | IMAGE | Evet | - |
| `original_resized_images` | Ön işleme öncesi orijinal yeniden boyutlandırılmış görüntü; referans olarak kullanılır. | IMAGE | Evet | - |
| `color_correction_method` | Oluşturulan görüntü renklerini orijinal görüntüyle eşleştirme yöntemi. lab: CIELAB uzayında renk aktarır, ayrıntıyı korur (en sadık). wavelet: düşük frekanslı rengi aktarır, büyütülmüş yüksek frekanslı ayrıntıyı korur. adain: kanal başına ortalama/standart sapma eşleştirir (en hızlı, genel renk tonu). none: renk aktarımını atlar (yalnızca geometri hizalaması). (varsayılan: "lab") | COMBO | Evet | `"lab"`<br>`"wavelet"`<br>`"adain"`<br>`"none"` |

**Not:** Her iki girdi de 4-D (batch, yükseklik, genişlik, kanal) veya 5-D (batch, kareler, yükseklik, genişlik, kanal) tensörler olabilir. Düğüm her ikisini de en küçük batch, kare sayısı, yükseklik ve genişliğe kırpar; bu nedenle tam olarak eşleşmeleri gerekmez. `none` dışında bir renk düzeltme yöntemi kullanıldığında, referans görüntü önce çıktı boyutuna yeniden boyutlandırılır. Renk düzeltmesi bellekten haberdar parçalar halinde işlenir; bellek tükenirse daha küçük bir parça boyutuna düşülür. Çıktı yüksekliği ve genişliği çift sayılara aşağı yuvarlanır. Referans görüntüde bir alfa kanalı (4 kanal) varsa, bu alfa kanalı korunur ve çıktıya uygulanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `images` | Hizalanmış, renk düzeltilmiş görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2PostProcessing/tr.md)

---
**Source fingerprint (SHA-256):** `00a3a3ef06edc7e0eca8f67a96095920a3e0e885dac3fb676d081e4c4c30bec5`
