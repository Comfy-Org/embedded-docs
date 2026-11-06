# Google Gemini Omni (Video)

Google Gemini Omni (Video), Google'un Gemini Omni Flash modellerini kullanarak bir metin isteminden sesli video oluşturur. Sonucu yönlendirmek veya mevcut görüntüleri düzenlemek için isteğe bağlı olarak referans görseller ve/veya videolar ekleyebilirsiniz. İstenen uzunluğu doğrudan istemde belirtin: Omni Flash ve Omni Flash 1.1 için 3 ile 10 saniye, Omni Flash 1.2 için 3 ile 15 saniye.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Videoyu oluşturmak için kullanılan Gemini video modeli. | DYNAMIC_COMBO | Evet | "Omni Flash 1.2"<br>"Omni Flash 1.1"<br>"Omni Flash" |

### Omni Flash 1.2 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturulacak videoyu veya eklenen bir videoya uygulanacak düzenlemeyi açıklayın. Uzunluğu doğrudan istemde belirtin; örn. "6 saniyelik bir klip" veya 'extend' görevi için "5 saniye uzat"; oluşturulan uzunluk 3-15 saniye olabilir ve 'extend' en fazla 10 saniye ekler. Çıktı seslidir. (varsayılan: "") | STRING | Evet | - |
| `resolution` | Çıktı çözünürlüğü. (varsayılan: "720p") | COMBO | Evet | "360p"<br>"720p"<br>"1080p"<br>"4k" |
| `aspect_ratio` | Çıktı en-boy oranı: 16:9 (yatay) veya 9:16 (dikey). 'edit' ve 'extend' görevleri bunun yerine giriş videosunun en-boy oranını korur. (varsayılan: "16:9") | COMBO | Evet | "16:9"<br>"9:16" |
| `task_type` | İstem ve eklenen medya ile ne yapılacağı. 'auto' ile model karar verir. 'text_to_video' yalnızca istemden oluşturur ve eklenen medyayı reddeder. 'image_to_video' bir görseli canlandırır veya iki görsel eklendiğinde başlangıç karesinden bitiş karesine enterpolasyon yapar. 'reference_to_video' eklenen medyayı özne referansları olarak değerlendirir. 'edit' tam olarak bir eklenen videoyu yeniden yazar ve 'extend' ona yeni görüntüler ekler, böylece çıktı giriş videosuyla başlar. (varsayılan: "auto") | COMBO | Evet | "auto"<br>"text_to_video"<br>"image_to_video"<br>"reference_to_video"<br>"edit"<br>"extend" |
| `seed` | Seed, düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. (varsayılan: 42) | INT | Evet | 0 ile 2147483647 arası |

### Omni Flash 1.1 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturulacak videoyu veya eklenen bir videoya uygulanacak düzenlemeyi açıklayın. Uzunluğu doğrudan istemde belirtin; örn. "6 saniyelik bir klip" veya 'extend' görevi için "5 saniye uzat"; oluşturulan uzunluk 3-10 saniye olabilir ve varsayılan olarak 10'dur. Çıktı seslidir. (varsayılan: "") | STRING | Evet | - |
| `resolution` | Çıktı çözünürlüğü. (varsayılan: "720p") | COMBO | Evet | "360p"<br>"720p"<br>"1080p"<br>"4k" |
| `aspect_ratio` | Çıktı en-boy oranı: 16:9 (yatay) veya 9:16 (dikey). 'edit' ve 'extend' görevleri bunun yerine giriş videosunun en-boy oranını korur. (varsayılan: "16:9") | COMBO | Evet | "16:9"<br>"9:16" |
| `task_type` | İstem ve eklenen medya ile ne yapılacağı. 'auto' ile model karar verir. 'text_to_video' yalnızca istemden oluşturur ve eklenen medyayı reddeder. 'image_to_video' bir görseli canlandırır veya iki görsel eklendiğinde başlangıç karesinden bitiş karesine enterpolasyon yapar. 'reference_to_video' eklenen medyayı özne referansları olarak değerlendirir. 'edit' tam olarak bir eklenen videoyu yeniden yazar ve 'extend' ona yeni görüntüler ekler, böylece çıktı giriş videosuyla başlar. (varsayılan: "auto") | COMBO | Evet | "auto"<br>"text_to_video"<br>"image_to_video"<br>"reference_to_video"<br>"edit"<br>"extend" |
| `seed` | Seed, düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. (varsayılan: 42) | INT | Evet | 0 ile 2147483647 arası |

### Omni Flash Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturulacak videoyu veya eklenen bir videoya uygulanacak düzenlemeyi açıklayın. Uzunluğu doğrudan istemde belirtin; örn. "6 saniyelik bir klip"; uzunluk 3-10 saniye olabilir. Çıktı 720p, 24 FPS ve seslidir. (varsayılan: "") | STRING | Evet | - |
| `aspect_ratio` | Çıktı en-boy oranı: 16:9 (yatay) veya 9:16 (dikey). 'edit' görevi bunun yerine giriş videosunun en-boy oranını korur. (varsayılan: "16:9") | COMBO | Evet | "16:9"<br>"9:16" |
| `task_type` | İstem ve eklenen medya ile ne yapılacağı. 'auto' ile model karar verir. 'text_to_video' yalnızca istemden oluşturur ve eklenen medyayı reddeder. 'image_to_video' bir görseli canlandırır veya iki görsel eklendiğinde başlangıç karesinden bitiş karesine enterpolasyon yapar. 'reference_to_video' eklenen medyayı özne referansları olarak değerlendirir. 'edit' tam olarak bir eklenen videoyu yeniden yazar. (varsayılan: "auto") | COMBO | Evet | "auto"<br>"text_to_video"<br>"image_to_video"<br>"reference_to_video"<br>"edit" |
| `temperature` | Rastgeleliği kontrol eder. Daha düşük değer daha odaklı/deterministik, daha yüksek değer daha çeşitlidir. (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 2.0 arası (adım 0.01) |
| `top_p` | Nucleus örnekleme: kümülatif olasılığı top_p'ye ulaşan en küçük token kümesinden örnekleme yapar. (varsayılan: 0.95) | FLOAT | Evet | 0.0 ile 1.0 arası (adım 0.01) |
| `seed` | Seed, düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. (varsayılan: 42) | INT | Evet | 0 ile 2147483647 arası |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Büyütülebilir yuva: en fazla 14 görsel bağlayın (`image_1`...`image_14`). Videoyu yönlendirmek veya canlandırmak için isteğe bağlı referans görsel(ler). 'image_to_video' görevinde ilki başlangıç karesi, isteğe bağlı ikincisi bitiş karesidir. | IMAGE | Hayır | 0 ile 14 görsel arası |
| `videos` | Büyütülebilir yuva: en fazla 3 video bağlayın (`video_1`...`video_3`). Yönlendirmek veya düzenlemek için isteğe bağlı referans video(lar). Her biri en fazla 10 saniye uzunluğunda. | VIDEO | Hayır | 0 ile 3 video arası |

**Notlar:**
- `prompt` boş olmamalıdır; boşsa düğüm hata verir.
- `text_to_video` görevi yalnızca istemden oluşturur — görsel veya video eklemek hata verir.
- `image_to_video` görevi yalnızca görselleri kabul eder (video kabul etmez) ve tam olarak 1 veya 2 görsel gerektirir: ilki başlangıç karesi, isteğe bağlı ikincisi bitiş karesidir.
- `edit` görevi (tüm modeller) ve `extend` görevi (yalnızca Omni Flash 1.1 ve 1.2) tam olarak bir giriş videosu gerektirir ve `aspect_ratio` değerini geçersiz kılarak o giriş videosunun en-boy oranını korur.
- En fazla 14 görsel ve 3 video eklenebilir. Eklenen her video 10 saniye veya daha kısa olmalıdır; Omni Flash 1.2 ile 15 saniye veya daha kısa; `extend` görevi için 25 saniye veya daha kısa olmalıdır ve bu görevin sonucu en fazla 30 saniye uzunluğunda olabilir.
- Omni Flash her zaman sesli 720p 24 FPS video çıkarır; çözünürlük seçimi yalnızca Omni Flash 1.1 ve 1.2 ile kullanılabilir.
- `temperature` ve `top_p` kontrolleri yalnızca Omni Flash modelinde kullanılabilir; Omni Flash 1.1 ve 1.2 sabit oluşturma ayarlarını kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` (ilk çıktı) | Sesli oluşturulan video. Omni Flash için: 720p, 24 FPS. Omni Flash 1.1 ve 1.2 için: `resolution` girişinde seçilen çözünürlük. | VIDEO |
| `text` (ikinci çıktı) | Model tarafından video ile birlikte oluşturulan metin içeriği (boş olabilir). | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmniV2/tr.md)

---
**Source fingerprint (SHA-256):** `1fc6017d4d6fbce8f04b2f0ded496553074b8498e3b7342179550fc768698897`
