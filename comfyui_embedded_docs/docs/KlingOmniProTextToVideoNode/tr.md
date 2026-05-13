> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProTextToVideoNode/tr.md)

Bu düğüm, bir metin açıklamasından video oluşturmak için en son Kling AI modelini kullanır. İsteğinizi uzak bir API'ye gönderir ve oluşturulan videoyu döndürür. Düğüm, videonun uzunluğunu, şeklini, kalitesini kontrol etmenize ve hatta çok çekimli storyboard'lar oluşturmanıza olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Evet | `"kling-v3-omni"`<br>`"kling-video-o1"` | Video oluşturma için kullanılacak belirli Kling modeli (varsayılan: `"kling-v3-omni"`). |
| `prompt` | STRING | Evet | 0 ila 2500 karakter | Video içeriğini tanımlayan bir metin istemi. Hem olumlu hem de olumsuz açıklamalar içerebilir. Storyboard'lar etkinleştirildiğinde yok sayılır. |
| `aspect_ratio` | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"` | Oluşturulacak videonun şekli veya boyutları. |
| `duration` | INT | Evet | 3 ila 15 saniye | Videonun saniye cinsinden uzunluğu (varsayılan: 5). |
| `resolution` | COMBO | Hayır | `"4k"`<br>`"1080p"`<br>`"720p"` | Videonun kalitesi veya piksel çözünürlüğü (varsayılan: `"1080p"`). |
| `hikaye_tahtaları` | DYNAMIC_COMBO | Hayır | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` | Bireysel istemler ve sürelerle bir dizi video segmenti oluşturun. o1 modeli için yok sayılır. |
| `ses_oluştur` | BOOLEAN | Hayır | True / False | Video için ses oluşturulup oluşturulmayacağı (varsayılan: False). |
| `seed` | INT | Hayır | 0 ila 2147483647 | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0). |

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

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Sağlanan metin istemine ve ayarlara göre oluşturulan video. |

---
**Source fingerprint (SHA-256):** `2f867e0bd2e7b0ec901a9ad8d2adcfe712ed479c1613b80f86af3a20863e9f4c`
