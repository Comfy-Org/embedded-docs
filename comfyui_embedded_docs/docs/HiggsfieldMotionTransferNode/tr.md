# Higgsfield Genjutsu Motion Transfer

**Higgsfield Genjutsu Motion Transfer** düğümü, kaynak klibin hareketini, kamera hareketini, zamanlamasını ve sesini korurken bir videoyu referans görsellerden alınan yeni karakterler, mekânlar veya stillerle yeniden biçimlendirir. Yeniden stilize edilecek klibi ve yeni görünümü tanımlayan bir veya daha fazla referans görselini bağlayın, ardından sonucu prompt içinde açıklayın. İstek Higgsfield API'sine gönderilir ve oluşturulan video döndürülür.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model. Bir model seçmek, ona özgü parametreleri gösterir: `video`, `reference_images`, `prompt`, `resolution` ve `seed`. | DYNAMIC_COMBO | Evet | `"genjutsu-v1.0"` |
| `video` | Hareketi, kamera hareketi, zamanlaması ve sesi korunan kaynak video. En az 4 saniye; yalnızca ilk 30 saniye kullanılır. | VIDEO | Evet | 4 - 30 saniye |
| `reference_images` | Büyütülebilir yuva: kullanılacak karakterler, mekânlar veya stiller için 1 ila 8 görsel (`image_1`, `image_2`, ...) bağlayın. Toplu bir girdi, her görsel için bir kez sayılır. | IMAGE | Evet | 1 - 8 görsel |
| `prompt` | İsteğe bağlı. Sonucu açıklayın; örneğin hangi referansın hangi kişinin yerini aldığını veya yeni bir ortamı. (varsayılan: boş) | STRING | Evet | Herhangi bir metin |
| `resolution` | Çıktı videosunun çözünürlüğü. (varsayılan: `"720p"`) | COMBO | Evet | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `seed` | `seed`, düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçlar `seed` değerinden bağımsız olarak deterministik değildir. Bu parametre "oluşturma sonrası kontrol" işlevine sahiptir (varsayılan: 42). | INT | Evet | 0 - 2147483647 |

Kaynak video, istek gönderilmeden önce doğrulanır: 4 saniyeden kısa bir klip reddedilir ve 30 saniyeden uzun bir klip ilk 30 saniyesine kırpılır. Sesi sonuca aktarılır. Referans görseller önce yüklenir ve düğüm sekiz yuva sunsa da bağlı tüm yuvalardaki toplam görsel sayısı 8'i aşamaz. Higgsfield'ın içerik denetimi girdiyi veya sonucu reddedebilir; bu, video döndürmek yerine bir hata oluşturur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
|-------------|-------------|-----------|
| `VIDEO` | Yeniden stilize edilmiş video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiggsfieldMotionTransferNode/tr.md)

---
**Source fingerprint (SHA-256):** `f0c30fb93dd2af8d564335290fdb6ff61c38e36ab62cef9641fd1aa81cc10cd2`
