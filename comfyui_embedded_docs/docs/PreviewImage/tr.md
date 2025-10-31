> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewImage/tr.md)

PreviewImage düğümü, geçici önizleme görüntüleri oluşturmak için tasarlanmıştır. Her görüntü için otomatik olarak benzersiz bir geçici dosya adı oluşturur, görüntüyü belirtilen bir seviyede sıkıştırır ve geçici bir dizine kaydeder. Bu işlevsellik, orijinal dosyaları etkilemeden işleme sırasında görüntülerin önizlemelerini oluşturmak için özellikle kullanışlıdır.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `images`  | `IMAGE`     | 'images' girdisi, işlenecek ve geçici önizleme görüntüleri olarak kaydedilecek görüntüleri belirtir. Bu, düğümün birincil girdisidir ve hangi görüntülerin önizleme oluşturma sürecinden geçeceğini belirler. |

## Çıktılar

Düğümün çıktı türleri bulunmamaktadır.