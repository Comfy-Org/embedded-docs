# Tripo: Modeli Bölümlere Ayır

Bu düğüm, bir 3B modeli tek tek parçalara ayırır. Modeli Tripo segmentasyon hizmetine gönderir, işin tamamlanmasını bekler ve parçalara ayrılmış modeli GLB biçiminde, virgülle ayrılmış bir parça adları listesiyle birlikte döndürür. Bu parça adları Tripo: Complete Mesh Parts, Tripo: Retopology ve Tripo: Convert model gibi sonraki adımları besler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | Parçalara ayrılacak 3B modelin görev kimliği. | MODEL_TASK_ID | Evet | N/A |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_file` | Parçalara ayrılmış GLB modelinin çıktı dosya adı, `<task_id>.glb` biçiminde. Yalnızca geriye dönük uyumluluk için tutulur. | STRING |
| `segment task_id` | Sonucu üreten segmentasyon işinin görev kimliği. | SEGMENT_TASK_ID |
| `GLB` | Parçalara ayrılmış 3B model, GLB dosyası olarak. | GLB |
| `part_names` | Parçaların virgülle ayrılmış adları. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSegmentNode/tr.md)

---
**Source fingerprint (SHA-256):** `3218f87bfdc347d58b639cbe57b01cf7625c95c753bf381e35b4a28376eeb0e8`
