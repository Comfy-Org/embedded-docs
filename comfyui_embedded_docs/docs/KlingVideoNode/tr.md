# Kling 3.0 Video

Bu düğüm, Kling V3 modeliyle video üretir. Metinden videoya (bir metin açıklamasından video oluşturma) ve görüntüden videoya (mevcut bir görüntüyü canlandırma) özelliklerini destekler. Ayrıca storyboard istemlerini kullanarak çok segmentli videolar oluşturabilir ve isteğe bağlı olarak ses üretebilir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `multi_shot` | Her biri kendi istemi ve süresine sahip bir dizi video segmenti üretir. Bir storyboard seçeneğine ayarlandığında, her storyboard'un istemi ve süresi için ek girdiler görünür. | DYNAMIC_COMBO | Evet | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `generate_audio` | Etkinleştirildiğinde düğüm, video için ses üretir. Not: `"kling-3.0-turbo"` her zaman yerel ses üretir, bu nedenle o model için ses geçişi yok sayılır. Varsayılan True'dur. | BOOLEAN | Evet | True<br>False |
| `model` | Model ve üretim ayarları. Bir model seçildiğinde çözünürlük ve en-boy oranı alt parametreleri görünür. | DYNAMIC_COMBO | Evet | `"kling-v3"`<br>`"kling-3.0-turbo"` |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. Varsayılan 0'dır. | INT | Evet | 0 ila 2147483647 |
| `start_frame` | İsteğe bağlı başlangıç kare görüntüsü. Bağlandığında görüntüden videoya moduna geçer. | IMAGE | Hayır | - |

### kling-v3 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model.resolution` | Üretilen video için çözünürlük. Varsayılan `"1080p"`. | COMBO | Evet | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `model.aspect_ratio` | Üretilen video için en-boy oranı. Görüntüden videoya modunda yok sayılır. | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"` |

### kling-3.0-turbo Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model.resolution` | Üretilen video için çözünürlük. Varsayılan `"720p"`. | COMBO | Evet | `"1080p"`<br>`"720p"` |
| `model.aspect_ratio` | Üretilen video için en-boy oranı. Görüntüden videoya modunda yok sayılır. | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"` |

### Çoklu Çekim Girdileri

**`multi_shot` `"disabled"` olarak ayarlandığında:**

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video için ana metin açıklaması. 1 ile 2500 karakter arasında olmalıdır. | STRING | Evet | 1 ila 2500 karakter |
| `negative_prompt` | Videoda görünmemesi gerekenleri açıklayan metin. Boş bırakılabilir. | STRING | Hayır | - |
| `duration` | Videonun saniye cinsinden uzunluğu. Varsayılan 5'tir. | INT | Evet | 3 ila 15 |

**`multi_shot` bir storyboard seçeneğine ayarlandığında (örn. `"3 storyboards"`):**

Her storyboard segmenti N için (1'den seçili storyboard sayısına kadar) aşağıdaki girdiler görünür:

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `storyboard_N_prompt` | Storyboard segmenti N için istem. En fazla 512 karakter. | STRING | Evet | 1 ila 512 karakter |
| `storyboard_N_duration` | Storyboard segmenti N için saniye cinsinden süre. Varsayılan 4'tür. | INT | Evet | 1 ila 15 |

**Kısıtlamalar ve davranış:**

- `start_frame` bağlı değilken metinden videoya modu kullanılır; `start_frame` bağlıyken görüntüden videoya modu kullanılır. Görüntüden videoya modunda `model.aspect_ratio` yok sayılır ve giriş görüntüsü en az 300x300 piksel olmalı ve en-boy oranı 1:2.5 ile 2.5:1 arasında olmalıdır.
- Storyboard modunda ana `prompt` ve `negative_prompt` kullanılmaz. Tüm storyboard sürelerinin toplamı 3 ile 15 saniye arasında olmalıdır.
- `negative_prompt` yalnızca `kling-v3` ile kullanılır; `kling-3.0-turbo` seçildiğinde yok sayılır.
- `kling-v3` için her storyboard API'ye ayrı bir segment olarak gönderilir. `kling-3.0-turbo` için storyboard istemleri ve süreleri tek bir çoklu çekim isteminde birleştirilir.
- `kling-3.0-turbo` için `generate_audio` yok sayılır çünkü bu model her zaman yerel ses üretir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Üretilen video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `2863d7a971a1978b6009e5321ed2112a9c04809281acd5f65d85ab72c4b49f08`
