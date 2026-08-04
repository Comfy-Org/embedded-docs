# LumaRay32ExtendVideoNode

Luma Ray 3.2 Extend Video, önceki bir Luma Ray 3.2 video üretimini, orijinal klibin sonrasına (ileri) veya öncesine (geri) yeni bir 5 saniyelik bölüm oluşturarak devam ettirir. Daha önceki bir Luma Ray 3.2 düğümünün `generation_id` çıktısını bağlayarak bu klibi uzantının başlangıç karesi (ileri) veya bitiş karesi (geri) olarak kullanın.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `source_generation_id` | Uzatılacak önceki Ray 3.2 videosunun üretim kimliği. Başka bir Luma Ray 3.2 düğümünün `generation_id` çıktısını bağlayın. Bu değer zorunludur ve boş olmamalıdır. | STRING | Evet | - |
| `direction` | İleri, önceki klipten sonra devam eder; geri, ondan önceye eklenir. "Forward (continue after)" seçildiğinde `loop` seçeneği de eklenir. | COMBO | Evet | "İleri (sonrasından devam et)"<br>"Geri (öncesine ekle)" |
| `loop` | Uzatılmış videoyu kesintisiz döngüye alır (yalnızca ileri uzatma). Yalnızca `direction` "Forward (continue after)" olduğunda kullanılabilir. Varsayılan: False. | BOOLEAN | Hayır | Doğru<br>Yanlış |
| `prompt` | Yeni içerik için metin istemi. 1 ile 6000 karakter arasında olmalıdır. | STRING | Evet | - |
| `resolution` | Uzatılmış video bölümü için çıktı çözünürlüğü. Varsayılan: "720p". | COMBO | Evet | "540p"<br>"720p"<br>"1080p" |
| `seed` | Tekrarlanabilir oluşturma sonuçları için rastgele tohum değeri. | INT | Evet | - |

**Not:** `loop` parametresi yalnızca `direction` "İleri (sonrasından devam et)" olarak ayarlandığında kullanılabilir. "Geri (öncesine ekle)" kullanıldığında döngü seçeneği mevcut değildir. `prompt` 1 ile 6000 karakter arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `generation_id` | Oluşturulan 5 saniyelik uzatılmış video bölümü. | VIDEO |
| `generation_id` | Bu oluşturma için benzersiz tanımlayıcıdır. Daha fazla uzatma için başka bir Luma Ray 3.2 Videoyu Uzat düğümüne bağlanabilir. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ExtendVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `a67ca53d4bcb9f3fd82bc0482b579f5f7fe4bf866f8d83cb922e1082ad320057`
