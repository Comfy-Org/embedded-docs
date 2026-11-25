# Ideogram 4.5 Metinden Görüntüye

Ideogram 4.6 veya 4.5 ile metin isteminden görüntüler oluşturun. İstem ayrıca, örneğin daha önceki bir çalıştırmadan dönen `final_prompt` gibi, metin dizeleri, renkler ve düzen üzerinde tam kontrol sağlayan bir Ideogram yapılandırılmış JSON altyazısını da kabul eder. Düğüm, görüntüyü gerçekte oluşturulduğu altyazıyla birlikte döndürür.

## Girdiler

Bir `model` seçimi hangi girdilerin görüneceğini belirler. Ideogram 4.6, `background`, `very_low` kalite kademesi, `(4K)` boyutları ve özel bir genişlik ve yükseklik ekler; 4.5 ise `(1K)` ve `(2K)` ön ayarlarını korur.

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model. `"ideogram-4.6"` isteğe bağlı saydam arka planla 4K'ya kadar oluşturur; `"ideogram-4.5"` önceki modeldir (varsayılan: `"ideogram-4.6"`). | DYNAMIC_COMBO | Evet | `"ideogram-4.6"`<br>`"ideogram-4.5"` |
| `prompt` | Metin istemi veya önceki bir `final_prompt` gibi bir Ideogram yapılandırılmış JSON altyazısı (varsayılan: boş dize). | STRING | Evet | 1 ile 10000 karakter arası |
| `magic_prompt` | Oluşturmadan önce istemi ayrıntılı bir yapılandırılmış altyazıya dönüştürür; `"off"` ifadenizi olabildiğince gerçek haliyle korur. Altyazı `final_prompt` olarak döndürülür (varsayılan: `"auto"`). Bu gelişmiş bir ayardır. | COMBO | Evet | `"auto"`<br>`"on"`<br>`"off"` |
| `seed` | Oluşturma için tohum. Metinden görüntüye, istem her çalıştırmada yeniden yazıldığından yalnızca tohumdan yeniden üretilemez; bir görüntüyü yeniden üretmek için `magic_prompt` `"off"` olarak ayarlanmış şekilde aynı tohum ve aynı model, boyut, kalite ve arka plan ayarlarıyla `final_prompt`'unu yeniden kullanın (varsayılan: 42). | INT | Evet | 0 ile 2147483647 arası |

### Ideogram 4.6 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size` | Çıktı boyutu. `"auto"` modelin isteme uygun bir tuval seçmesini sağlar. Bir ön ayar hem piksel boyutunu hem de en-boy oranını sabitler; `(1K)`, `(2K)` ve `(4K)` kademeleri sabit bir uzun kenar yerine piksel bütçesini tanımlar. Aşağıdaki genişlik ve yüksekliği kullanmak için `"custom"` seçin (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(4K) 4096x4096 (1:1)"`<br>`"(4K) 2880x5760 (1:2)"`<br>`"(4K) 5760x2880 (2:1)"`<br>`"(4K) 3328x4992 (2:3)"`<br>`"(4K) 4992x3328 (3:2)"`<br>`"(4K) 3584x4480 (4:5)"`<br>`"(4K) 4480x3584 (5:4)"`<br>`"(4K) 2880x5120 (9:16)"`<br>`"(4K) 5120x2880 (16:9)"`<br>`"(4K) 3200x5120 (5:8)"`<br>`"(4K) 5120x3200 (8:5)"`<br>`"(4K) 3456x4608 (3:4)"`<br>`"(4K) 4608x3456 (4:3)"`<br>`"(4K) 2304x5888 (9:23)"`<br>`"(4K) 5888x2304 (23:9)"`<br>`"(4K) 2496x6656 (3:8)"`<br>`"(4K) 6656x2496 (8:3)"`<br>`"(4K) 2560x6144 (5:12)"`<br>`"(4K) 6144x2560 (12:5)"`<br>`"(4K) 2048x6144 (1:3)"`<br>`"(4K) 6144x2048 (3:1)"`<br>`"custom"` |
| `width` | Özel çıktı genişliği piksel cinsinden, yalnızca `size` `"custom"` olduğunda kullanılır (varsayılan: 2048). | INT | Evet | 256 ile 8192 arası (adım: 32) |
| `height` | Özel çıktı yüksekliği piksel cinsinden, yalnızca `size` `"custom"` olduğunda kullanılır (varsayılan: 2048). | INT | Evet | 256 ile 8192 arası (adım: 32) |
| `quality` | Kalite kademesi. Daha yüksek kademeler daha pahalıdır ve daha uzun sürer (varsayılan: `"medium"`). | COMBO | Evet | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `background` | `"transparent"` görüntüyü alfa kanalıyla döndürür, `"opaque"` katı bir arka planı zorlar, `"auto"` istemi takip eder (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"opaque"`<br>`"transparent"` |

### Ideogram 4.5 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `size` | Çıktı boyutu. `"auto"` modelin isteme uygun bir tuval seçmesini sağlar; bir ön ayar hem piksel boyutunu hem de en-boy oranını sabitler (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1296x3168 (9:22)"`<br>`"(2K) 3168x1296 (22:9)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"(1K) 720x1280 (9:16)"`<br>`"(1K) 1280x720 (16:9)"`<br>`"(1K) 720x1440 (1:2)"`<br>`"(1K) 1440x720 (2:1)"` |
| `quality` | Kalite kademesi. Daha yüksek kademeler daha pahalıdır ve daha uzun sürer (varsayılan: `"medium"`). | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"` |

### Parametre Kısıtlamaları

- **İstem:** en az bir boşluk olmayan karakter ve en fazla 10000 karakter. Kendi JSON altyazınızı sağlarken `magic_prompt`'u `"off"` olarak ayarlayın.
- **Özel boyut (4.6):** genişlik çarpı yükseklik 16.777.216 pikseli (4096x4096) aşmamalıdır, her kenar 256 ile 8192 arasında olmalı ve 32'nin katına yuvarlanmalıdır ve uzun kenar kısa kenarın 6 katını aşmamalıdır.
- **`very_low` kalite (4.6):** 4.194.304 piksel (2048x2048) ile sınırlıdır; daha büyük boyutlar hata verir.
- **Yeniden üretilebilirlik:** `magic_prompt` `"auto"` veya `"on"` olarak ayarlandığında istem her çalıştırmada yeniden yazılır, bu nedenle aynı tohum farklı bir görüntü üretebilir.
- **İçerik güvenliği:** Ideogram'ın içerik güvenliği filtresi oluşturmayı engellerse, düğüm görüntü döndürmek yerine hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Oluşturulan görüntü bir toplu iş olarak. | IMAGE |
| `final_prompt` | Görüntünün oluşturulduğu yapılandırılmış altyazı. Görüntüyü yeniden üretmek için `magic_prompt` `"off"` olarak ayarlanmış ve aynı tohum, model, boyut, kalite ve arka plan ile geri besleyin. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramTextToImageApi/tr.md)

---
**Source fingerprint (SHA-256):** `953fee48c0337e6ded4e72332c27279496eeb9c108c0700c2fa14095855047f1`
