# RemeshMesh

Remesh Mesh, orijinal yüzeyin etrafındaki dar bant mesafe alanını örnekleyerek ve Dual Contouring ile çıkararak, ağı temiz ve düzgün bir mozaik dokuyla yeniden oluşturur. Bu işlem, dağınık, manifold olmayan veya kendisiyle kesişen topolojiyi normalleştirir ve tam yüz sayısına ulaşmak için Decimate Mesh'ten önce çalıştırılması amaçlanır. İşlem, etkin hesaplama aygıtında çalışır ve çıktı ağı kaynaklı (welded) kalır.

## Girdiler

### Genel Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Yeniden oluşturulacak giriş ağı. | MESH | Evet | — |
| `resolution` | Voksel ızgara çözünürlüğü (çıktı yoğunluğu). 256 ~ 100 bin yüz, 512 ~ 1M. Tam bir yüz sayısı için Decimate Mesh ile devam edin. (varsayılan: 512) | INT | Evet | 32 - 2048 |
| `sign_mode` | Yüzey çıkarımı için kullanılan işaretli mesafe modu. "udf", dağınık/manifold olmayan girdilere karşı dayanıklıdır; "sdf", QEF (İkinci Dereceden Hata Fonksiyonu) keskin özellik kurtarma ile temiz bir tek yüzey üretir, ancak tutarlı yönlendirme gerektirir. Bir mod seçmek, moda özel alt seçenekleri ortaya çıkarır. (varsayılan: "udf") | DYNAMIC_COMBO | Evet | "udf"<br>"sdf" |
| `band` | Voksel birimi cinsinden dar bant genişliği. UDF modunda yüzeyi de kaydırır. (gelişmiş, varsayılan: 1.0) | FLOAT | Evet | 0.5 - 4.0 |
| `project_back` | Köşeleri orijinal yüzeye doğru doğrusal olarak enterpolasyon yapar (0 = saf DC, 1 = yapıştırılmış). (gelişmiş, varsayılan: 0.0) | FLOAT | Evet | 0.0 - 1.0 |
| `fix_poles` | Değerlik-3 köşe çiftlerini birleştirir (DC T-birleşim yapaylığı). (gelişmiş, varsayılan: false) | BOOLEAN | Evet | true / false |
| `smooth_iters` | Taubin yumuşatma yinelemesi (0 = kapalı). 2-3, DC merdiven benzeri yapaylıkları temizler; daha yüksek değerler QEF kenarlarını aşırı yumuşatır. (varsayılan: 0) | INT | Evet | 0 - 20 |
| `drop_small_components` | En büyük bileşenin yüz sayısının bu oranının altındaki bileşenleri atar. 0 devre dışı bırakır. (gelişmiş, varsayılan: 0.01) | FLOAT | Evet | 0.0 - 0.5 |
| `precluster_max_verts` | Alan sorgularından önce giriş köşe sayısını sınırlar; bunun üzerindeki girdiler önce bu değere küme-azaltılır. Büyük ağlarda OOM'u önler. (gelişmiş, varsayılan: 20.000.000) | INT | Evet | 0 - 100.000.000 |

### "udf" Modu Girdileri

Bu parametreler, `sign_mode` `"udf"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `qef` | Daha keskin kenarlar için QEF (İkinci Dereceden Hata Fonksiyonu) ikili köşe yerleşimi. (varsayılan: false) | BOOLEAN | Hayır | true / false |
| `drop_inverted_components` | İçe dönük normal (negatif hacimli) kapalı bileşenleri — UDF iç kabuğu — atar. (varsayılan: false) | BOOLEAN | Hayır | true / false |
| `drop_enclosed_components` | En büyüğün sınırlama kutusunun içinde kalan ve ağ-içi ışın testinde başarısız olan bileşenleri atar. Meşru iç içe parçalar için devre dışı bırakın. (varsayılan: false) | BOOLEAN | Hayır | true / false |

### "sdf" Modu Girdileri

Bu parametreler, `sign_mode` `"sdf"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `qef` | QEF (İkinci Dereceden Hata Fonksiyonu) ikili köşe yerleşimi (keskin özellikleri kurtarır) ile kenar-kesişim merkezi arasında seçim. (varsayılan: true) | BOOLEAN | Hayır | true / false |
| `manifold` | Manifold Dual Contouring: çok katmanlı durumlar için voksel başına 1-4 ikili köşe. Daha yavaştır. (varsayılan: false) | BOOLEAN | Hayır | true / false |

Not: `qef` seçeneğinin varsayılan değeri seçilen moda göre farklılık gösterir — "udf" modunda false, "sdf" modunda true. `precluster_max_verts` değeri 0'dan büyükse ve giriş ağı bu değerden daha fazla köşeye sahipse, alan sorgularından önce ağ bu hedefe küme-azaltılır. İşlem sonrasında düğüm, girişten çıktıya yüz sayısı değişimini düğüm üzerinde görüntüler (örneğin, "yüz: 1,23M → 200K (-%84)").

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mesh` | Düzgün mozaik dokuya ve kaynaklı topolojiye sahip yeniden oluşturulmuş ağ. Girişte mevcut olduğunda köşe renkleri korunur; UV'ler, normaller ve teğetler aktarılmaz. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemeshMesh/tr.md)

---
**Source fingerprint (SHA-256):** `33b9603aad2aa8f4122dab75aa9d60caa0ab7ed81300461f3b773bb997251d99`
