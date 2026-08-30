# Meshy: Taslak Modeli İyileştir

Meshy: Refine Draft Model düğümü, önceki bir Meshy görevinden alınan 3D taslak modeli alır ve isteğe bağlı olarak bir metin istemi veya referans görsel kullanarak dokular ekleyerek modeli iyileştirir. İyileştirme işini Meshy API'sine gönderir ve görev tamamlandığında bitmiş modeli GLB ve FBX dosyaları olarak döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Taslak modeli iyileştirmek için kullanılan AI modeli. | COMBO | Evet | `"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `meshy_task_id` | İyileştirmek istediğiniz taslak modelin benzersiz görev kimliği. | MESHY_TASK_ID | Evet | - |
| `enable_pbr` | Temel renge ek olarak PBR Haritaları (metalik, pürüzlülük, normal) oluşturur. Not: Heykel stili kullanılırken bu değer false olarak ayarlanmalıdır; çünkü Heykel stili kendi PBR haritalarını üretir. (varsayılan: False) | BOOLEAN | Evet | - |
| `texture_prompt` | Dokulandırma sürecini yönlendirmek için bir metin istemi sağlar. En fazla 600 karakter. `texture_image` ile aynı anda kullanılamaz. (varsayılan: boş dize) | STRING | Evet | - |
| `texture_image` | `texture_image` veya `texture_prompt` öğelerinden yalnızca biri aynı anda kullanılabilir. | IMAGE | Hayır | - |
| `texture_resolution` | Temel renk doku çözünürlüğü. Daha yüksek çözünürlükler daha fazla yüzey detayı yakalar. | COMBO | Evet | `"2k"`<br>`"4k"<br>`"8k"` |

**Not:** `texture_prompt` ve `texture_image` girdileri birbirini dışlar. Aynı işlemde dokulandırma için hem metin istemi hem de görsel sağlayamazsınız.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_file` | Oluşturulan GLB modelinin dosya adı. (Yalnızca geriye dönük uyumluluk içindir) | STRING |
| `meshy_task_id` | Gönderilen iyileştirme işi için benzersiz görev kimliği. | MESHY_TASK_ID |
| `GLB` | GLB formatında nihai iyileştirilmiş 3B model. | FILE3DGLB |
| `FBX` | FBX formatında nihai iyileştirilmiş 3B model. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRefineNode/tr.md)

---
**Source fingerprint (SHA-256):** `73c9d712c4fd9fdd2792600ce874916ce9447d386407353c886f624641fa0e0f`
