**Meshy: Taslak Modeli İyileştir** düğümü, önceden oluşturulmuş bir 3D taslak modeli alır ve isteğe bağlı olarak dokular ekleyerek kalitesini artırır. Meshy API'sine bir iyileştirme görevi gönderir ve işlem tamamlandığında nihai 3D model dosyalarını döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | İyileştirme için kullanılacak AI modelini belirtir. Şu anda yalnızca "latest" (en son) model mevcuttur. | COMBO | Evet | `"latest"` |
| `meshy_task_id` | İyileştirmek istediğiniz taslak modelin benzersiz görev kimliği. | MESHY_TASK_ID | Evet | - |
| `enable_pbr` | Temel renge ek olarak PBR Haritaları (metalik, pürüzlülük, normal) oluşturur. Not: Heykel stili kullanılırken bu değer false olarak ayarlanmalıdır, çünkü Heykel stili kendi PBR haritalarını oluşturur. (varsayılan: `False`) | BOOLEAN | Hayır | - |
| `texture_prompt` | Doku oluşturma sürecini yönlendirmek için bir metin istemi sağlar. Maksimum 600 karakter. `texture_image` ile aynı anda kullanılamaz. (varsayılan: boş dize) | STRING | Hayır | - |
| `texture_image` | `texture_image` veya `texture_prompt` girdilerinden yalnızca biri aynı anda kullanılabilir. | IMAGE | Hayır | - |

**Not:** `texture_prompt` ve `texture_image` girdileri birbirini dışlar. Aynı işlemde doku oluşturma için hem metin istemi hem de görsel sağlayamazsınız.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `meshy_task_id` | Oluşturulan GLB modelinin dosya adı. (Yalnızca geriye dönük uyumluluk içindir) | STRING |
| `GLB` | Gönderilen iyileştirme işi için benzersiz görev kimliği. | MESHY_TASK_ID |
| `FBX` | GLB formatında nihai iyileştirilmiş 3D model. | FILE3DGLB |
| `FBX` | FBX formatında nihai iyileştirilmiş 3D model. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRefineNode/tr.md)

---
**Source fingerprint (SHA-256):** `cdf620ead0a4504cbb5d5554e0fe40e4cadd08884726f147cd486e63ab37f278`
