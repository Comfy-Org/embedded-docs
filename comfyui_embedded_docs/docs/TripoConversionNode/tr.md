> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/tr.md)

TripoConversionNode, Tripo API'sini kullanarak 3B modelleri farklı dosya formatları arasında dönüştürür. Önceki bir Tripo işleminden alınan görev kimliğini alır ve ortaya çıkan modeli çeşitli dışa aktarma seçenekleriyle istediğiniz formata dönüştürür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | MODEL_TASK_ID,RIG_TASK_ID,RETARGET_TASK_ID | Evet | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID | Önceki bir Tripo işleminden (model oluşturma, rigleme veya yeniden hedefleme) alınan görev kimliği |
| `format` | COMBO | Evet | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF | Dönüştürülecek 3B model için hedef dosya formatı |
| `quad` | BOOLEAN | Hayır | Doğru/Yanlış | Üçgenlerin dörtgenlere dönüştürülüp dönüştürülmeyeceği (varsayılan: Yanlış) |
| `face_limit` | INT | Hayır | -1 - 500000 | Çıktı modelindeki maksimum yüz sayısı, sınırsız için -1 kullanın (varsayılan: -1) |
| `texture_size` | INT | Hayır | 128 - 4096 | Çıktı dokularının piksel cinsinden boyutu (varsayılan: 4096) |
| `texture_format` | COMBO | Hayır | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP | Dışa aktarılan dokular için format (varsayılan: JPEG) |

**Not:** `original_model_task_id`, önceki bir Tripo işleminden (model oluşturma, rigleme veya yeniden hedefleme) alınan geçerli bir görev kimliği olmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| *İsimlendirilmiş çıktı yok* | - | Bu düğüm, dönüşümü eşzamansız olarak işler ve sonucu Tripo API sistemi aracılığıyla döndürür |