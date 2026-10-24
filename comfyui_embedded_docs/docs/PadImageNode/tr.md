# Pad Image

Bir görüntüye düz bir renk veya kenarlarının aynalanmış bir kopyasıyla dolgu ekler. Dolgu, her kenar için tam piksel değeri olarak, bir boyut çarpanı olarak veya genişlik ve yüksekliği bir sayıya tam bölünebilir yapan en küçük miktar olarak ayarlanabilir; bu, kaydetme veya döşeme öncesinde kullanışlıdır. Orijinal görüntü konumunu korur: `left` ve `top` dolgusu ondan önce, `right` ve `bottom` ise sonra eklenir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Dolgu eklenecek görüntü. | IMAGE | Evet | - |
| `padding_type` | Eklenecek dolgu miktarı: her kenar için tam miktarlar için `"pad dimensions"`, girdiye göre çıktı boyutu için `"pad by multiplier"` veya bir sonraki kata ulaşmak için `"pad to multiple"`. Bir seçenek seçildiğinde parametreleri görünür. | DYNAMIC_COMBO | Evet | `"pad dimensions"`<br>`"pad by multiplier"`<br>`"pad to multiple"` |
| `left` | Sola eklenecek piksel sayısı. `padding_type` `"pad dimensions"` olduğunda kullanılabilir (varsayılan: 0). | INT | Evet | 0 ile 16384 arası |
| `top` | Üste eklenecek piksel sayısı. `padding_type` `"pad dimensions"` olduğunda kullanılabilir (varsayılan: 0). | INT | Evet | 0 ile 16384 arası |
| `right` | Sağa eklenecek piksel sayısı. `padding_type` `"pad dimensions"` olduğunda kullanılabilir (varsayılan: 0). | INT | Evet | 0 ile 16384 arası |
| `bottom` | Alta eklenecek piksel sayısı. `padding_type` `"pad dimensions"` olduğunda kullanılabilir (varsayılan: 0). | INT | Evet | 0 ile 16384 arası |
| `multiplier` | Girdiye göre çıktı boyutu; örneğin 1.5 her kenara %25 ekler. Dolgu karşılıklı kenarlar arasında eşit olarak bölünür. `padding_type` `"pad by multiplier"` olduğunda kullanılabilir (varsayılan: 1.0). | FLOAT | Evet | 1.0 ile 8.0 arası (adım: 0.01) |
| `multiple` | Genişlik ve yükseklik bu sayıya bölünebilir olacak şekilde dolgu ekler. Dolgu karşılıklı kenarlar arasında eşit olarak bölünür; artan piksel sağa ve alta gider. `padding_type` `"pad to multiple"` olduğunda kullanılabilir (varsayılan: 32). | INT | Evet | 1 ile 16384 arası |
| `padding_style` | Dolgulu alanın neyle doldurulacağı: `"color"` veya `"mirror image"`. Bir seçenek seçildiğinde parametreleri görünür. | DYNAMIC_COMBO | Evet | `"color"`<br>`"mirror image"` |
| `color` | Dolgulu alan için dolgu rengi; alfa yok sayılır. `padding_style` `"color"` olduğunda kullanılabilir (varsayılan: `"#000000"`). | COLOR | Evet | - |
| `feathering` | Dolgulu kenarlarda görüntü kenarının bu kadar pikselini dolgu rengiyle karıştırır. 0 keskin bir kenar bırakır. `padding_style` `"color"` olduğunda kullanılabilir (varsayılan: 0). | INT | Evet | 0 ile 16384 arası |

`"mirror image"` görüntü kenarlarını bir renkle doldurmak yerine yansıtır. Kenar pikseli tekrarlanmaz ve dolgu görüntünün kendisinden daha geniş veya daha yüksek olduğunda, kalan kısmı kaplamak için aynalanmış görüntü tekrarlanır. Her dolgu miktarı 0 çıktığında girdi görüntüsü değiştirilmeden döndürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Girdinin batch boyutu ve kanal sayısıyla birlikte dolgulu görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PadImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `9373cd6aa287befba74374b9b2a6c38b20344b5715e9aaa4cf49282ae930c91d`
