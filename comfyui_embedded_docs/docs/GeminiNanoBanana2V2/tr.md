# Nano Banana 2

ComfyUI düğüm belgelerini İngilizceden Türkçeye çevirmede uzmanlaşmış teknik çeviri uzmanısınız.

## Çeviri Kuralları

1. **Çevrilmemesi gereken içerik:**
   - Ters tırnak içindeki parametre adları: `image`, `seed`, `model`
   - BÜYÜK harflerle veri türleri: IMAGE, STRING, INT, FLOAT, MODEL, CONDITIONING, vb.
   - Range sütunundaki değerler: sayılar, "auto", seçenek adları
   - Kod, dosya yolları

2. **Çevrilmesi gereken içerik:**
   - Bölüm başlıkları: ## Genel Bakış, ## Girdiler, ## Çıktılar
   - Tüm açıklayıcı metinler
   - Parametre açıklamaları

3. **Çeviri kalitesi:**
   - Standart Türkçe kullanın
   - Profesyonel ama anlaşılır bir üslup koruyun
   - Teknik doğruluğu sağlayın
   - Standart Türkçe teknik terminolojiyi kullanın

4. **Format:**
   - Tüm Markdown biçimlendirmesini koruyun
   - Tablo yapısını koruyun
   - Belgenin başına herhangi bir not veya bağlantı eklemeyin (otomatik olarak eklenecektir)

Lütfen aşağıdaki belgeyi Türkçeye çevirin (belgenin başlangıç notunu dahil etmeyin):

## Genel Bakış

Bu düğüm, Google'ın Vertex AI API'sine bir metin istemi göndererek görseller oluşturur veya düzenler. Talimatlarınıza göre yeni görseller oluşturmak veya mevcut olanları değiştirmek için belirli bir Gemini modeli kullanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `prompt` | Oluşturulacak görseli veya uygulanacak düzenlemeleri tanımlayan metin istemi. Modelin uyması gereken kısıtlamaları, stilleri veya detayları ekleyin. | STRING | Evet | Yok |
| `model` | Görsel oluşturma için kullanılacak Gemini modelini seçer. Şu anda yalnızca bir seçenek mevcuttur. | COMBO | Evet | `"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | Tohum belirli bir değere sabitlendiğinde, model tekrarlanan istekler için aynı yanıtı vermek üzere elinden gelenin en iyisini yapar. Deterministik çıktı garanti edilmez. Ayrıca, modeli veya sıcaklık gibi parametre ayarlarını değiştirmek, aynı tohum değerini kullansanız bile yanıtta farklılıklara neden olabilir. Varsayılan olarak rastgele bir tohum değeri kullanılır. (varsayılan: 42) | INT | Evet | 0 ile 18446744073709551615 arası |
| `response_modalities` | Yanıtın biçimini belirler. Yalnızca bir görsel almak için "IMAGE" veya hem bir görsel hem de bir metin açıklaması almak için "IMAGE+TEXT" seçeneğini belirleyin. (varsayılan: "IMAGE") | COMBO | Evet | `"IMAGE"`<br>`"IMAGE+TEXT"` |
| `system_prompt` | Bir yapay zekanın davranışını belirleyen temel talimatlar. Bu gelişmiş bir parametredir. | STRING | Hayır | Yok |

**`model` parametresi hakkında not:** `model` parametresi, çözünürlük, en boy oranı ve düşünme seviyesi için ek alt parametreler içeren dinamik bir birleşik kutudur. Bu alt parametreler model seçimi içinde tanımlanır ve bu tabloda ayrı girişler olarak listelenmez.

**Görsel girişi hakkında not:** Modele giriş olarak en fazla 14 görsel sağlayabilirsiniz. Bu görseller, `model` parametresinin görsel alt alanı aracılığıyla iletilir ve düzenleme veya oluşturma için görsel bağlam olarak kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | Oluşturulan veya düzenlenen görsel. | IMAGE |
| `thought_image` | Model tarafından oluşturulan bir metin açıklaması veya başlık. | STRING |
| `thought_image` | Modelin düşünme sürecindeki ilk görsel. Yalnızca düşünme_seviyesi YÜKSEK ve IMAGE+TEXT modalitesi ile kullanılabilir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2V2/tr.md)

---
**Source fingerprint (SHA-256):** `6b91afcdd12e08ff0e3afdbb5596bfd63463cda4d2b031019dedf03bd122fa87`
