# MetaMuseImageEditApi

Meta'nın Muse Image modelini ve bir metin promptu kullanarak en fazla 10 referans görüntüsünü düzenler veya birleştirir. İstediğiniz düzenlemeyi prompt içinde açıklayın ve gerektiğinde referans görüntülere `@Image1`, `@Image2` vb. şeklinde atıfta bulunun. Düğüm, referans görüntüleri yükler, Meta Muse Image API'sini çağırır ve düzenlenmiş sonucu bir görüntü olarak döndürür.

## Girdiler

Düğüm, bir `model` seçici tarafından kontrol edilir. Aşağıda açıklanan modele özgü girdiler, bir model seçildiğinde görünür; bağladığınız referans görüntüleri gerektiği gibi artırılıp azaltılabilir.

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model. | DYNAMIC_COMBO | Evet | "muse-image-1.0" |

### muse-image-1.0 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Düzenleme talimatları. Girdi görüntülerine `@Image1` tarzı referansları destekler. Varsayılan: boş dize. Prompt en az bir karakter içermelidir. | STRING | Evet | Any text with a minimum length of 1 character |
| `aspect_ratio` | Çıktının en-boy oranı. Görüntüler yaklaşık 2,5 megapiksel olarak işlenir (1:1 için 1600x1600, 16:9 için 2048x1152); "auto", girdinin en-boy oranını korur. | COMBO | Evet | "auto"<br>"1:1"<br>"3:2"<br>"2:3"<br>"4:3"<br>"3:4"<br>"5:4"<br>"4:5"<br>"16:9"<br>"9:16"<br>"21:9"<br>"9:21"<br>"2:1"<br>"1:2" |
| `reasoning_strength` | Modelin işleme öncesinde ne kadar düşüneceğini, plan yapacağını ve kendini iyileştireceğini belirler. | COMBO | Evet | "high"<br>"low" |
| `enable_web_search` | Modelin görüntüyü planlarken gerçekler ve güncel bilgiler için web'de arama yapmasını sağlar. Varsayılan: true. | BOOLEAN | Evet | true or false (default: true) |
| `enable_image_search` | Modelin görüntüyü planlarken referans görüntüleri aramasını sağlar. Varsayılan: true. | BOOLEAN | Evet | true or false (default: true) |
| `enable_shell` | Modelin planlama sırasında hassas düzenler, çizelgeler ve diyagramlar için kod çalıştırmasını sağlar; kapalıyken miktarlar ve hizalama yaklaşık olarak belirlenir. Varsayılan: true. | BOOLEAN | Evet | true or false (default: true) |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen seed; API'de seed bulunmadığından, bu değer ne olursa olsun gerçek sonuçlar deterministik değildir. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 arası (adım 1) |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Genişletilebilir yuva: düzenlemek veya birleştirmek için 1 ila 10 referans görüntüsü bağlayın (`image_1` ile `image_10` arası). Prompt içinde bunlara girdi sırasına göre numaralandırılmış `@Image1`, `@Image2`, ... şeklinde atıfta bulunun; toplu bir girdi, görüntü başına bir kez sayılır. | IMAGE | Evet | 1 ile 10 arası reference images |

Not: prompt boş olamaz ve içerdiği her `@ImageN` referansı, girdi sırasındaki bağlı görüntülerden biriyle eşleşmelidir (örneğin, `@Image1` bağlanan ilk referans görüntüsüdür). Prompt, bağlı olmayan bir görüntü numarasına atıfta bulunursa veya 10'dan fazla referans görüntüsü bağlanırsa düğüm hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Muse Image modeli tarafından döndürülen düzenlenmiş veya birleştirilmiş görüntü. API birden çok görüntü döndürürse, bunlar toplu olarak döndürülür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MetaMuseImageEditApi/tr.md)

---
**Source fingerprint (SHA-256):** `5c009ca45199f9c70465f12d48a46b685abebd0194c3d437121b9df0636dbea7`
