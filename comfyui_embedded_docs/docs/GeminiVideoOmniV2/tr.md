# Google Gemini Omni (Video)

Google Gemini Omni (Video), Google'ın Gemini Omni Flash modellerini kullanarak bir metin isteminden sesli video üretir. Sonucu yönlendirmek veya mevcut görüntüleri düzenlemek için isteğe bağlı olarak referans görseller ve/veya videolar ekleyebilirsiniz. İstenen süreyi (3-10 saniye) doğrudan istemde belirtin.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Videoyu üretmek için kullanılan Gemini video modeli. | DYNAMIC_COMBO | Evet | "Omni Flash 1.1"<br>"Omni Flash" |

### Omni Flash 1.1 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Üretilecek videoyu veya ekli bir videoya uygulanacak düzenlemeyi açıklayın. Süreyi doğrudan istemde belirtin, örn. "6 saniyelik klip" veya 'extend' görevi için "5 saniye uzat"; üretilen süre 3-10 saniye olabilir ve varsayılan 10 saniyedir. Çıktı ses içerir. (varsayılan: "") | STRING | Evet | - |
| `resolution` | Çıktı çözünürlüğü. (varsayılan: "720p") | COMBO | Evet | "360p"<br>"720p"<br>"1080p"<br>"4k" |
| `aspect_ratio` | Çıktı en-boy oranı: 16:9 (yatay) veya 9:16 (dikey). 'edit' ve 'extend' görevleri bunun yerine girdi videosunun en-boy oranını korur. (varsayılan: "16:9") | COMBO | Evet | "16:9"<br>"9:16" |
| `task_type` | İstem ve ekli medyayla ne yapılacağı. 'auto' ile model karar verir. 'text_to_video' yalnızca istemden üretir ve ekli medyayı reddeder. 'image_to_video' bir görseli canlandırır veya iki görsel eklendiğinde başlangıç karesinden bitiş karesine enterpolasyon yapar. 'reference_to_video' ekli medyayı özne referansı olarak ele alır. 'edit' tam olarak bir ekli videoyu yeniden yazar, 'extend' ise ona yeni görüntüler ekler; böylece çıktı, girdi videosuyla başlar. (varsayılan: "auto") | COMBO | Evet | "auto"<br>"text_to_video"<br>"image_to_video"<br>"reference_to_video"<br>"edit"<br>"extend" |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. (varsayılan: 42) | INT | Evet | 0 ile 2147483647 arası |

### Omni Flash Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Üretilecek videoyu veya ekli bir videoya uygulanacak düzenlemeyi açıklayın. Süreyi doğrudan istemde belirtin, örn. "6 saniyelik klip"; süre 3-10 saniye olabilir. Çıktı 720p, 24 FPS ve ses içerir. (varsayılan: "") | STRING | Evet | - |
| `aspect_ratio` | Çıktı en-boy oranı: 16:9 (yatay) veya 9:16 (dikey). 'edit' görevi bunun yerine girdi videosunun en-boy oranını korur. (varsayılan: "16:9") | COMBO | Evet | "16:9"<br>"9:16" |
| `task_type` | İstem ve ekli medyayla ne yapılacağı. 'auto' ile model karar verir. 'text_to_video' yalnızca istemden üretir ve ekli medyayı reddeder. 'image_to_video' bir görseli canlandırır veya iki görsel eklendiğinde başlangıç karesinden bitiş karesine enterpolasyon yapar. 'reference_to_video' ekli medyayı özne referansı olarak ele alır. 'edit' tam olarak bir ekli videoyu yeniden yazar. (varsayılan: "auto") | COMBO | Evet | "auto"<br>"text_to_video"<br>"image_to_video"<br>"reference_to_video"<br>"edit" |
| `temperature` | Rastgeleliği kontrol eder. Düşük değerler daha odaklı/deterministik, yüksek değerler daha çeşitlidir. (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 2 arası.0 (step 0.01) |
| `top_p` | Nucleus örneklemesi: kümülatif olasılığı top_p değerine ulaşan en küçük token kümesinden örnekleme yapar. (varsayılan: 0.95) | FLOAT | Evet | 0.0 ile 1 arası.0 (step 0.01) |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. (varsayılan: 42) | INT | Evet | 0 ile 2147483647 arası |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Genişletilebilir yuva: en fazla 14 görsel bağlayın (`image_1`...`image_14`). Videoyu yönlendirmek veya canlandırmak için isteğe bağlı referans görsel(ler)i. 'image_to_video' görevinde ilk görsel başlangıç karesi, isteğe bağlı ikinci görsel ise bitiş karesidir. | IMAGE | Hayır | 0 ile 14 arası images |
| `videos` | Genişletilebilir yuva: en fazla 3 video bağlayın (`video_1`...`video_3`). Yönlendirme veya düzenleme için isteğe bağlı referans videoları. Her biri en fazla 10 saniye uzunluğunda. | VIDEO | Hayır | 0 ile 3 arası videos |

**Notlar:**
- `prompt` boş olmamalıdır; boş olması durumunda düğüm hata verir.
- `text_to_video` görevi yalnızca istemden üretir; görsel veya video eklemek hata verir.
- `image_to_video` görevi yalnızca görsel kabul eder (video değil) ve tam olarak 1 veya 2 görsel gerektirir: ilki başlangıç karesi, isteğe bağlı ikincisi ise bitiş karesidir.
- `edit` görevi (her iki modelde) ve `extend` görevi (yalnızca Omni Flash 1.1) tam olarak bir girdi videosu gerektirir ve `aspect_ratio` değerini geçersiz kılarak bu girdi videosunun en-boy oranını korur.
- En fazla 14 görsel ve 3 video eklenebilir ve eklenen her video 10 saniye veya daha kısa olmalıdır.
- Omni Flash her zaman sesli 720p 24 FPS video çıktısı verir; çözünürlük seçimi yalnızca Omni Flash 1.1 ile kullanılabilir.
- `temperature` ve `top_p` kontrolleri yalnızca Omni Flash modelinde kullanılabilir; Omni Flash 1.1 sabit üretim ayarlarını kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` (ilk çıktı) | Ses içeren üretilmiş video. Omni Flash için: 720p, 24 FPS. Omni Flash 1.1 için: `resolution` girdisinde seçilen çözünürlük. | VIDEO |
| `text` (ikinci çıktı) | Modelin video ile birlikte ürettiği metin içeriği (boş olabilir). | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmniV2/tr.md)

---
**Source fingerprint (SHA-256):** `7a0dda4bcd662c9df3c680297ec9de7886d35e618de8b3ce0cd95b9afd13a892`
