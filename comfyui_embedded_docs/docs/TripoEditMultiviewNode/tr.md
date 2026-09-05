# TripoEditMultiviewNode

Tripo: Edit Multiview, Tripo: Image to Multiview sonucunun dört görünümünü, her görünüm için ayrı bir metin talimatı kullanarak düzenler. Talimat içermeyen görünümler değişmeden kalır. Düzenlenen görüntüler, bir 3D model oluşturmak için Tripo: Multiview to Model düğümüne bağlanmak üzere tasarlanmıştır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `multiview_task_id` | Görünümleri düzenlenecek olan Tripo: Image to Multiview sonucunun Görev Kimliği. | MULTIVIEW_TASK_ID | Evet | Görev Kimliği |
| `front_prompt` | Ön görünüme uygulanacak düzenlemeyi tanımlayan metin talimatı. Boş olduğunda ön görünüm değişmeden kalır. Varsayılan: boş. | STRING | Hayır | Çok satırlı metin |
| `left_prompt` | Sol görünüme uygulanacak düzenlemeyi tanımlayan metin talimatı. Boş olduğunda sol görünüm değişmeden kalır. Varsayılan: boş. | STRING | Hayır | Çok satırlı metin |
| `back_prompt` | Arka görünüme uygulanacak düzenlemeyi tanımlayan metin talimatı. Boş olduğunda arka görünüm değişmeden kalır. Varsayılan: boş. | STRING | Hayır | Çok satırlı metin |
| `right_prompt` | Sağ görünüme uygulanacak düzenlemeyi tanımlayan metin talimatı. Boş olduğunda sağ görünüm değişmeden kalır. Varsayılan: boş. | STRING | Hayır | Çok satırlı metin |

Not: Dört talimattan (`front_prompt`, `left_prompt`, `back_prompt`, `right_prompt`) en az biri boş olmayan metin içermelidir; aksi takdirde düğüm bir hata verir. `multiview_task_id`, Tripo: Image to Multiview düğümünden gelmelidir. Düzenlenmiş bir multiview seti yeniden düzenlenemez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `front` | Düzenlenmiş ön görünüm görüntüsü. | IMAGE |
| `sol` | Düzenlenmiş sol görünüm görüntüsü. | IMAGE |
| `arka` | Düzenlenmiş arka görünüm görüntüsü. | IMAGE |
| `sağ` | Düzenlenmiş sağ görünüm görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoEditMultiviewNode/tr.md)

---
**Source fingerprint (SHA-256):** `7a25f3867776c01ab606d43a988b5491e543b72d3eedac1779fa170453c1ca21`
