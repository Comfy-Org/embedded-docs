# Meshy: Görüntüden Modele

Meshy: Image to Model düğümü, tek bir girdi görüntüsünden 3D model oluşturmak için Meshy API'sini kullanır. Görüntünüzü yükler, bir işleme görevi gönderir ve oluşturulan 3D model dosyalarını (GLB ve FBX) referans için görev kimliğiyle birlikte döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Üretim için kullanılacak AI model sürümünü belirtir. | COMBO | Evet | `"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `image` | 3D modele dönüştürülecek girdi görüntüsü. | IMAGE | Evet | - |
| `should_remesh` | `"false"` olarak ayarlandığında, işlenmemiş üçgen bir ağ döndürür. | DYNAMIC_COMBO | Evet | `"true"`<br>`"false"` |
| `topology` | Yeniden ağ oluşturulmuş model için hedef çokgen topolojisi. Bu girdi yalnızca `should_remesh` `"true"` olarak ayarlandığında kullanılabilir. | COMBO | Hayır* | `"triangle"`<br>`"quad"` |
| `target_polycount` | Yeniden ağ oluşturulmuş model için hedef çokgen sayısı. Bu girdi yalnızca `should_remesh` `"true"` olarak ayarlandığında kullanılabilir. Varsayılan: 300000. | INT | Hayır* | 100 - 300000 |
| `symmetry_mode` | Oluşturulan 3D modele uygulanan simetriyi kontrol eder. | COMBO | Evet | `"auto"`<br>`"on"`<br>`"off"` |
| `should_texture` | Dokuların oluşturulup oluşturulmayacağını belirler. `"false"` olarak ayarlandığında doku aşamasını atlar ve dokusuz bir ağ döndürür. | DYNAMIC_COMBO | Evet | `"true"`<br>`"false"` |
| `enable_pbr` | Temel renge ek olarak PBR Haritaları (metalik, pürüzlülük, normal) oluşturun. Bu girdi yalnızca `should_texture` `"true"` olarak ayarlandığında kullanılabilir. Varsayılan: `False`. | BOOLEAN | Hayır* | - |
| `texture_prompt` | Doku oluşturma sürecini yönlendirmek için bir metin istemi sağlayın. Maksimum 600 karakter. `texture_image` ile aynı anda kullanılamaz. Bu girdi yalnızca `should_texture` `"true"` olarak ayarlandığında kullanılabilir. Varsayılan: boş dize. | STRING | Hayır* | - |
| `texture_image` | `texture_image` ve `texture_prompt` öğelerinden yalnızca biri aynı anda kullanılabilir. Bu girdi yalnızca `should_texture` `"true"` olarak ayarlandığında kullanılabilir. | IMAGE | Hayır* | - |
| `texture_resolution` | Temel renk doku çözünürlüğü. Daha yüksek çözünürlükler daha fazla yüzey detayı yakalar. Bu girdi yalnızca `should_texture` `"true"` olarak ayarlandığında kullanılabilir. | COMBO | Hayır* | `"2k"`<br>`"4k"`<br>`"8k"` |
| `pose_mode` | Oluşturulan model için poz modunu belirtin. Bu gelişmiş bir parametredir. | COMBO | Evet | `""` (boş)<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. Varsayılan: 0. | INT | Evet | 0 - 2147483647 |
| `ultra_mode` | Daha ince yüzey detayıyla daha yüksek doğrulukta geometri için ek bir iyileştirme geçişi çalıştırın. Varsayılan: `False`. | BOOLEAN | Evet | - |

**Parametre Kısıtlamaları Hakkında Not:**

* `topology` ve `target_polycount` girdileri yalnızca `should_remesh` `"true"` olarak ayarlandığında kullanılabilir.
* `enable_pbr`, `texture_prompt`, `texture_image` ve `texture_resolution` girdileri yalnızca `should_texture` `"true"` olarak ayarlandığında kullanılabilir.
* `should_texture` `"true"` olarak ayarlandığında, `texture_prompt` ve `texture_image` aynı anda kullanılamaz. Her ikisi de sağlanırsa düğüm bir hata verir.
* `texture_prompt` maksimum 600 karakter uzunluğundadır.
* `ultra_mode`, `"meshy-7"` veya `"latest"` modelini gerektirir. `ultra_mode` `"meshy-6"` modeliyle etkinleştirilirse düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model_file` | Oluşturulan GLB modelinin dosya adı. Yalnızca geriye dönük uyumluluk için korunmaktadır. | STRING |
| `meshy_task_id` | Referans veya sorun giderme amacıyla kullanılabilen Meshy API görevi için benzersiz tanımlayıcı. | MESHY_TASK_ID |
| `GLB` | GLB dosya formatında oluşturulan 3D model. | FILE3DGLB |
| `FBX` | FBX dosya formatında oluşturulan 3D model. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `689828ad52de4493e1039aecc408e18af4122d2c0e2511fd254ba0f1d56bad14`
