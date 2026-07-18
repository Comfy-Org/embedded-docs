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

DrawBBoxes düğümü, bir görüntü üzerine sınırlayıcı kutular, etiketler ve güven skorları çizerek nesne tespit sonuçlarını görselleştirir. Giriş görüntüsü sağlanmazsa, çizilen tüm kutuları içerecek kadar büyük boş bir tuval oluşturur. Toplu işlemeyi destekleyerek, birden fazla görüntü için farklı tespit kümeleri çizmenize veya aynı tespitleri bir toplu iş boyunca tekrarlamanıza olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görsel` | Sınırlayıcı kutuların çizileceği giriş görüntüsü(leri). Sağlanmazsa, boş bir tuval oluşturulur. | IMAGE | Hayır | - |
| `bboxlar` | Sınırlayıcı kutu sözlüklerinin bir listesi. Her sözlük, `x`, `y`, `width`, `height` anahtarlarını ve isteğe bağlı olarak `label` ile `score` anahtarlarını içermelidir. | BOUNDINGBOX | Evet | - |

**Giriş Kısıtlamaları:**
*   `bboxes` girişi zorunludur ve sağlanmalıdır.
*   Düğüm, `bboxes` için farklı giriş formatlarını otomatik olarak işler. Tek bir sözlük, toplu işteki tüm görüntülere uygulanır. Düz bir sözlük listesi, her görüntü için aynı tespit kümesi olarak değerlendirilir. Bir liste listesi, toplu işteki her görüntü için farklı tespitler belirlemenize olanak tanır.
*   Bir `image` sağlanmazsa, düğüm, varsayılan minimum boyutu 640x640 olan ve sağlanan tüm sınırlayıcı kutuları sığdıracak kadar büyük boyutlara sahip boş bir görüntü oluşturur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `çıktı_görseli` | Üzerine çizilmiş sınırlayıcı kutular, etiketler ve güven skorları bulunan çıktı görüntüsü(leri). | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DrawBBoxes/tr.md)

---
**Source fingerprint (SHA-256):** `436fbd3de0d5e09ca07b099a32c9b9482a8006459dc8635e066ffa82f6c755df`
