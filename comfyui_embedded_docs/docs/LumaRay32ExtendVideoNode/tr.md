# Luma Ray 3.2 Video Uzat

Luma Ray 3.2 Extend Video, önceki bir Luma Ray 3.2 video üretimini, özgün klipten sonra (ileri) veya ondan önce (geriye) yeni bir 5 saniyelik segment oluşturarak sürdürür. Bu klibi uzatmanın başlangıç karesi (ileri) veya bitiş karesi (geriye) olarak kullanmak için daha önceki bir Luma Ray 3.2 düğümünün `generation_id` çıktısını bağlayın. Uzatmalar her zaman 5 saniye uzunluğundadır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `source_generation_id` | Uzatılacak önceki Ray 3.2 videosunun üretim kimliği. Başka bir Luma Ray 3.2 düğümünün `generation_id` çıktısını bağlayın. Varsayılan: "" (boş). Bu değer gereklidir ve boş olmamalıdır. | STRING | Evet | – |
| `direction` | İleri, önceki klipten sonra devam eder; geriye ise ondan önce başa eklenir. İleri, kaynak klibi başlangıç karesi olarak kullanır; geriye ise onu bitiş karesi olarak kullanır. "Forward (continue after)" seçildiğinde `loop` seçeneği eklenir. | DYNAMIC_COMBO | Evet | "Forward (continue after)"<br>"Backward (lead-in before)" |
| `prompt` | Yeni içerik için metin istemi. Varsayılan: "" (boş). 1 ile 6000 karakter arasında olmalıdır. | STRING | Evet | 1 ile 6000 karakter |
| `resolution` | Uzatılmış video segmenti için çıktı çözünürlüğü. Varsayılan: "720p". | COMBO | Evet | "540p"<br>"720p"<br>"1080p" |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum; sonuçlar tohumdan bağımsız olarak deterministik değildir. Varsayılan: 0. | INT | Evet | 0 ile 0xFFFFFFFFFFFFFFFF (18446744073709551615) |

### İleri (sonrasından devam) Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `loop` | Uzatılmış videoyu kesintisiz olarak döngüye alır (yalnızca ileri uzatma). Varsayılan: False. | BOOLEAN | Hayır | True<br>False |

### Geriye (öncesine ekleme) Girdileri

Bu yön ek parametre eklemez.

**Not:** Uzatmalar her zaman 5 saniyedir. `loop` parametresi yalnızca `direction` "Forward (continue after)" olduğunda kullanılabilir; "Backward (lead-in before)" kullanıldığında `loop` seçeneği kullanılamaz. `prompt` 1 ile 6000 karakter arasında olmalıdır. `source_generation_id` gereklidir ve önceki bir Luma Ray 3.2 düğümünün `generation_id` çıktısından bağlanmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Oluşturulan 5 saniyelik uzatılmış video segmenti. | VIDEO |
| `generation_id` | Bu üretim için benzersiz tanımlayıcı; daha fazla uzatma için başka bir Luma Ray 3.2 Extend Video düğümüne bağlanabilir. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ExtendVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `a67ca53d4bcb9f3fd82bc0482b579f5f7fe4bf866f8d83cb922e1082ad320057`
