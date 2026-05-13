> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerate/tr.md)

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

TextGenerate düğümü, kullanıcının istemine dayalı olarak metin oluşturmak için bir CLIP modeli kullanır. İsteğe bağlı olarak, metin oluşturmayı yönlendirmek için ek bağlam olarak görseller, videolar veya ses dosyaları kullanabilir. Çıktının uzunluğunu kontrol edebilir, desteklenen modeller için bir düşünme modu etkinleştirebilir ve çeşitli ayarlarla rastgele örnekleme kullanmayı veya örnekleme yapmadan metin oluşturmayı seçebilirsiniz.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Evet | Yok | İstemi tokenize etmek ve metin oluşturmak için kullanılan CLIP modeli. |
| `istem` | STRING | Evet | Yok | Oluşturmayı yönlendiren metin istemi. Bu alan birden çok satırı ve dinamik istemleri destekler. Varsayılan değer boş bir dizedir. |
| `görsel` | IMAGE | Hayır | Yok | Oluşturulan metni etkilemek için metin istemiyle birlikte kullanılabilen isteğe bağlı bir görsel. |
| `video` | IMAGE | Hayır | Yok | Bir görsel yığını olarak video kareleri. 24 FPS olduğu varsayılır; dahili olarak 1 FPS'ye alt örneklenir. |
| `ses` | AUDIO | Hayır | Yok | Oluşturulan metni etkilemek için metin istemiyle birlikte kullanılabilen isteğe bağlı bir ses girişi. |
| `maks_uzunluk` | INT | Evet | 1 ila 2048 | Modelin oluşturacağı maksimum token sayısı. Varsayılan değer 256'dır. |
| `örnekleme_modu` | COMBO | Evet | `"on"`<br>`"off"` | Metin oluşturma sırasında rastgele örnekleme kullanılıp kullanılmayacağını kontrol eder. "on" olarak ayarlandığında, örneklemeyi kontrol etmek için ek parametreler kullanılabilir hale gelir. Varsayılan "on"dur. |
| `düşünme` | BOOLEAN | Hayır | True veya False | Model destekliyorsa düşünme modunda çalışır. Varsayılan değer False'dur. |
| `use_default_template` | BOOLEAN | Hayır | True veya False | Modelde varsa, yerleşik sistem istemini/şablonunu kullanır. Varsayılan değer True'dur. Bu gelişmiş bir parametredir. |
| `temperature` | FLOAT | Hayır | 0.01 ila 2.0 | Çıktının rastgeleliğini kontrol eder. Daha düşük değerler çıktıyı daha öngörülebilir, daha yüksek değerler daha yaratıcı yapar. Bu parametre yalnızca `örnekleme_modu` "on" olduğunda kullanılabilir. Varsayılan değer 0.7'dir. |
| `top_k` | INT | Hayır | 0 ila 1000 | Örnekleme havuzunu en olası sonraki K token ile sınırlar. 0 değeri bu filtreyi devre dışı bırakır. Bu parametre yalnızca `örnekleme_modu` "on" olduğunda kullanılabilir. Varsayılan değer 64'tür. |
| `top_p` | FLOAT | Hayır | 0.0 ila 1.0 | Çekirdek örneklemesi kullanır, seçimleri kümülatif olasılığı bu değerden düşük olan tokenlerle sınırlar. Bu parametre yalnızca `örnekleme_modu` "on" olduğunda kullanılabilir. Varsayılan değer 0.95'tir. |
| `min_p` | FLOAT | Hayır | 0.0 ila 1.0 | Dikkate alınacak tokenler için minimum bir olasılık eşiği belirler. Bu parametre yalnızca `örnekleme_modu` "on" olduğunda kullanılabilir. Varsayılan değer 0.05'tir. |
| `repetition_penalty` | FLOAT | Hayır | 0.0 ila 5.0 | Tekrarı azaltmak için daha önce oluşturulmuş tokenleri cezalandırır. 1.0 değeri herhangi bir ceza uygulamaz. Bu parametre yalnızca `örnekleme_modu` "on" olduğunda kullanılabilir. Varsayılan değer 1.05'tir. |
| `presence_penalty` | FLOAT | Hayır | 0.0 ila 5.0 | Yeni tokenleri, metinde şimdiye kadar görünüp görünmediklerine göre cezalandırarak modelin yeni konular hakkında konuşmasını teşvik eder. Bu parametre yalnızca `örnekleme_modu` "on" olduğunda kullanılabilir. Varsayılan değer 0.0'dır. |
| `seed` | INT | Hayır | 0 ila 18446744073709551615 | Örnekleme "on" olduğunda tekrarlanabilir sonuçlar için rastgele sayı üretecini başlatmak için kullanılan bir sayı. Varsayılan değer 0'dır. |

**Not:** `temperature`, `top_k`, `top_p`, `min_p`, `repetition_penalty`, `presence_penalty` ve `seed` parametreleri yalnızca `sampling_mode` "on" olarak ayarlandığında düğüm arayüzünde etkin ve görünür olur.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `generated_text` | STRING | Model tarafından giriş istemi ve isteğe bağlı görsel, video veya ses temel alınarak oluşturulan metin. |

---
**Source fingerprint (SHA-256):** `dc6868bd7ebb63c485a4346113834f845416d7359759b2d428525398bdedf343`
