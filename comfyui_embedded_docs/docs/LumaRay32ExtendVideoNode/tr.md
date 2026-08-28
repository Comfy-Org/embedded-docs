# Luma Ray 3.2 Video Uzat

Luma Ray 3.2 Extend Video, önceki bir Luma Ray 3.2 video üretimini, orijinal klibin sonrasına (forward) veya öncesine (backward) 5 saniyelik yeni bir bölüm ekleyerek sürdürür. Önceki bir Luma Ray 3.2 düğümünün `generation_id` çıktısını bağlayarak bu klibi uzatmanın başlangıç karesi (forward) veya bitiş karesi (backward) olarak kullanın.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `direction` | Forward, önceki klipten sonra devam eder; backward, ondan önceye eklenir. Forward, kaynak klibi başlangıç karesi olarak kullanır; backward ise onu bitiş karesi olarak kullanır. "Forward (continue after)" seçildiğinde `loop` seçeneği eklenir. | DYNAMIC_COMBO | Evet | "Forward (continue after)"<br>"Backward (lead-in before)" |
| `source_generation_id` | Uzatılacak önceki Ray 3.2 videosunun Üretim Kimliği. Başka bir Luma Ray 3.2 düğümünün `generation_id` çıktısını bağlayın. Bu değer zorunludur ve boş olmamalıdır. | STRING | Evet | – |
| `prompt` | Yeni içerik için metin istemi. 1 ile 6000 karakter arasında olmalıdır. | STRING | Evet | 1 ila 6000 karakter |
| `resolution` | Uzatılmış video bölümü için çıktı çözünürlüğü. Varsayılan: "720p". | COMBO | Evet | "540p"<br>"720p"<br>"1080p" |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; sonuçlar tohum değerinden bağımsız olarak belirleyici değildir. Varsayılan: 0. | INT | Evet | 0 ila 0xFFFFFFFFFFFFFFFF |

### Forward (continue after) Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `loop` | Uzatılmış videoyu kesintisiz olarak döngüye al (yalnızca ileri uzatma). Varsayılan: False. | BOOLEAN | Hayır | True<br>False |

### Backward (lead-in before) Girdileri

Bu yön ek parametre eklemez.

**Not:** Uzantılar her zaman 5 saniyedir. `loop` parametresi yalnızca `direction` "Forward (continue after)" olduğunda kullanılabilir; "Backward (lead-in before)" kullanıldığında `loop` seçeneği kullanılamaz. `prompt` 1 ila 6000 karakter arasında olmalıdır. `source_generation_id` zorunludur ve önceki bir Luma Ray 3.2 düğümünün `generation_id` çıktısından bağlanmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Oluşturulan 5 saniyelik uzatılmış video bölümü. | VIDEO |
| `generation_id` | Bu üretim için benzersiz tanımlayıcı; daha fazla uzatma için başka bir Luma Ray 3.2 Extend Video düğümüne bağlanabilir. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ExtendVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `a67ca53d4bcb9f3fd82bc0482b579f5f7fe4bf866f8d83cb922e1082ad320057`
