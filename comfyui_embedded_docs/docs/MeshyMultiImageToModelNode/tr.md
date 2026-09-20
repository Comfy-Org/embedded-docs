# Meshy: Çoklu Görüntüden Modele

Bu düğüm, Meshy API'yi kullanarak birden fazla girdi görselinden 3B model oluşturur. Sağlanan görselleri yükler, bir işleme görevi gönderir ve sonuçta oluşan 3B model dosyalarını (GLB ve FBX) referans için görev kimliğiyle birlikte döndürür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak AI model sürümünü belirtir. | COMBO | Evet | `"meshy-7.1"`<br>`"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `should_remesh` | Oluşturulan ağın (mesh) işlenip işlenmeyeceğini belirler. `"false"` olarak ayarlandığında düğüm işlenmemiş üçgensel ağ döndürür. `"true"` olarak ayarlandığında aşağıdaki remesh ayarları gösterilir. | DYNAMIC_COMBO | Evet | `"true"`<br>`"false"` |
| `symmetry_mode` | Oluşturulan modele simetri uygulanıp uygulanmayacağını kontrol eder. | COMBO | Evet | `"auto"`<br>`"on"`<br>`"off"` |
| `should_texture` | Dokuların oluşturulup oluşturulmayacağını belirler. `"false"` olarak ayarlandığında doku aşaması atlanır ve dokusuz bir ağ döndürülür. `"true"` olarak ayarlandığında aşağıdaki doku ayarları gösterilir. | DYNAMIC_COMBO | Evet | `"true"`<br>`"false"` |
| `pose_mode` | Oluşturulan model için duruş modunu belirtin. | COMBO | Evet | `""` (boş)<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmamasını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Evet | 0 ila 2147483647 |
| `ultra_mode` | Daha yüksek sadakatli geometri ve daha ince yüzey ayrıntısı için 2048³'te ek bir iyileştirme geçişi çalıştırır. `"meshy-7.1"`, `"meshy-7"` veya `"latest"` modelini gerektirir (varsayılan: `False`). | BOOLEAN | Hayır | `True`<br>`False` |

### Remesh Ayarları (`should_remesh` `"true"` olduğunda görünür)

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `topology` | Yeniden işlenmiş çıktı için hedef çokgen türü. | COMBO | Hayır | `"triangle"`<br>`"quad"` |
| `target_polycount` | Yeniden işlenmiş model için hedef çokgen sayısı (varsayılan: 300000). | INT | Hayır | 100 ila 300000 |

### Doku Ayarları (`should_texture` `"true"` olduğunda görünür)

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `enable_pbr` | Temel renge ek olarak PBR Haritaları (metalik, pürüzlülük, normal) oluşturun. (varsayılan: False) | BOOLEAN | Hayır | True / False |
| `texture_prompt` | Doku oluşturma sürecini yönlendirmek için bir metin istemi sağlayın. Maksimum 600 karakter. `texture_image` ile aynı anda kullanılamaz. (varsayılan: boş) | STRING | Hayır | 600 karaktere kadar |
| `texture_image` | `texture_image` veya `texture_prompt` öğelerinden yalnızca biri aynı anda kullanılabilir. | IMAGE | Hayır | - |
| `texture_resolution` | Temel renk dokusu çözünürlüğü. Daha yüksek çözünürlükler daha fazla yüzey detayı yakalar. | COMBO | Hayır | `"2k"`<br>`"4k"`<br>`"8k"` |

### Görsel Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `images` | Genişletilebilir yuva: 2 ila 4 girdi görseli bağlayın (`image_1`, `image_2`, `image_3`, `image_4`). Bu görseller 3B model oluşturmak için kullanılır. | IMAGE | Evet | 2 ila 4 görsel |

**Notlar**

* `images` girdisi için 2 ila 4 görsel sağlamanız gerekir.
* `topology` ve `target_polycount` parametreleri yalnızca `should_remesh` `"true"` olarak ayarlandığında etkindir.
* `enable_pbr`, `texture_prompt`, `texture_image` ve `texture_resolution` parametreleri yalnızca `should_texture` `"true"` olarak ayarlandığında etkindir.
* `texture_prompt` ve `texture_image` birbirini dışlar; ikisini aynı anda kullanamazsınız. `texture_prompt` 600 karakterle sınırlıdır.
* `seed` değeri sonuçları deterministik yapmaz; değiştirmek yalnızca düğümün oluşturma görevini yeniden çalıştırmasına neden olur.
* `ultra_mode` için `"meshy-7.1"`, `"meshy-7"` veya `"latest"` modeli gerekir; başka bir model hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model_file` | Oluşturulan GLB modelinin dosya adı. Bu çıktı yalnızca geriye dönük uyumluluk için sağlanmıştır. | STRING |
| `meshy_task_id` | Meshy API görevi için benzersiz tanımlayıcı. | MESHY_TASK_ID |
| `GLB` | GLB formatında oluşturulan 3B model. | FILE3DGLB |
| `FBX` | FBX formatında oluşturulan 3B model. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyMultiImageToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `9475279c0990fc069b4fef2bf0e2e20218ca1a9591a261ce6d33a2b651782ddb`
