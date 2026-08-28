# RemeshMesh

Remesh Mesh, orijinal yüzey çevresindeki dar bant mesafe alanını örnekleyerek ve Dual Contouring ile çıkararak mesh'i temiz ve düzgün bir mozaiklemeyle yeniden oluşturur. Bu; dağınık, manifold olmayan veya kendisiyle kesişen topolojiyi normalleştirir ve tam bir yüz sayısına ulaşmak için Decimate Mesh'ten önce çalıştırılması amaçlanır. İşlem, etkin hesaplama aygıtında çalışır ve çıktı mesh'i kaynaklı kalır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `mesh` | Yeniden oluşturulacak girdi mesh'i. | MESH | Evet | — |
| `çözünürlük` | Voksel ızgara çözünürlüğü (çıktı yoğunluğu). 256 ~ 100 bin yüz, 512 ~ 1 milyon. Tam bir yüz sayısı için ardından Decimate Mesh kullanın. (varsayılan: 512) | INT | Evet | 32 - 2048 |
| `sign_mode` | Yüzey çıkarımı için kullanılan işaretli mesafe modu. "udf", dağınık/manifold olmayan girdilere karşı dayanıklıdır; "sdf", QEF (Quadratic Error Function) keskin özellik kurtarma ile temiz tek bir yüzey üretir, ancak tutarlı sargı yönü gerektirir. Bir mod seçmek, o moda özgü alt seçenekleri gösterir. (varsayılan: "udf") | DYNAMIC_COMBO | Evet | "udf"<br>"sdf" |
| `band` | Voksel biriminde dar bant genişliği. UDF modunda ayrıca yüzeyi öteler. (gelişmiş, varsayılan: 1.0) | FLOAT | Evet | 0.5 - 4.0 |
| `project_back` | Köşeleri orijinal yüzeye doğru doğrusal olarak enterpole et (0 = saf DC, 1 = tutturulmuş). (gelişmiş, varsayılan: 0.0) | FLOAT | Evet | 0.0 - 1.0 |
| `fix_poles` | Valens-3 köşe çiftlerini birleştir (DC T-kavşağı artefaktı). (gelişmiş, varsayılan: false) | BOOLEAN | Evet | true / false |
| `smooth_iters` | Taubin yumuşatma yineleme sayısı (0 = kapalı). 2-3, DC merdiven benzeri artefaktları temizler; daha yüksek değerler QEF kenarlarını aşırı yumuşatır. (varsayılan: 0) | INT | Evet | 0 - 20 |
| `drop_small_components` | En büyük bileşenin yüz sayısının bu oranının altındaki bileşenleri at. 0 devre dışı bırakır. (gelişmiş, varsayılan: 0.01) | FLOAT | Evet | 0.0 - 0.5 |
| `precluster_max_verts` | Alan sorgularından önce girdi köşe sayısını sınırla; bunun üzerindeki girdiler önce buna göre küme-seyreltme uygulanarak azaltılır. Büyük mesh'lerde OOM'u önler. (gelişmiş, varsayılan: 20.000.000) | INT | Evet | 0 - 100,000,000 |

### "udf" Modu Girdileri

Bu parametreler, `sign_mode` değeri `"udf"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `qef` | Daha keskin kenarlar için QEF (Quadratic Error Function) çift köşe yerleşimi. (varsayılan: false) | BOOLEAN | Hayır | true / false |
| `drop_inverted_components` | İçe normal (negatif hacimli) kapalı bileşenleri at — UDF iç kabuğu. (varsayılan: false) | BOOLEAN | Hayır | true / false |
| `drop_enclosed_components` | En büyük bileşenin sınır kutusu (bbox) içindeki, mesh içinde nokta ışın testini geçemeyen bileşenleri at. Geçerli iç içe parçalar için devre dışı bırakın. (varsayılan: false) | BOOLEAN | Hayır | true / false |

### "sdf" Modu Girdileri

Bu parametreler, `sign_mode` değeri `"sdf"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `qef` | QEF (Quadratic Error Function) çift köşe yerleşimi (keskin özellikleri kurtarır) ile kenar-kesişim merkezi arasında seçim yapar. (varsayılan: true) | BOOLEAN | Hayır | true / false |
| `manifold` | Manifold Dual Contouring: çok katmanlı durumlar için voksel başına 1-4 çift köşe. Daha yavaş. (varsayılan: false) | BOOLEAN | Hayır | true / false |

Not: `qef` seçeneğinin varsayılan değeri seçilen moda göre farklılık gösterir — "udf" modunda false, "sdf" modunda true. `precluster_max_verts` değeri 0'dan büyükse ve girdi mesh'i bu değerden daha fazla köşeye sahipse, mesh alan sorgularından önce küme-seyreltme ile bu hedefe indirilir. İşlem sonrasında düğüm, girdiden çıktıya yüz sayısı değişimini düğüm üzerinde görüntüler (örneğin, "yüzler: 1.23M → 200K (-84%)").

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `ağ` | Düzgün mozaikleme ve kaynaklı topolojiye sahip yeniden oluşturulmuş mesh. Girdide mevcut olduğunda köşe renkleri korunur; UV'ler, normaller ve teğetler aktarılmaz. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemeshMesh/tr.md)

---
**Source fingerprint (SHA-256):** `33b9603aad2aa8f4122dab75aa9d60caa0ab7ed81300461f3b773bb997251d99`
