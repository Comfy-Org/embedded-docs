> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyMultiImageToModelNode/tr.md)

Bu düğüm, birden fazla girdi görüntüsünden 3B model oluşturmak için Meshy API'sini kullanır. Sağlanan görüntüleri yükler, bir işleme görevi gönderir ve ortaya çıkan 3B model dosyalarını (GLB ve FBX) referans için görev kimliğiyle birlikte döndürür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
| :--- | :--- | :--- | :--- | :--- |
| `model` | COMBO | Evet | `"latest"` | Kullanılacak AI model sürümünü belirtir. |
| `images` | IMAGE | Evet | 2 ila 4 görüntü | 3B modeli oluşturmak için kullanılan bir dizi görüntü. 2 ila 4 arasında görüntü sağlamalısınız. |
| `should_remesh` | COMBO | Evet | `"true"`<br>`"false"` | Oluşturulan ağın işlenip işlenmeyeceğini belirler. `"false"` olarak ayarlandığında, düğüm işlenmemiş bir üçgen ağ döndürür. |
| `topology` | COMBO | Hayır | `"triangle"`<br>`"quad"` | Yeniden ağ oluşturma çıktısı için hedef çokgen türü. Bu parametre yalnızca `should_remesh` `"true"` olarak ayarlandığında kullanılabilir ve gereklidir. |
| `target_polycount` | INT | Hayır | 100 ila 300000 | Yeniden ağ oluşturulan model için hedef çokgen sayısı (varsayılan: 300000). Bu parametre yalnızca `should_remesh` `"true"` olarak ayarlandığında kullanılabilir. |
| `symmetry_mode` | COMBO | Evet | `"auto"`<br>`"on"`<br>`"off"` | Oluşturulan modele simetri uygulanıp uygulanmayacağını kontrol eder. |
| `should_texture` | COMBO | Evet | `"true"`<br>`"false"` | Dokuların oluşturulup oluşturulmayacağını belirler. `"false"` olarak ayarlanması doku aşamasını atlar ve dokusuz bir ağ döndürür. |
| `enable_pbr` | BOOLEAN | Hayır | True / False | `should_texture` `"true"` olduğunda, bu seçenek temel renge ek olarak PBR Haritaları (metalik, pürüzlülük, normal) oluşturur (varsayılan: False). |
| `texture_prompt` | STRING | Hayır | - | Doku oluşturma sürecini yönlendirmek için bir metin istemi (maksimum 600 karakter). `texture_image` ile aynı anda kullanılamaz. Bu parametre yalnızca `should_texture` `"true"` olarak ayarlandığında kullanılabilir. |
| `texture_image` | IMAGE | Hayır | - | Doku oluşturma sürecini yönlendirmek için bir görüntü. `texture_image` veya `texture_prompt`'tan aynı anda yalnızca biri kullanılabilir. Bu parametre yalnızca `should_texture` `"true"` olarak ayarlandığında kullanılabilir. |
| `pose_mode` | COMBO | Evet | `""` (boş)<br>`"A-pose"`<br>`"T-pose"` | Oluşturulan model için poz modunu belirtir. |
| `seed` | INT | Evet | 0 ila 2147483647 | Oluşturma işlemi için bir tohum değeri (varsayılan: 0). Tohumdan bağımsız olarak sonuçlar deterministik değildir, ancak tohumu değiştirmek düğümün yeniden çalışmasını tetikleyebilir. |

**Parametre Kısıtlamaları:**

* `images` girdisi için 2 ila 4 arasında görüntü sağlamalısınız.
* `topology` ve `target_polycount` parametreleri yalnızca `should_remesh` `"true"` olarak ayarlandığında etkindir.
* `enable_pbr`, `texture_prompt` ve `texture_image` parametreleri yalnızca `should_texture` `"true"` olarak ayarlandığında etkindir.
* `texture_prompt` ve `texture_image` aynı anda kullanılamaz; bunlar birbirini dışlayan seçeneklerdir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
| :--- | :--- | :--- |
| `model_file` | STRING | Oluşturulan GLB modelinin dosya adı. Bu çıktı, geriye dönük uyumluluk için sağlanmıştır. |
| `meshy_task_id` | MESHY_TASK_ID | Meshy API görevi için benzersiz tanımlayıcı. |
| `GLB` | FILE3DGLB | GLB formatında oluşturulan 3B model. |
| `FBX` | FILE3DFBX | FBX formatında oluşturulan 3B model. |

---
**Source fingerprint (SHA-256):** `e6f75f50645c8b2cf5ebbe037edb077ef1eb0ea1baf67c581d60ac0033686d00`
