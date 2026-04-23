> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageRemixNode/tr.md)

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

Reve Image Remix düğümü, yeni bir görsel oluşturmak için Reve API'sini kullanır. Bir veya daha fazla referans görselini bir metin istemiyle birleştirerek, sağlanan açıklamaya dayalı yeni, yeniden düzenlenmiş bir görsel oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `reference_images` | IMAGE | Evet | 1 ila 6 görsel | Remiks için temel olarak kullanılacak bir veya daha fazla referans görseli. 1 ila 6 arasında görsel ekleyebilirsiniz. |
| `prompt` | STRING | Evet | 1 ila 2560 karakter | İstenen görselin metin açıklaması. Belirli görselleri indekslerine göre referans göstermek için XML `<img>` etiketleri ekleyebilirsiniz (örn. `<img>0</img>`, `<img>1</img>`). |
| `model` | COMBO | Evet | `reve-remix@20250915`<br>`reve-remix-fast@20251030` | Remiks için kullanılacak model sürümü. Her model seçeneği, yapılandırılabilir en-boy oranları ve test zamanı ölçeklendirmesi içerir. |
| `upscale` | COMBO | Hayır | `"disabled"`<br>`"enabled"` | Oluşturulan görselin ölçeklendirilip ölçeklendirilmeyeceğini kontrol eder. Etkinleştirildiğinde, bir ölçeklendirme faktörü seçebilirsiniz. |
| `remove_background` | BOOLEAN | Hayır | `true`<br>`false` | Etkinleştirildiğinde, oluşturulan görselden arka planı kaldırmaya çalışır. |
| `seed` | INT | Hayır | 0 ila 2147483647 | Bir tohum değeri. Bu değeri değiştirmek düğümün yeniden çalışmasına neden olur, ancak sonuçlar deterministik değildir. (varsayılan: 0) |

**Not:** `model` parametresi, `aspect_ratio` (örn. "auto", "16:9", "1:1") ve `test_time_scaling` için iç içe ayarlar içeren dinamik bir birleşik giriştir. `upscale` parametresi "enabled" olarak ayarlandığında, iç içe bir `upscale_factor` ayarını ortaya çıkarır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Reve remiks işlemi tarafından oluşturulan yeni görsel. |