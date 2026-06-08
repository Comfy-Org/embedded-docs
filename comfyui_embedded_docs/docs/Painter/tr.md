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

Painter düğümü, ComfyUI içinde doğrudan görüntü veya maske oluşturmak veya düzenlemek için etkileşimli bir tuval sağlar. Boş bir tuvalle veya mevcut bir görüntüyle başlamanıza, bir fırça aracı kullanarak üzerine çizim yapmanıza ve hem sonuç görüntüsünü hem de karşılık gelen bir alfa maskesini çıktı olarak vermenize olanak tanır. Maske, boyanan alanları tanımlar ve bu alanlar daha sonra temel görüntü veya arka plan rengi üzerine birleştirilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | Üzerine boyanacak isteğe bağlı temel görüntü. Sağlanmazsa, belirtilen arka plan rengi, genişlik ve yükseklik kullanılarak boş bir tuval oluşturulur. | IMAGE | Hayır | - |
| `mask` | Genellikle düğümün yerleşik etkileşimli aracı tarafından oluşturulan boyama verileri. Bu parametre, kullanıcı arayüzünün boyama aracı tarafından yönetilir ve standart bir sokete bağlanması amaçlanmamıştır. | STRING | Evet | - |
| `genişlik` | Tuvalin piksel cinsinden genişliği, temel bir `görüntü` sağlanmadığında kullanılır. Değer 64'ün katı olmalıdır. Varsayılan 512'dir. | INT | Evet | 64 ila 4096 |
| `yükseklik` | Tuvalin piksel cinsinden yüksekliği, temel bir `görüntü` sağlanmadığında kullanılır. Değer 64'ün katı olmalıdır. Varsayılan 512'dir. | INT | Evet | 64 ila 4096 |
| `arka_plan_rengi` | Tuval için arka plan rengi, onaltılık kod olarak belirtilir (ör. #000000). Bu yalnızca temel bir `görüntü` sağlanmadığında kullanılır. Varsayılan siyahtır (#000000). | COLOR | Evet | - |

**Not:** `mask` girişi, düğümün özel kullanıcı arayüzü aracıyla çalışmak üzere tasarlanmıştır. Tuval üzerinde boyama yaptığınızda, araç bu değeri otomatik olarak doldurur. `width` ve `height` girişleri standart kullanıcı arayüzünde gizlidir ancak yeni bir görüntü oluştururken tuval boyutlarını tanımlar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | Nihai birleştirilmiş görüntü. Bu, boyanan alanların (`mask`'tan) sağlanan temel `görüntü` veya renkli arka plan üzerine harmanlanmasının sonucudur. | IMAGE |
| `MASK` | Boyamadan çıkarılan alfa kanalı (şeffaflık) maskesi. Beyaz alanlar boyanan bölgeleri, siyah alanlar ise dokunulmamış arka planı temsil eder. | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Painter/tr.md)

---
**Source fingerprint (SHA-256):** `ae926b6d30aab65737bd99a58cb7de5a71fa36e61a677dbc97fc30b8ef8d2418`
