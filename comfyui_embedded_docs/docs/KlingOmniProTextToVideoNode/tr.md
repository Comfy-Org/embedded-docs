# Kling Omni Metinden Videoya (Pro)

Bu düğüm, bir metin açıklamasından video oluşturmak için en son Kling AI modelini kullanır. İsteminizi uzak bir API'ye gönderir ve oluşturulan videoyu döndürür. Düğüm, videonun uzunluğunu, şeklini, kalitesini kontrol etmenize ve hatta çok çekimli storyboard'lar oluşturmanıza olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_name` | Video oluşturma için kullanılacak belirli Kling modeli (varsayılan: `"kling-v3-omni"`). | COMBO | Evet | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Video içeriğini tanımlayan metin istemi. Hem olumlu hem olumsuz açıklamalar içerebilir. Storyboard'lar etkinleştirildiğinde yok sayılır. | STRING | Evet | 0 ila 2500 karakter |
| `aspect_ratio` | Oluşturulacak videonun şekli veya boyutları. | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | Videonun saniye cinsinden uzunluğu (varsayılan: 5). | INT | Evet | 3 ila 15 saniye |
| `resolution` | Videonun kalitesi veya piksel çözünürlüğü (varsayılan: `"1080p"`). Dahili olarak standart, pro veya 4k kaliteye eşlenir. | COMBO | Hayır | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `hikaye_tahtaları` | Her biri ayrı istemlere ve sürelere sahip bir dizi video bölümü oluşturun. o1 modeli için yok sayılır. | DYNAMIC_COMBO | Hayır | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `ses_oluştur` | Video için ses oluşturulup oluşturulmayacağı (varsayılan: False). | BOOLEAN | Hayır | True / False |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Hayır | 0 ila 2147483647 |

### Storyboard Alt Girdileri

`storyboards` değeri `"disabled"` dışında bir değere ayarlandığında, her storyboard bölümü için aşağıdaki girdiler görünür. Aşağıdaki parametre adlarında `{i}`, 1'den seçilen storyboard sayısına kadar olan bölüm numarasıdır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `storyboard_{i}_prompt` | Storyboard bölümü {i} için istem. En fazla 512 karakter. | STRING | Evet | 1 ila 512 karakter |
| `storyboard_{i}_duration` | Storyboard bölümü {i} için saniye cinsinden süre (varsayılan: 4). | INT | Evet | 1 ila 15 saniye |

### Parametre Kısıtlamaları ve Sınırlamaları

- **Modele özgü sınırlamalar:**
  - `kling-video-o1` modeli yalnızca **5 veya 10 saniyelik** süreleri destekler.
  - `kling-video-o1` modeli ses oluşturmayı **desteklemez**.
  - `kling-video-o1` modeli 4k çözünürlüğü **desteklemez**.
  - `kling-video-o1` modeli storyboard'ları **desteklemez**.
- **Storyboard kısıtlamaları:**
  - Storyboard'lar etkinleştirildiğinde `prompt` alanı yok sayılır.
  - Her storyboard kendi istemini (1 ila 512 karakter) ve süresini gerektirir.
  - Tüm storyboard'ların toplam süresi, genel `duration` parametresine tam olarak eşit olmalıdır.
- **İstem gereksinimleri:**
  - Storyboard'lar **devre dışıyken** `prompt` alanı gereklidir (minimum 1 karakter).
  - Storyboard'lar **etkinken** `prompt` alanı boş olabilir (0 karakter).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Sağlanan metin istemi ve ayarlara göre oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProTextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `d2fbbe7c6aae283eb3fa7f73d788b809098a9a4dd6e8ada54697d43fd5bf10f2`
