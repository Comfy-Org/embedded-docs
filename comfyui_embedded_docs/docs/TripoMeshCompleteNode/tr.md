# Tripo: Ağ Parçalarını Tamamla

Parçalara ayrılmış bir 3B modelin parçalarını tamamlar ve meshin eksik veya hasarlı bölgelerini onarır. Bir Tripo mesh segmentasyon sonucunun görev kimliğini alır, Tripo'dan tamamlama işini ister ve tamamlanmasını bekler. İsteğe bağlı olarak işi belirli parça adlarıyla sınırlayabilirsiniz. Tamamlanan model bir GLB dosyası olarak döndürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `segment_task_id` | Bir Tripo mesh segmentasyon görevinin görev kimliği. Bu görevden parçalara ayrılmış modelin parçaları tamamlanır. Önceki bir Tripo mesh segmentasyon düğümünün SEGMENT_TASK_ID çıktısını bağlayın. | SEGMENT_TASK_ID | Evet | Tek görev kimliği |
| `part_names` | Tamamlanacak, virgülle ayrılmış parça adları. Boş bırakılırsa tüm parçalar tamamlanır. Varsayılan: boş dize. Adların çevresindeki fazladan boşluklar kaldırılır ve yinelenen adlar yok sayılır. | STRING | Hayır | Serbest metin veya boş |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-----------|-----------|
| `model_file` | Tamamlanan modelin dosya adı. Bu çıktı yalnızca geriye dönük uyumluluk için mevcuttur. | STRING |
| `model task_id` | Tamamlanan Tripo mesh tamamlama görevinin görev kimliği. Model görev kimliği bekleyen diğer Tripo düğümleri tarafından girdi olarak kullanılabilir. | MODEL_TASK_ID |
| `GLB` | Onarılmış parçalarla tamamlanan 3B model, GLB dosyası olarak indirilir. | GLB |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMeshCompleteNode/tr.md)

---
**Source fingerprint (SHA-256):** `c5709231fa2e33e6f3c9b25669acca1d4ae9adb882b90210d703aeddc0d11ecc`
