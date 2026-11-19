# Ideogram 4.5 Hassas Düzenleme

Ideogram 4.6 veya 4.5 hassas düzenlemesiyle, bir metin istemi kılavuzluğunda bir görüntü düzenleyin: yalnızca istemin istediği şeyler değişir, dokunulmayan pikseller aynı kalır ve çıktı görsel 1'in boyutunu korur. 4.6'da tüm görüntü düzenlemesi, kaynak 16,7 MP'nin veya kenar başına 8192 pikselin üzerindeyse daha küçük bir görüntü döndürür; çünkü yüklemeden önce küçültülür. Görsel 1 düzenlenecek görseldir ve referans olarak en fazla 4 görsel daha bağlanabilir. Görsel 1'in tek bir bölgesi de bir maske veya sınırlayıcı kutularla seçilerek tek başına düzenlenebilir; bu, görüntüyü tam boyutta döndürür.

## Girdiler

Bir `model` seçmek, hangi girdilerin görüneceğini belirler. Her iki model de bir bölgeyi `context_window` aracılığıyla düzenler; ancak 4.6 maskesini `mask` üzerinden alırken 4.5 bunu `context_window_mask` üzerinden alır ve 4.6 varsayılan olarak `"none"` yerine `"auto"` kullanır.

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model. `"ideogram-4.6"` daha büyük kaynakları ve daha geniş bölgeleri işler; `"ideogram-4.5"` önceki modeldir (varsayılan: `"ideogram-4.6"`). | DYNAMIC_COMBO | Evet | `"ideogram-4.6"`<br>`"ideogram-4.5"` |
| `images` | Büyütülebilir yuva: görsel 1 düzenlenecek görseldir ve görsel 2 ile 5 isteğe bağlı referanslardır (`image_1` ... `image_5`). İstemde bunlara @Image1, @Image2, ... olarak başvurun; toplu bir girdi her görsel için bir kez sayılır. Her görselin en-boy oranı 1:6 ile 6:1 arasında olmalıdır; ancak bir bağlam penceresi kullanılırken görsel 1'in en-boy oranı denetlenmez. | IMAGE | Evet | 1 ile 5 görsel arası |
| `prompt` | Düzenleme talimatları. Bağlı görsellere @Image1 tarzı referansları destekler (varsayılan: boş dize). | STRING | Evet | 1 ile 10000 karakter arası |
| `quality` | Kalite düzeyi. Daha yüksek düzeyler daha fazla maliyetlidir ve daha uzun sürer (varsayılan: `"medium"`). | COMBO | Evet | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Üretim için tohum. Aynı görseller, istem, ayarlar ve tohum aynı veya çok benzer sonucu verir (varsayılan: 42). | INT | Evet | 0 ile 2147483647 arası |

### Ideogram 4.6 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `context_window` | Düzenlenecek görsel 1 bölgesi. `"auto"` maskenin çevresindeki bölgeyi düzenler ve görsel 1'i tam boyutta tutar veya maske bağlı değilken tüm görüntüyü düzenler; `"none"` tüm görüntüyü düzenler; `"custom"` `context_window_bboxes` içindeki bölgeyi düzenler ve görsel 1'i tam boyutta tutar (varsayılan: `"auto"`). | COMBO | Hayır | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Düzenlenecek görsel 1 bölgesi; örneğin Create Bounding Boxes çıktısı. `context_window` `"custom"` olduğunda gereklidir; aksi durumda kullanılmaz. Birkaç kutu tek bir bölgede birleştirilir; bu bölge, kenar başına en az 256 piksel ve 6:1 en-boy oranı olacak şekilde büyütülür. Bölge kenar başına 8192 piksele ve yaklaşık 16,7 MP'ye (ör. 4096x4096) kadar olabilir. | BOUNDING_BOX | Hayır | - |
| `mask` | Beyaz, düzenlenecek alanı işaretler; düzenleme bölgesi bunun çevresine yerleştirilir. Maske hem beyaz (düzenle) hem de siyah (koru) alanlar içermelidir. Bağlı olduğu her durumda, her `context_window` modunda gönderilir ve görsel sınırını 4'e düşürür (aşağıdaki kısıtlamalara bakın). | MASK | Hayır | - |

### Ideogram 4.5 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `context_window` | Düzenlenecek görsel 1 bölgesi. `"none"` tüm görüntüyü düzenler. `"auto"` `context_window_mask` çevresindeki bir bölgeyi, `"custom"` ise `context_window_bboxes` içindeki bölgeyi düzenler; her ikisi de görsel 1'i tam boyutta tutar ve görüntünün geri kalanını değiştirmeden bırakır (varsayılan: `"none"`). | COMBO | Hayır | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Düzenlenecek görsel 1 bölgesi; örneğin Create Bounding Boxes çıktısı. `context_window` `"custom"` olduğunda gereklidir; aksi durumda kullanılmaz. Bölge kenar başına 4608 piksele ve yaklaşık 4 MP'ye (ör. 2048x2048) kadar olabilir. | BOUNDING_BOX | Hayır | - |
| `context_window_mask` | Beyaz, düzenlenecek alanı işaretler; düzenleme bölgesi bunun çevresine yerleştirilir. `context_window` `"auto"` olduğunda gereklidir; aksi durumda kullanılmaz. Maske hem beyaz (düzenle) hem de siyah (koru) alanlar içermelidir. | MASK | Hayır | - |

### Parametre Kısıtlamaları

- **Görsel sayısı:** en az 1, en fazla 5 görsel; toplu bir girdi her görsel için bir kez sayılır. Bir maske bağlı olduğunda en fazla 4 görsel kabul edilir; yani görsel 1 ve 3 referans.
- **Çıktı boyutu:** düğümde boyut, genişlik veya yükseklik girdisi yoktur. Bölge düzenlemesi, tam görüntüyü görsel 1'in boyutunda döndürür. Tüm görüntü düzenlemesi, görsel 1'in yüklendiği boyutu döndürür: 4.6'da 16,7 MP'nin veya kenar başına 8192 pikselin üzerindeki bir görüntü önce küçültülür; 4.5'te aynı durum yaklaşık 4 MP'nin veya kenar başına 4608 pikselin üzerinde gerçekleşir.
- **Bölge kaynak boyutu:** bir bağlam penceresi kullanılırken görsel 1, 8192x8192 piksele (yaklaşık 67 MP) kadar olabilir; daha büyük kaynaklar hata verir.
- **Bölge sınırları:** `context_window_bboxes` içindeki bir bölge 4.6'da kenar başına 8192 piksele ve yaklaşık 16,7 MP'ye, 4.5'te ise kenar başına 4608 piksele ve yaklaşık 4 MP'ye kadar olabilir. Tamamen görsel 1'in dışında kalan kutular hata verir.
- **İstem etiketleri:** `@ImageN` büyük/küçük harfe duyarsız olarak eşleştirilir ve bağlı görsel sayısını aşmamalıdır; istem yalnızca boşluklardan oluşmamalı ve en fazla 10000 karakter olmalıdır.
- **Yükleme sınırı:** görsel 1, maske ve referanslar birlikte Ideogram'ın 50 MB'lık yüklemesine sığmalıdır; görsel 1 gerektiğinde JPEG olarak yeniden kodlanır ve hâlâ sığmıyorsa düğüm hata verir.
- **İçerik güvenliği:** Ideogram'ın içerik güvenliği filtresi sonucu engellerse, düğüm görüntü döndürmek yerine hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Düzenlenmiş görüntü, toplu olarak, görsel 1'in boyutunda. 4.6'da tüm görüntü düzenlemesi, kaynak 16.7 MP veya kenar başına 8192 pikseli aşarsa daha küçük döner. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/tr.md)

---
**Source fingerprint (SHA-256):** `84f042739a8d7bc1a4b268f6175be6a598b67d32b9311fdf204a923472f5fcc9`
