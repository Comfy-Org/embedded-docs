# YuE2 Müzik Oluştur

Bir stil, şarkı sözleri ve ABC notasyonundan müzik token'ları ve akustik koşullandırma üretir. Koşullandırmayı ve saniye cinsinden üretilen süreyi döndürür; bu değer Empty YuE2 Latent Audio düğümüne sağlanmalıdır. ABC girdisi boş bırakılırsa, seçilen mod yok sayılır ve otomatik olarak off modu kullanılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|-------|
| `clip` | Müzik girdilerini tokenize etmek ve kodlamak için kullanılan CLIP modeli. | CLIP | Evet | - |
| `stil` | Müzikal stili tanımlayan metin. Çok satırlı girdiyi ve dinamik istemleri destekler. | STRING | Evet | Çok satırlı metin |
| `şarkı sözleri` | Üretilen müzik için şarkı sözleri. Çok satırlı girdiyi ve dinamik istemleri destekler. | STRING | Evet | Çok satırlı metin |
| `abc` | ABC oluşturucuyu bağlayın veya düzenlenmiş bir partisyon sağlayın. Otomatik olarak off modunu kullanmak için boş bırakın. varsayılan: "" | STRING | Evet | Çok satırlı metin |
| `tohum` | Üretim için rastgele tohum. varsayılan: 0 | INT | Evet | 0 ile 18446744073709551615 arası |
| `mod` | full: melodi ve akorları üretir; melody: yalnızca melodi üretir, cover'lar için önerilir. varsayılan: "full" | COMBO | Evet | "full"<br>"melody" |
| `max_duration` | Saniye cinsinden maksimum süre. Uzun istemlerde otomatik olarak azaltılır; üretim daha erken durabilir. varsayılan: 360.0 | FLOAT | Evet | 0.04 ile 900.0 arası |
| `sıcaklık` | Üretim için örnekleme sıcaklığı. varsayılan: 1.0 (gelişmiş) | FLOAT | Evet | 0.0 ile 5.0 arası |
| `top_p` | Nucleus örnekleme olasılık eşiği. varsayılan: 0.95 (gelişmiş) | FLOAT | Evet | 0.01 ile 1.0 arası |
| `top_k` | Top-k örnekleme sınırı. varsayılan: 100 (gelişmiş) | INT | Evet | 1 ile 32768 arası |
| `repetition_penalty` | Tekrarlanan token'lara uygulanan ceza. varsayılan: 1.2 (gelişmiş) | FLOAT | Evet | 0.01 ile 10.0 arası |
| `cfg_scale` | Stil ve şarkı sözleri için otoregresif yönlendirme. 1.0, ABC iş akışıyla eşleşecek şekilde CFG'yi devre dışı bırakır. Orijinal off modu yönlendirmesiyle eşleşmek için 1.01 kullanın. varsayılan: 1.0 (gelişmiş, isteğe bağlı) | FLOAT | Hayır | 0.0 ile 100.0 arası |

Not: Eğer `abc` boşsa veya yalnızca boşluk karakterleri içeriyorsa, `mode` seçimi yok sayılır ve otomatik olarak off modu kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-----------|-----------|
| `CONDITIONING` | Müzik token'larından üretilen akustik koşullandırma. | CONDITIONING |
| `seconds` | Üretilen sesin saniye cinsinden süresi. Bu değeri Empty YuE2 Latent Audio düğümüne sağlayın. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/YuE2GenerateMusic/tr.md)

---
**Source fingerprint (SHA-256):** `5a88e185d2998c51acff7f0c76c8c35ca30b80b88cb541d97f9ab91566b5a3ed`
