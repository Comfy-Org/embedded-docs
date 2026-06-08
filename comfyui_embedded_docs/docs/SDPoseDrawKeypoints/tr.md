SDPoseDrawKeypoints düğümü, poz tahmin verilerini (anahtar noktaları) alır ve bunları boş bir tuval üzerinde görsel bir iskelet olarak çizer. Vücut, eller, yüz ve ayaklar gibi pozun farklı bölümlerini özelleştirilebilir çizgi kalınlıkları ve nokta boyutlarıyla seçerek çizmenize olanak tanır. Ortaya çıkan görüntü, görselleştirme amacıyla veya poz görüntüsü gerektiren diğer düğümler için girdi olarak kullanılabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `anahtar_noktalar` | Çizilecek poz anahtar noktası verileri. Bu veriler tipik olarak bir poz algılama düğümünden gelir. | POSE_KEYPOINT | Evet | - |
| `gövde_çiz` | Ana vücut iskeletinin çizilip çizilmeyeceğini kontrol eder (varsayılan: True). | BOOLEAN | Hayır | - |
| `elleri_çiz` | El anahtar noktalarının çizilip çizilmeyeceğini kontrol eder (varsayılan: True). | BOOLEAN | Hayır | - |
| `yüzü_çiz` | Yüz anahtar noktalarının çizilip çizilmeyeceğini kontrol eder (varsayılan: True). | BOOLEAN | Hayır | - |
| `ayakları_çiz` | Ayak anahtar noktalarının çizilip çizilmeyeceğini kontrol eder (varsayılan: False). | BOOLEAN | Hayır | - |
| `çizgi_genişliği` | Vücut iskeletini çizmek için kullanılan çizgilerin kalınlığı (varsayılan: 4). | INT | Hayır | 1 ila 10 |
| `yüz_nokta_boyutu` | Yüz anahtar noktalarını çizmek için kullanılan noktaların boyutu (varsayılan: 3). | INT | Hayır | 1 ila 10 |
| `puan_eşiği` | Bir anahtar noktanın çizilmesi için gereken minimum güven puanı. Bu değerin altındaki puanlara sahip anahtar noktaları yok sayılır (varsayılan: 0.3). | FLOAT | Hayır | 0.0 ila 1.0 |

**Not:** `keypoints` girdisi boş veya `None` ise, düğüm boş bir 64x64 görüntü çıktısı verecektir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Çizilmiş poz anahtar noktalarını içeren bir görüntü. Görüntü boyutları, girdi anahtar noktası verilerinde belirtilen `canvas_height` ve `canvas_width` değerleriyle eşleşir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseDrawKeypoints/tr.md)

---
**Source fingerprint (SHA-256):** `c01397ed3608b65b737b60c2ae50919e0217cfe63b3695b68f176c2d69faa9c1`
