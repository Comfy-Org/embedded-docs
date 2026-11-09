# WeVisOne-VL Detect

WeVisOne-VL Detect, bir görüntüdeki nesneleri metin istemine göre bulur ve seçtiğiniz göreve bağlı olarak kutular, alfa matları, noktalar veya modelin kendi yanıtını döndürür. Açık sözcük dağarcıklı algılama ve bölütleme, gönderme ifadeleri, işaretleme, sayma ve OCR temellendirmeyi kapsar ve toplu işteki her görüntü için tek istem çalıştırır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Kontrol noktasını yükleyen WeVisOne-VL metin kodlayıcısı. | CLIP | Evet | - |
| `image` | Aranacak görüntü veya görüntü grubu. | IMAGE | Evet | - |
| `task` | Düğümün ne döndürmesi gerektiği. Segmentation, kutular ve alfa matları döndürür; detection, referring, ocr ve ocr_grounding kutular döndürür; point ve count_point noktalar döndürür; count_box kutularla sayar; visual_prompt, `bboxes` içindeki referans kutulara benzer nesneleri bulur; freeform, sorguyu değiştirmeden gönderir ve yalnızca metin döndürür (varsayılan: "segmentation"). | COMBO | Evet | `"segmentation"`<br>`"detection"`<br>`"referring"`<br>`"point"`<br>`"count_box"`<br>`"count_point"`<br>`"ocr"`<br>`"ocr_grounding"`<br>`"visual_prompt"`<br>`"freeform"` |
| `query` | Ne bulunacağı, sade bir dille (örneğin "kırmızı kupa"). `detection` ve `point` her satırda bir etiket okur, `count_box` ve `count_point` adını verdiğiniz özneyi sayar, `ocr_grounding` bu tam metni arar, `visual_prompt` bunun yerine `bboxes` kullanır ve `freeform` bunu istemin tamamı olarak gönderir. `ocr` bunu yok sayar. | STRING | Evet | - |
| `bboxes` | `visual_prompt` tarafından bulunacak nesnenin örnekleri olarak kullanılan referans kutuları. | BOUNDING_BOX | Hayır | - |
| `individual_masks` | Her kare için birleşik tek mat yerine, `bboxes` sırasına göre ve kare kare her kutu için bir mat döndür (varsayılan: false). | BOOLEAN | Hayır | true<br>false |
| `max_length` | Modelin yanıtı için üretebileceği maksimum token sayısı (varsayılan: 4096). | INT | Evet | 1 ile 32768 arası |

**Not:** Matlar yalnızca model nesne referanslarıyla yanıt verdiğinde doldurulur; segmentation ve visual prompt görevlerinin istediği de budur. Diğer görevler kutular, noktalar veya boş matla birlikte metin döndürür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `masks` | Eşleşen nesnelerin alfa matları; varsayılan olarak her kare için bir tane veya `individual_masks` ile her kutu için bir tane. | MASK |
| `bboxes` | Her görüntüde bulunan kutular; `x`, `y`, `width`, `height` ve `label` olarak saklanır. | BOUNDING_BOX |
| `points` | Piksel cinsinden JSON olarak noktalar, `[{"x", "y", "label", "frame"}]` biçiminde; `point` ve `count_point` görevleri tarafından doldurulur. | STRING |
| `text` | Modelin ham yanıtı, her görüntü için bir satır. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WeVisOneDetect/tr.md)

---
**Source fingerprint (SHA-256):** `0cef1dfcab790e145ace51401a84cdc10282835330cda5a3770f5b20a32d475e`
