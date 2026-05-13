> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RTDETR_detect/tr.md)

RT-DETR Algılama düğümü, RT-DETR modeli kullanarak giriş görüntülerinde nesne algılama gerçekleştirir. Nesneleri tanımlar, etraflarına sınırlayıcı kutular çizer ve COCO veri kümesi sınıflarına göre etiketler. Sonuçları güven puanına, nesne sınıfına göre filtreleyebilir ve toplam algılama sayısını sınırlayabilirsiniz.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | Yok | Nesne algılama için kullanılan RT-DETR modeli. |
| `görsel` | IMAGE | Evet | Yok | İçinde nesne algılanacak giriş görüntüsü(ler)i. Düğüm, görüntüleri en fazla 32'lik gruplar halinde işler. |
| `eşik` | FLOAT | Hayır | Yok | Bir algılamanın sonuçlara dahil edilmesi için gereken minimum güven puanı (varsayılan: 0.5). |
| `sınıf_adı` | COMBO | Hayır | `"all"`<br>`"person"`<br>`"bicycle"`<br>`"car"`<br>`"motorcycle"`<br>`"airplane"`<br>`"bus"`<br>`"train"`<br>`"truck"`<br>`"boat"`<br>`"traffic light"`<br>`"fire hydrant"`<br>`"stop sign"`<br>`"parking meter"`<br>`"bench"`<br>`"bird"`<br>`"cat"`<br>`"dog"`<br>`"horse"`<br>`"sheep"`<br>`"cow"`<br>`"elephant"`<br>`"bear"`<br>`"zebra"`<br>`"giraffe"`<br>`"backpack"`<br>`"umbrella"`<br>`"handbag"`<br>`"tie"`<br>`"suitcase"`<br>`"frisbee"`<br>`"skis"`<br>`"snowboard"`<br>`"sports ball"`<br>`"kite"`<br>`"baseball bat"`<br>`"baseball glove"`<br>`"skateboard"`<br>`"surfboard"`<br>`"tennis racket"`<br>`"bottle"`<br>`"wine glass"`<br>`"cup"`<br>`"fork"`<br>`"knife"`<br>`"spoon"`<br>`"bowl"`<br>`"banana"`<br>`"apple"`<br>`"sandwich"`<br>`"orange"`<br>`"broccoli"`<br>`"carrot"`<br>`"hot dog"`<br>`"pizza"`<br>`"donut"`<br>`"cake"`<br>`"chair"`<br>`"couch"`<br>`"potted plant"`<br>`"bed"`<br>`"dining table"`<br>`"toilet"`<br>`"tv"`<br>`"laptop"`<br>`"mouse"`<br>`"remote"`<br>`"keyboard"`<br>`"cell phone"`<br>`"microwave"`<br>`"oven"`<br>`"toaster"`<br>`"sink"`<br>`"refrigerator"`<br>`"book"`<br>`"clock"`<br>`"vase"`<br>`"scissors"`<br>`"teddy bear"`<br>`"hair drier"`<br>`"toothbrush"` | Algılamaları sınıfa göre filtreleyin. Filtrelemeyi devre dışı bırakmak için 'all' olarak ayarlayın (varsayılan: "all"). |
| `maksimum_tespit` | INT | Hayır | Yok | Görüntü başına döndürülecek maksimum algılama sayısı. Azalan güven puanı sırasına göre (varsayılan: 100). |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `bboxes` | BOUNDINGBOX | Her bir giriş görüntüsü için bir sınırlayıcı kutu listesi. Her kutu koordinatları (x, y, genişlik, yükseklik), bir sınıf etiketi ve bir güven puanı içerir. |

---
**Source fingerprint (SHA-256):** `0c32aa9e17b8ea81e52cb45df2a40f7c1faeb39fdf18dfc643d1d31ed0bfdefd`
