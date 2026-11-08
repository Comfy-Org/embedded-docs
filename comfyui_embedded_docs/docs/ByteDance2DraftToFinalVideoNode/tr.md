# ByteDance Seedance 2.5 Taslaktan Son Videoya

Bu düğüm, bir Seedance 2.5 Draft taslağının nihai videosunu 1080p olarak veya kurumsal hesaplar için 4k olarak işler. Taslak, hızlı bir 480p önizlemedir: bir Seedance 2.5 video düğümünde (metinden videoya, ilk-son kareden videoya veya referanstan videoya) `model` değerini `Seedance 2.5 Draft` olarak ayarlayın, çalıştırın ve `draft_task_id` çıktısını buraya bağlayın. Nihai video, taslağın sahnesini ve hareketini korur; taslağı üreten prompt, referanslar, süre, en-boy oranı ve ses ayarını yeniden kullanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `draft_task_id` | Seedance 2.5 Draft modeliyle çalıştırılan bir Seedance 2.5 düğümünün `draft_task_id` çıktısı veya yapıştırılan bir taslak görev kimliği. Üretici düğümü yeniden çalıştırdığınızda, seed kontrolünü sabit olarak ayarlayın; aksi halde bir sonraki çalıştırma, incelediğiniz taslağı yeniden kullanmak yerine yeni bir taslak oluşturur. | STRING | Evet | - |
| `watermark` | Videoya filigran eklenip eklenmeyeceği. Varsayılan değer False'tir. Bu gelişmiş bir ayardır. | BOOLEAN | Hayır | True / False |
| `resolution` | Nihai videonun çözünürlüğü. `"4k"` yalnızca kurumsal hesaplar için kullanılabilir. Varsayılan: `"1080p"`. | COMBO | Hayır | `"1080p"`<br>`"4k"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | İşleme görevi tamamlandığında sağlayıcıdan indirilen, işlenmiş nihai video. | VIDEO |

**Not:** Bir taslak, oluşturulduktan sonra 7 gün boyunca işlenebilir. Taslak görev kimliği taslağı tek başına tanımlar; bu nedenle prompt, referanslar, süre, en-boy oranı ve ses ayarının yeniden iletilmesi gerekmez.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2DraftToFinalVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `bf96a485d5febde26e22433d190cfe42bd21dc6316d66141ad23d4b95a845dc5`
