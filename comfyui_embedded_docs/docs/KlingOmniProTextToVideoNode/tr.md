# Kling Omni Metinden Videoya (Pro)

Bu düğüm, bir metin açıklamasından video üretmek için en güncel Kling AI modelini kullanır. İsteminizi uzak bir API'ye gönderir ve üretilen videoyu döndürür. Düğüm; videonun uzunluğunu, şeklini, kalitesini kontrol etmenizi ve hatta çok çekimli storyboard'lar oluşturmanızı sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_name` | Video üretimi için kullanılacak belirli Kling modeli (varsayılan: `"kling-v3-omni"`). | COMBO | Evet | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Video içeriğini tanımlayan bir metin istemi. Hem olumlu hem de olumsuz açıklamalar içerebilir. Storyboard'lar etkinleştirildiğinde yok sayılır. | STRING | Evet | 0 ile 2500 karakter arası |
| `aspect_ratio` | Oluşturulacak videonun şekli veya boyutları. | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | Videonun saniye cinsinden süresi (varsayılan: 5). | INT | Evet | 3 ile 15 saniye arası |
| `resolution` | Videonun kalitesi veya piksel çözünürlüğü (varsayılan: `"1080p"`). | COMBO | Hayır | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `storyboards` | Her biri ayrı istemler ve süreler içeren bir dizi video segmenti oluşturur. o1 modeli için yok sayılır. | DYNAMIC_COMBO | Hayır | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `generate_audio` | Video için ses oluşturulup oluşturulmayacağı (varsayılan: False). | BOOLEAN | Hayır | True / False |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Hayır | 0 ile 2147483647 arası |

### Storyboard Alt Girdileri

`storyboards` parametresi `"disabled"` dışında bir değere ayarlandığında, her storyboard segmenti için aşağıdaki girdiler görünür. Aşağıdaki parametre adlarında `{i}`, seçilen storyboard sayısına kadar 1'den başlayan segment numarasıdır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `storyboard_{i}_prompt` | Storyboard segmenti {i} için istem. Maksimum 512 karakter. | STRING | Evet | 1 ile 512 karakter arası |
| `storyboard_{i}_duration` | Storyboard segmenti {i} için saniye cinsinden süre (varsayılan: 4). | INT | Evet | 1 ile 15 saniye arası |

### Parametre Kısıtları ve Sınırlamalar

- **Modele özgü sınırlamalar:**
  - `kling-video-o1` modeli yalnızca **5 veya 10 saniyelik** süreleri destekler.
  - `kling-video-o1` modeli ses üretimini **desteklemez**.
  - `kling-video-o1` modeli 4k çözünürlüğü **desteklemez**.
  - `kling-video-o1` modeli storyboard'ları **desteklemez**.
- **Storyboard kısıtları:**
  - Storyboard'lar etkinleştirildiğinde `prompt` alanı yok sayılır.
  - Her storyboard, kendi istemini (1 ile 512 karakter arası) ve süresini gerektirir.
  - Tüm storyboard'ların toplam süresi, genel `duration` parametresine tam olarak eşit olmalıdır.
- **İstem gereksinimleri:**
  - Storyboard'lar **devre dışı** olduğunda `prompt` alanı gereklidir (en az 1 karakter).
  - Storyboard'lar **etkin** olduğunda `prompt` alanı boş olabilir (0 karakter).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Sağlanan metin istemine ve ayarlara göre üretilen video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProTextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `d2fbbe7c6aae283eb3fa7f73d788b809098a9a4dd6e8ada54697d43fd5bf10f2`
