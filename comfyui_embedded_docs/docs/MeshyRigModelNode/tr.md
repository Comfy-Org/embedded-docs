> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRigModelNode/tr.md)

**Meshy: Rig Model** düğümü, önceki bir Meshy görevinden alınan 3B modeli alır ve model için otomatik olarak bir iskelet oluşturarak, poz verilebilir ve canlandırılabilir, donanımlı bir karakter üretir. Düğüm, donanımlı modeli hem GLB hem de FBX dosya formatlarında çıktı olarak verir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `meshy_task_id` | STRING | Evet | Yok | Donanımı yapılacak modeli oluşturan önceki bir Meshy işlemine (örn. metinden 3B'ye veya görüntüden 3B'ye) ait benzersiz görev kimliği. |
| `height_meters` | FLOAT | Evet | 0,1 ila 15,0 | Karakter modelinin metre cinsinden yaklaşık yüksekliği. Ölçekleme ve donanım doğruluğuna yardımcı olur (varsayılan: 1,7). |
| `texture_image` | IMAGE | Hayır | Yok | Modelin UV açılımlı temel renk doku görüntüsü. |

**Not:** Otomatik donanım oluşturma işlemi şu anda dokusuz ağlar, insansı olmayan varlıklar veya uzuv ve gövde yapısı net olmayan insansı varlıklar için uygun değildir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `rig_task_id` | STRING | Geriye dönük uyumluluk için eski bir çıktı olup, GLB modelinin dosya adını içerir. |
| `GLB` | STRING | Bu donanım oluşturma işlemi için benzersiz görev kimliği olup, sonuca başvurmak için kullanılabilir. |
| `FBX` | FILE3DGLB | GLB dosya formatında kaydedilmiş, donanımlı 3B karakter modeli. |
| `FBX` | FILE3DFBX | FBX dosya formatında kaydedilmiş, donanımlı 3B karakter modeli. |

---
**Source fingerprint (SHA-256):** `91e06e3465d3d309d2267ae307ec5a704af3903b7a6d7fb6011217dd58a63973`
