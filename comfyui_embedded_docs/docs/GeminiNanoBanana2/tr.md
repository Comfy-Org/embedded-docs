# Nano Banana 2

GeminiNanoBanana2 düğümü, Google'ın Vertex AI Gemini modelini kullanarak görüntüler oluşturur veya düzenler. Metin istemini, isteğe bağlı referans görüntüleri veya dosyalarla birlikte API'ye gönderir ve oluşturulan görüntü ile varsa eşlik eden metni döndürür. Bu düğüm kullanımdan kaldırılmış olarak işaretlenmiştir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturulacak görüntüyü veya uygulanacak düzenlemeleri tanımlayan metin istemi. Modelin izlemesi gereken tüm kısıtlamaları, stilleri veya ayrıntıları ekleyin. Boş olamaz. (varsayılan: boş) | STRING | Evet | N/A |
| `model` | Görüntü oluşturmak için kullanılacak belirli Gemini modeli. | COMBO | Evet | "Nano Banana 2 (Gemini 3.1 Flash Image)" |
| `seed` | Tohum belirli bir değere sabitlendiğinde, model tekrarlanan istekler için aynı yanıtı sağlamaya çalışır. Deterministik çıktı garanti edilmez. Ayrıca, modeli veya sıcaklık gibi parametre ayarlarını değiştirmek, aynı tohum değerini kullansanız bile yanıtta farklılıklara neden olabilir. Varsayılan olarak rastgele bir tohum değeri kullanılır. (varsayılan: 42) | INT | Evet | 0 ile 18446744073709551615 |
| `aspect_ratio` | 'auto' olarak ayarlanırsa, girdi görüntünüzün en boy oranına uyar; görüntü sağlanmazsa, genellikle 16:9 oranında bir görüntü oluşturulur. (varsayılan: "auto") | COMBO | Evet | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"9:16"<br>"16:9"<br>"21:9" |
| `resolution` | Hedef çıktı çözünürlüğü. 2K/4K için yerleşik Gemini ölçekleyicisi kullanılır. | COMBO | Evet | "1K"<br>"2K"<br>"4K" |
| `response_modalities` | Modelin döndürdüğü içerik türünü belirler: "IMAGE" yalnızca bir görüntü döndürür, "IMAGE+TEXT" ayrıca metin döndürür. (gelişmiş) | COMBO | Evet | "IMAGE"<br>"IMAGE+TEXT" |
| `thinking_level` | Modelin muhakeme sürecinin derinliğini kontrol eder. | COMBO | Evet | "MINIMAL"<br>"HIGH" |
| `images` | İsteğe bağlı referans görüntüsü veya görüntüleri. Birden fazla görüntü eklemek için Batch Images düğümünü kullanın (14'e kadar). | IMAGE | Hayır | 1 ila 14 görüntü |
| `files` | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). Gemini Generate Content Input Files düğümünden girdi kabul eder. | CUSTOM | Hayır | N/A |
| `system_prompt` | Bir yapay zekanın davranışını belirleyen temel talimatlar. (varsayılan: modele her zaman bir görüntü üretmesini söyleyen ön tanımlı bir istem) (gelişmiş) | STRING | Hayır | N/A |

**Not:** `images` girdisi en fazla 14 görüntü destekler. Daha fazlası sağlanırsa, düğüm bir hata verir. `prompt` girdisi boş veya yalnızca boşluk karakterlerinden oluşamaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Modelin oluşturduğu veya düzenlediği ana görüntü. | IMAGE |
| `string` | Modelin döndürdüğü herhangi bir metin içeriği. | STRING |
| `thought_image` | Modelin düşünme sürecinden ilk görüntü. Yalnızca thinking_level HIGH ve IMAGE+TEXT modalitesiyle kullanılabilir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2/tr.md)

---
**Source fingerprint (SHA-256):** `d781c92f04d420985f8a5a593eb5f28f1f7b2af13abd11f2a7f6f285edcd9900`
