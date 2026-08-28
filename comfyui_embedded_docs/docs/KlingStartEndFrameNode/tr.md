# Kling Başlangıç-Bitiş Karesinden Videoya

Bu düğüm, sağladığınız başlangıç ve bitiş görselleri arasında geçiş yapan bir video dizisi oluşturur. İlk kareden son kareye yumuşak bir dönüşüm üretmek için aradaki tüm kareleri üretir. Bu düğüm, görüntüden videoya API'sini çağırır ancak yalnızca `image_tail` istek alanıyla çalışan girdi seçeneklerini destekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `başlangıç_karesi` | Referans Görsel - URL veya Base64 kodlu dize, 10MB'ı aşamaz, çözünürlük 300*300px'den az olamaz, en-boy oranı 1:2.5 ~ 2.5:1 arasında olmalıdır. Base64, data:image önekini içermemelidir. | IMAGE | Evet | - |
| `bitiş_karesi` | Referans Görsel - Bitiş karesi kontrolü. URL veya Base64 kodlu dize, 10MB'ı aşamaz, çözünürlük 300*300px'den az olamaz. Base64, data:image önekini içermemelidir. | IMAGE | Evet | - |
| `istem` | Pozitif metin istemi. Boş olmamalı ve 500 karakteri aşmamalıdır. | STRING | Evet | - |
| `negatif_istem` | Negatif metin istemi. 500 karakteri aşamaz. Boş bırakılırsa istekten çıkarılır. | STRING | Evet | - |
| `cfg_ölçeği` | İstem yönlendirmesinin gücünü kontrol eder (varsayılan: 0.5) | FLOAT | Evet | 0.0-1.0 |
| `en_boy_oranı` | Oluşturulan video için en-boy oranı (varsayılan: "16:9") | COMBO | Evet | "16:9"<br>"9:16"<br>"1:1" |
| `mod` | Video oluşturma için kullanılacak yapılandırma, şu biçimi izler: mod / süre / model_adı. (varsayılan: "pro mode / 5s duration / kling-v2-5-turbo") | COMBO | Evet | "pro mode / 5s duration / kling-v2-5-turbo"<br>"pro mode / 10s duration / kling-v2-5-turbo" |

**Görsel Kısıtlamaları:**

- Hem `start_frame` hem de `end_frame` gereklidir ve dosya boyutu 10MB'ı aşamaz.
- En küçük çözünürlük: her iki görsel için 300×300 piksel.
- `start_frame` en-boy oranı 1:2.5 ile 2.5:1 arasında olmalıdır.
- Base64 kodlu görseller "data:image" önekini içermemelidir.

**İstem Kısıtlamaları:**

- `prompt` boş olmamalı ve 500 karakteri aşmamalıdır.
- `negative_prompt` 500 karakteri aşamaz; boş olduğunda istekle birlikte gönderilmez.

**Mod Notları:**

- Her iki mod seçeneği de kling-v2-5-turbo modeliyle pro modu kullanır ve yalnızca süre (5 saniye veya 10 saniye) bakımından farklılık gösterir.
- Düğümün fiyat rozetinde gösterildiği gibi üretim başına fiyatlandırma: 5s modu 0,35 USD, 10s modu 0,70 USD maliyeti vardır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan video dizisi | VIDEO |
| `video_kimliği` | Oluşturulan video için benzersiz tanımlayıcı | STRING |
| `süre` | Oluşturulan videonun süresi | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/tr.md)

---
**Source fingerprint (SHA-256):** `a27977226360a425614255f8330ce7fd8ba94b8c3020eb8fdddc01eb74f035c1`
