# Ideogram 4.5 Hassas Düzenleme

Ideogram 4.6 veya 4.5 hassas düzenleme ile bir metin istemi rehberliğinde bir görüntüyü düzenleyin: yalnızca istemin istediği şeyler değişir, dokunulmayan pikseller aynı kalır ve çıktı, 1. görüntünün boyutunu korur. 1. görüntü düzenlenecek görüntüdür ve referans olarak en fazla 4 ek görüntü bağlanabilir. 1. görüntünün tek bir bölgesi, bir maske veya sınırlayıcı kutularla seçilerek kendi başına da düzenlenebilir; bu, görüntüyü tam boyutta döndürür.

## Girdiler

Bir `model` seçmek, hangi girdilerin görüneceğini belirler. Her iki model de bir bölgeyi `context_window` aracılığıyla düzenler, ancak 4.6 maskesini `mask` üzerinden alırken 4.5 bunu `context_window_mask` üzerinden alır ve 4.6 varsayılan olarak `"none"` yerine `"auto"` kullanır.

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model. `"ideogram-4.6"` daha büyük kaynakları ve daha geniş bölgeleri işler; `"ideogram-4.5"` önceki modeldir (varsayılan: `"ideogram-4.6"`). | DYNAMIC_COMBO | Evet | `"ideogram-4.6"`<br>`"ideogram-4.5"` |
| `images` | Büyütülebilir yuva: 1. görüntü düzenlenecek görüntüdür ve 2 ile 5 arasındaki görüntüler isteğe bağlı referanslardır (`image_1` ... `image_5`). İstemde bunlara @Image1, @Image2, ... olarak başvurun; toplu girdi her görüntü için bir kez sayılır. Her görüntünün en-boy oranı 1:6 ile 6:1 arasında olmalıdır; ancak bir bağlam penceresi kullanılırken 1. görüntünün en-boy oranı kontrol edilmez. | IMAGE | Evet | 1 ile 5 görsel arası |
| `prompt` | Düzenleme talimatları. Bağlanan görüntülere @Image1 tarzı başvuruları destekler (varsayılan: boş dize). | STRING | Evet | 1 ile 10000 karakter arası |
| `quality` | Kalite kademesi. Daha yüksek kademeler daha pahalıdır ve daha uzun sürer (varsayılan: `"medium"`). | COMBO | Evet | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Üretim için tohum. Aynı görüntüler, istem, ayarlar ve tohum aynı sonucu verir (varsayılan: 42). | INT | Evet | 0 ile 2147483647 arası |

### Ideogram 4.6 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `context_window` | 1. görüntünün düzenlenecek bölgesi. `"auto"`, `mask` çevresini düzenler ve 1. görüntüyü tam boyutta tutar; maske bağlı değilse tüm görüntüyü düzenler; `"none"` maskeli olsa bile tüm görüntüyü düzenler; `"custom"` ise `context_window_bboxes` içindeki bölgeyi düzenler ve 1. görüntüyü tam boyutta tutar. Tüm görüntü düzenlemeleri, 16,7 MP veya kenar başına 8192 piksel üzerindeki görüntüleri önce küçültür (varsayılan: `"auto"`). | COMBO | Hayır | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | 1. görüntünün düzenlenecek bölgesi; örneğin Create Bounding Boxes çıktısı. `context_window` değeri `"custom"` olduğunda gereklidir; aksi halde kullanılmaz. Birkaç kutu tek bir bölgede birleştirilir; bu bölge en az kenar başına 256 piksele ve 6:1 en-boy oranına genişletilir. Bölge, kenar başına 8192 piksele ve yaklaşık 16,7 MP'ye kadar olabilir (ör. 4096x4096). | BOUNDING_BOX | Hayır | - |
| `mask` | Beyaz, neyin düzenleneceğini işaretler; düzenleme bölgesi bunun çevresine yerleştirilir. Maske hem beyaz (düzenle) hem de siyah (koru) alanlar içermelidir. Yalnızca `context_window` değeri `"auto"` iken kullanılır. | MASK | Hayır | - |

### Ideogram 4.5 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `context_window` | 1. görüntünün düzenlenecek bölgesi. `"none"` tüm görüntüyü düzenler. `"auto"`, `context_window_mask` çevresindeki bir bölgeyi; `"custom"` ise `context_window_bboxes` içindeki bölgeyi düzenler; her ikisi de 1. görüntüyü tam boyutta tutar ve görüntünün geri kalanını değiştirmez (varsayılan: `"none"`). | COMBO | Hayır | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | 1. görüntünün düzenlenecek bölgesi; örneğin Create Bounding Boxes çıktısı. `context_window` değeri `"custom"` olduğunda gereklidir; aksi halde kullanılmaz. Bölge, kenar başına 4608 piksele ve yaklaşık 4 MP'ye kadar olabilir (ör. 2048x2048). | BOUNDING_BOX | Hayır | - |
| `context_window_mask` | Beyaz, neyin düzenleneceğini işaretler; düzenleme bölgesi bunun çevresine yerleştirilir. `context_window` değeri `"auto"` olduğunda gereklidir; aksi halde kullanılmaz. Maske hem beyaz (düzenle) hem de siyah (koru) alanlar içermelidir. | MASK | Hayır | - |

### Parametre Kısıtları

- **Görüntü sayısı:** en az 1 ve en fazla 5 görüntü; toplu girdi her görüntü için bir kez sayılır. Bir maske ile en fazla 4 görüntü kabul edilir; yani 1. görüntü ve 3 referans.
- **Çıktı boyutu:** sonuç, 1. görüntünün boyutunu korur; bu nedenle bu düğümde boyut, genişlik veya yükseklik girdisi yoktur. 4.6'da 16,7 MP veya kenar başına 8192 piksel üzerindeki bir görüntü önce küçültülür; 4.5'te aynı işlem yaklaşık 4 MP veya kenar başına 4608 piksel üzerinde gerçekleşir.
- **Bölge kaynağı boyutu:** bir bağlam penceresi kullanılırken 1. görüntü 8192x8192 piksele kadar olabilir (yaklaşık 67 MP); daha büyük kaynaklar hata verir.
- **Bölge sınırları:** `context_window_bboxes` içinden gelen bir bölge 4.6'da kenar başına 8192 piksele ve yaklaşık 16,7 MP'ye kadar, 4.5'te ise kenar başına 4608 piksele ve yaklaşık 4 MP'ye kadar olabilir. Tamamen 1. görüntünün dışında kalan kutular hata verir.
- **İstem etiketleri:** `@ImageN` büyük/küçük harfe duyarsız olarak eşleştirilir ve bağlı görüntü sayısını aşmamalıdır; istem yalnızca boşluklardan oluşmamalı ve en fazla 10000 karakter olmalıdır.
- **Yükleme sınırı:** 1. görüntü, maske ve referanslar birlikte Ideogram'ın 50 MB'lık yükleme sınırına sığmalıdır; gerektiğinde 1. görüntü JPEG olarak yeniden kodlanır ve hâlâ sığmazsa düğüm hata verir.
- **İçerik güvenliği:** Ideogram'ın içerik güvenliği filtresi sonucu engellerse, düğüm bir görüntü döndürmek yerine hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Düzenlenen görüntü, 1. görüntünün boyutunda toplu olarak. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/tr.md)

---
**Source fingerprint (SHA-256):** `84f042739a8d7bc1a4b268f6175be6a598b67d32b9311fdf204a923472f5fcc9`
