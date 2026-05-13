> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageToVideoNode/tr.md)

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

ByteDance Görüntüden Videoya düğümü, bir API aracılığıyla ByteDance modellerini kullanarak, girdi görüntüsü ve metin istemine dayalı videolar oluşturur. Bir başlangıç görüntü karesi alır ve sağlanan açıklamayı takip eden bir video dizisi oluşturur. Düğüm, video çözünürlüğü, en boy oranı, süre ve diğer oluşturma parametreleri için çeşitli özelleştirme seçenekleri sunar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | STRING | Evet | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"`<br>`"seedance-1-0-lite-i2v-250428"`<br>`"seedance-1-0-pro-fast-251015"` | Video oluşturma için kullanılacak ByteDance modeli (varsayılan: `"seedance-1-0-pro-fast-251015"`). |
| `prompt` | STRING | Evet | - | Videoyu oluşturmak için kullanılan metin istemi. Boşluklar temizlendikten sonra en az 1 karakter uzunluğunda olmalıdır. |
| `görüntü` | IMAGE | Evet | - | Video için kullanılacak ilk kare. 300x300 ile 6000x6000 piksel arasında olmalı ve en boy oranı 0,4 ile 2,5 arasında olmalıdır. |
| `çözünürlük` | STRING | Evet | `"480p"`<br>`"720p"`<br>`"1080p"` | Çıktı videosunun çözünürlüğü. |
| `en-boy oranı` | STRING | Evet | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` | Çıktı videosunun en boy oranı. |
| `süre` | INT | Evet | 3 - 12 | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). `seedance-1-5-pro-251215` modeli için desteklenen minimum süre 4 saniyedir. |
| `seed` | INT | Hayır | 0 - 2147483647 | Oluşturma için kullanılacak tohum değeri (varsayılan: 0). |
| `sabit kamera` | BOOLEAN | Hayır | - | Kameranın sabitlenip sabitlenmeyeceğini belirtir. Platform, isteminize kamerayı sabitlemek için bir talimat ekler, ancak gerçek etkiyi garanti etmez (varsayılan: False). |
| `filigran` | BOOLEAN | Hayır | - | Videoya "AI tarafından oluşturuldu" filigranı eklenip eklenmeyeceği (varsayılan: False). |
| `ses_oluştur` | BOOLEAN | Hayır | - | Bu parametre, `seedance-1-5-pro-251215` dışındaki tüm modeller için yok sayılır (varsayılan: False). |

**Not:** İstem, aşağıdaki kelimeleri (büyük/küçük harf duyarsız) içermemelidir: `resolution`, `ratio`, `duration`, `seed`, `camerafixed`, `watermark`. Bu parametreler, kendilerine ayrılmış girişler aracılığıyla ayarlanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Girdi görüntüsü ve istem parametrelerine dayalı olarak oluşturulan video dosyası. |

---
**Source fingerprint (SHA-256):** `e47e14c69f4bdf4921a5a5eaec20fb775473483e80cdd9dd6700d2c7f9219e65`
