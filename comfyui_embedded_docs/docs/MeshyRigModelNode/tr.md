# Meshy: Modeli Rigle

Meshy: Rig Model düğümü, önceki bir Meshy görevinden bir 3D model alır ve bunun için otomatik olarak bir iskelet oluşturarak poze verilebilen ve canlandırılabilen, riglenmiş bir karakter üretir. Düğüm, riglenmiş modeli hem GLB hem de FBX dosya formatlarında çıktı olarak verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `meshy_task_id` | Riglenecek modeli üreten önceki bir Meshy işleminden (örn. metinden 3D'ye veya görüntüden 3D'ye) alınan benzersiz görev kimliği. | STRING | Evet | N/A |
| `height_meters` | Karakter modelinin metre cinsinden yaklaşık yüksekliği. Ölçekleme ve rigleme doğruluğuna yardımcı olur (varsayılan: 1.7). | FLOAT | Evet | 0.1 ila 15.0 |
| `texture_image` | Modelin UV açılmış temel renk doku görüntüsü. | IMAGE | Hayır | N/A |

**Not:** Otomatik rigleme işlemi şu anda dokusuz mesh'ler, insansı olmayan varlıklar veya uzuv ve gövde yapısı belirsiz insansı varlıklar için uygun değildir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_file` | Geriye dönük uyumluluk için GLB modelinin dosya adını içeren eski (legacy) bir çıktı. | STRING |
| `rig_task_id` | Bu rigleme işlemine ait benzersiz görev kimliği; sonuca referans vermek için kullanılabilir. | STRING |
| `GLB` | GLB dosya formatında kaydedilmiş, riglenmiş 3D karakter modeli. | FILE3DGLB |
| `FBX` | FBX dosya formatında kaydedilmiş, riglenmiş 3D karakter modeli. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRigModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `6ae79359fa54f36dd2491a952fe54fa56866038758e8cd475a2d2f8e9e47e3b3`
