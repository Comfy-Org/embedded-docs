# Kling 3.0 Video

Bu düğüm, Kling V3 modelini kullanarak videolar üretir. Metinden videoya modunu (bir metin açıklamasından video oluşturma) ve görüntüden videoya modunu (mevcut bir görüntüyü canlandırma) destekler. Ayrıca, her bölüm için ayrı istemlerle (storyboard'lar) çok bölümlü videolar oluşturma ve isteğe bağlı olarak eşlik eden ses üretme gibi gelişmiş özellikler sunar.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `çoklu çekim` | Her biri için ayrı istemler ve süreler içeren bir dizi video segmenti üretir. Bir storyboard seçeneğine ayarlandığında, her storyboard için ek istem ve süre girdileri görünür. | DYNAMIC_COMBO | Evet | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `model` | Model ve üretim ayarları. Bir model seçmek, çözünürlük ve en-boy oranı alt parametrelerini ortaya çıkarır. | DYNAMIC_COMBO | Evet | `"kling-v3"`<br>`"kling-3.0-turbo"` |
| `ses oluştur` | Etkinleştirildiğinde, düğüm video için ses üretir. Not: `"kling-3.0-turbo"` her zaman doğal ses üretir, bu nedenle bu anahtar o model için yok sayılır. Varsayılan: True. | BOOLEAN | Evet | True<br>False |
| `tohum` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. Varsayılan: 0. | INT | Evet | 0 ile 2147483647 |
| `başlangıç karesi` | İsteğe bağlı başlangıç karesi görüntüsü. Bağlandığında görüntüden videoya moduna geçilir. | IMAGE | Hayır | - |

### kling-v3 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `çözünürlük` | Üretilen video için çözünürlük. Varsayılan: `"1080p"`. | COMBO | Evet | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `en boy oranı` | Üretilen video için en-boy oranı. Görüntüden videoya modunda yok sayılır. | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"` |

### kling-3.0-turbo Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `çözünürlük` | Üretilen video için çözünürlük. Varsayılan: `"720p"`. | COMBO | Evet | `"1080p"`<br>`"720p"` |
| `en boy oranı` | Üretilen video için en-boy oranı. Görüntüden videoya modunda yok sayılır. | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"` |

### Çoklu Çekim Girdileri

**`multi_shot` `"disabled"` olarak ayarlandığında:**

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video için ana metin açıklaması. 1 ila 2500 karakter arasında olmalıdır. | STRING | Evet | 1 ile 2500 characters |
| `negative_prompt` | Videoda ne olmaması gerektiğini tanımlayan metin. Boş bırakılabilir. | STRING | Hayır | - |
| `duration` | Videonun saniye cinsinden uzunluğu. Varsayılan: 5. | INT | Evet | 3 ile 15 |

**`multi_shot` bir storyboard seçeneğine ayarlandığında (örn. `"3 storyboards"`):**

Her storyboard segmenti N için (1'den seçilen storyboard sayısına kadar) aşağıdaki girdiler görünür:

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `storyboard_N_prompt` | Storyboard segmenti N için istem. En fazla 512 karakter. | STRING | Evet | 1 ile 512 characters |
| `storyboard_N_duration` | Storyboard segmenti N için saniye cinsinden süre. Varsayılan: 4. | INT | Evet | 1 ile 15 |

**Kısıtlar ve davranış:**

- `start_frame` bağlı değilken metinden videoya modu kullanılır; `start_frame` bağlıyken görüntüden videoya modu kullanılır. Görüntüden videoya modunda `model.aspect_ratio` yok sayılır ve giriş görüntüsü en az 300x300 piksel olmalı ve en-boy oranı 1:2.5 ile 2.5:1 arasında olmalıdır.
- Storyboard modunda ana `prompt` ve `negative_prompt` kullanılmaz. Tüm storyboard sürelerinin toplamı 3 ila 15 saniye arasında olmalıdır.
- `negative_prompt` yalnızca `kling-v3` ile kullanılır; `kling-3.0-turbo` seçildiğinde yok sayılır.
- `kling-v3` için her storyboard API'ye ayrı bir segment olarak gönderilir. `kling-3.0-turbo` için storyboard istemleri ve süreleri tek bir çoklu çekim isteminde birleştirilir.
- `kling-3.0-turbo` için `generate_audio` yok sayılır çünkü bu model her zaman doğal ses üretir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Üretilen video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `2863d7a971a1978b6009e5321ed2112a9c04809281acd5f65d85ab72c4b49f08`
