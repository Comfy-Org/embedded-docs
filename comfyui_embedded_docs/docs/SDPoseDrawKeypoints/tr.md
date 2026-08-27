# SDPoseDrawKeypoints

SDPoseDrawKeypoints düğümü, poz tahmini verilerini (anahtar noktalar) alır ve bunları boş bir tuval üzerinde görsel bir iskelet olarak çizer. Pozun gövde, kafa, eller, yüz ve ayaklar gibi farklı bölümlerini özelleştirilebilir çizgi genişlikleri ve nokta boyutlarıyla seçerek çizmenize olanak tanır. Ortaya çıkan görüntü, görselleştirme için veya poz görüntüsü gerektiren diğer düğümler için girdi olarak kullanılabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `anahtar_noktalar` | Çizilecek poz anahtar noktası verisi. Bu veri genellikle bir poz algılama düğümünden gelir ve bir veya daha fazla kare içerebilir. | POSE_KEYPOINT | Evet | - |
| `gövde_çiz` | Ana gövde iskeletinin çizilip çizilmediğini kontrol eder (varsayılan: True). | BOOLEAN | Hayır | - |
| `elleri_çiz` | El anahtar noktalarının çizilip çizilmediğini kontrol eder (varsayılan: True). | BOOLEAN | Hayır | - |
| `yüzü_çiz` | Yüz anahtar noktalarının çizilip çizilmediğini kontrol eder (varsayılan: True). | BOOLEAN | Hayır | - |
| `ayakları_çiz` | Ayak anahtar noktalarının çizilip çizilmediğini kontrol eder (varsayılan: False). | BOOLEAN | Hayır | - |
| `çizgi_genişliği` | Gövde ve kafa iskeletini çizmek için kullanılan çizgilerin genişliği (varsayılan: 4). | INT | Hayır | 1 ile 10 |
| `yüz_nokta_boyutu` | Yüz anahtar noktalarını çizmek için kullanılan noktaların boyutu (varsayılan: 3). | INT | Hayır | 1 ile 10 |
| `puan_eşiği` | Bir anahtar noktanın çizilebilmesi için gereken minimum güven puanı. Bu değerin altında puana sahip anahtar noktalar yok sayılır (varsayılan: 0.3). | FLOAT | Hayır | 0.0 ile 1.0 |
| `Kafa Çiz` | Kafa anahtar noktalarının (burun, gözler, kulaklar) çizilip çizilmediğini kontrol eder (varsayılan: True). | BOOLEAN | Hayır | - |

**Not:** `keypoints` girdisi boş veya `None` ise düğüm boş bir 64x64 görüntü çıkarır.

**Not:** `draw_body` ve `draw_head` bağımsız çalışır. `draw_head` devre dışı bırakıldığında, `draw_body` etkin olsa bile kafa anahtar noktaları çizilmez. `draw_body` devre dışı bırakılıp `draw_head` etkinleştirildiğinde yalnızca kafa anahtar noktaları ve boyun noktası çizilir. Her ikisi de devre dışı bırakılırsa gövde veya kafa anahtar noktaları çizilmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Çizilmiş poz anahtar noktalarını içeren bir görüntü. Görüntü boyutları, girdi anahtar noktası verisinde belirtilen `canvas_height` ve `canvas_width` değerleriyle eşleşir. Girdi birden fazla kare içerdiğinde bir görüntü grubu döndürülür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseDrawKeypoints/tr.md)

---
**Source fingerprint (SHA-256):** `2b2b9530b55c56e278666bd5d139bb6a1bb503b75b948a89266b9982b5a295e4`
