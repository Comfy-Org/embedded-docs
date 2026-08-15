# Kling 3.0 Video

Bu düğüm, Kling V3 modelini kullanarak videolar oluşturur. Metinden videoya modunu destekler; bu modda bir metin açıklamasından video oluşturulur. Ayrıca görüntüden videoya modu da vardır; bu modda mevcut bir görüntü animasyonlandırılır. Bunlara ek olarak, her bölüm için ayrı promptlar içeren çok parçalı videolar (storyboard) oluşturma ve isteğe bağlı olarak eşlik eden ses üretme gibi gelişmiş özellikler sunar.

## Girdiler

### Genel Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `çoklu çekim` | Ayrı promptlar ve sürelerle bir dizi video bölümü oluşturun. Bir storyboard seçeneğine ayarlandığında, her storyboard'un promptu ve süresi için ek girdiler görünür. | COMBO | Evet | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `model` | Model ve üretim ayarları. Bir model seçmek, onun `model.resolution` ve `model.aspect_ratio` alt parametrelerini ortaya çıkarır. | COMBO | Evet | `"kling-v3"`<br>`"kling-3.0-turbo"` |
| `ses oluştur` | Etkinleştirildiğinde, düğüm video için ses üretir. Not: `"kling-3.0-turbo"` her zaman yerel ses üretir, bu nedenle bu anahtar o model için yok sayılır. Varsayılan True'dur. | BOOLEAN | Evet | True<br>False |
| `tohum` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. Varsayılan 0'dır. | INT | Evet | 0 ile 2147483647 |
| `başlangıç karesi` | İsteğe bağlı başlangıç karesi görüntüsü. Bağlandığında görüntüden videoya moduna geçer. | IMAGE | Hayır | - |

### kling-v3 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `çözünürlük` | Oluşturulan video için çözünürlük. Varsayılan `"1080p"`dir. | COMBO | Evet | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `en boy oranı` | Oluşturulan video için en-boy oranı. Görüntüden videoya modunda yok sayılır. | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"` |

### kling-3.0-turbo Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `çözünürlük` | Oluşturulan video için çözünürlük. Varsayılan `"720p"`dir. | COMBO | Evet | `"1080p"`<br>`"720p"` |
| `en boy oranı` | Oluşturulan video için en-boy oranı. Görüntüden videoya modunda yok sayılır. | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"` |

### Çoklu Çekim Girdileri

**`multi_shot` `"disabled"` olarak ayarlandığında:**

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video için ana metin açıklaması. 1 ile 2500 karakter arasında olmalıdır. | STRING | Evet | 1 ile 2500 karakter |
| `negative_prompt` | Videoda ne olmaması gerektiğini açıklayan metin. Boş bırakılabilir. | STRING | Hayır | - |
| `duration` | Videonun saniye cinsinden uzunluğu. Varsayılan 5'tir. | INT | Evet | 3 ile 15 |

**`multi_shot` bir storyboard seçeneğine ayarlandığında (örn. `"3 storyboards"`):**

Her storyboard bölümü N için (1'den seçilen storyboard sayısına kadar) aşağıdaki girdiler görünür:

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `storyboard_N_prompt` | Storyboard bölümü N için prompt. En fazla 512 karakter. | STRING | Evet | 1 ile 512 karakter |
| `storyboard_N_duration` | Storyboard bölümü N için saniye cinsinden süre. Varsayılan 4'tür. | INT | Evet | 1 ile 15 |

**Kısıtlamalar ve davranış:**

- `start_frame` bağlı değilken metinden videoya modu kullanılır; `start_frame` bağlıyken görüntüden videoya modu kullanılır. Görüntüden videoya modunda `model.aspect_ratio` yok sayılır ve giriş görüntüsü en az 300x300 piksel olmalı ve en-boy oranı 1:2.5 ile 2.5:1 arasında olmalıdır.
- Storyboard modunda ana `prompt` ve `negative_prompt` kullanılmaz. Tüm storyboard sürelerinin toplamı 3 ile 15 saniye arasında olmalıdır.
- `kling-v3` için her storyboard API'ye ayrı bir bölüm olarak gönderilir. `kling-3.0-turbo` için storyboard promptları ve süreleri tek bir çoklu çekim promptunda birleştirilir.
- `kling-3.0-turbo` için `generate_audio` yok sayılır çünkü bu model her zaman yerel ses üretir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `2863d7a971a1978b6009e5321ed2112a9c04809281acd5f65d85ab72c4b49f08`
