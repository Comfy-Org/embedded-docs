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

Bir metin istemi ve çıktı ayarlarına dayalı olarak eşzamanlı şekilde videolar oluşturur. Bu düğüm, metin açıklamaları ve çeşitli oluşturma parametreleri kullanarak video içeriği oluşturur ve oluşturma işlemi tamamlandığında nihai video çıktısını üretir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `istem` | Video oluşturma için istem (varsayılan: boş dize). En az 3 karakter uzunluğunda olmalıdır. | STRING | Evet | - |
| `model` | Kullanılacak video oluşturma modeli. | COMBO | Evet | `"ray_1_6"`<br>`"ray_2"` |
| `en_boy_oranı` | Oluşturulan video için en boy oranı (varsayılan: "16:9"). | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` |
| `çözünürlük` | Video için çıktı çözünürlüğü (varsayılan: "540p"). Bu parametre `ray_1_6` modeli kullanılırken yok sayılır. | COMBO | Evet | `"540p"`<br>`"720p"`<br>`"1080p"` |
| `süre` | Oluşturulan videonun süresi. Bu parametre `ray_1_6` modeli kullanılırken yok sayılır. | COMBO | Evet | `"5s"`<br>`"9s"` |
| `döngü` | Videonun döngüye girip girmeyeceği (varsayılan: Yanlış). | BOOLEAN | Evet | - |
| `tohum` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar tohum değerinden bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Evet | 0 ile 18446744073709551615 arası |
| `luma_kavramları` | Luma Concepts düğümü aracılığıyla kamera hareketini belirlemek için isteğe bağlı Kamera Kavramları. | CUSTOM | Hayır | - |

**Not:** `ray_1_6` modeli kullanılırken `duration` ve `resolution` parametreleri otomatik olarak yok sayılır ve oluşturmayı etkilemez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `44482bc91c3df2cc9ac22d06197668af45849e8bfde8bd435905f11f2593342c`
