SDPoseKeypointExtractor düğümü, SDPose modelini kullanarak giriş görüntülerinden insan pozu anahtar noktalarını tespit eder. Tam görüntüleri veya sınırlayıcı kutularla tanımlanmış belirli bölgeleri işleyebilir ve tespit edilen anahtar noktalarını, her kişi için koordinatları ve her anahtar nokta için bir güven puanı içeren OpenPose formatında çıktı olarak verir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Anahtar nokta tespiti için kullanılan SDPose modeli. `heatmap_head` özelliğine sahip, özellikle SDPose deposundan bir model olmalıdır. | MODEL | Evet | - |
| `vae` | Giriş görüntülerini işleme için gizli uzaya kodlamak amacıyla kullanılan VAE modeli. | VAE | Evet | - |
| `görüntü` | Poz anahtar noktalarının çıkarılacağı giriş görüntüsü veya görüntü grubu. | IMAGE | Evet | - |
| `toplu_boyut` | Tam görüntü modunda (yani `sınırlayıcı_kutular` sağlanmadığında) aynı anda işlenecek görüntü sayısı. Bu, işlemi hızlandırabilir. (varsayılan: 16) | INT | Hayır | 1 ile 10000 |
| `sınırlayıcı_kutular` | Daha doğru tespitler için isteğe bağlı sınırlayıcı kutular. Çoklu kişi tespiti için gereklidir. Sağlanırsa, düğüm belirtilen her bölgeden anahtar noktaları çıkarır. | BOUNDINGBOX | Hayır | - |

**Parametre Kısıtlamaları:**
*   `model` girişi, belirli bir SDPose modeli olmalıdır. Sağlanan modelde `heatmap_head` özelliği yoksa, düğüm bir hata verecektir.
*   Düğüm, `bboxes` girişine bağlı olarak iki farklı modda çalışır:
    1.  **Sınırlayıcı Kutu Modu:** `bboxes` sağlandığında, belirtilen her bölgeyi ayrı ayrı işler. Bu, tek bir görüntüde birden fazla kişiyi tespit etmek için gereklidir.
    2.  **Tam Görüntü Modu:** `bboxes` sağlanmadığında, tüm görüntüyü bir grup olarak işler. `batch_size` parametresi yalnızca bu modda geçerlidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `keypoints` | OpenPose çerçeve formatında anahtar noktalar (canvas_width, canvas_height, people). Çıktı, tespit edilen kişileri içerir; her biri bir dizi anahtar nokta koordinatı (x, y) ve bunlara karşılık gelen güven puanlarına sahiptir. | POSE_KEYPOINT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseKeypointExtractor/tr.md)

---
**Source fingerprint (SHA-256):** `7903b51c9137aa08bb8843362740fcf93cea9c09d142bd1db3b5eee945c853e4`
