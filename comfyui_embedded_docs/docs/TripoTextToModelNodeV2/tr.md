# TripoTextToModelNodeV2

Generates a 3D model from a text description using the Tripo service. The node sends the prompt and settings to Tripo, waits for the generation task to finish, and returns the finished 3D file together with the task identifier.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|---------|--------|
| `prompt` | Üretilecek modelin metin açıklaması. Boş olmamalıdır. | STRING | Evet | Çok satırlı metin |
| `negative_prompt` | Üretilen modelde görünmemesi gerekenleri açıklayan metin. En fazla 255 karakter. | STRING | Hayır | Çok satırlı metin, en fazla 255 karakter |
| `model_version` | Üretim için kullanılan Tripo model sürümü (varsayılan: `v3.1_20260211`). | COMBO | Hayır | Desteklenen Tripo model sürümlerinin listesi |
| `texture` | Doku haritaları üretir. Kapalı olduğunda çıplak geometri döndürür ve `pbr` yok sayılır (varsayılan: True). | BOOLEAN | Hayır | True<br>False |
| `pbr` | PBR malzeme haritaları (temel renk, metalik, pürüzlülük, normal). `texture` gerektirir (varsayılan: True). | BOOLEAN | Hayır | True<br>False |
| `image_seed` | Görüntü üretimi için seed değeri (varsayılan: 42). | INT | Hayır | 0 - 2147483647 |
| `model_seed` | Model üretimi için seed değeri (varsayılan: 42). | INT | Hayır | 0 - 2147483647 |
| `texture_seed` | Doku üretimi için seed değeri (varsayılan: 42). | INT | Hayır | 0 - 2147483647 |
| `texture_quality` | Doku ayrıntı düzeyi (varsayılan: "standard"). "detailed" = HD dokular, "extreme" = 8K Ultra dokular. | COMBO | Hayır | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `face_limit` | Maksimum yüz sayısı. -1, Tripo'nun uyarlamalı seçim yapmasını sağlar (v3.x standardında yaklaşık 1,4M yüz, detailed'da 2M). Tripo sessizce sınırlar: quad ağlarda 150.000 (varsayılan: -1). | INT | Hayır | -1 - 2000000 |
| `quad` | Quad ağ çıktısı. Tripo quad ağları FBX olarak teslim eder, bu nedenle sonuç FBX çıktısına gelir ve GLB çıktısı boş kalır (varsayılan: False). | BOOLEAN | Hayır | True<br>False |
| `geometry_quality` | Geometri ayrıntı düzeyi (varsayılan: "standard"). | COMBO | Hayır | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | Temiz, el yapımı tarzı topolojiye sahip düşük poligonlu ağ (500-20.000 yüz, quad 500-10.000). Basit konular için en iyisidir; karmaşık olanlar başarısız olabilir (varsayılan: False). | BOOLEAN | Hayır | True<br>False |
| `auto_size` | Dokulu modelleri metre cinsinden gerçek dünya boyutlarına ölçekler. Tripo, boyutu modelin sahne dönüşümü olarak saklar ve model dönüştürüldüğünde, riglendiğinde veya yeniden hedeflendiğinde bunu gömer; doku olmadan yok sayılır (varsayılan: True). | BOOLEAN | Hayır | True<br>False |

### Notlar

- `prompt` zorunludur ve boş veya yalnızca boşluk karakterlerinden oluşamaz.
- `texture` False olarak ayarlandığında, `pbr` zorla kapatılır ve `auto_size` etkisiz olur.
- `smart_low_poly` etkinleştirildiğinde ve `face_limit` -1 değilse, üçgen ağlar için `face_limit` 500 ile 20.000 arasında, `quad` etkinleştirildiğinde ise 500 ile 10.000 arasında olmalıdır.
- `quad` etkinleştirildiğinde, Tripo bir FBX dosyası döndürür; bu nedenle `GLB` çıktısı boş kalır ve `FBX` çıktısı doldurulur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model task_id` | Modeli üreten Tripo üretim görevinin tanımlayıcısı. | MODEL_TASK_ID |
| `GLB` | GLB biçiminde üretilen model. `quad` etkinleştirildiğinde boş olur. | FILE3D_GLB |
| `FBX` | FBX biçiminde üretilen model. Yalnızca `quad` etkinleştirildiğinde doldurulur. | FILE3D_FBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNodeV2/tr.md)

---
**Source fingerprint (SHA-256):** `8af7044188c6dbb87d23298bf7b99fe826bdc7bd7ba0948db2066887274faa00`
