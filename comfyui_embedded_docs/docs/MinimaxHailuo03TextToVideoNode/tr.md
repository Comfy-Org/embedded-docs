# MiniMax H3 Metinden Videoya

Bu düğüm, MiniMax H3 model ailesini (MiniMax H3, MiniMax H3 Max ve MiniMax H3 Max Turbo) kullanarak bir metin isteminden video oluşturur. Modeli seçer, bir metin istemi girersiniz ve çözünürlük, en-boy oranı ve süre gibi ayarları düzenlersiniz. Düğüm isteği MiniMax API'sine gönderir, oluşturma görevinin tamamlanmasını bekler ve ortaya çıkan videoyu döndürür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video oluşturmak için kullanılacak model (varsayılan: "MiniMax H3"). Bir model seçmek, aşağıdaki bölümlerde açıklanan modele özgü ayarları da gösterir. | DYNAMIC_COMBO | Evet | "MiniMax H3"<br>"MiniMax H3 Max"<br>"MiniMax H3 Max Turbo" |
| `seed` | Rastgele tohum. Aynı tohumla yapılan aynı istek benzer sonuçlar verir, ancak aynı sonuçlar garanti edilmez (varsayılan: 42). | INT | Evet | 0 ile 4294967295 |
| `watermark` | Videoya AIGC filigranı eklenip eklenmeyeceği (varsayılan: false). Etkinleştirildiğinde yalnızca "MiniMax H3" modeli desteklenir. | BOOLEAN | Hayır | true<br>false |

### MiniMax H3 Girdileri

Bu ayarlar, "MiniMax H3" modeli seçildiğinde görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi. En az bir boşluk dışı karakter içermelidir. | STRING | Evet | Herhangi bir metin |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | "768P"<br>"2K" |
| `ratio` | Çıktı videosunun en-boy oranı (varsayılan: "16:9"). | COMBO | Evet | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Çıktı videosunun saniye cinsinden süresi (4-15) (varsayılan: 5). | INT | Evet | 4 ile 15 |

### MiniMax H3 Max ve MiniMax H3 Max Turbo Girdileri

Bu ayarlar "MiniMax H3 Max" ve "MiniMax H3 Max Turbo" modelleri tarafından paylaşılır ve bu modellerden biri seçildiğinde görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi. En az bir boşluk dışı karakter içermelidir ve 50.000 karaktere kadar olabilir. | STRING | Evet | En fazla 50000 karakter |
| `resolution` | Çıktı videosunun çözünürlüğü (varsayılan: "768P"). | COMBO | Evet | "480P"<br>"768P" |
| `ratio` | Çıktı videosunun en-boy oranı (varsayılan: "16:9"). | COMBO | Evet | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Çıktı videosunun saniye cinsinden süresi (5-15) (varsayılan: 5). | INT | Evet | 5 ile 15 |
| `prompt_expansion_mode` | Oluşturmadan önce istemi yeniden yazmak için ne kadar çaba harcanacağı (varsayılan: "balanced"). | COMBO | Evet | "balanced"<br>"quality" |

### Notlar

- Tüm modeller için istem en az bir boşluk dışı karakter içermelidir.
- `watermark` ayarı yalnızca "MiniMax H3" tarafından desteklenir. "MiniMax H3 Max" veya "MiniMax H3 Max Turbo" ile etkinleştirilmesi hataya neden olur.
- "MiniMax H3 Max" ve "MiniMax H3 Max Turbo" modelleri istemi 50.000 karakterle sınırlar.
- Çözünürlük ve süre sınırları seçilen modele bağlıdır: "MiniMax H3" "768P" ve "2K" çözünürlüğü ile 4-15 saniyelik videoları destekler; "MiniMax H3 Max" ve "MiniMax H3 Max Turbo" ise "480P" ve "768P" çözünürlüğü ile 5-15 saniyelik videoları destekler.
- Bu düğüm için gösterilen tahmini fiyat, seçilen model, çözünürlük ve süreye göre hesaplanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Sağlanan metin isteminden oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03TextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `4d3de190d18de4370aff878279755e881841d2ada28320a7c1d7c52061071c05`
