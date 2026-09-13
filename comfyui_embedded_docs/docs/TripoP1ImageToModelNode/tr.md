# Tripo P1: Görüntüden Modele

Tripo P1: Image to Model, tek bir 2B görüntüyü Tripo P1 API'sini kullanarak 3B modele dönüştürür. Düşük poligonlu, oyun için hazır mesh'ler üretmek üzere optimize edilmiştir ve yalnızca geometriden oluşan bir mesh ile PBR haritalı dokulu bir model arasında seçim yapmanıza olanak tanır. Tamamlanan model bir GLB dosyası olarak döndürülür.

## Girdiler

### Ortak Girdiler

Bu parametreler her zaman kullanılabilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `output_mode` | Sonuç türünü seçer. "Geometry only" dokusuz bir mesh döndürür; "Textured" renk/PBR haritaları ekler ve ek doku ayarlarını gösterir. | DYNAMIC_COMBO | Evet | `"Geometry only"`<br>`"Textured"` |
| `image` | 3B modeli oluşturmak için kullanılan kaynak 2B görüntü. Tek bir görüntü gereklidir; hiçbiri sağlanmazsa düğüm hata verir. | IMAGE | Evet | - |
| `enable_image_autofix` | Daha iyi üretim kalitesi için giriş görüntüsünü ön işleme tabi tutar. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |
| `face_limit` | Hedef yüz sayısı, 48-20000. -1, Tripo'nun uyarlamalı seçim yapmasını sağlar. (varsayılan: -1) | INT | Hayır | -1 - 20000 |
| `model_seed` | Geometri oluşturmada kullanılan tohum, sonuçların yeniden üretilebilmesini sağlar. (varsayılan: 42) | INT | Hayır | 0 - 2147483647 |
| `auto_size` | Çıktıyı yaklaşık gerçek dünya metrelerine ölçeklendirir. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |
| `export_uv` | Oluşturma sırasında UV açımı yapar. Daha hızlı yalnızca geometri çalıştırmaları için kapatın. (varsayılan: True) | BOOLEAN | Hayır | True<br>False |
| `compress_geometry` | meshopt geometri sıkıştırması uygular (EXT_meshopt_compression). Daha küçük dosyalar, ancak ComfyUI'nin 3B önizlemesi bunları görüntüleyemez; düzenlemeden önce sıkıştırmayı açın. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |

### Yalnızca Geometri Girdileri

Ek parametre yoktur. Çıktı, dokusuz bir meshtir.

### Dokulu Girdileri

Bu parametreler `output_mode` "Textured" olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `pbr` | PBR haritalarını dahil et. Açıkken temel doku da zorunlu olarak açılır. (varsayılan: True) | BOOLEAN | Evet | True<br>False |
| `texture_quality` | detailed = HD dokular, extreme = 8K Ultra dokular. (varsayılan: "standard") | COMBO | Evet | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_alignment` | Kaynak görüntüye görsel sadakati mi yoksa mesh geometrisine hizalamayı mı önceliklendirir. (varsayılan: "original_image") | COMBO | Evet | `"original_image"`<br>`"geometry"` |
| `orientation` | Çıktıyı kaynak görüntüyle eşleşecek şekilde döndürür. Yalnızca dokulu olduğunda uygulanır. (varsayılan: "default") | COMBO | Evet | `"default"`<br>`"align_image"` |
| `texture_seed` | Doku oluşturmada kullanılan tohum, dokulu sonuçların yeniden üretilebilmesini sağlar. (varsayılan: 42) | INT | Evet | 0 - 2147483647 |

Not: `output_mode` "Geometry only" olduğunda istek için doku oluşturma devre dışı bırakılır. "Textured" modunda her zaman bir renk dokusu istenir; `pbr` devre dışı bırakıldığında PBR haritaları kaldırılır ancak temel renk dokusu korunur; `pbr` etkinleştirildiğinde ise temel doku da zorunlu olarak açılır. `texture_alignment` ve `orientation` yalnızca "Textured" modunda kullanılabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_file` | Oluşturulan model dosya adını (`<task_id>.glb`) içeren bir dize. Yalnızca geriye dönük uyumluluk için tutulur. | STRING |
| `model task_id` | Tamamlanan oluşturma işi için Tripo API tarafından döndürülen benzersiz görev kimliği. | MODEL_TASK_ID |
| `GLB` | GLB biçiminde oluşturulan 3B model. | FILE3DGLB |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `1369da2ef732556896bce3415e7b99023f310544b8077ea4c6b1730bec59ee99`
