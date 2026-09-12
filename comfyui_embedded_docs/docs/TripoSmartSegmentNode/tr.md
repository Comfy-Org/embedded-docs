# TripoSmartSegmentNode

Bir 3B modeli anlamsal olarak anlamlı parçalara böler ve her parçaya bir ad verir. Mevcut bir modeli (bir görev kimliği aracılığıyla sağlanan) segmentlere ayırabilir veya önce bir görüntüden model oluşturup ardından onu segmentlere ayırabilir. Ortaya çıkan `segment task_id`, Complete Mesh Parts, Retopology, Texture model ve Convert model gibi diğer Tripo düğümleri tarafından bir Tripo: Segment Model sonucuyla aynı şekilde kullanılabilir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `source` | Mevcut bir modeli segmentlere ayırın veya bir görüntüden model oluşturup segmentlere ayırın. Seçilen seçenek, hangi ek girdilerin görüneceğini belirler. | DYNAMIC_COMBO | Evet | `"model"`<br>`"image"` |

### Model Girdileri

`source` `"model"` olarak ayarlandığında gösterilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | Bir GLB sonucu. Quad (FBX) mesh'leri önce Tripo: Convert model (GLTF) üzerinden geçmelidir. | MODEL_TASK_ID | Evet | - |
| `granularity` | Modelin parçalara ne kadar ince bölündüğü (varsayılan: "medium"). | COMBO | Hayır | `"coarse"`<br>`"medium"`<br>`"fine"` |
| `hint` | Aranacak parçaları adlandıran isteğe bağlı metin, örn. 'kılıçlı ve zırhlı oyun karakteri' (varsayılan: boş). | STRING | Hayır | - |

### Görüntü Girdileri

`source` `"image"` olarak ayarlandığında gösterilir. Tripo önce görüntüden bir model oluşturur, ardından onu segmentlere ayırır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Segmentlere ayrılacak modeli oluşturmak için kullanılan görüntü. | IMAGE | Evet | - |
| `granularity` | Modelin parçalara ne kadar ince bölündüğü (varsayılan: "medium"). | COMBO | Hayır | `"coarse"`<br>`"medium"`<br>`"fine"` |
| `hint` | Aranacak parçaları adlandıran isteğe bağlı metin, örn. 'kılıçlı ve zırhlı oyun karakteri' (varsayılan: boş). | STRING | Hayır | - |

**Notlar:**

- `granularity` ve `hint` her iki `source` seçeneği tarafından da paylaşılır ve isteğe bağlıdır. `hint` boş bırakıldığında hizmete hiçbir ipucu gönderilmez.
- `source` `"model"` olduğunda yalnızca GLB modelleri kabul edilir. Quad (FBX) mesh'leri gibi diğer biçimler önce Tripo: Convert model (GLTF) ile dönüştürülmelidir.
- Görev, son bir duruma ulaşana kadar yoklanır; tahmini süre yaklaşık 180 saniyedir. Tripo eksik bir segmentasyon sonucu döndürürse düğüm bir hata bildirir.
- Fiyat rozeti: `source` `"image"` olduğunda yaklaşık 0,85 USD ve `source` `"model"` olduğunda yaklaşık 0,55 USD (değerler yaklaşık olarak gösterilir).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `segment task_id` | Segmentasyon görevinin görev kimliği; diğer Tripo düğümleri için girdi olarak kullanılabilir. | SEGMENT_TASK_ID |
| `model task_id` | Segmentlere ayrılan model (görüntüden oluşturulan veya içe aktarılan). | MODEL_TASK_ID |
| `GLB` | Segmentlere ayrılmış 3B model dosyası. | FILE3DGLB |
| `part_names` | Parçaların virgülle ayrılmış adları. | STRING |
| `parts` | Tripo'nun bulduğu parçaların açıklaması. | STRING |
| `mask` | Segmentasyon tarafından üretilen maske görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSmartSegmentNode/tr.md)

---
**Source fingerprint (SHA-256):** `ba041da49e20b1ac085770078cce6ac87ef70eee927ba0ee9e5655a058893f1c`
