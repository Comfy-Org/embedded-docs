# Meta Muse Görüntü Düzenleme

Bir metin istemi ve Meta'nın Muse Image modelini kullanarak en fazla 10 referans görüntüyü düzenler veya birleştirir. İstenen düzenlemeyi istemde açıklayın ve gerektiğinde referans görüntülere `@Image1`, `@Image2` vb. şekilde başvurun. Düğüm referans görüntüleri yükler, Meta Muse Image API'sini çağırır ve düzenlenmiş sonucu görüntü olarak döndürür.

## Girdiler

Düğüm, bir `model` seçicisi tarafından kontrol edilir. Aşağıda açıklanan modele özgü girdiler, bir model seçildiğinde görünür ve bağladığınız referans görüntüler gerektiği kadar artırılabilir veya azaltılabilir.

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model. | DYNAMIC_COMBO | Evet | "muse-image-1.0" |

### muse-image-1.0 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Düzenleme talimatları. Girdi görüntülerine `@Image1` tarzı başvuruları destekler. Varsayılan: boş dize. İstem en az bir karakter içermelidir. | STRING | Evet | Minimum uzunluğu 1 karakter olan herhangi bir metin |
| `aspect_ratio` | Çıktının en-boy oranı. Görüntüler yaklaşık 2,5 megapiksel olarak oluşturulur (1:1 1600x1600, 16:9 2048x1152); "auto" girdinin en-boy oranını korur. | COMBO | Evet | "auto"<br>"1:1"<br>"3:2"<br>"2:3"<br>"4:3"<br>"3:4"<br>"5:4"<br>"4:5"<br>"16:9"<br>"9:16"<br>"21:9"<br>"9:21"<br>"2:1"<br>"1:2" |
| `reasoning_strength` | Modelin oluşturmadan önce ne kadar düşündüğünü, planladığını ve kendini iyileştirdiğini belirtir. | COMBO | Evet | "high"<br>"low" |
| `enable_web_search` | Modelin görüntüyü planlarken gerçekleri ve canlı bilgileri web'de aramasını sağlar. Varsayılan: true. | BOOLEAN | Evet | true veya false (varsayılan: true) |
| `enable_image_search` | Modelin görüntüyü planlarken referans görüntüleri aramasını sağlar. Varsayılan: true. | BOOLEAN | Evet | true veya false (varsayılan: true) |
| `enable_shell` | Modelin planlama sırasında kod çalıştırmasını sağlar; hassas yerleşimler, grafikler ve diyagramlar içindir; kapalıyken miktarlar ve hizalama yaklaşık olarak belirlenir. Varsayılan: true. | BOOLEAN | Evet | true veya false (varsayılan: true) |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirlemek için tohum; API'de tohum yoktur, bu nedenle bu değerden bağımsız olarak gerçek sonuçlar deterministik değildir. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 arası (adım 1) |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Büyütülebilir yuva: düzenlemek veya birleştirmek için 1 ile 10 arasında referans görüntü bağlayın (`image_1` ile `image_10` arası). İstemde bunlara `@Image1`, `@Image2`, ... şeklinde, girdi sırasına göre numaralandırılmış olarak başvurun; toplu girdi, görüntü başına bir kez sayılır. | IMAGE | Evet | 1 ile 10 referans görüntü |

Not: istem boş olamaz ve içerdiği her `@ImageN` başvurusu, girdi sırasına göre bağlı görüntülerden biriyle eşleşmelidir (örneğin, `@Image1` bağlı ilk referans görüntüdür). İstem bağlı olmayan bir görüntü numarasına başvurursa veya 10'dan fazla referans görüntü bağlanırsa düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Muse Image modeli tarafından döndürülen düzenlenmiş veya birleştirilmiş görüntü. API birden fazla görüntü döndürürse, bunlar toplu olarak döndürülür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MetaMuseImageEditApi/tr.md)

---
**Source fingerprint (SHA-256):** `5c009ca45199f9c70465f12d48a46b685abebd0194c3d437121b9df0636dbea7`
