# RT-DETR Tespit

RT-DETR Detect düğümü, RT-DETR modeli kullanarak giriş görüntülerinde nesne tespiti gerçekleştirir. Görüntüdeki nesneleri bulur ve her tespit için ilgili COCO veri kümesi sınıfıyla etiketlenmiş sınırlayıcı kutu koordinatlarını döndürür. Sonuçları güven puanına ve nesne sınıfına göre filtreleyebilir ve görüntü başına döndürülen toplam tespit sayısını sınırlayabilirsiniz.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Nesne tespiti için kullanılan RT-DETR modeli. | MODEL | Evet | N/A |
| `image` | Nesnelerin tespit edileceği giriş görüntüsü/görüntüleri. Düğüm, görüntüleri en fazla 32'lik gruplar halinde işler ve tespit için bunları dahili olarak yeniden boyutlandırır. | IMAGE | Evet | N/A |
| `threshold` | Bir tespitin sonuçlara dahil edilmesi için gereken minimum güven puanı (varsayılan: 0.5). | FLOAT | Evet | N/A |
| `class_name` | Tespitleri sınıfa göre filtreleyin. Filtrelemeyi devre dışı bırakmak için 'all' olarak ayarlayın (varsayılan: "all"). | COMBO | Evet | `"all"`<br>`"person"`<br>`"bicycle"`<br>`"car"`<br>`"motorcycle"`<br>`"airplane"`<br>`"bus"`<br>`"train"`<br>`"truck"`<br>`"boat"`<br>`"traffic light"`<br>`"fire hydrant"`<br>`"stop sign"`<br>`"parking meter"`<br>`"bench"`<br>`"bird"`<br>`"cat"`<br>`"dog"`<br>`"horse"`<br>`"sheep"`<br>`"cow"`<br>`"elephant"`<br>`"bear"`<br>`"zebra"`<br>`"giraffe"`<br>`"backpack"`<br>`"umbrella"`<br>`"handbag"`<br>`"tie"`<br>`"suitcase"`<br>`"frisbee"`<br>`"skis"`<br>`"snowboard"`<br>`"sports ball"`<br>`"kite"`<br>`"baseball bat"`<br>`"baseball glove"`<br>`"skateboard"`<br>`"surfboard"`<br>`"tennis racket"`<br>`"bottle"`<br>`"wine glass"`<br>`"cup"`<br>`"fork"`<br>`"knife"`<br>`"spoon"`<br>`"bowl"`<br>`"banana"`<br>`"apple"`<br>`"sandwich"`<br>`"orange"`<br>`"broccoli"`<br>`"carrot"`<br>`"hot dog"`<br>`"pizza"`<br>`"donut"`<br>`"cake"`<br>`"chair"`<br>`"couch"`<br>`"potted plant"`<br>`"bed"`<br>`"dining table"`<br>`"toilet"`<br>`"tv"`<br>`"laptop"`<br>`"mouse"`<br>`"remote"`<br>`"keyboard"`<br>`"cell phone"`<br>`"microwave"`<br>`"oven"`<br>`"toaster"`<br>`"sink"`<br>`"refrigerator"`<br>`"book"`<br>`"clock"`<br>`"vase"`<br>`"scissors"`<br>`"teddy bear"`<br>`"hair drier"`<br>`"toothbrush"` |
| `max_detections` | Görüntü başına döndürülecek maksimum tespit sayısı. Azalan güven puanı sırasına göre (varsayılan: 100). | INT | Evet | N/A |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `bboxes` | Her giriş görüntüsü için sınırlayıcı kutu listesi. Her kutu (x, y, genişlik, yükseklik) koordinatlarını, bir sınıf etiketini ve bir güven puanını içerir. | BOUNDINGBOX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RTDETR_detect/tr.md)

---
**Source fingerprint (SHA-256):** `658a47cae788da207a52edc6bf8a428c9f3d8cf415e5f20f71d6125ad6d49734`
