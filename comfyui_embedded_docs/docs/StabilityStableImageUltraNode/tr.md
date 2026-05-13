> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityStableImageUltraNode/tr.md)

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

> Bu dokümantasyon yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme öneriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityStableImageUltraNode/en.md)

İstem ve çözünürlüğe göre eşzamanlı olarak görseller oluşturur. Bu düğüm, Stability AI'nın Stable Image Ultra modelini kullanarak metin isteminizi işler ve belirtilen en-boy oranı ve stille eşleşen bir görsel oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | - | Çıktı görselinde görmek istediğiniz şey. Öğeleri, renkleri ve konuları net bir şekilde tanımlayan güçlü, betimleyici bir istem daha iyi sonuçlar verecektir. Belirli bir kelimenin ağırlığını kontrol etmek için `(kelime:ağırlık)` biçimini kullanın; burada `kelime` ağırlığını kontrol etmek istediğiniz kelime ve `ağırlık` 0 ile 1 arasında bir değerdir. Örneğin: `Gökyüzü net bir (mavi:0.3) ve (yeşil:0.8) idi` ifadesi, mavi ve yeşil olan ancak maviden daha yeşil bir gökyüzünü belirtir. |
| `aspect_ratio` | COMBO | Evet | `"1:1"`<br>`"16:9"`<br>`"21:9"`<br>`"2:3"`<br>`"3:2"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"9:21"` | Oluşturulan görselin en-boy oranı (varsayılan: "1:1"). |
| `style_preset` | COMBO | Hayır | `"3d-model"`<br>`"analog-film"`<br>`"anime"`<br>`"cinematic"`<br>`"comic-book"`<br>`"digital-art"`<br>`"enhance"`<br>`"fantasy-art"`<br>`"isometric"`<br>`"line-art"`<br>`"low-poly"`<br>`"modeling-compound"`<br>`"neon-punk"`<br>`"origami"`<br>`"photographic"`<br>`"pixel-art"`<br>`"tile-texture"` | Oluşturulan görselin isteğe bağlı istenen stili. Herhangi bir stil ön ayarı uygulamamak için "Yok" seçeneğini seçin. |
| `seed` | INT | Evet | 0 - 4294967294 | Gürültü oluşturmak için kullanılan rastgele tohum değeri. |
| `image` | IMAGE | Hayır | - | Görselden görsele oluşturma için isteğe bağlı giriş görseli. |
| `negative_prompt` | STRING | Hayır | - | Çıktı görselinde görmek istemediğiniz şeyi tanımlayan bir metin parçası. Bu gelişmiş bir özelliktir. |
| `image_denoise` | FLOAT | Hayır | 0.0 - 1.0 | Giriş görselinin gürültü giderme oranı; 0.0, girişle aynı görseli verir, 1.0 ise hiç görsel sağlanmamış gibidir (varsayılan: 0.5). |

**Not:** Bir giriş görseli sağlanmadığında, `image_denoise` parametresi otomatik olarak devre dışı bırakılır ve yok sayılır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | IMAGE | Giriş parametrelerine göre oluşturulan görsel. |

---
**Source fingerprint (SHA-256):** `2fd9e106a3460a39c33ecc9a15ab6414dab1914fdc43e4f546827e02c889cf62`
