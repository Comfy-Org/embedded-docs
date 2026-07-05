# Meshy: Çoklu Görüntüden Modele

Bu düğüm, birden fazla girdi görüntüsünden 3B model oluşturmak için Meshy API'sini kullanır. Sağlanan görüntüleri yükler, bir işleme görevi gönderir ve ortaya çıkan 3B model dosyalarını (GLB ve FBX) referans için görev kimliğiyle birlikte döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak AI model sürümünü belirtir. | COMBO | Evet | `"latest"` |
| `images` | 3B modeli oluşturmak için kullanılan bir dizi görüntü. 2 ila 4 arasında görüntü sağlamalısınız. | IMAGE | Evet | 2 ila 4 görüntü |
| `should_remesh` | Oluşturulan ağın işlenip işlenmeyeceğini belirler. `"false"` olarak ayarlandığında, düğüm işlenmemiş bir üçgen ağ döndürür. | COMBO | Evet | `"true"`<br>`"false"` |
| `topology` | Yeniden ağ oluşturma çıktısı için hedef çokgen türü. Bu parametre yalnızca `should_remesh` `"true"` olarak ayarlandığında kullanılabilir ve gereklidir. | COMBO | Hayır | `"triangle"`<br>`"quad"` |
| `target_polycount` | Yeniden ağ oluşturulan model için hedef çokgen sayısı (varsayılan: 300000). Bu parametre yalnızca `should_remesh` `"true"` olarak ayarlandığında kullanılabilir. | INT | Hayır | 100 ila 300000 |
| `symmetry_mode` | Oluşturulan modele simetri uygulanıp uygulanmayacağını kontrol eder. | COMBO | Evet | `"auto"`<br>`"on"`<br>`"off"` |
| `should_texture` | Dokuların oluşturulup oluşturulmayacağını belirler. `"false"` olarak ayarlanması doku aşamasını atlar ve dokusuz bir ağ döndürür. | COMBO | Evet | `"true"`<br>`"false"` |
| `enable_pbr` | `should_texture` `"true"` olduğunda, bu seçenek temel renge ek olarak PBR Haritaları (metalik, pürüzlülük, normal) oluşturur (varsayılan: False). | BOOLEAN | Hayır | True / False |
| `texture_prompt` | Doku oluşturma sürecini yönlendirmek için bir metin istemi (maksimum 600 karakter). `texture_image` ile aynı anda kullanılamaz. Bu parametre yalnızca `should_texture` `"true"` olarak ayarlandığında kullanılabilir. | STRING | Hayır | - |
| `texture_image` | Doku oluşturma sürecini yönlendirmek için bir görüntü. `texture_image` veya `texture_prompt`'tan aynı anda yalnızca biri kullanılabilir. Bu parametre yalnızca `should_texture` `"true"` olarak ayarlandığında kullanılabilir. | IMAGE | Hayır | - |
| `pose_mode` | Oluşturulan model için poz modunu belirtir. | COMBO | Evet | `""` (boş)<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | Oluşturma işlemi için bir tohum değeri (varsayılan: 0). Tohumdan bağımsız olarak sonuçlar deterministik değildir, ancak tohumu değiştirmek düğümün yeniden çalışmasını tetikleyebilir. | INT | Evet | 0 ila 2147483647 |

**Parametre Kısıtlamaları:**

* `images` girdisi için 2 ila 4 arasında görüntü sağlamalısınız.
* `topology` ve `target_polycount` parametreleri yalnızca `should_remesh` `"true"` olarak ayarlandığında etkindir.
* `enable_pbr`, `texture_prompt` ve `texture_image` parametreleri yalnızca `should_texture` `"true"` olarak ayarlandığında etkindir.
* `texture_prompt` ve `texture_image` aynı anda kullanılamaz; bunlar birbirini dışlayan seçeneklerdir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model_file` | Oluşturulan GLB modelinin dosya adı. Bu çıktı, geriye dönük uyumluluk için sağlanmıştır. | STRING |
| `meshy_task_id` | Meshy API görevi için benzersiz tanımlayıcı. | MESHY_TASK_ID |
| `GLB` | GLB formatında oluşturulan 3B model. | FILE3DGLB |
| `FBX` | FBX formatında oluşturulan 3B model. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyMultiImageToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `e6f75f50645c8b2cf5ebbe037edb077ef1eb0ea1baf67c581d60ac0033686d00`
