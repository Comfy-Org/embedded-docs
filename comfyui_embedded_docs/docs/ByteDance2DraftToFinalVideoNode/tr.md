# ByteDance Seedance 2.5 Draft to Final Video

Bu düğüm, bir Seedance 2.5 Draft'ın 1080p nihai videosunu oluşturur. Taslak, hızlı bir 480p önizlemedir: bir Seedance 2.5 video düğümünde (metinden videoya, ilk-son kareden videoya veya referanstan videoya) `model` değerini `Seedance 2.5 Draft` olarak ayarlayın, çalıştırın ve `draft_task_id` çıktısını buraya bağlayın. Nihai video, taslağın sahnesini ve hareketini korur ve taslağı üreten prompt, referanslar, süre, en boy oranı ve ses ayarını yeniden kullanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `draft_task_id` | `Seedance 2.5 Draft` modeliyle çalıştırılan bir Seedance 2.5 düğümünün `draft_task_id` çıktısı veya yapıştırılmış bir taslak görev kimliği. Bu düğümün seed kontrolünü sabit olarak ayarlayın; aksi takdirde bir sonraki çalıştırma, incelediğiniz taslağı yeniden kullanmak yerine yeni bir taslak üretir. | STRING | Evet | - |
| `watermark` | Videoya filigran eklenip eklenmeyeceği. Varsayılan değer False'tur. Bu gelişmiş bir ayardır. | BOOLEAN | Hayır | True / False |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | İşleme görevi tamamlandığında sağlayıcıdan indirilen, oluşturulmuş 1080p nihai video. | VIDEO |

**Not:** Bir taslak, oluşturulduktan sonra 7 gün boyunca işlenebilir. Taslak görev kimliği taslağı tek başına tanımlar; bu nedenle prompt, referanslar, süre, en boy oranı ve ses ayarının yeniden iletilmesi gerekmez.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2DraftToFinalVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `c9a607826915f09ec199748964010a00a239b5efab3647a3b97fdceee6b04cde`
