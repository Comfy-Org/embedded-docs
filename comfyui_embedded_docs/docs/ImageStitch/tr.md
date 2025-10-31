> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageStitch/tr.md)

Bu düğüm, iki görüntüyü belirtilen bir yönde (yukarı, aşağı, sol, sağ) birleştirmenize olanak tanır ve boyut eşleme ile görüntüler arası boşluk desteği sunar.

## Girişler

| Parametre Adı | Veri Türü | Giriş Türü | Varsayılan | Aralık | Açıklama |
|---------------|-----------|-------------|---------|--------|-------------|
| `image1` | IMAGE | Gerekli | - | - | Birleştirilecek ilk görüntü |
| `image2` | IMAGE | İsteğe Bağlı | Yok | - | Birleştirilecek ikinci görüntü, sağlanmazsa yalnızca ilk görüntüyü döndürür |
| `direction` | STRING | Gerekli | right | right/down/left/up | İkinci görüntünün birleştirileceği yön: sağ, aşağı, sol veya yukarı |
| `match_image_size` | BOOLEAN | Gerekli | True | True/False | İkinci görüntünün boyutlarını ilk görüntünün boyutlarına göre yeniden boyutlandırıp boyutlandırmayacağı |
| `spacing_width` | INT | Gerekli | 0 | 0-1024 | Görüntüler arasındaki boşluğun genişliği, çift sayı olmalıdır |
| `spacing_color` | STRING | Gerekli | white | white/black/red/green/blue | Birleştirilmiş görüntüler arasındaki boşluğun rengi |

> `spacing_color` için, "white/black" dışındaki renkler kullanıldığında, eğer `match_image_size` `false` olarak ayarlanmışsa, dolgu alanı siyah renkle doldurulacaktır

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Birleştirilmiş görüntü |

## İş Akışı Örneği

Aşağıdaki iş akışında, farklı boyutlara sahip 3 giriş görüntüsünü örnek olarak kullanıyoruz:

- image1: 500x300
- image2: 400x250
- image3: 300x300

![workflow](./asset/workflow.webp)

**İlk Görüntü Birleştirme Düğümü**

- `match_image_size`: false, görüntüler orijinal boyutlarında birleştirilecek
- `direction`: yukarı, `image2`, `image1`'in üzerine yerleştirilecek
- `spacing_width`: 20
- `spacing_color`: siyah

Çıktı görüntüsü 1:

![output1](./asset/output-1.webp)

**İkinci Görüntü Birleştirme Düğümü**

- `match_image_size`: true, ikinci görüntü ilk görüntünün yüksekliğine veya genişliğine uyacak şekilde ölçeklenecek
- `direction`: sağ, `image3` sağ tarafta görünecek
- `spacing_width`: 20
- `spacing_color`: beyaz

Çıktı görüntüsü 2:

![output2](./asset/output-2.webp)