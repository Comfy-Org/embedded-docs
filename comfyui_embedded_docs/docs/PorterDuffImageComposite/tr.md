> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PorterDuffImageComposite/tr.md)

PorterDuffImageComposite düğümü, Porter-Duff birleştirme operatörlerini kullanarak görüntü birleştirme işlemleri gerçekleştirmek üzere tasarlanmıştır. Kaynak ve hedef görüntülerin çeşitli karıştırma modlarına göre birleştirilmesine olanak tanıyarak, görüntü saydamlığını manipüle etme ve görüntüleri yaratıcı şekillerde üst üste bindirme yoluyla karmaşık görsel efektler oluşturmayı sağlar.

## Girdiler

| Parametre | Veri Tipi | Açıklama |
| --------- | ------------ | ----------- |
| `kaynak`  | `IMAGE`     | Hedef görüntünün üzerine birleştirilecek kaynak görüntü tensörü. Seçilen birleştirme moduna bağlı olarak nihai görsel sonucun belirlenmesinde kritik bir rol oynar. |
| `kaynak_alfa` | `MASK` | Kaynak görüntünün alfa kanalıdır ve kaynak görüntüdeki her pikselin saydamlığını belirtir. Kaynak görüntünün hedef görüntüyle nasıl karıştığını etkiler. |
| `hedef` | `IMAGE` | Kaynak görüntünün üzerine birleştirildiği arka plan görevi gören hedef görüntü tensörüdür. Karıştırma moduna bağlı olarak nihai birleştirilmiş görüntüye katkıda bulunur. |
| `hedef_alfa` | `MASK` | Hedef görüntünün alfa kanalıdır ve hedef görüntünün piksellerinin saydamlığını tanımlar. Kaynak ve hedef görüntülerin karışımını etkiler. |
| `mod` | COMBO[STRING] | Uygulanacak Porter-Duff birleştirme modudur ve kaynak ile hedef görüntülerin birbirleriyle nasıl karıştırılacağını belirler. Her mod farklı görsel efektler oluşturur. |

## Çıktılar

| Parametre | Veri Tipi | Açıklama |
| --------- | ------------ | ----------- |
| `image`   | `IMAGE`     | Belirtilen Porter-Duff modunun uygulanmasından elde edilen birleştirilmiş görüntü. |
| `mask`    | `MASK`      | Birleştirilmiş görüntünün alfa kanalıdır ve her pikselin saydamlığını gösterir. |