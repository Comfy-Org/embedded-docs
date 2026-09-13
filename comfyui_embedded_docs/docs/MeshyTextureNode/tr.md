# Meshy: Doku Modeli

Meshy: Texture Model düğümü, yapay zekâ tarafından oluşturulan dokuları mevcut bir 3D modele uygular. Önceki bir Meshy 3D üretim veya dönüştürme görevinden alınan bir görev kimliğini kullanır ve doku kaplama sürecini bir metin stili istemi ya da referans görselle yönlendirir. Düğüm, doku kaplanmış modeli GLB ve FBX dosya biçimlerinde döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Doku kaplama için kullanılacak AI model sürümü. | COMBO | Evet | `"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `meshy_task_id` | Önceki bir Meshy 3D üretim veya dönüştürme görevinden alınan benzersiz tanımlayıcı (görev kimliği). Bu, doku kaplanacak temel 3D modeli sağlar. | MESHY_TASK_ID | Evet | - |
| `orijinal UV'yi etkinleştir` | Modelin yeni UV'leri oluşturulmak yerine özgün UV'sini kullanın. Etkinleştirildiğinde (varsayılan: `True`), Meshy yüklenen modeldeki mevcut dokuları korur. Modelin özgün UV'si yoksa çıktının kalitesi o kadar iyi olmayabilir. Bu gelişmiş bir seçenektir. | BOOLEAN | Evet | true / false |
| `pbr` | Doku kaplanmış model için Fiziksel Tabanlı İşleme (PBR) malzeme çıktısını etkinleştirir (varsayılan: `False`). Bu gelişmiş bir seçenektir. | BOOLEAN | Evet | true / false |
| `metin stil istemi` | Metin kullanarak nesne için istediğiniz doku stilini tanımlayın (varsayılan: boş dize). En fazla 600 karakter. `image_style` ile aynı anda kullanılamaz. | STRING | Evet | - |
| `görsel stil` | Doku kaplama sürecini yönlendirmek için 2D görsel. `text_style_prompt` ile aynı anda kullanılamaz. | IMAGE | Hayır | - |
| `texture_resolution` | Temel renk doku çözünürlüğü. Daha yüksek çözünürlükler daha fazla yüzey ayrıntısı yakalar. | COMBO | Evet | `"2k"`<br>`"4k"`<br>`"8k"` |

**Parametre Kısıtlamaları:**

* Bir `text_style_prompt` veya bir `image_style` sağlamalısınız, ancak ikisini aynı anda sağlayamazsınız.
* `text_style_prompt` en fazla 600 karakter ile sınırlıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model_file` | Oluşturulan GLB modelinin dosya adı. Bu çıktı yalnızca geriye dönük uyumluluk için sağlanır. | STRING |
| `meshy_task_id` | Bu doku kaplama işi için benzersiz görev tanımlayıcısı; sonuca başvurmak için kullanılabilir. | MESHY_TASK_ID |
| `GLB` | GLB dosya biçiminde kaydedilen doku kaplanmış 3D model. | FILE3DGLB |
| `FBX` | FBX dosya biçiminde kaydedilen doku kaplanmış 3D model. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureNode/tr.md)

---
**Source fingerprint (SHA-256):** `30d51f6efe3602f27d99706840c974baf2c4397a4f9a191f3478e7eff372e319`
