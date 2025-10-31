> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBatch/tr.md)

`ImageBatch` düğümü, iki görüntüyü tek bir toplu işlemde birleştirmek için tasarlanmıştır. Görüntülerin boyutları eşleşmiyorsa, bunları birleştirmeden önce ikinci görüntüyü otomatik olarak ilkinin boyutlarına yeniden ölçeklendirir.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `görüntü1`  | `IMAGE`     | Toplu işleme birleştirilecek ilk görüntü. Gerekirse ikinci görüntünün ayarlanacağı boyutlar için referans görevi görür. |
| `görüntü2`  | `IMAGE`     | Toplu işleme birleştirilecek ikinci görüntü. Farklılık gösteriyorsa, ilk görüntünün boyutlarına uyacak şekilde otomatik olarak yeniden ölçeklendirilir. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | Birleştirilmiş görüntü toplu işlemi. Gerekirse ikinci görüntü, ilkinin boyutlarına uyacak şekilde yeniden ölçeklendirilmiştir. |