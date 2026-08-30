# Meshy: Doku Modeli

Meshy: Texture Düğümü, 3B modele yapay zeka tarafından üretilen dokuları uygular. Önceki bir Meshy 3B oluşturma veya dönüştürme düğümünden bir görev kimliği (task ID) alır ve model için yeni dokular oluşturmak üzere bir metin açıklaması veya bir referans görüntü kullanır. Düğüm, dokulu modeli GLB ve FBX dosya formatlarında çıktı olarak verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Dokulama için kullanılacak yapay zeka modeli sürümü. | COMBO | Evet | `"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `meshy_task_id` | Önceki bir Meshy 3B oluşturma veya dönüştürme görevinden benzersiz tanımlayıcı (görev kimliği). Dokulanacak temel 3B modeli sağlar. | MESHY_TASK_ID | Evet | - |
| `orijinal UV'yi etkinleştir` | Yeni UV'ler oluşturmak yerine modelin orijinal UV'sini kullanın. Etkinleştirildiğinde (varsayılan: `True`), Meshy yüklenen modelin mevcut dokularını korur. Modelin orijinal UV'si yoksa, çıktının kalitesi iyi olmayabilir. Bu gelişmiş bir seçenektir. | BOOLEAN | Hayır | true / false |
| `pbr` | Dokulu model için Fiziksel Tabanlı Render (PBR) malzeme çıktısını etkinleştirir (varsayılan: `False`). Bu gelişmiş bir seçenektir. | BOOLEAN | Hayır | true / false |
| `metin stil istemi` | Nesnenin istediğiniz doku stilini metin kullanarak tanımlayın. Maksimum 600 karakter. `image_style` ile aynı anda kullanılamaz. | STRING | Hayır | - |
| `görsel stil` | Dokulama sürecini yönlendirmek için 2B bir görüntü. `text_style_prompt` ile aynı anda kullanılamaz. | IMAGE | Hayır | - |
| `texture_resolution` | Temel renk doku çözünürlüğü. Daha yüksek çözünürlükler daha fazla yüzey detayı yakalar. | COMBO | Evet | `"2k"`<br>`"4k"`<br>`"8k"` |

**Parametre Kısıtlamaları:**

* `text_style_prompt` veya `image_style` alanlarından birini sağlamalısınız, ancak ikisini aynı anda sağlayamazsınız.
* `text_style_prompt` en fazla 600 karakterle sınırlıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model_dosyası` | Oluşturulan GLB modelinin dosya adı. Bu çıktı yalnızca geriye dönük uyumluluk için sağlanır. | STRING |
| `meshy_görev_id` | Bu dokulama işi için benzersiz görev tanımlayıcısı; sonuca referans vermek için kullanılabilir. | MESHY_TASK_ID |
| `GLB` | GLB dosya formatında kaydedilen dokulu 3B model. | FILE3DGLB |
| `FBX` | FBX dosya formatında kaydedilen dokulu 3B model. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureNode/tr.md)

---
**Source fingerprint (SHA-256):** `30d51f6efe3602f27d99706840c974baf2c4397a4f9a191f3478e7eff372e319`
