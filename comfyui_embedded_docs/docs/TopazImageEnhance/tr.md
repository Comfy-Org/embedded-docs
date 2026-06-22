# Topaz Görüntü İyileştirme

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

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Görüntü iyileştirme için kullanılacak yapay zeka modeli. | COMBO | Evet | `"Reimagine"` |
| `görüntü` | İyileştirilecek giriş görüntüsü. Yalnızca bir görüntü desteklenir. | IMAGE | Evet | - |
| `istem` | Yaratıcı yükseltme yönlendirmesi için isteğe bağlı bir metin istemi (varsayılan: boş). | STRING | Hayır | - |
| `konu_tespiti` | İyileştirmenin görüntünün hangi kısmına odaklanacağını kontrol eder (varsayılan: "All"). | COMBO | Hayır | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `yüz_iyileştirme` | Görüntüde yüzler varsa bunları iyileştirmek için etkinleştirin (varsayılan: True). | BOOLEAN | Hayır | - |
| `yüz_iyileştirme_yaratıcılığı` | Yüz iyileştirme için yaratıcılık seviyesini ayarlar (varsayılan: 0.0). | FLOAT | Hayır | 0.0 - 1.0 |
| `yüz_iyileştirme_gücü` | İyileştirilmiş yüzlerin arka plana göre ne kadar keskin olduğunu kontrol eder (varsayılan: 1.0). | FLOAT | Hayır | 0.0 - 1.0 |
| `doldurmak_için_kırp` | Varsayılan olarak, çıktı en boy oranı farklı olduğunda görüntüye posta kutusu eklenir. Bunun yerine görüntüyü çıktı boyutlarını dolduracak şekilde kırpmak için etkinleştirin (varsayılan: False). | BOOLEAN | Hayır | - |
| `çıktı_genişliği` | Çıktı görüntüsünün istenen genişliği. 0 değeri, genellikle orijinal boyuta veya belirtilmişse `çıktı_yüksekliği` değerine göre otomatik olarak hesaplanacağı anlamına gelir (varsayılan: 0). | INT | Hayır | 0 - 32000 |
| `çıktı_yüksekliği` | Çıktı görüntüsünün istenen yüksekliği. 0 değeri, genellikle orijinal boyuta veya belirtilmişse `çıktı_genişliği` değerine göre otomatik olarak hesaplanacağı anlamına gelir (varsayılan: 0). | INT | Hayır | 0 - 32000 |
| `yaratıcılık` | İyileştirmenin genel yaratıcılık seviyesini kontrol eder (varsayılan: 3). | INT | Hayır | 1 - 9 |
| `yüz_koruma` | Görüntüdeki kişilerin yüz kimliğini koruyun (varsayılan: True). | BOOLEAN | Hayır | - |
| `renk_koruma` | Giriş görüntüsünün orijinal renklerini koruyun (varsayılan: True). | BOOLEAN | Hayır | - |

**Not:** Bu düğüm yalnızca tek bir giriş görüntüsünü işleyebilir. Birden fazla görüntüden oluşan bir grup sağlamak hataya neden olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | İyileştirilmiş çıktı görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/tr.md)

---
**Source fingerprint (SHA-256):** `69f2c929f2cd11f13557e064e30a4514e3862e127a2bdb3a3f40ec92023f255d`
