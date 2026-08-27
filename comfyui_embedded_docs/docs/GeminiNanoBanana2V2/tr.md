# Nano Banana 2

Bu düğüm, Google'ın Vertex AI API'sine Gemini görüntü modelleri üzerinden bir metin istemi göndererek görüntüler oluşturur veya düzenler. Açıklamadan yeni görüntüler oluşturur veya isteğe bağlı referans görüntülerini kullanarak mevcut görüntüleri değiştirir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak Gemini görüntü modelini seçer. Seçilen model, kullanılabilir çözünürlük seçeneklerini ve modele özgü girdileri belirler. | DYNAMIC_COMBO | Evet | `"Nano Banana 2 (Gemini 3.1 Flash Image)"`<br>`"Nano Banana 2 Lite"` |
| `prompt` | Oluşturulacak görüntüyü veya uygulanacak düzenlemeleri tanımlayan metin istemi. Modelin izlemesi gereken kısıtlamaları, stilleri veya ayrıntıları ekleyin. Boş olmamalıdır. (varsayılan: boş) | STRING | Evet | N/A |
| `seed` | Seed belirli bir değere sabitlendiğinde, model tekrarlanan isteklerde aynı yanıtı sağlamak için elinden geleni yapar. Deterministik çıktı garanti edilmez. Ayrıca, aynı seed değerini kullansanız bile modeli veya sıcaklık gibi parametre ayarlarını değiştirmek yanıtta farklılıklara neden olabilir. Varsayılan olarak rastgele bir seed değeri kullanılır. (varsayılan: 42) | INT | Evet | 0 ile 18446744073709551615 arası |
| `response_modalities` | Yanıt biçimini belirler. IMAGE yalnızca bir görüntü döndürür; IMAGE+TEXT bir görüntü ve bir metin yanıtı döndürür. (varsayılan: IMAGE) Gelişmiş parametre. | COMBO | Evet | `"IMAGE"`<br>`"IMAGE+TEXT"` |
| `system_prompt` | Bir yapay zekanın davranışını belirleyen temel talimatlar. Varsayılan olarak, modele her zaman bir görüntü üretmesini söyleyen yerleşik bir istem kullanılır. Gelişmiş parametre. | STRING | Hayır | N/A |
| `temperature` | Üretimdeki rastlantısallığı kontrol eder. Düşük değer daha odaklı/deterministik olur. (varsayılan: 1.0) Gelişmiş parametre. | FLOAT | Hayır | 0.0 ile 2.0 (adım 0.01) |
| `top_p` | Çekirdek örnekleme eşiği. Düşük değer daha odaklı, yüksek değer daha çeşitlidir. (varsayılan: 0.95) Gelişmiş parametre. | FLOAT | Hayır | 0.0 ile 1.0 (adım 0.01) |

### Nano Banana 2 (Gemini 3.1 Flash Image) Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | 'auto' olarak ayarlanırsa, girdi görüntünüzün en boy oranıyla eşleşir; görüntü sağlanmazsa genellikle 16:9 kare bir görüntü üretilir. (varsayılan: auto) | COMBO | Evet | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"`<br>`"1:4"`<br>`"4:1"`<br>`"8:1"`<br>`"1:8"` |
| `resolution` | Hedef çıktı çözünürlüğü. | COMBO | Evet | `"1K"`<br>`"2K"`<br>`"4K"` |
| `thinking_level` | Model tarafından kullanılan düşünme seviyesini seçer. | COMBO | Evet | `"MINIMAL"`<br>`"HIGH"` |

### Nano Banana 2 Lite Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | 'auto' olarak ayarlanırsa, girdi görüntünüzün en boy oranıyla eşleşir; görüntü sağlanmazsa genellikle 16:9 kare bir görüntü üretilir. (varsayılan: auto) | COMBO | Evet | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"`<br>`"1:4"`<br>`"4:1"`<br>`"8:1"`<br>`"1:8"` |
| `resolution` | Hedef çıktı çözünürlüğü. | COMBO | Evet | `"1K"` |
| `thinking_level` | Model tarafından kullanılan düşünme seviyesini seçer. | COMBO | Evet | `"MINIMAL"`<br>`"HIGH"` |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | İsteğe bağlı referans görüntüsü/görüntüleri. Toplam en fazla 14 görüntü. Genişletilebilir yuva: `image_1` ile `image_14` arasını bağlayın. | IMAGE | Hayır | 0 ile 14 görüntü |
| `files` | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). Gemini Generate Content Input Files düğümünden gelen girdileri kabul eder. | GEMINI_INPUT_FILES | Hayır | N/A |

**Not:** `images` girdisine en fazla 14 referans görüntüsü bağlanabilir; bu sınırın aşılması hata oluşturur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Oluşturulan veya düzenlenen görüntü. | IMAGE |
| `STRING` | Model tarafından oluşturulan bir metin açıklaması veya başlık. `response_modalities` `IMAGE` olarak ayarlandığında olduğu gibi metin döndürülmediğinde boştur. | STRING |
| `thought_image` | Modelin düşünme sürecinden gelen ilk görüntü. Yalnızca `thinking_level` HIGH ve IMAGE+TEXT modalitesiyle kullanılabilir. | IMAGE |

**Not:** `response_modalities` `IMAGE` olarak ayarlandığında `STRING` çıktısı boştur. Model bu modda bir görüntü üretmezse, düğüm, modelin muhakemesini görüntülemek için IMAGE+TEXT moduna geçilmesini öneren bir hata oluşturur.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2V2/tr.md)

---
**Source fingerprint (SHA-256):** `347d28aeb46aa91f7515a31c385a3e3f805a1861116a21dd2ef6575ab7fd4f3e`
