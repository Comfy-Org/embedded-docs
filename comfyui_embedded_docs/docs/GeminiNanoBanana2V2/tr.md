# Nano Banana 2

Bu düğüm, Gemini 3.1 Flash Image modelleri aracılığıyla Google'ın Vertex AI API'sine bir metin istemi göndererek görüntüler oluşturur veya düzenler. Bir açıklamadan yeni görüntüler oluşturur veya isteğe bağlı referans görüntüleri kullanarak mevcut görüntüleri değiştirir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturulacak görüntüyü veya uygulanacak düzenlemeleri tanımlayan metin istemi. Modelin izlemesi gereken kısıtlamaları, stilleri veya ayrıntıları ekleyin. Boş olmamalıdır. | STRING | Evet | N/A |
| `model` | Görüntü oluşturma için kullanılacak Gemini modelini seçer. Bu parametre; çözünürlük, en-boy oranı, düşünme düzeyi ve referans girdileri için ek alt parametreler içerir. | COMBO | Evet | `"Nano Banana 2 (Gemini 3.1 Flash Image)"<br>"Nano Banana 2 Lite"` |
| `seed` | Tohum belirli bir değere sabitlendiğinde model, tekrarlanan isteklerde aynı yanıtı sağlamak için elinden gelenin en iyisini yapar. Deterministik çıktı garanti edilmez. Ayrıca, modeli veya sıcaklık gibi parametre ayarlarını değiştirmek, aynı tohum değerini kullansanız bile yanıtta farklılıklara neden olabilir. Varsayılan olarak rastgele bir tohum değeri kullanılır. (varsayılan: 42) | INT | Evet | 0 to 18446744073709551615 |
| `response_modalities` | Yanıt biçimini belirler. IMAGE yalnızca bir görüntü döndürür; IMAGE+TEXT bir görüntü ve bir metin yanıtı döndürür. (varsayılan: IMAGE) Gelişmiş parametre. | COMBO | Evet | `"IMAGE"<br>"IMAGE+TEXT"` |
| `system_prompt` | Bir yapay zekânın davranışını belirleyen temel talimatlardır. Varsayılan olarak, modele her zaman bir görüntü üretmesini söyleyen yerleşik bir istem kullanılır. Gelişmiş parametre. | STRING | Hayır | N/A |
| `temperature` | Üretimdeki rastgeleliği kontrol eder. Düşük değerler daha odaklı/deterministik sonuçlar verir. (varsayılan: 1.0) Gelişmiş parametre. | FLOAT | Hayır | 0.0 to 2.0 (step 0.01) |
| `top_p` | Çekirdek örnekleme eşiği. Düşük değerler daha odaklı, yüksek değerler daha çeşitlidir. (varsayılan: 0.95) Gelişmiş parametre. | FLOAT | Hayır | 0.0 to 1.0 (step 0.01) |

### Nano Banana 2 (Gemini 3.1 Flash Image) Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | 'auto' olarak ayarlanırsa giriş görüntünüzün en-boy oranıyla eşleşir; görüntü sağlanmazsa genellikle 16:9 oranında bir görüntü üretilir. (varsayılan: auto) | COMBO | Evet | `"auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"9:16"<br>"16:9"<br>"21:9"<br>"1:4"<br>"4:1"<br>"8:1"<br>"1:8"` |
| `resolution` | Hedef çıktı çözünürlüğü. | COMBO | Evet | `"1K"<br>"2K"<br>"4K"` |
| `thinking_level` | Model tarafından kullanılan düşünme düzeyini seçer. | COMBO | Evet | `"MINIMAL"<br>"HIGH"` |

### Nano Banana 2 Lite Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | 'auto' olarak ayarlanırsa giriş görüntünüzün en-boy oranıyla eşleşir; görüntü sağlanmazsa genellikle 16:9 oranında bir görüntü üretilir. (varsayılan: auto) | COMBO | Evet | `"auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"9:16"<br>"16:9"<br>"21:9"<br>"1:4"<br>"4:1"<br>"8:1"<br>"1:8"` |
| `resolution` | Hedef çıktı çözünürlüğü. | COMBO | Evet | `"1K"` |
| `thinking_level` | Model tarafından kullanılan düşünme düzeyini seçer. | COMBO | Evet | `"MINIMAL"<br>"HIGH"` |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | İsteğe bağlı referans görüntüleri. Toplam 14 görüntüye kadar. Genişletilebilir yuva: `image_1` ile `image_14` arasını bağlayın. | IMAGE | Hayır | 0 to 14 images |
| `files` | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). Gemini Generate Content Input Files düğümünden girdi kabul eder. | GEMINI_INPUT_FILES | Hayır | N/A |

**Not:** `images` girişine en fazla 14 referans görüntüsü bağlanabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Oluşturulan veya düzenlenen görüntü. | IMAGE |
| `STRING` | Model tarafından oluşturulan metin açıklaması veya başlık. | STRING |
| `thought_image` | Modelin düşünme sürecinden gelen ilk görüntü. Yalnızca thinking_level HIGH ve IMAGE+TEXT modalitesiyle kullanılabilir. | IMAGE |

**Not:** `response_modalities` değeri `IMAGE` olarak ayarlandığında `STRING` çıktısı boştur.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2V2/tr.md)

---
**Source fingerprint (SHA-256):** `347d28aeb46aa91f7515a31c385a3e3f805a1861116a21dd2ef6575ab7fd4f3e`
