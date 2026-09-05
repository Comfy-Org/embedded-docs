# TripoSegmentNode

Bu düğüm, bir 3D modeli tek tek parçalara böler. Modeli Tripo segmentasyon hizmetine gönderir, işin bitmesini bekler ve bölünmüş modeli, virgülle ayrılmış parça adları listesiyle birlikte GLB formatında döndürür. Bu parça adları; Tripo: Complete Mesh Parts, Tripo: Retopology ve Tripo: Convert model gibi sonraki adımları besler.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | Parçalara ayrılacak 3D modelin görev kimliği. | MODEL_TASK_ID | Evet | N/A |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
|-------------|-------------|-----------|
| `model_file` | Bölünmüş GLB modelin çıktı dosya adı. Yalnızca geriye dönük uyumluluk için korunur. | STRING |
| `segment task_id` | Sonucu üreten segmentasyon işinin görev kimliği. | SEGMENT_TASK_ID |
| `GLB` | GLB dosyası olarak bölünmüş 3D model. | GLB |
| `part_names` | Parçaların virgülle ayrılmış adları. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSegmentNode/tr.md)

---
**Source fingerprint (SHA-256):** `d27580a7f2118e76cecff5e1d682c7605f966bf657d7a02b2d2ddf764d9b72d0`
