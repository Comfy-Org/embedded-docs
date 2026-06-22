# Porter-Duff Görüntü Birleştirme

PorterDuffImageComposite düğümü, Porter-Duff birleştirme operatörlerini kullanarak görüntü birleştirme işlemi gerçekleştirmek için tasarlanmıştır. Kaynak ve hedef görüntülerin çeşitli karıştırma modlarına göre birleştirilmesine olanak tanır; böylece görüntü saydamlığını değiştirerek ve görüntüleri yaratıcı şekillerde üst üste bindirerek karmaşık görsel efektler oluşturulmasını sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `kaynak` | Hedef görüntünün üzerine birleştirilecek kaynak görüntü tensörü. Seçilen birleştirme moduna bağlı olarak nihai görsel sonucun belirlenmesinde önemli bir rol oynar. | `IMAGE` |
| `kaynak_alfa` | Kaynak görüntünün alfa kanalı; kaynak görüntüdeki her pikselin saydamlığını belirtir. Kaynak görüntünün hedef görüntüyle nasıl karışacağını etkiler. | `MASK` |
| `hedef` | Kaynak görüntünün üzerine birleştirildiği arka plan görevi gören hedef görüntü tensörü. Karıştırma moduna bağlı olarak birleştirilmiş nihai görüntüye katkıda bulunur. | `IMAGE` |
| `hedef_alfa` | Hedef görüntünün alfa kanalı; hedef görüntüdeki piksellerin saydamlığını tanımlar. Kaynak ve hedef görüntülerin karışmasını etkiler. | `MASK` |
| `mod` | Uygulanacak Porter-Duff birleştirme modu; kaynak ve hedef görüntülerin nasıl birleştirileceğini belirler. Her mod farklı görsel efektler oluşturur. | COMBO[STRING] |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Belirtilen Porter-Duff modunun uygulanmasıyla elde edilen birleştirilmiş görüntü. | `IMAGE` |
| `mask` | Birleştirilmiş görüntünün alfa kanalı; her pikselin saydamlığını gösterir. | `MASK` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PorterDuffImageComposite/tr.md)
