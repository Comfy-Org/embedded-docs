# Ideogram 4.5 Hassas Düzenleme

Metin istemiyle yönlendirilen bir görüntüyü Ideogram 4.6 veya 4.5 hassas düzenleme ile düzenleyin: yalnızca istemin istediği şeyler değişir. Bölge düzenlemesi, görüntü 1'i tam boyutunda ve çözünürlüğünde tutar. Tüm görüntü düzenlemesi, görüntü 1 modelin sınırının üzerindeyse yüklemeden önce onu ölçeklendirir; bu nedenle sonuç girdiden daha küçük olabilir: 4.6'da 16.7 MP veya kenar başına 8192 piksel, 4.5'te yaklaşık 4 MP veya kenar başına 4608 piksel. Görüntü 1 düzenlenecek görüntüdür ve 4 adede kadar başka görüntü referans olarak bağlanabilir. Görüntü 1'in tek bir bölgesi de kendi başına düzenlenebilir; bu, bir maske veya sınırlayıcı kutularla seçilir ve görüntüyü tam boyutta döndürür.

## Girdiler

Bir `model` seçmek hangi girdilerin görüneceğini belirler. Her iki model de `context_window` aracılığıyla bir bölgeyi düzenler, ancak 4.6 maskesini `mask` üzerinden alırken 4.5 bunu `context_window_mask` üzerinden alır ve 4.6 varsayılan olarak `"none"` yerine `"auto"` kullanır.

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model. `"ideogram-4.6"` daha büyük kaynakları ve daha geniş bölgeleri işler; `"ideogram-4.5"` önceki modeldir (varsayılan: `"ideogram-4.6"`). | DYNAMIC_COMBO | Evet | `"ideogram-4.6"`<br>`"ideogram-4.5"` |
| `images` | Büyütülebilir yuva: görüntü 1 düzenlenecek görüntüdür ve 2 ile 5 arasındaki görüntüler isteğe bağlı referanslardır (`image_1` ... `image_5`). İstemde bunlara @Image1, @Image2, ... olarak başvurun; toplu bir girdi her görüntü için bir kez sayılır. Her görüntünün en-boy oranı 1:6 ile 6:1 arasında olmalıdır; ancak bir bağlam penceresi kullanılırken görüntü 1 için en-boy oranı denetlenmez. | IMAGE | Evet | 1 ile 5 görsel arası |
| `prompt` | Düzenleme talimatları. Bağlı görüntülere @Image1 tarzı referansları destekler (varsayılan: boş dize). | STRING | Evet | 1 ile 10000 karakter arası |
| `quality` | Kalite düzeyi. Daha yüksek kademeler daha fazla maliyetlidir ve daha uzun sürer (varsayılan: `"medium"`). | COMBO | Evet | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Üretim için tohum. 4.6'da aynı görüntüler, istem, ayarlar ve tohum aynı veya çok benzer bir sonuç verir; 4.5'te aynı sonucu verir (varsayılan: 42). | INT | Evet | 0 ile 2147483647 arası |

### Ideogram 4.6 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `context_window` | Düzenlenecek görüntü 1 bölgesi. `"auto"` maskenin etrafındaki bölgeyi düzenler ve görüntü 1'i tam boyutta tutar veya maske bağlı değilse tüm görüntüyü düzenler; `"none"` tüm görüntüyü düzenler; `"custom"` `context_window_bboxes` içindeki bölgeyi düzenler ve görüntü 1'i tam boyutta tutar (varsayılan: `"auto"`). Bağlı bir `mask` üç modda da gönderilir, `"none"` dahil. | COMBO | Hayır | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Düzenlenecek görüntü 1 bölgesi, örneğin Create Bounding Boxes çıktısı. `context_window` `"custom"` olduğunda gereklidir; aksi halde kullanılmaz. Birkaç kutu tek bir bölgede birleştirilir; bu bölge kenar başına en az 256 piksele büyütülür ve yalnızca 6:1 maksimum en-boy oranı içinde kalmak gerektiğinde daha fazla genişletilir. Bölge kenar başına 8192 piksele ve yaklaşık 16.7 MP'ye kadar olabilir (ör. 4096x4096); alan, her kenar 32'nin katına yukarı yuvarlandıktan sonra denetlenir, bu nedenle ham alanı 16.7 MP'nin altında olsa bile 4097x4095 bölgesi reddedilir. | BOUNDING_BOX | Hayır | - |
| `mask` | Beyaz, neyin düzenleneceğini işaretler; düzenleme bölgesi bunun etrafına yerleştirilir. Maske hem beyaz (düzenle) hem de siyah (koru) alanlar içermelidir. Her `context_window` modunda bağlı olduğunda gönderilir ve görüntü sınırını 4'e düşürür (aşağıdaki kısıtlamalara bakın). | MASK | Hayır | - |

### Ideogram 4.5 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `context_window` | Düzenlenecek görüntü 1 bölgesi. `"none"` tüm görüntüyü düzenler. `"auto"` `context_window_mask` etrafındaki bir bölgeyi ve `"custom"` `context_window_bboxes` içindeki bölgeyi düzenler; her ikisi de görüntü 1'i tam boyutta tutar ve görüntünün geri kalanını değiştirmeden bırakır (varsayılan: `"none"`). | COMBO | Hayır | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | Düzenlenecek görüntü 1 bölgesi, örneğin Create Bounding Boxes çıktısı. `context_window` `"custom"` olduğunda gereklidir; aksi halde kullanılmaz. Birkaç kutu tek bir bölgede birleştirilir; bu bölge kenar başına en az 256 piksele büyütülür ve yalnızca 6:1 maksimum en-boy oranı içinde kalmak gerektiğinde daha fazla genişletilir; bu nedenle 32x32 gibi küçük bir kutu da çevresindeki pikselleri düzenler. Bölge kenar başına 4608 piksele ve yaklaşık 4 MP'ye kadar olabilir (ör. 2048x2048); her kenar 32'nin katına yukarı yuvarlandıktan sonra denetlenir. | BOUNDING_BOX | Hayır | - |
| `context_window_mask` | Beyaz, neyin düzenleneceğini işaretler; düzenleme bölgesi bunun etrafına yerleştirilir. `context_window` `"auto"` olduğunda gereklidir; aksi halde kullanılmaz. Maske hem beyaz (düzenle) hem de siyah (koru) alanlar içermelidir. | MASK | Hayır | - |

### Parametre Kısıtlamaları

- **Görüntü sayısı:** en az 1 ve en fazla 5 görüntü; toplu bir girdi her görüntü için bir kez sayılır. Düğüm bir maske kullandığında en fazla 4 görüntü kabul edilir, yani görüntü 1 ve 3 referans. 4.6'da bağlı bir `mask` her modda kullanılır; 4.5'te maske `context_window_mask`'tir ve yalnızca `"auto"` içinde kullanılır, bu nedenle `"none"` ve `"custom"` bir maske bağlıyken hâlâ 5 görüntü kabul eder.
- **Çıktı boyutu:** düğümün boyut, genişlik veya yükseklik girdisi yoktur. Bir bölge düzenlemesi tam görüntüyü görüntü 1'in boyutunda döndürür. Bir tüm görüntü düzenlemesi, görüntü 1'in yüklendiği boyutu döndürür: 4.6'da kenar başına 16.7 MP veya 8192 pikselin üzerindeki bir görüntü önce ölçeklendirilir ve 4.5'te aynı durum yaklaşık 4 MP veya kenar başına 4608 pikselin üzerinde gerçekleşir.
- **Bölge kaynak boyutu:** bir bağlam penceresi kullanılırken görüntü 1 toplamda 67,108,864 piksele kadar olabilir (yaklaşık 67 MP), örneğin 8192x8192 veya 10000x5000; sınır tek bir kenarda değil alandadır.
- **Bölge sınırları:** `context_window_bboxes` içinden gelen bir bölge 4.6'da kenar başına 8192 piksele ve yaklaşık 16.7 MP'ye, 4.5'te ise kenar başına 4608 piksele ve yaklaşık 4 MP'ye kadar olabilir. Kutular yalnızca birleştirilmiş bölgeleri görüntü 1'in dışına çıktığında hata verir; bu nedenle görüntünün solunda kalan bir kutu ile sağında kalan bir başka kutu, görüntüyü kapsayan bir bölgede birleşir.
- **İstem etiketleri:** `@ImageN` büyük/küçük harfe duyarsız eşleştirilir ve bağlı görüntü sayısını aşmamalıdır; istem boşluk dışı karakterler içermeli ve en fazla 10000 karakter olmalıdır.
- **Yükleme sınırı:** görüntü 1, maske ve referanslar birlikte Ideogram'ın 50 MB yükleme sınırına sığmalıdır. Bir 4.6 düzenlemesi ve bir 4.5 bölge düzenlemesi, dosyalar sığmadığında görüntü 1'i JPEG olarak yeniden kodlar ve hâlâ sığmıyorsa hata verir; bir 4.5 tüm görüntü düzenlemesi her zaman PNG gönderir ve böyle bir yedeği yoktur.
- **İçerik güvenliği:** Ideogram'ın içerik güvenliği filtresi sonucu engellerse, düğüm görüntü döndürmek yerine hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Düzenlenen görüntü, görüntü 1'in boyutunda bir toplu olarak. Kaynak yükleme bütçesinin üzerindeyse tüm görüntü düzenlemesi daha küçük döner: 4.6'da 16.7 MP veya kenar başına 8192 piksel, 4.5'te yaklaşık 4 MP veya kenar başına 4608 piksel. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/tr.md)

---
**Source fingerprint (SHA-256):** `84f042739a8d7bc1a4b268f6175be6a598b67d32b9311fdf204a923472f5fcc9`
