# Ideogram 4.5 Hassas Düzenleme

Ideogram 4.6 veya 4.5 hassas düzenleme ile bir metin istemi rehberliğinde bir görseli düzenleyin: yalnızca istemin istediği şeyler değişir. Bölge düzenlemesi, görsel 1'i tam boyutunda ve çözünürlüğünde tutar. Tüm görsel düzenlemesi, görsel 1 modelin sınırının üzerindeyse yüklemeden önce onu küçültür; böylece sonuç girdiden daha küçük olabilir: 4.6'da 16,7 MP veya her kenar için 8192 piksel, 4.5'te yaklaşık 4 MP veya her kenar için 4608 piksel. Görsel 1 düzenlenecek görseldir ve referans olarak en fazla 4 görsel daha bağlanabilir. Görsel 1'in tek bir bölgesi, bir maske veya sınırlayıcı kutularla seçilerek tek başına da düzenlenebilir; bu, görseli tam boyutta döndürür.

## Girdiler

Bir `model` seçmek, hangi girdilerin görüneceğini belirler. Her iki model de bir bölgeyi `context_window` aracılığıyla düzenler; ancak 4.6 maskesini `mask` üzerinden alırken 4.5 bunu `context_window_mask` üzerinden alır ve 4.6 varsayılan olarak `"none"` yerine `"auto"` kullanır.

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model. `"ideogram-4.6"` daha büyük kaynakları ve daha geniş bölgeleri işler; `"ideogram-4.5"` önceki modeldir (varsayılan: `"ideogram-4.6"`). | DYNAMIC_COMBO | Evet | `"ideogram-4.6"`<br>`"ideogram-4.5"` |
| `images` | Büyütülebilir yuva: görsel 1 düzenlenecek görseldir ve görsel 2 ile 5 isteğe bağlı referanslardır (`image_1` ... `image_5`). İstemde bunlara @Image1, @Image2, ... olarak başvurun; toplu bir girdi her görsel için bir kez sayılır. Her görselin en-boy oranı 1:6 ile 6:1 arasında olmalıdır; ancak bir bağlam penceresi kullanılırken görsel 1'in en-boy oranı kontrol edilmez. | IMAGE | Evet | 1 ile 5 görsel arası |
| `prompt` | Düzenleme talimatları. Bağlı görsellere @Image1 tarzı referansları destekler (varsayılan: boş dize). | STRING | Evet | 1 ile 10000 karakter arası |
| `quality` | Kalite kademesi. Daha yüksek kademeler daha maliyetlidir ve daha uzun sürer (varsayılan: `"medium"`). | COMBO | Evet | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Üretim için tohum. 4.6'da aynı görseller, istem, ayarlar ve tohum aynı veya çok benzer bir sonuç verir; 4.5'te aynı sonucu verir (varsayılan: 42). | INT | Evet | 0 ile 2147483647 arası |

### Ideogram 4.6 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `context_window` | Görsel 1'in düzenlenecek bölgesi. `"auto"` maskenin etrafındaki bölgeyi düzenler ve görsel 1'i tam boyutta tutar; maske bağlı değilse tüm görseli düzenler. `"none"` tüm görseli düzenler. `"custom"` `context_window_bboxes` içindeki bölgeyi düzenler ve görsel 1'i tam boyutta tutar (varsayılan: `"auto"`). Bağlı bir `mask` üç modda da, `"none"` dahil, gönderilir. | COMBO | Hayır | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Görsel 1'in düzenlenecek bölgesi; örneğin Create Bounding Boxes çıktısı. `context_window` `"custom"` olduğunda gereklidir; aksi durumda kullanılmaz. Birkaç kutu tek bir bölgede birleştirilir; bu bölge her kenarı en az 256 piksel olacak şekilde büyütülür ve yalnızca 6:1 maksimum en-boy oranında kalmak gerektiğinde daha fazla genişletilir. Bölge her kenar için 8192 piksele ve yaklaşık 16,7 MP'ye kadar olabilir (ör. 4096x4096); alan, her kenar 32'nin katına yukarı yuvarlandıktan sonra kontrol edilir; bu nedenle 4097x4095 bölgesi ham alanı 16,7 MP'nin altında olsa bile reddedilir. | BOUNDING_BOX | Hayır | - |
| `mask` | Beyaz, düzenlenecek alanı işaretler; düzenleme bölgesi bunun etrafına yerleştirilir. Maskede hem beyaz (düzenle) hem de siyah (koru) alanlar bulunmalıdır. Bağlı olduğu her durumda, her `context_window` modunda gönderilir ve görsel sınırını 4'e düşürür (aşağıdaki kısıtlara bakın). | MASK | Hayır | - |

### Ideogram 4.5 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `context_window` | Görsel 1'in düzenlenecek bölgesi. `"none"` tüm görseli düzenler. `"auto"` `context_window_mask` etrafındaki bir bölgeyi, `"custom"` ise `context_window_bboxes` içindeki bölgeyi düzenler; her ikisi de görsel 1'i tam boyutta tutar ve görselin geri kalanını değiştirmeden bırakır (varsayılan: `"none"`). | COMBO | Hayır | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Görsel 1'in düzenlenecek bölgesi; örneğin Create Bounding Boxes çıktısı. `context_window` `"custom"` olduğunda gereklidir; aksi durumda kullanılmaz. Birkaç kutu tek bir bölgede birleştirilir; bu bölge her kenarı en az 256 piksel olacak şekilde büyütülür ve yalnızca 6:1 maksimum en-boy oranında kalmak gerektiğinde daha fazla genişletilir; bu nedenle 32x32 gibi küçük bir kutu da çevresindeki pikselleri düzenler. Bölge her kenar için 4608 piksele ve yaklaşık 4 MP'ye kadar olabilir (ör. 2048x2048); her kenar 32'nin katına yukarı yuvarlandıktan sonra kontrol edilir. | BOUNDING_BOX | Hayır | - |
| `context_window_mask` | Beyaz, düzenlenecek alanı işaretler; düzenleme bölgesi bunun etrafına yerleştirilir. `context_window` `"auto"` olduğunda gereklidir; aksi durumda kullanılmaz. Maskede hem beyaz (düzenle) hem de siyah (koru) alanlar bulunmalıdır. | MASK | Hayır | - |

### Parametre Kısıtları

- **Görsel sayısı:** en az 1, en fazla 5 görsel; toplu bir girdi her görsel için bir kez sayılır. Düğüm bir maske kullandığında en fazla 4 görsel kabul edilir; yani görsel 1 ve 3 referans. 4.6'da bağlı bir `mask` her modda kullanılır; 4.5'te maske `context_window_mask`'tir ve yalnızca `"auto"` içinde kullanılır; bu nedenle `"none"` ve `"custom"` bir maske bağlıyken hâlâ 5 görsel kabul eder.
- **Çıktı boyutu:** düğümde boyut, genişlik veya yükseklik girdisi yoktur. Bölge düzenlemesi tam görseli görsel 1'in boyutunda döndürür. Tüm görsel düzenlemesi, yüklendiği haliyle görsel 1'in boyutunu döndürür: 4.6'da 16,7 MP veya her kenar için 8192 pikselin üzerindeki bir görsel önce küçültülür; 4.5'te aynı işlem yaklaşık 4 MP veya her kenar için 4608 pikselin üzerinde gerçekleşir ve alanı, her kenar 32'nin katına yukarı yuvarlandıktan sonra ölçülür; bu nedenle 4 MP'nin hemen altındaki bir görsel, örneğin 2049x2047, de küçültülür.
- **Bölge kaynak boyutu:** bağlam penceresi kullanımdayken görsel 1 toplamda 67.108.864 piksele kadar olabilir (yaklaşık 67 MP), örneğin 8192x8192 veya 10000x5000; sınır tek bir kenarda değil alan üzerindedir.
- **Bölge sınırları:** `context_window_bboxes` içinden gelen bir bölge, 4.6'da her kenar için 8192 piksele ve yaklaşık 16,7 MP'ye kadar, 4.5'te ise her kenar için 4608 piksele ve yaklaşık 4 MP'ye kadar olabilir. Birleştirilmiş bölge görsel 1'in dışına düştüğünde veya modelin kenar, alan ya da 6:1 en-boy oranı sınırını aştığında kutular hata verir; bu nedenle 4096x4096'lık bir kutu, 8192x8192'lik bir görsel içinde olsa bile 4.5'te başarısız olur. Görselin solunda bir kutu ve sağında başka bir kutu, görseli kapsayan bir bölgede birleşir; bu sorun değildir.
- **İstem etiketleri:** `@ImageN` büyük/küçük harf duyarsız eşleştirilir ve bağlı görsel sayısını aşmamalıdır; istem yalnızca boşluklardan oluşmamalı ve en fazla 10000 karakter olmalıdır.
- **Yükleme sınırı:** görsel 1, maske ve referanslar birlikte Ideogram'ın 50 MB'lık yükleme sınırına sığmalıdır. Bir 4.6 düzenlemesi ve bir 4.5 bölge düzenlemesi, dosyalar sığmadığında görsel 1'i JPEG olarak yeniden kodlar ve hâlâ sığmazsa hata verir; 4.5 tüm görsel düzenlemesi her zaman PNG gönderir ve böyle bir yedek mekanizması yoktur.
- **İçerik güvenliği:** Ideogram'ın içerik güvenliği filtresi sonucu engellerse, düğüm görsel döndürmek yerine hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Düzenlenmiş görsel, toplu (batch) olarak, görsel 1'in boyutunda. Kaynak yükleme bütçesinin üzerindeyse tüm görsel düzenlemesi daha küçük döner: 4.6'da 16,7 MP veya her kenar için 8192 piksel, 4.5'te yaklaşık 4 MP veya her kenar için 4608 piksel. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/tr.md)

---
**Source fingerprint (SHA-256):** `9218070f5e55b3bd8da0701d4b4ea969cb7b1c2ebfc06669a523e64ce4bcf342`
