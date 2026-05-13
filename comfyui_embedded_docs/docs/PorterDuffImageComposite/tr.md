> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PorterDuffImageComposite/tr.md)

PorterDuffImageComposite düğümü, Porter-Duff birleştirme operatörlerini kullanarak görüntü birleştirme işlemi gerçekleştirmek için tasarlanmıştır. Kaynak ve hedef görüntülerin çeşitli karıştırma modlarına göre birleştirilmesine olanak tanır; böylece görüntü saydamlığını değiştirerek ve görüntüleri yaratıcı şekillerde üst üste bindirerek karmaşık görsel efektler oluşturulmasını sağlar.

## Girişler

| Parametre | Veri Türü | Açıklama |
| --------- | ------------ | ----------- |
| `kaynak`  | `IMAGE`     | Hedef görüntünün üzerine birleştirilecek kaynak görüntü tensörü. Seçilen birleştirme moduna bağlı olarak nihai görsel sonucun belirlenmesinde önemli bir rol oynar. |
| `kaynak_alfa` | `MASK` | Kaynak görüntünün alfa kanalı; kaynak görüntüdeki her pikselin saydamlığını belirtir. Kaynak görüntünün hedef görüntüyle nasıl karışacağını etkiler. |
| `hedef` | `IMAGE` | Kaynak görüntünün üzerine birleştirildiği arka plan görevi gören hedef görüntü tensörü. Karıştırma moduna bağlı olarak birleştirilmiş nihai görüntüye katkıda bulunur. |
| `hedef_alfa` | `MASK` | Hedef görüntünün alfa kanalı; hedef görüntüdeki piksellerin saydamlığını tanımlar. Kaynak ve hedef görüntülerin karışmasını etkiler. |
| `mod` | COMBO[STRING] | Uygulanacak Porter-Duff birleştirme modu; kaynak ve hedef görüntülerin nasıl birleştirileceğini belirler. Her mod farklı görsel efektler oluşturur. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
| --------- | ------------ | ----------- |
| `image`   | `IMAGE`     | Belirtilen Porter-Duff modunun uygulanmasıyla elde edilen birleştirilmiş görüntü. |
| `mask`    | `MASK`      | Birleştirilmiş görüntünün alfa kanalı; her pikselin saydamlığını gösterir. |