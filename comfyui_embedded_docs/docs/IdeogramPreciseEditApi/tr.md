# Ideogram 4.5 Hassas Düzenleme

Ideogram 4.5 hassas düzenleme ile bir görseli metin istemi rehberliğinde düzenleyin: yalnızca istemin talep ettiği şeyler değişir, dokunulmamış pikseller aynı kalır ve çıktı, 1. görselin boyutunu korur. 1. görsel, düzenlenecek görseldir ve en fazla 4 ek görsel referans olarak bağlanabilir. 1. görselin tek bir bölgesi de kendi başına düzenlenebilir; bu bölge bir maske veya sınırlayıcı kutularla seçilir ve görsel tam boyutta döndürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `model` | Kullanılacak model. (varsayılan: `"ideogram-4.5"`) | DYNAMIC_COMBO | Evet | `"ideogram-4.5"` |
| `images` | Büyütülebilir yuva: 1. görsel düzenlenecek görseldir ve 2 ile 5 arasındaki görseller isteğe bağlı referanslardır (`image_1` ... `image_5`). İstemde bunlara @Image1, @Image2, ... olarak başvurun; toplu bir girdi, görsel başına bir kez sayılır. Her görselin en-boy oranı 1:6 ile 6:1 arasında olmalıdır; ancak bir bağlam penceresi kullanılırken 1. görselin en-boy oranı kontrol edilmez. | IMAGE | Evet | 1 ila 5 görsel |
| `prompt` | Düzenleme talimatları. Bağlı görsellere @Image1 tarzı referansları destekler. (varsayılan: boş dize) | STRING | Evet | 1 ila 10000 karakter |
| `quality` | Kalite kademesi. Daha yüksek kademeler daha pahalıdır ve daha uzun sürer. (varsayılan: `"medium"`) | COMBO | Evet | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Üretim için tohum. Aynı görseller, istem, ayarlar ve tohum aynı sonucu verir. (varsayılan: 42) | INT | Evet | 0 ila 2147483647 |
| `context_window` | 1. görselin düzenlenecek bölgesi. `"none"` tüm görseli düzenler. `"auto"` `context_window_mask` etrafındaki bir bölgeyi ve `"custom"` `context_window_bboxes` içindeki bölgeyi düzenler; her ikisi de 1. görseli tam boyutta tutar ve görselin geri kalanını değiştirmeden bırakır. (varsayılan: `"none"`) | COMBO | Hayır | `"none"`<br>`"auto"`<br>`"custom"` |
| `context_window_bboxes` | 1. görselin düzenlenecek bölgesi, örneğin Create Bounding Boxes çıktısı. `context_window` `"custom"` olduğunda gereklidir; aksi durumda kullanılmaz. Birkaç kutu tek bir bölgede birleştirilir; bu bölge her kenarı en az 256 piksel ve en-boy oranı 6:1 olacak şekilde büyütülür. Bölge her kenarı en fazla 4608 piksel ve yaklaşık 4 MP (ör. 2048x2048) olabilir. | BOUNDING_BOX | Hayır | - |
| `context_window_mask` | Beyaz, düzenlenecek alanı işaret eder; düzenleme bölgesi bunun etrafına yerleştirilir. `context_window` `"auto"` olduğunda gereklidir; aksi durumda kullanılmaz. Maske hem beyaz (düzenle) hem de siyah (koru) alanlar içermelidir. | MASK | Hayır | - |

### Parametre Kısıtlamaları

- **Görsel sayısı:** en az 1 ve en fazla 5 görsel; toplu bir girdi, görsel başına bir kez sayılır. 1. görsel düzenlenecek görseldir ve 2 ile 5 arasındaki görseller referanstır. `context_window_mask` ile en fazla 4 görsel kabul edilir, yani 1. görsel ve 3 referans.
- **Çıktı boyutu:** sonuç, 1. görselin boyutunu korur, bu nedenle bu düğümün boyut, genişlik veya yükseklik girdileri yoktur. Bu, bir bölge düzenlendiğinde de geçerlidir; burada tam görsel, yalnızca bölge değiştirilmiş olarak geri gelir.
- **Görsel en-boy oranı:** her görsel, yüksekliğinin 6 katından daha geniş ve genişliğinin 6 katından daha uzun olmamalıdır (1:6 ile 6:1 arasında). `context_window` `"auto"` veya `"custom"` olduğunda 1. görsel muaf tutulur, çünkü yalnızca seçilen bölgesi gönderilir.
- **Bölge kaynak boyutu:** bir bağlam penceresi kullanılırken 1. görsel en fazla 8192x8192 piksel (yaklaşık 67 MP) olabilir; daha büyük kaynaklar hata verir. Bağlam penceresi olmadan, yaklaşık 4 MP'den büyük veya uzun kenarı 4608 pikselden büyük görseller gönderilmeden önce küçültülür.
- **Bölge sınırları:** `context_window_bboxes` içinden gelen bir bölge her kenarı en fazla 4608 piksel ve yaklaşık 4 MP olabilir; tamamen 1. görselin dışında kalan kutular hata verir.
- **İstem etiketleri:** `@ImageN` büyük/küçük harfe duyarsız olarak eşleştirilir ve bağlı görsel sayısını aşmamalıdır; istem yalnızca boşluktan oluşmamalı ve en fazla 10000 karakter olmalıdır.
- **Yükleme sınırı:** 1. görsel, maske ve referanslar birlikte Ideogram'ın 50 MB yükleme sınırına sığmalıdır; 1. görsel gerektiğinde JPEG olarak yeniden kodlanır ve hâlâ sığmıyorsa düğüm hata verir.
- **İçerik güvenliği:** Ideogram'ın içerik güvenliği filtresi sonucu engellerse, düğüm bir görsel döndürmek yerine hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `IMAGE` | Düzenlenmiş görsel, toplu olarak, 1. görselin boyutunda. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/tr.md)

---
**Source fingerprint (SHA-256):** `84f042739a8d7bc1a4b268f6175be6a598b67d32b9311fdf204a923472f5fcc9`
