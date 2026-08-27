# Meshy: Çoklu Görüntüden Modele

Bu düğüm, birden fazla giriş görselinden 3B model oluşturmak için Meshy API'sini kullanır. Sağlanan görselleri yükler, bir işleme görevi gönderir ve sonuçta oluşan 3B model dosyalarını (GLB ve FBX) referans için görev kimliğiyle birlikte döndürür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Tipi | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak yapay zeka modeli sürümünü belirtir. | COMBO | Evet | `"latest"` |
| `should_remesh` | Oluşturulan ağın işlenip işlenmeyeceğini belirler. `"false"` olarak ayarlandığında düğüm, işlenmemiş bir üçgen ağ döndürür. `"true"` olarak ayarlandığında aşağıdaki remesh ayarları gösterilir. | DYNAMIC_COMBO | Evet | `"true"`<br>`"false"` |
| `symmetry_mode` | Oluşturulan modele simetri uygulanıp uygulanmayacağını kontrol eder. | COMBO | Evet | `"auto"`<br>`"on"`<br>`"off"` |
| `should_texture` | Dokuların oluşturulup oluşturulmayacağını belirler. `"false"` olarak ayarlanması doku aşamasını atlar ve dokusuz bir ağ döndürür. `"true"` olarak ayarlandığında aşağıdaki doku ayarları gösterilir. | DYNAMIC_COMBO | Evet | `"true"`<br>`"false"` |
| `pose_mode` | Oluşturulan model için poz modunu belirtin. | COMBO | Evet | `""` (boş)<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Evet | 0 ile 2147483647 |

### Remesh Ayarları (`should_remesh` `"true"` olarak ayarlandığında görünür)

| Parametre | Açıklama | Veri Tipi | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `topology` | Remesh edilmiş çıktı için hedef çokgen türü. | COMBO | Hayır | `"triangle"`<br>`"quad"` |
| `target_polycount` | Remesh edilmiş model için hedef çokgen sayısı (varsayılan: 300000). | INT | Hayır | 100 ile 300000 |

### Doku Ayarları (`should_texture` `"true"` olarak ayarlandığında görünür)

| Parametre | Açıklama | Veri Tipi | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `enable_pbr` | Temel rengin yanı sıra PBR Haritaları (metalik, pürüzlülük, normal) oluşturun. (varsayılan: False) | BOOLEAN | Hayır | True / False |
| `texture_prompt` | Dokulandırma sürecini yönlendirmek için bir metin istemi sağlayın. En fazla 600 karakter. `texture_image` ile aynı anda kullanılamaz. (varsayılan: boş) | STRING | Hayır | - |
| `texture_image` | `texture_image` veya `texture_prompt` öğelerinden yalnızca biri aynı anda kullanılabilir. | IMAGE | Hayır | - |

### Görsel Girdileri

| Parametre | Açıklama | Veri Tipi | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `images` | Genişletilebilir yuva: 2 ila 4 giriş görseli bağlayın (`image_1`, `image_2`, `image_3`, `image_4`). Bu görseller 3B modeli oluşturmak için kullanılır. | IMAGE | Evet | 2 ila 4 görsel |

**Notlar**

* `images` girdisi için 2 ila 4 görsel sağlamanız gerekir.
* `topology` ve `target_polycount` parametreleri yalnızca `should_remesh` `"true"` olarak ayarlandığında etkindir.
* `enable_pbr`, `texture_prompt` ve `texture_image` parametreleri yalnızca `should_texture` `"true"` olarak ayarlandığında etkindir.
* `texture_prompt` ve `texture_image` birbirini dışlar; ikisini aynı anda kullanamazsınız. `texture_prompt` 600 karakterle sınırlıdır.
* `seed` değeri sonuçları deterministik yapmaz; değiştirilmesi yalnızca düğümün oluşturma görevini yeniden çalıştırmasına neden olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
| --- | --- | --- |
| `model_file` | Oluşturulan GLB modelinin dosya adı. Bu çıktı yalnızca geriye dönük uyumluluk için sağlanır. | STRING |
| `meshy_task_id` | Meshy API görevi için benzersiz tanımlayıcı. | MESHY_TASK_ID |
| `GLB` | GLB formatında oluşturulan 3B model. | FILE3DGLB |
| `FBX` | FBX formatında oluşturulan 3B model. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyMultiImageToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `c2282cad611bbbc8c0a618df6a68fcd9f6e3c29c6d08b2c96a117c29765d8a7a`
