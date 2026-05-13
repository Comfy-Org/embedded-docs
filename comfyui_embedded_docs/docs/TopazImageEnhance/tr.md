> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/tr.md)

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

Topaz Image Enhance düğümü, endüstri standardında yükseltme ve görüntü iyileştirme sağlar. Bulut tabanlı bir yapay zeka modeli kullanarak tek bir giriş görüntüsünü işleyerek kaliteyi, detayı ve çözünürlüğü artırır. Düğüm, iyileştirme süreci üzerinde yaratıcı yönlendirme, konu odaklama ve yüz koruma seçenekleri dahil olmak üzere ince ayarlı kontrol sunar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `"Reimagine"` | Görüntü iyileştirme için kullanılacak yapay zeka modeli. |
| `image` | IMAGE | Evet | - | İyileştirilecek giriş görüntüsü. Yalnızca bir görüntü desteklenir. |
| `prompt` | STRING | Hayır | - | Yaratıcı yükseltme yönlendirmesi için isteğe bağlı bir metin istemi (varsayılan: boş). |
| `subject_detection` | COMBO | Hayır | `"All"`<br>`"Foreground"`<br>`"Background"` | İyileştirmenin görüntünün hangi kısmına odaklanacağını kontrol eder (varsayılan: "All"). |
| `face_enhancement` | BOOLEAN | Hayır | - | Görüntüde yüzler varsa bunları iyileştirmek için etkinleştirin (varsayılan: True). |
| `face_enhancement_creativity` | FLOAT | Hayır | 0.0 - 1.0 | Yüz iyileştirme için yaratıcılık seviyesini ayarlar (varsayılan: 0.0). |
| `face_enhancement_strength` | FLOAT | Hayır | 0.0 - 1.0 | İyileştirilmiş yüzlerin arka plana göre ne kadar keskin olduğunu kontrol eder (varsayılan: 1.0). |
| `crop_to_fill` | BOOLEAN | Hayır | - | Varsayılan olarak, çıktı en boy oranı farklı olduğunda görüntüye posta kutusu eklenir. Bunun yerine görüntüyü çıktı boyutlarını dolduracak şekilde kırpmak için etkinleştirin (varsayılan: False). |
| `output_width` | INT | Hayır | 0 - 32000 | Çıktı görüntüsünün istenen genişliği. 0 değeri, genellikle orijinal boyuta veya belirtilmişse `output_height` değerine göre otomatik olarak hesaplanacağı anlamına gelir (varsayılan: 0). |
| `output_height` | INT | Hayır | 0 - 32000 | Çıktı görüntüsünün istenen yüksekliği. 0 değeri, genellikle orijinal boyuta veya belirtilmişse `output_width` değerine göre otomatik olarak hesaplanacağı anlamına gelir (varsayılan: 0). |
| `creativity` | INT | Hayır | 1 - 9 | İyileştirmenin genel yaratıcılık seviyesini kontrol eder (varsayılan: 3). |
| `face_preservation` | BOOLEAN | Hayır | - | Görüntüdeki kişilerin yüz kimliğini koruyun (varsayılan: True). |
| `color_preservation` | BOOLEAN | Hayır | - | Giriş görüntüsünün orijinal renklerini koruyun (varsayılan: True). |

**Not:** Bu düğüm yalnızca tek bir giriş görüntüsünü işleyebilir. Birden fazla görüntüden oluşan bir grup sağlamak hataya neden olur.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | İyileştirilmiş çıktı görüntüsü. |

---
**Source fingerprint (SHA-256):** `69f2c929f2cd11f13557e064e30a4514e3862e127a2bdb3a3f40ec92023f255d`
