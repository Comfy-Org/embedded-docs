# Tripo: Model Dokulama (Eski)

Tripo: Texture model (Legacy) düğümü, Tripo API aracılığıyla mevcut bir Tripo 3D modeline dokular ekler. Başka bir Tripo düğümü tarafından oluşturulan bir modelin görev kimliğini alır ve doku işi tamamlandığında dokulu bir GLB veya FBX modeli döndürür. Malzeme haritalarını, doku kalitesini, hizalamayı ve tohumu kontrol edebilir; dokuları bir metin istemi, bir stil görüntüsü veya referans görüntülerle yönlendirebilirsiniz. Bu düğüm, doku aracının eski bir sürümüdür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | Doku uygulanacak modelin Tripo görev kimliği. Model görev kimliklerini ve segmentasyon görev kimliklerini kabul eder. | MODEL_TASK_ID, SEGMENT_TASK_ID | Evet | - |
| `texture` | Yok sayılır: bu düğüm her zaman doku üretir. Eski iş akışları için korunmuştur. (varsayılan: True) | BOOLEAN | Hayır | true<br>false |
| `pbr` | PBR malzeme haritaları (temel renk, metalik, pürüzlülük, normal); kapalı olduğunda düz renkli bir doku verir. (varsayılan: True) | BOOLEAN | Hayır | true<br>false |
| `texture_seed` | Doku üretimi için rastgele tohum. (varsayılan: 42) | INT | Hayır | 0 – 2147483647 |
| `texture_quality` | Doku çözünürlüğü kalitesi: detailed = HD dokular, extreme = 8K Ultra dokular. (varsayılan: "standard"). Yaklaşık maliyet: standard $0.10, detailed $0.20, extreme $0.30. | COMBO | Hayır | "standard"<br>"detailed"<br>"extreme" |
| `texture_alignment` | Üretilen dokuları modele hizalamak için kullanılan yöntem. (varsayılan: "original_image") | COMBO | Hayır | "original_image"<br>"geometry" |
| `texture_prompt` | Doku kaplama için isteğe bağlı metin yönlendirmesi. Renkleri çıkarabilecek bir kaynak görüntü taşımayan içe aktarılmış modeller (Tripo: Import Model) için pratikte gereklidir. Referans görüntülerle birlikte kullanılamaz. (varsayılan: "") | STRING | Hayır | - |
| `model_version` | Doku modeli: v3.x ile üretilen mesh'ler için v3.0, v2.5 ile üretilen mesh'ler için v2.5. (varsayılan: v3.0_20250812) | COMBO | Hayır | Birden fazla seçenek mevcut |
| `style_image` | Dokuların sanatsal stili için referans görüntü. Yalnızca `texture_prompt` ile birlikte kullanılır. | IMAGE | Hayır | - |
| `reference` | Dokulara yol gösteren referans görüntüler. `texture_prompt` veya `style_image` ile birleştirilemez. (varsayılan: "none") | DYNAMIC_COMBO | Hayır | "none"<br>"image"<br>"multiview" |
| `part_names` | Tripo: Segment Model'den alınan, doku uygulanacak virgülle ayrılmış parça adları. Boş bırakılırsa her parçaya doku uygulanır. (varsayılan: "") | STRING | Hayır | - |

### `image` Referans Girdileri

Bu girdiler, `reference` değeri `"image"` olarak ayarlandığında kullanılabilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_image` | Dokuların izlemesi gereken tek referans görüntü. | IMAGE | Evet | - |

### `multiview` Referans Girdileri

Bu girdiler, `reference` değeri `"multiview"` olarak ayarlandığında kullanılabilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image_front` | Önden görünüm (0°). | IMAGE | Evet | - |
| `image_left` | Sol görünüm (90°). | IMAGE | Evet | - |
| `image_back` | Arka görünüm (180°). | IMAGE | Evet | - |
| `image_right` | Sağ görünüm (270°). | IMAGE | Evet | - |

**Not:** `"image"` ve `"multiview"` referans modları, boş olmayan bir `texture_prompt` ile veya `style_image` ile birleştirilemez. `style_image` girdisi, boş olmayan bir `texture_prompt` gerektirir. `texture_prompt` boş bırakıldığında, kaynak modelin zaten kendi kaynak görüntüsüne sahip olması gerekir (örneğin, metinden modele, görüntüden modele, çoklu görünümden modele veya daha önceki bir doku kaplama görevi tarafından üretilen modeller). Kaynak görüntü taşımayan modeller — içe aktarılmış, segmentlenmiş, tamamlanmış veya retopoloji uygulanmış modeller gibi — `texture_prompt` ile kaplanmalıdır; referans görüntüler yalnızca Tripo API'nin kendisinin ürettiği modeller için kabul edilir. Her parçaya doku uygulamak için `part_names` girdisi boş bırakılabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_file` | Üretilen model dosyası (yalnızca geriye dönük uyumluluk için). | STRING |
| `model task_id` | Tamamlanan doku üretim görevinin görev kimliği; diğer Tripo düğümleri için girdi olarak kullanılabilir. | MODEL_TASK_ID |
| `GLB` | GLB formatında üretilen dokulu model. Kaynak bir quad mesh veya FBX içe aktarımı olduğunda boştur. | FILE3DGLB |
| `FBX` | FBX formatında üretilen dokulu model. Tripo, quad mesh'ler ve FBX içe aktarımları için FBX döndürür; aksi halde boştur. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/tr.md)

---
**Source fingerprint (SHA-256):** `850685123b5f14cded5829d86a7307452a1e812e78d11f52806e64ea41d66350`
