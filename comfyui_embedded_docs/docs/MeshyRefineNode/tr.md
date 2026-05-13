> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRefineNode/tr.md)

**Meshy: Taslak Modeli İyileştir** düğümü, önceden oluşturulmuş bir 3D taslak modeli alır ve isteğe bağlı olarak dokular ekleyerek kalitesini artırır. Meshy API'sine bir iyileştirme görevi gönderir ve işlem tamamlandığında nihai 3D model dosyalarını döndürür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `"latest"` | İyileştirme için kullanılacak AI modelini belirtir. Şu anda yalnızca "latest" (en son) model mevcuttur. |
| `meshy_task_id` | MESHY_TASK_ID | Evet | - | İyileştirmek istediğiniz taslak modelin benzersiz görev kimliği. |
| `enable_pbr` | BOOLEAN | Hayır | - | Temel renge ek olarak PBR Haritaları (metalik, pürüzlülük, normal) oluşturur. Not: Heykel stili kullanılırken bu değer false olarak ayarlanmalıdır, çünkü Heykel stili kendi PBR haritalarını oluşturur. (varsayılan: `False`) |
| `texture_prompt` | STRING | Hayır | - | Doku oluşturma sürecini yönlendirmek için bir metin istemi sağlar. Maksimum 600 karakter. `texture_image` ile aynı anda kullanılamaz. (varsayılan: boş dize) |
| `texture_image` | IMAGE | Hayır | - | `texture_image` veya `texture_prompt` girdilerinden yalnızca biri aynı anda kullanılabilir. |

**Not:** `texture_prompt` ve `texture_image` girdileri birbirini dışlar. Aynı işlemde doku oluşturma için hem metin istemi hem de görsel sağlayamazsınız.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `meshy_task_id` | STRING | Oluşturulan GLB modelinin dosya adı. (Yalnızca geriye dönük uyumluluk içindir) |
| `GLB` | MESHY_TASK_ID | Gönderilen iyileştirme işi için benzersiz görev kimliği. |
| `FBX` | FILE3DGLB | GLB formatında nihai iyileştirilmiş 3D model. |
| `FBX` | FILE3DFBX | FBX formatında nihai iyileştirilmiş 3D model. |

---
**Source fingerprint (SHA-256):** `cdf620ead0a4504cbb5d5554e0fe40e4cadd08884726f147cd486e63ab37f278`
