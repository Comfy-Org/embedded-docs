# TripoImageToModelNodeV2

Tripo: Image to Model düğümü, tek bir referans görüntüyü Tripo'nun görselden modele hizmetini kullanarak bir 3D modele dönüştürür. Görüntüyü yükler, bir üretim görevi gönderir, görevin tamamlanmasını bekler ve elde edilen 3D dosyayı görev kimliğiyle birlikte döndürür. Bu bir API düğümüdür, bu nedenle geçerli bir Comfy API anahtarı gerektirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | 3D modeli oluşturmak için kullanılan referans görüntü. | IMAGE | Evet | — |
| `model_version` | Üretim için kullanılacak model sürümü. Ayarlanmazsa düğüm, Tripo'nun v3.1 (20260211) sürümüne geri döner. | COMBO | Hayır | Tripo model sürümleri listesi |
| `texture` | Doku haritaları oluşturur. Kapalı olduğunda çıplak geometri döndürür ve `pbr` yok sayılır (varsayılan: true). | BOOLEAN | Hayır | true<br>false |
| `pbr` | PBR malzeme haritaları (temel renk, metalik, pürüzlülük, normal). `texture` gerektirir (varsayılan: true). | BOOLEAN | Hayır | true<br>false |
| `model_seed` | Geometri üretim adımında kullanılan seed (varsayılan: 42). | INT | Hayır | 0 ile 2147483647 arası |
| `orientation` | Üretilen modele uygulanan yönlendirme ayarı (varsayılan: DEFAULT). | COMBO | Hayır | Tripo yönlendirme seçenekleri, varsayılan `DEFAULT` |
| `texture_seed` | Doku üretim adımında kullanılan seed (varsayılan: 42). | INT | Hayır | 0 ile 2147483647 arası |
| `texture_quality` | detailed = HD dokular, extreme = 8K Ultra dokular (varsayılan: "standard"). | COMBO | Hayır | "standard"<br>"detailed"<br>"extreme" |
| `texture_alignment` | Dokuların üretilen geometri üzerinde nasıl hizalandığı (varsayılan: "original_image"). | COMBO | Hayır | "original_image"<br>"geometry" |
| `face_limit` | Maksimum yüz sayısı. -1, Tripo'nun uyarlamalı seçim yapmasını sağlar (v3.x standardında yaklaşık 1,4M yüz, detailed modunda 2M). Tripo sessizce sınırlar: quad mesh'ler için 150.000 (varsayılan: -1). | INT | Hayır | -1 ile 2000000 arası |
| `quad` | Quad mesh çıktısı. Tripo, quad mesh'leri FBX olarak teslim eder; bu nedenle sonuç FBX çıktısına gelir ve GLB çıktısı boş kalır (varsayılan: false). | BOOLEAN | Hayır | true<br>false |
| `geometry_quality` | Üretilen geometrinin kalite düzeyi (varsayılan: "standard"). | COMBO | Hayır | "standard"<br>"detailed" |
| `smart_low_poly` | Temiz, el yapımı tarzda topolojiye sahip düşük poligonlu mesh (500-20.000 yüz, quad 500-10.000). Basit nesneler için en iyisidir; karmaşık olanlar başarısız olabilir (varsayılan: false). | BOOLEAN | Hayır | true<br>false |
| `auto_size` | Dokulu modelleri metre cinsinden gerçek dünya boyutlarına ölçekler. Tripo, boyutu modelin sahne dönüşümü olarak saklar ve model dönüştürüldüğünde, riglendiğinde veya yeniden hedeflendiğinde bunu içine işler; doku olmadan yok sayılır (varsayılan: true). | BOOLEAN | Hayır | true<br>false |

**Notlar:**

- `image` gereklidir; görüntü sağlanmazsa düğüm hata verir.
- `smart_low_poly` etkinleştirildiğinde ve `face_limit` -1 dışında bir değere ayarlandığında, sınır üçgen mesh'ler için 500 ile 20.000 arasında, `quad` etkinleştirildiğinde ise 500 ile 10.000 arasında olmalıdır. Diğer değerler hata verir.
- `texture` devre dışı bırakıldığında, `pbr` ayarından bağımsız olarak zorla kapatılır ve `auto_size` etkisiz olur.
- `face_limit` değeri -1 olduğunda Tripo'ya "no limit" olarak gönderilir ve hizmetin uyarlamalı seçim yapmasına izin verir.
- Düğümün döndüremeyeceği yeni bir 3D dosya biçimi (GLB veya FBX dışında herhangi bir şey) hataya neden olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model task_id` | Üretim işinin Tripo görev kimliği. | MODEL_TASK_ID |
| `GLB` | Üretilen model GLB dosyası olarak. `quad` etkinleştirildiğinde boş olur. | FILE3DGLB |
| `FBX` | Üretilen model FBX dosyası olarak. Yalnızca `quad` etkinleştirildiğinde doldurulur. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNodeV2/tr.md)

---
**Source fingerprint (SHA-256):** `c8c069432f67a019995b9f4dedbf5ca3f7594ae4004104277068106821189c11`
