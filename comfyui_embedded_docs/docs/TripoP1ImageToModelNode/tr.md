> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/tr.md)

## Genel Bakış

Bu düğüm, Tripo P1 API'sini kullanarak tek bir 2D görüntüyü 3D modele dönüştürür. Düşük poligonlu, oyunlara hazır ağlar (mesh) oluşturmak için optimize edilmiştir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | 3D modele dönüştürülecek giriş görüntüsü. |
| `output_mode` | DICT | Evet | Açıklamaya bakın | Çıktı modunu ve kalite ayarlarını belirten bir sözlük. Bu parametre, oluşturulan modelin türünü ve doku kalitesini kontrol eder. Mevcut seçenekler `_build_p1_output_mode` yardımcı fonksiyonu tarafından tanımlanır ve `texture_quality` ("standard", "high", "ultra" gibi) ile `image_alignment` ayarlarını içerir. |
| `enable_image_autofix` | BOOLEAN | Hayır | True<br>False | Daha iyi üretim kalitesi için giriş görüntüsünü ön işleme tabi tutar. (varsayılan: False) |
| `face_limit` | INT | Hayır | - | Oluşturulan ağdaki yüz sayısını sınırlar. -1 değeri sınırlama olmadığı anlamına gelir. (varsayılan: -1) |
| `model_seed` | INT | Hayır | - | Tekrarlanabilir model üretimi için tohum değeri. Sağlanmazsa rastgele bir tohum kullanılır. (varsayılan: None) |
| `auto_size` | BOOLEAN | Hayır | True<br>False | Oluşturulan model için en uygun boyutu otomatik olarak belirler. (varsayılan: False) |
| `export_uv` | BOOLEAN | Hayır | True<br>False | Modelle birlikte UV koordinatlarını dışa aktarır. (varsayılan: True) |
| `compress_geometry` | BOOLEAN | Hayır | True<br>False | Dosya boyutunu küçültmek için geometri verilerini sıkıştırır. (varsayılan: False) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model_file` | STRING | Oluşturulan 3D modelin dosya yolu. Bu çıktı yalnızca geriye dönük uyumluluk için sağlanmıştır. |
| `model task_id` | MODEL_TASK_ID | Model oluşturma isteği için benzersiz görev kimliği. |
| `GLB` | FILE3DGLB | GLB formatında oluşturulan 3D model. |

---
**Source fingerprint (SHA-256):** `2ac611603dd6eb88700a8105c19f97a8c4eefe5f4efb23d8854ccc27af590626`
