# ByteDance Seedance 2.0 Referanstan Videoya

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

ByteDance Seedance 2.0 Referans Videoya düğümü, metin isteminize ve sağlanan referans materyallerine dayanarak videolar oluşturmak, düzenlemek veya genişletmek için Seedance 2.0 AI modelini kullanır. Oluşturma sürecini yönlendirmek için referans olarak görseller, videolar ve ses kullanabilir; video düzenleme ve genişletme gibi görevleri destekler.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak AI modeli. Seedance 2.0 maksimum kalite içindir, Seedance 2.0 Fast ise hız için optimize edilmiştir. Bir model seçmek, `prompt`, `resolution`, `duration`, `ratio`, `generate_audio` için ek zorunlu girişleri ve `reference_images`, `reference_videos`, `reference_audios`, `reference_assets` ve `auto_downscale` için isteğe bağlı girişleri ortaya çıkarır. | COMBO | Evet | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol etmek için kullanılan bir sayı. Tohum değerinden bağımsız olarak sonuçlar deterministik değildir (varsayılan: 0). | INT | Hayır | 0 ile 2147483647 arası |
| `watermark` | Oluşturulan videoya filigran eklenip eklenmeyeceği (varsayılan: False). | BOOLEAN | Hayır | `True` / `False` |

**Önemli Kısıtlamalar:**
*   Düğümün çalışması için en az bir referans görseli veya videosu (`reference_images`, `reference_videos` veya `reference_assets` girişleri aracılığıyla sağlanan) gereklidir.
*   Toplamda en fazla 9 referans görseli kullanılabilir (`reference_images` ve `reference_assets` kaynaklarındakiler dahil).
*   Toplamda en fazla 3 referans videosu kullanılabilir (`reference_videos` ve `reference_assets` kaynaklarındakiler dahil).
*   Toplamda en fazla 3 referans ses klibi kullanılabilir (`reference_audios` ve `reference_assets` kaynaklarındakiler dahil).
*   Her referans videosu en az 1,8 saniye uzunluğunda olmalıdır. Tüm referans videolarının toplam süresi 15,1 saniyeyi geçemez.
*   Her referans ses klibi en az 1,8 saniye uzunluğunda olmalıdır. Tüm referans seslerinin toplam süresi 15,1 saniyeyi geçemez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/tr.md)

---
**Source fingerprint (SHA-256):** `72c8a2f821b9fb9853a4d0428785c432d0852ae562080292817f8a7d52967c7f`
