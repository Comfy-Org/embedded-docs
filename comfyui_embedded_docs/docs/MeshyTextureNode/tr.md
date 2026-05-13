> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureNode/tr.md)

**Meshy: Doku Düğümü**, yapay zeka tarafından oluşturulan dokuları bir 3D modele uygular. Önceki bir Meshy 3D oluşturma veya dönüştürme düğümünden bir görev kimliği alır ve model için yeni dokular oluşturmak üzere bir metin açıklaması veya referans görseli kullanır. Düğüm, dokulu modeli GLB ve FBX dosya formatlarında çıktı olarak verir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `"latest"` | Doku oluşturma için kullanılacak yapay zeka modeli sürümü. Şu anda yalnızca "latest" (en son) sürüm mevcuttur. |
| `meshy_task_id` | MESHY_TASK_ID | Evet | - | Önceki bir Meshy 3D oluşturma veya dönüştürme görevinden alınan benzersiz tanımlayıcı (görev kimliği). Doku oluşturulacak temel 3D modeli sağlar. |
| `orijinal UV'yi etkinleştir` | BOOLEAN | Hayır | - | Yeni UV'ler oluşturmak yerine modelin orijinal UV'sini kullanın. Etkinleştirildiğinde (varsayılan: `True`), Meshy yüklenen modeldeki mevcut dokuları korur. Modelin orijinal UV'si yoksa, çıktının kalitesi iyi olmayabilir. |
| `pbr` | BOOLEAN | Hayır | - | Dokulu model için Fiziksel Tabanlı İşleme (PBR) malzeme çıktısını etkinleştirir (varsayılan: `False`). |
| `metin stil istemi` | STRING | Hayır | - | Nesnenin istediğiniz doku stilini metin kullanarak tanımlayın. Maksimum 600 karakter. `görsel stil` ile aynı anda kullanılamaz. |
| `görsel stil` | IMAGE | Hayır | - | Doku oluşturma sürecine rehberlik edecek 2D bir görsel. `metin stil istemi` ile aynı anda kullanılamaz. |

**Parametre Kısıtlamaları:**

* Bir `text_style_prompt` veya bir `image_style` sağlamanız gerekir, ancak ikisini aynı anda sağlayamazsınız.
* `text_style_prompt` en fazla 600 karakterle sınırlıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `meshy_görev_id` | STRING | Oluşturulan GLB modelinin dosya adı. Bu çıktı, geriye dönük uyumluluk için sağlanmıştır. |
| `GLB` | MODEL_TASK_ID | Sonuca başvurmak için kullanılabilen, bu doku oluşturma işine ait benzersiz görev tanımlayıcısı. |
| `FBX` | FILE3DGLB | GLB dosya formatında kaydedilmiş dokulu 3D model. |
| `FBX` | FILE3DFBX | FBX dosya formatında kaydedilmiş dokulu 3D model. |

---
**Source fingerprint (SHA-256):** `380b682a8290c69e71a204c8c3d6c2d4fb2c15f4bc1679b98c7fc4fd9ec9e1b3`
