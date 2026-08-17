# Kling Başlangıç-Bitiş Karesinden Videoya

Bu düğüm, sağladığınız başlangıç ve bitiş görselleri arasında geçiş yapan bir video dizisi oluşturur. İlk kareden son kareye yumuşak bir dönüşüm üretmek için aradaki tüm kareleri üretir. Bu düğüm, görüntüden videoya API'sini çağırır ancak yalnızca `image_tail` istek alanıyla çalışan girdi seçeneklerini destekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `start_frame` | Referans Görsel - URL veya Base64 kodlu dize, 10MB'ı aşamaz, çözünürlük 300*300px'den az olamaz, en-boy oranı 1:2.5 ~ 2.5:1 arasında olmalıdır. Base64, data:image önekini içermemelidir. | IMAGE | Evet | - |
| `end_frame` | Referans Görsel - Bitiş karesi kontrolü. URL veya Base64 kodlu dize, 10MB'ı aşamaz, çözünürlük 300*300px'den az olamaz. Base64, data:image önekini içermemelidir. | IMAGE | Evet | - |
| `prompt` | Pozitif metin istemi | STRING | Evet | - |
| `negative_prompt` | Negatif metin istemi | STRING | Evet | - |
| `cfg_scale` | İstem yönlendirmesinin gücünü kontrol eder (varsayılan: 0.5) | FLOAT | Hayır | 0.0-1.0 |
| `aspect_ratio` | Oluşturulan video için en-boy oranı (varsayılan: "16:9") | COMBO | Hayır | "16:9"<br>"9:16"<br>"1:1" |
| `mode` | Video üretimi için kullanılacak yapılandırma, şu biçimdedir: mode / duration / model_name. (varsayılan: "pro mode / 5s duration / kling-v2-5-turbo"). Mevcut tüm seçenekler kling-v2-5-turbo modeliyle pro modu kullanır ve yalnızca video süresine göre farklılık gösterir. | COMBO | Hayır | "pro mode / 5s duration / kling-v2-5-turbo"<br>"pro mode / 10s duration / kling-v2-5-turbo" |

**Görsel Kısıtlamaları:**

- Hem `start_frame` hem de `end_frame` sağlanmalı ve dosya boyutu 10MB'ı aşmamalıdır
- Her iki görsel için minimum çözünürlük: 300×300 piksel
- `start_frame` en-boy oranı 1:2.5 ile 2.5:1 arasında olmalıdır
- Base64 kodlu görseller "data:image" önekini içermemelidir

**İstem Kısıtlamaları:**

- Pozitif istem boş olmamalıdır
- Hem pozitif hem de negatif istemler 500 karakterle sınırlıdır
- `negative_prompt` boş bırakılırsa istekten çıkarılır

**Fiyatlandırma:**

- "pro mode / 5s duration / kling-v2-5-turbo": üretim başına 0.35 USD
- "pro mode / 10s duration / kling-v2-5-turbo": üretim başına 0.70 USD

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan video dizisi | VIDEO |
| `video_id` | Oluşturulan video için benzersiz tanımlayıcı | STRING |
| `duration` | Oluşturulan videonun süresi | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/tr.md)

---
**Source fingerprint (SHA-256):** `a27977226360a425614255f8330ce7fd8ba94b8c3020eb8fdddc01eb74f035c1`
