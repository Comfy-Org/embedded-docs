# Tripo: Çoklu Görünümü Düzenle

Tripo: Image to Multiview sonucunun görünümlerini, her görünüm için ayrı bir metin talimatı kullanarak düzenler. Talimatı olmayan görünümler değişmeden kalır. Düzenlenen görüntülerin, 3B model oluşturmak için Tripo: Multiview to Model düğümüne bağlanması amaçlanmıştır; düzenlenmiş bir çoklu görünüm kümesi tekrar düzenlenemez.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `multiview_task_id` | Görünümleri düzenlenecek Tripo: Image to Multiview sonucunun görev kimliği. Tripo: Image to Multiview düğümünden gelmelidir. | MULTIVIEW_TASK_ID | Evet | Görev Kimliği |
| `front_prompt` | Ön görünüme uygulanacak düzenlemeyi açıklayan metin talimatı. Boş olduğunda ön görünüm değişmeden kalır. Varsayılan: boş dize. | STRING | Hayır | Çok satırlı metin |
| `left_prompt` | Sol görünüme uygulanacak düzenlemeyi açıklayan metin talimatı. Boş olduğunda sol görünüm değişmeden kalır. Varsayılan: boş dize. | STRING | Hayır | Çok satırlı metin |
| `back_prompt` | Arka görünüme uygulanacak düzenlemeyi açıklayan metin talimatı. Boş olduğunda arka görünüm değişmeden kalır. Varsayılan: boş dize. | STRING | Hayır | Çok satırlı metin |
| `right_prompt` | Sağ görünüme uygulanacak düzenlemeyi açıklayan metin talimatı. Boş olduğunda sağ görünüm değişmeden kalır. Varsayılan: boş dize. | STRING | Hayır | Çok satırlı metin |

Not: Dört metin talimatından (`front_prompt`, `left_prompt`, `back_prompt`, `right_prompt`) en az biri boş olmayan metin içermelidir; yalnızca boşluk karakterlerinden oluşan metin boş kabul edilir ve tüm metin talimatları boşsa düğüm bir hata verir.

Not: Maliyet, düzenleme talimatı içeren her görünüm için yaklaşık 0,05 USD'dir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `front` | Düzenlenmiş ön görünüm görüntüsü. | IMAGE |
| `left` | Düzenlenmiş sol görünüm görüntüsü. | IMAGE |
| `back` | Düzenlenmiş arka görünüm görüntüsü. | IMAGE |
| `right` | Düzenlenmiş sağ görünüm görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoEditMultiviewNode/tr.md)

---
**Source fingerprint (SHA-256):** `db8b0a3ffe4332fcbcaac4da0d7b07217d01d2f05526750540f6036293e013ab`
