# Kling Başlangıç-Bitiş Karesinden Videoya

Bu düğüm, sağladığınız başlangıç ve bitiş görüntüleri arasında geçiş yapan bir video dizisi oluşturur. İlk kareden son kareye yumuşak bir dönüşüm üretmek için aradaki tüm kareleri oluşturur. Bu düğüm, görüntüden videoya API'sini çağırır ancak yalnızca `image_tail` istek alanıyla çalışan girdi seçeneklerini destekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `start_frame` | Referans Görüntü - URL veya Base64 ile kodlanmış dize, 10MB'ı aşamaz, çözünürlük 300*300px'ten az olamaz, en-boy oranı 1:2.5 ~ 2.5:1 arasında olmalıdır. Base64, data:image ön ekini içermemelidir. | IMAGE | Evet | - |
| `end_frame` | Referans Görüntü - Bitiş karesi kontrolü. URL veya Base64 ile kodlanmış dize, 10MB'ı aşamaz, çözünürlük 300*300px'ten az olamaz. Base64, data:image ön ekini içermemelidir. | IMAGE | Evet | - |
| `prompt` | Pozitif metin istemi. Boş olmamalıdır ve 500 karakteri aşamaz. | STRING | Evet | - |
| `negative_prompt` | Negatif metin istemi. 500 karakteri aşamaz. Boş bırakılırsa istekten çıkarılır. | STRING | Evet | - |
| `cfg_scale` | İstem yönlendirmesinin gücünü kontrol eder (varsayılan: 0.5). | FLOAT | Evet | 0.0-1.0 |
| `aspect_ratio` | Oluşturulan video için en-boy oranı (varsayılan: "16:9"). | COMBO | Evet | "16:9"<br>"9:16"<br>"1:1" |
| `mode` | Video oluşturma için kullanılacak yapılandırma, şu biçimde: mod / süre / model_adı. (varsayılan: "pro mode / 5s duration / kling-v2-5-turbo") | COMBO | Evet | "pro mode / 5s duration / kling-v2-5-turbo"<br>"pro mode / 10s duration / kling-v2-5-turbo" |

**Görüntü Kısıtlamaları:**

- Hem `start_frame` hem de `end_frame` gereklidir ve dosya boyutları 10MB'ı aşamaz.
- Minimum çözünürlük: her iki görüntü için 300×300 piksel.
- `start_frame` en-boy oranı 1:2.5 ile 2.5:1 arasında olmalıdır.
- Base64 ile kodlanmış görüntüler "data:image" ön ekini içermemelidir.

**İstem Kısıtlamaları:**

- `prompt` boş olmamalıdır ve 500 karakteri aşamaz.
- `negative_prompt` 500 karakteri aşamaz; boş olduğunda istekle birlikte gönderilmez.

**Mod Notları:**

- Her iki mod seçeneği de kling-v2-5-turbo modeliyle pro modu kullanır ve yalnızca süre açısından farklılık gösterir (5 saniye veya 10 saniye).
- Oluşturma başına fiyatlandırma, düğümün fiyat rozetinde gösterildiği gibi: 5 sn modunun maliyeti $0.35 USD, 10 sn modunun maliyeti $0.70 USD'dir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan video dizisi. | VIDEO |
| `video_id` | Oluşturulan video için benzersiz tanımlayıcı. | STRING |
| `duration` | Oluşturulan videonun süresi. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/tr.md)

---
**Source fingerprint (SHA-256):** `a27977226360a425614255f8330ce7fd8ba94b8c3020eb8fdddc01eb74f035c1`
