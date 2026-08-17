# SDPoseDrawKeypoints

SDPoseDrawKeypoints düğümü, poz tahmin verilerini (anahtar noktalar) alır ve bunları boş bir tuval üzerinde görsel bir iskelet olarak çizer. Pozun farklı bölümlerini (gövde, kafa, eller, yüz ve ayaklar gibi) özelleştirilebilir çizgi genişlikleri ve nokta boyutlarıyla seçerek çizmenize olanak tanır. Ortaya çıkan görüntü, görselleştirme için veya poz görüntüsü gerektiren diğer düğümler için girdi olarak kullanılabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `keypoints` | Çizilecek poz anahtar noktası verileri. Bu veriler genellikle bir poz algılama düğümünden gelir. | POSE_KEYPOINT | Evet | - |
| `draw_body` | Ana gövde iskeletinin çizilip çizilmeyeceğini kontrol eder (varsayılan: True). | BOOLEAN | Hayır | - |
| `draw_hands` | El anahtar noktalarının çizilip çizilmeyeceğini kontrol eder (varsayılan: True). | BOOLEAN | Hayır | - |
| `draw_face` | Yüz anahtar noktalarının çizilip çizilmeyeceğini kontrol eder (varsayılan: True). | BOOLEAN | Hayır | - |
| `draw_feet` | Ayak anahtar noktalarının çizilip çizilmeyeceğini kontrol eder (varsayılan: False). | BOOLEAN | Hayır | - |
| `stick_width` | Gövde iskeletini çizmek için kullanılan çizgilerin genişliği (varsayılan: 4). | INT | Hayır | 1 to 10 |
| `face_point_size` | Yüz anahtar noktalarını çizmek için kullanılan noktaların boyutu (varsayılan: 3). | INT | Hayır | 1 to 10 |
| `score_threshold` | Bir anahtar noktanın çizilebilmesi için sahip olması gereken minimum güven skoru. Bu değerin altındaki skorlara sahip anahtar noktalar yok sayılır (varsayılan: 0.3). | FLOAT | Hayır | 0.0 to 1.0 |
| `draw_head` | Kafa anahtar noktalarının (burun, gözler, kulaklar) ve kafa bağlantılarının çizilip çizilmeyeceğini kontrol eder (varsayılan: True). | BOOLEAN | Hayır | - |

**Not:** `keypoints` girdisi boş veya `None` ise, düğüm boş bir 64x64 görüntü çıkarır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Çizilmiş poz anahtar noktalarını içeren bir görüntü. Görüntü boyutları, girdi anahtar noktası verilerinde belirtilen `canvas_height` ve `canvas_width` değerleriyle eşleşir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseDrawKeypoints/tr.md)

---
**Source fingerprint (SHA-256):** `2b2b9530b55c56e278666bd5d139bb6a1bb503b75b948a89266b9982b5a295e4`
