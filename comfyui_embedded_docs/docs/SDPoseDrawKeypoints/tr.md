> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseDrawKeypoints/tr.md)

SDPoseDrawKeypoints düğümü, poz tahmin verilerini (anahtar noktaları) alır ve bunları boş bir tuval üzerinde görsel bir iskelet olarak çizer. Vücut, eller, yüz ve ayaklar gibi pozun farklı bölümlerini özelleştirilebilir çizgi kalınlıkları ve nokta boyutlarıyla seçici olarak çizmenize olanak tanır. Ortaya çıkan görüntü, görselleştirme amacıyla veya poz görüntüsü gerektiren diğer düğümler için girdi olarak kullanılabilir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `keypoints` | POSE_KEYPOINT | Evet | - | Çizilecek poz anahtar noktası verileri. Bu veriler tipik olarak bir poz algılama düğümünden gelir. |
| `draw_body` | BOOLEAN | Hayır | - | Ana vücut iskeletinin çizilip çizilmeyeceğini kontrol eder (varsayılan: True). |
| `draw_hands` | BOOLEAN | Hayır | - | El anahtar noktalarının çizilip çizilmeyeceğini kontrol eder (varsayılan: True). |
| `draw_face` | BOOLEAN | Hayır | - | Yüz anahtar noktalarının çizilip çizilmeyeceğini kontrol eder (varsayılan: True). |
| `draw_feet` | BOOLEAN | Hayır | - | Ayak anahtar noktalarının çizilip çizilmeyeceğini kontrol eder (varsayılan: False). |
| `stick_width` | INT | Hayır | 1 ila 10 | Vücut iskeletini çizmek için kullanılan çizgilerin kalınlığı (varsayılan: 4). |
| `face_point_size` | INT | Hayır | 1 ila 10 | Yüz anahtar noktalarını çizmek için kullanılan noktaların boyutu (varsayılan: 3). |
| `score_threshold` | FLOAT | Hayır | 0.0 ila 1.0 | Bir anahtar noktanın çizilmesi için gereken minimum güven puanı. Bu değerin altındaki puanlara sahip anahtar noktaları yok sayılır (varsayılan: 0.3). |

**Not:** `keypoints` girdisi boş veya `None` ise, düğüm 64x64 boyutunda boş bir görüntü çıktısı verecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | IMAGE | Çizilmiş poz anahtar noktalarını içeren bir görüntü. Görüntü boyutları, girdi anahtar noktası verilerinde belirtilen `canvas_height` ve `canvas_width` değerleriyle eşleşir. |