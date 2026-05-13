> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageStitch/tr.md)

Bu düğüm, iki görüntüyü belirtilen bir yönde (yukarı, aşağı, sol, sağ) birleştirmenize olanak tanır; boyut eşleştirme ve görüntüler arası boşluk desteği sunar.

## Girişler

| Parametre Adı | Veri Türü | Giriş Türü | Varsayılan | Aralık | Açıklama |
|---------------|-----------|-------------|---------|--------|-------------|
| `image1` | IMAGE | Zorunlu | - | - | Birleştirilecek ilk görüntü |
| `image2` | IMAGE | İsteğe Bağlı | Yok | - | Birleştirilecek ikinci görüntü; sağlanmazsa yalnızca ilk görüntü döndürülür |
| `direction` | STRING | Zorunlu | sağ | sağ/aşağı/sol/yukarı | İkinci görüntünün birleştirileceği yön: sağ, aşağı, sol veya yukarı |
| `match_image_size` | BOOLEAN | Zorunlu | Doğru | Doğru/Yanlış | İkinci görüntünün boyutlarının ilk görüntüyle eşleşecek şekilde yeniden boyutlandırılıp boyutlandırılmayacağı |
| `spacing_width` | INT | Zorunlu | 0 | 0-1024 | Görüntüler arasındaki boşluğun genişliği; çift sayı olmalıdır |
| `spacing_color` | STRING | Zorunlu | beyaz | beyaz/siyah/kırmızı/yeşil/mavi | Birleştirilen görüntüler arasındaki boşluğun rengi |

> `spacing_color` için, "beyaz/siyah" dışındaki renkler kullanıldığında, `match_image_size` `yanlış` olarak ayarlanırsa, dolgu alanı siyahla doldurulur

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Birleştirilmiş görüntü |

## İş Akışı Örneği

Aşağıdaki iş akışında, örnek olarak farklı boyutlarda 3 adet giriş görüntüsü kullanılmıştır:

- image1: 500x300
- image2: 400x250
- image3: 300x300

![workflow](./asset/workflow.webp)

**Birinci Görüntü Birleştirme Düğümü**

- `match_image_size`: yanlış, görüntüler orijinal boyutlarında birleştirilecektir
- `direction`: yukarı, `image2` `image1`'in üzerine yerleştirilecektir
- `spacing_width`: 20
- `spacing_color`: siyah

Çıktı görüntüsü 1:

![output1](./asset/output-1.webp)

**İkinci Görüntü Birleştirme Düğümü**

- `match_image_size`: doğru, ikinci görüntü ilk görüntünün yüksekliği veya genişliğiyle eşleşecek şekilde ölçeklenecektir
- `direction`: sağ, `image3` sağ tarafta görünecektir
- `spacing_width`: 20
- `spacing_color`: beyaz

Çıktı görüntüsü 2:

![output2](./asset/output-2.webp)