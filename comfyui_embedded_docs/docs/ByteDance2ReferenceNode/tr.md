> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/tr.md)

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

ByteDance Seedance 2.0 Referans Videoya düğümü, metin isteminize ve sağlanan referans materyallerine dayanarak videolar oluşturmak, düzenlemek veya uzatmak için Seedance 2.0 AI modelini kullanır. Oluşturma sürecine rehberlik etmesi için referans olarak görseller, videolar ve ses kullanabilir; video düzenleme ve uzatma gibi görevleri destekler.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` | Kullanılacak AI modeli. Seedance 2.0 maksimum kalite içindir, Seedance 2.0 Fast ise hız için optimize edilmiştir. Bir model seçmek, `prompt`, `resolution`, `duration`, `ratio`, `generate_audio` için ek zorunlu girdileri ve `reference_images`, `reference_videos`, `reference_audios`, `reference_assets` ile `auto_downscale` için isteğe bağlı girdileri ortaya çıkarır. |
| `seed` | INT | Hayır | 0 ile 2147483647 arası | Düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol etmek için kullanılan bir sayı. Seed değerinden bağımsız olarak sonuçlar deterministik değildir (varsayılan: 0). |
| `watermark` | BOOLEAN | Hayır | `True` / `False` | Oluşturulan videoya filigran eklenip eklenmeyeceği (varsayılan: False). |

**Önemli Kısıtlamalar:**
*   Düğümün çalışması için en az bir referans görseli veya videosu (`reference_images`, `reference_videos` veya `reference_assets` girdileri aracılığıyla sağlanan) gereklidir.
*   Her referans videosu en az 1,8 saniye uzunluğunda olmalıdır. Tüm referans videolarının birleşik süresi 15,1 saniyeyi geçemez.
*   Her referans ses klibi en az 1,8 saniye uzunluğunda olmalıdır. Tüm referans seslerinin birleşik süresi 15,1 saniyeyi geçemez.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video` | VIDEO | Oluşturulan video dosyası. |