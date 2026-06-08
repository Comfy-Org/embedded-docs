Bu düğüm, bir metin açıklamasından video oluşturmak için en son Kling AI modelini kullanır. İsteğinizi uzak bir API'ye gönderir ve oluşturulan videoyu döndürür. Düğüm, videonun uzunluğunu, şeklini, kalitesini kontrol etmenize ve hatta çok çekimli storyboard'lar oluşturmanıza olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model_name` | Video oluşturma için kullanılacak belirli Kling modeli (varsayılan: `"kling-v3-omni"`). | COMBO | Evet | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Video içeriğini tanımlayan bir metin istemi. Hem olumlu hem de olumsuz açıklamalar içerebilir. Storyboard'lar etkinleştirildiğinde yok sayılır. | STRING | Evet | 0 ila 2500 karakter |
| `aspect_ratio` | Oluşturulacak videonun şekli veya boyutları. | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | Videonun saniye cinsinden uzunluğu (varsayılan: 5). | INT | Evet | 3 ila 15 saniye |
| `resolution` | Videonun kalitesi veya piksel çözünürlüğü (varsayılan: `"1080p"`). | COMBO | Hayır | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `hikaye_tahtaları` | Bireysel istemler ve sürelerle bir dizi video segmenti oluşturun. o1 modeli için yok sayılır. | DYNAMIC_COMBO | Hayır | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `ses_oluştur` | Video için ses oluşturulup oluşturulmayacağı (varsayılan: False). | BOOLEAN | Hayır | True / False |
| `seed` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Hayır | 0 ila 2147483647 |

### Parametre Kısıtlamaları ve Sınırlamaları

- **Modele özgü sınırlamalar:**
  - `kling-video-o1` modeli yalnızca **5 veya 10 saniyelik** süreleri destekler.
  - `kling-video-o1` modeli ses oluşturmayı **desteklemez**.
  - `kling-video-o1` modeli 4k çözünürlüğü **desteklemez**.
  - `kling-video-o1` modeli storyboard'ları **desteklemez**.
- **Storyboard kısıtlamaları:**
  - Storyboard'lar etkinleştirildiğinde, `prompt` alanı yok sayılır.
  - Her storyboard kendi istemini (1 ila 512 karakter) ve süresini gerektirir.
  - Tüm storyboard'ların toplam süresi, genel `duration` parametresine tam olarak eşit olmalıdır.
- **İstem gereksinimleri:**
  - Storyboard'lar **devre dışı** bırakıldığında, `prompt` alanı zorunludur (minimum 1 karakter).
  - Storyboard'lar **etkinleştirildiğinde**, `prompt` alanı boş olabilir (0 karakter).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Sağlanan metin istemine ve ayarlara göre oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProTextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `2f867e0bd2e7b0ec901a9ad8d2adcfe712ed479c1613b80f86af3a20863e9f4c`
