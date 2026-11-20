# Ideogram 4.5 Düzenleme

## Girdiler

Bir `model` seçmek hangi girdilerin görüneceğini belirler. Ideogram 4.6, `background`, `(4K)` boyutları ve kenar başına 8192 piksele kadar özel boyutlar ekler; 4.5, kenar başına en fazla 4608 piksel olan `(1K)` ve `(2K)` ön ayarlarını korur. Her iki model de burada `very_low`, `low`, `medium` ve `high` kalite kademelerini sunar.

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model. `"ideogram-4.6"` isteğe bağlı saydam arka planla 4K'ya kadar oluşturur; `"ideogram-4.5"` önceki modeldir (varsayılan: `"ideogram-4.6"`). | DYNAMIC_COMBO | Evet | `"ideogram-4.6"`<br>`"ideogram-4.5"` |
| `images` | Büyütülebilir yuva: 1. görüntü düzenlenecek görüntüdür ve 2 ile 5 arasındaki görüntüler isteğe bağlı referanslardır (`image_1` ... `image_5`). İstemde bunlara @Image1, @Image2, ... olarak başvurun; toplu bir girdi her görüntü için bir kez sayılır. Her görüntü 1:6 ile 6:1 arasında bir en-boy oranına sahip olmalıdır. | IMAGE | Evet | 1 ile 5 görüntü arası |
| `prompt` | Düzenleme talimatları. Bağlı görüntülere @Image1 tarzı referansları destekler (varsayılan: boş dize). | STRING | Evet | 1 ile 10000 karakter arası |
| `seed` | Üretim için tohum. Aynı görüntüler, istem, ayarlar ve tohum aynı veya çok benzer sonucu verir (varsayılan: 42). | INT | Evet | 0 ile 2147483647 arası |

### Ideogram 4.6 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size` | Çıktı boyutu. `"auto"` görüntülerden ve istemden yaklaşık 2K boyutunda bir tuval seçer, `"source"` 1. görüntünün boyutunu korur (16,7 MP veya kenar başına 8192 piksel üzerindeki görüntüler önce küçültülür) ve farklı en-boy oranına sahip bir ön ayar sahneyi yeniden oluşturur. Aşağıdaki genişlik ve yüksekliği kullanmak için `"custom"` seçin (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"source"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(4K) 4096x4096 (1:1)"`<br>`"(4K) 2880x5760 (1:2)"`<br>`"(4K) 5760x2880 (2:1)"`<br>`"(4K) 3328x4992 (2:3)"`<br>`"(4K) 4992x3328 (3:2)"`<br>`"(4K) 3584x4480 (4:5)"`<br>`"(4K) 4480x3584 (5:4)"`<br>`"(4K) 2880x5120 (9:16)"`<br>`"(4K) 5120x2880 (16:9)"`<br>`"(4K) 3200x5120 (5:8)"`<br>`"(4K) 5120x3200 (8:5)"`<br>`"(4K) 3456x4608 (3:4)"`<br>`"(4K) 4608x3456 (4:3)"`<br>`"(4K) 2304x5888 (9:23)"`<br>`"(4K) 5888x2304 (23:9)"`<br>`"(4K) 2496x6656 (3:8)"`<br>`"(4K) 6656x2496 (8:3)"`<br>`"(4K) 2560x6144 (5:12)"`<br>`"(4K) 6144x2560 (12:5)"`<br>`"(4K) 2048x6144 (1:3)"`<br>`"(4K) 6144x2048 (3:1)"`<br>`"custom"` |
| `width` | Piksel cinsinden özel çıktı genişliği; yalnızca `size` `"custom"` olduğunda kullanılır (varsayılan: 2048). | INT | Evet | 256 ile 8192 arası (adım 32) |
| `height` | Piksel cinsinden özel çıktı yüksekliği; yalnızca `size` `"custom"` olduğunda kullanılır (varsayılan: 2048). | INT | Evet | 256 ile 8192 arası (adım 32) |
| `quality` | Kalite kademesi. Daha yüksek kademeler daha pahalıdır ve daha uzun sürer (varsayılan: `"medium"`). | COMBO | Evet | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `background` | `"transparent"` görüntüyü alfa kanalıyla döndürür, `"opaque"` opak bir arka planı zorunlu kılar, `"auto"` istemi takip eder (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"opaque"`<br>`"transparent"` |

### Ideogram 4.5 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size` | Çıktı boyutu. `"auto"` görüntülerden ve istemden yaklaşık 2K boyutunda bir tuval seçer, `"source"` 1. görüntünün boyutunu korur (yaklaşık 4 MP veya kenar başına 4608 piksel üzerindeki görüntüler önce küçültülür) ve farklı en-boy oranına sahip bir ön ayar sahneyi yeniden oluşturur. Aşağıdaki genişlik ve yüksekliği kullanmak için `"custom"` seçin (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"source"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"custom"` |
| `width` | Piksel cinsinden özel çıktı genişliği; yalnızca `size` `"custom"` olduğunda kullanılır (varsayılan: 2048). | INT | Evet | 256 ile 4608 arası (adım 32) |
| `height` | Piksel cinsinden özel çıktı yüksekliği; yalnızca `size` `"custom"` olduğunda kullanılır (varsayılan: 2048). | INT | Evet | 256 ile 4608 arası (adım 32) |
| `quality` | Kalite kademesi. Daha yüksek kademeler daha pahalıdır ve daha uzun sürer (varsayılan: `"medium"`). | COMBO | Evet | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |

### Parametre Kısıtları

- **Görüntü sayısı:** en az 1 ve en fazla 5 görüntü; toplu bir girdi her görüntü için bir kez sayılır. 1. görüntü düzenlenecek görüntüdür, geri kalanlar referanstır.
- **Görüntü en-boy oranı:** her görüntü, yüksekliğinin 6 katından daha geniş olamaz ve genişliğinin 6 katından daha yüksek olamaz (1:6 ile 6:1 arası).
- **İstem etiketleri:** `@ImageN` büyük/küçük harfe duyarsız olarak eşleştirilir ve bağlı görüntü sayısını aşmamalıdır; istem yalnızca boşluktan oluşmamalı ve en fazla 10000 karakter olmalıdır.
- **Özel boyut:** genişlik çarpı yükseklik, 4.6 üzerinde 16,7 MP'yi (4096x4096) ve 4.5 üzerinde 4194304 pikseli (2048x2048) aşmamalıdır; uzun kenar, kısa kenarın 6 katını aşmamalıdır. Genişlik ve yükseklik 32'nin katlarına yuvarlanır.
- **Yükleme ölçekleme:** 4.6, 1. görüntüyü kenar başına en fazla 16,7 MP ve 8192 piksel olacak şekilde gönderir; bu, görüntüyü yükleme sınırının altında tuttuğunda onu JPEG olarak yeniden kodlar; 4.5 ise 1. görüntüyü yaklaşık 4 MP veya kenar başına 4608 pikselin üzerinde küçültür.
- **İçerik güvenliği:** Ideogram'ın içerik güvenliği filtresi sonucu engellerse, düğüm bir görüntü döndürmek yerine hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Düzenlenmiş veya birleştirilmiş görüntü, toplu olarak. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramEditApi/tr.md)

---
**Source fingerprint (SHA-256):** `58c189d65502373ff7b56f5f32d9f2e7ee8019fc58f1bbbb80abc859cf978f67`
