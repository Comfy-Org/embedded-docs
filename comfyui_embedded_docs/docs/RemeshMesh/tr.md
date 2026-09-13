# Mesh'i Yeniden Oluştur (Dar Bant DC)

Remesh Mesh, orijinal yüzeyin çevresindeki dar bantlı bir mesafe alanını örnekleyerek ve bunu Dual Contouring ile çıkararak bir ağı temiz, tekdüze bir mozaikleme ile yeniden oluşturur. Bu, dağınık, manifold olmayan veya kendiyle kesişen topolojiyi normalleştirir ve tam bir yüz sayısına ulaşmak için Decimate Mesh'ten önce çalıştırılmak üzere tasarlanmıştır. İşleme etkin hesaplama aygıtında çalışır ve çıktı ağı kaynaklanmış kalır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Yeniden oluşturulacak giriş ağı. | MESH | Evet | — |
| `resolution` | Voksel ızgara çözünürlüğü (çıktı yoğunluğu). 256 ~ 100k yüz, 512 ~ 1M. Tam bir yüz sayısı için ardından Decimate Mesh kullanın. (varsayılan: 512) | INT | Evet | 32 - 2048 |
| `sign_mode` | Yüzey çıkarma modu. "udf", dağınık/manifold olmayan girdilere karşı dayanıklıdır; "sdf", QEF (Quadratic Error Function) keskin özellik kurtarma ile temiz tek bir yüzey üretir, ancak tutarlı sarım gerektirir. Bir mod seçildiğinde o moda özgü alt seçenekler görünür. (varsayılan: "udf") | DYNAMIC_COMBO | Evet | "udf"<br>"sdf" |
| `band` | Voksel birimleri cinsinden dar bant genişliği. UDF modunda yüzeyi de kaydırır. (gelişmiş, varsayılan: 1.0) | FLOAT | Evet | 0.5 - 4.0 |
| `project_back` | Köşeleri orijinal yüzeye doğru doğrusal olarak interpole eder (0 = saf DC, 1 = oturtulmuş). (gelişmiş, varsayılan: 0.0) | FLOAT | Evet | 0.0 - 1.0 |
| `fix_poles` | Değerlik-3 köşe çiftlerini daraltır (DC T-birleşim artefaktı). (gelişmiş, varsayılan: false) | BOOLEAN | Evet | true / false |
| `smooth_iters` | Taubin yumuşatma yinelemeleri (0 = kapalı). 2-3, DC merdiven benzeri artefaktları temizler; daha yüksek değerler QEF kenarlarını aşırı yumuşatır. (varsayılan: 0) | INT | Evet | 0 - 20 |
| `drop_small_components` | En büyük bileşenin yüz sayısının bu oranının altındaki bileşenleri atar. 0 devre dışı bırakır. (gelişmiş, varsayılan: 0.01) | FLOAT | Evet | 0.0 - 0.5 |
| `precluster_max_verts` | Alan sorgularından önce giriş köşe sayısını sınırlar; bunun üzerindeki girdiler önce bu değere küme-indirgenir. Büyük ağlarda OOM'u önler. (gelişmiş, varsayılan: 20,000,000) | INT | Evet | 0 - 100,000,000 |

### "udf" Modu Girdileri

Bu parametreler `sign_mode` `"udf"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `qef` | Daha keskin kenarlar için QEF (Quadratic Error Function) dual köşe yerleşimi. (gelişmiş, varsayılan: false) | BOOLEAN | Hayır | true / false |
| `drop_inverted_components` | İçe dönük normalli (negatif hacimli) kapalı bileşenleri atar — UDF iç kabuğu. (gelişmiş, varsayılan: false) | BOOLEAN | Hayır | true / false |
| `drop_enclosed_components` | En büyük bileşenin sınırlayıcı kutusu içinde olup point-in-mesh raycast'ini geçemeyen bileşenleri atar. Meşru iç içe parçalar için devre dışı bırakın. (gelişmiş, varsayılan: false) | BOOLEAN | Hayır | true / false |

### "sdf" Modu Girdileri

Bu parametreler `sign_mode` `"sdf"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `qef` | QEF (Quadratic Error Function) dual köşe yerleşimi (keskin özellikleri kurtarır) ile kenar geçişli ağırlık merkezi karşılaştırması. (varsayılan: true) | BOOLEAN | Hayır | true / false |
| `manifold` | Manifold Dual Contouring: çok katmanlı durumlar için voksel başına 1-4 dual köşe. Daha yavaş. (varsayılan: false) | BOOLEAN | Hayır | true / false |

Not: `qef` seçeneği, seçilen moda bağlı olarak farklı bir varsayılana sahiptir — "udf" modunda false, "sdf" modunda true. `precluster_max_verts` 0'dan büyük olduğunda ve giriş ağının köşe sayısı bu değerden fazla olduğunda, alan sorgularından önce ağ bu hedefe kadar küme-indirgenir. İşleme sonrasında düğüm, girişten çıkışa yüz sayısı değişimini düğüm üzerinde gösterir (örneğin, "faces: 1.23M → 200K (-84%)").

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mesh` | Tekdüze mozaikleme ve kaynaklanmış topolojiye sahip yeniden oluşturulmuş ağ. Girişte mevcutsa köşe renkleri korunur; UV'ler, normaller ve teğetler aktarılmaz. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemeshMesh/tr.md)

---
**Source fingerprint (SHA-256):** `aa9b7e4465196fab81a4a484ca9dd03d999b4621a611aed2b39d618e53702a06`
