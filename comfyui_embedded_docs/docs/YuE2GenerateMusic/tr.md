# YuE2 Müzik Oluştur

Bir stil, şarkı sözleri ve bir ABC notasyonundan müzik token'ları ve akustik koşullandırma üretir. Koşullandırmayı ve saniye cinsinden üretilen süreyi döndürür; bu değer Empty YuE2 Latent Audio düğümüne sağlanmalıdır. ABC girdisi boş bırakılırsa, seçilen mod yok sayılır ve otomatik olarak off modu kullanılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip` | Müzik girdilerini token'laştırmak ve kodlamak için kullanılan CLIP modeli. | CLIP | Evet | - |
| `style` | Müzikal stili açıklayan metin. Çok satırlı girdiyi ve dinamik prompt'ları destekler. | STRING | Evet | Çok satırlı metin |
| `lyrics` | Üretilen müzik için şarkı sözleri. Çok satırlı girdiyi ve dinamik prompt'ları destekler. | STRING | Evet | Çok satırlı metin |
| `abc` | ABC üreticisini bağlayın veya düzenlenmiş bir partisyon sağlayın. Otomatik olarak off modunu kullanmak için boş bırakın. varsayılan: "" | STRING | Evet | Çok satırlı metin |
| `seed` | Üretim için rastgele tohum. varsayılan: 0 | INT | Evet | 0 - 18446744073709551615 |
| `mode` | full: melodi ve akorları üretir; melody: yalnızca melodi üretir, cover'lar için önerilir. varsayılan: "full" | COMBO | Evet | "full"<br>"melody" |
| `max_duration` | Saniye cinsinden maksimum süre. Uzun prompt'lar için otomatik olarak azaltılır; üretim daha erken durabilir. varsayılan: 360.0 | FLOAT | Evet | 0.04 - 900.0 |
| `temperature` | Üretim için örnekleme sıcaklığı. varsayılan: 1.0 (gelişmiş) | FLOAT | Evet | 0.0 - 5.0 |
| `top_p` | Nucleus örnekleme olasılık eşiği. varsayılan: 0.95 (gelişmiş) | FLOAT | Evet | 0.01 - 1.0 |
| `top_k` | Top-k örnekleme sınırı. varsayılan: 100 (gelişmiş) | INT | Evet | 1 - 32768 |
| `repetition_penalty` | Yinelenen token'lara uygulanan ceza. varsayılan: 1.2 (gelişmiş) | FLOAT | Evet | 0.01 - 10.0 |

Not: `abc` boşsa veya yalnızca boşluk içeriyorsa, `mode` seçimi yok sayılır ve otomatik olarak off modu kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `CONDITIONING` | Müzik token'larından üretilen akustik koşullandırma. | CONDITIONING |
| `seconds` | Üretilen ses süresi saniye cinsinden. Bu değeri Empty YuE2 Latent Audio düğümüne sağlayın. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/YuE2GenerateMusic/tr.md)

---
**Source fingerprint (SHA-256):** `54f5d46cf083726bdf97c86e5683b2727840f75bb553bddf9525cfbf5affa44c`
