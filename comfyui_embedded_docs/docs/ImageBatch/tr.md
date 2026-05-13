> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBatch/tr.md)

`ImageBatch` düğümü, iki görüntüyü tek bir toplu işte birleştirmek için tasarlanmıştır. Görüntülerin boyutları eşleşmezse, birleştirmeden önce ikinci görüntüyü otomatik olarak birinci görüntünün boyutlarına uyacak şekilde yeniden ölçeklendirir.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `image1`  | `IMAGE`     | Toplu işe eklenecek ilk görüntü. Gerekirse ikinci görüntünün ayarlanacağı boyutlar için referans görevi görür. |
| `image2`  | `IMAGE`     | Toplu işe eklenecek ikinci görüntü. Birinci görüntünün boyutlarından farklıysa, otomatik olarak bu boyutlara uyacak şekilde yeniden ölçeklendirilir. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | Birleştirilmiş toplu görüntü; gerekirse ikinci görüntü, birinci görüntünün boyutlarına uyacak şekilde yeniden ölçeklendirilir. |