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

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | İstemi tokenize etmek ve metin oluşturmak için kullanılan CLIP modeli. | CLIP | Evet | Yok |
| `istem` | Oluşturmayı yönlendiren metin istemi. Bu alan birden çok satırı ve dinamik istemleri destekler. Varsayılan değer boş bir dizedir. | STRING | Evet | Yok |
| `görsel` | Oluşturulan metni etkilemek için metin istemiyle birlikte kullanılabilen isteğe bağlı bir görsel. | IMAGE | Hayır | Yok |
| `video` | Bir görsel yığını olarak video kareleri. 24 FPS olduğu varsayılır; dahili olarak 1 FPS'ye alt örneklenir. | IMAGE | Hayır | Yok |
| `ses` | Oluşturulan metni etkilemek için metin istemiyle birlikte kullanılabilen isteğe bağlı bir ses girişi. | AUDIO | Hayır | Yok |
| `maks_uzunluk` | Modelin oluşturacağı maksimum token sayısı. Varsayılan değer 256'dır. | INT | Evet | 1 ila 2048 |
| `örnekleme_modu` | Metin oluşturma sırasında rastgele örnekleme kullanılıp kullanılmayacağını kontrol eder. "on" olarak ayarlandığında, örneklemeyi kontrol etmek için ek parametreler kullanılabilir hale gelir. Varsayılan "on"dur. | COMBO | Evet | `"on"`<br>`"off"` |
| `düşünme` | Model destekliyorsa düşünme modunda çalışır. Varsayılan değer False'dur. | BOOLEAN | Hayır | True veya False |
| `use_default_template` | Modelde varsa, yerleşik sistem istemini/şablonunu kullanır. Varsayılan değer True'dur. Bu gelişmiş bir parametredir. | BOOLEAN | Hayır | True veya False |
| `temperature` | Çıktının rastgeleliğini kontrol eder. Daha düşük değerler çıktıyı daha öngörülebilir, daha yüksek değerler daha yaratıcı yapar. Bu parametre yalnızca `örnekleme_modu` "on" olduğunda kullanılabilir. Varsayılan değer 0.7'dir. | FLOAT | Hayır | 0.01 ila 2.0 |
| `top_k` | Örnekleme havuzunu en olası sonraki K token ile sınırlar. 0 değeri bu filtreyi devre dışı bırakır. Bu parametre yalnızca `örnekleme_modu` "on" olduğunda kullanılabilir. Varsayılan değer 64'tür. | INT | Hayır | 0 ila 1000 |
| `top_p` | Çekirdek örneklemesi kullanır, seçimleri kümülatif olasılığı bu değerden düşük olan tokenlerle sınırlar. Bu parametre yalnızca `örnekleme_modu` "on" olduğunda kullanılabilir. Varsayılan değer 0.95'tir. | FLOAT | Hayır | 0.0 ila 1.0 |
| `min_p` | Dikkate alınacak tokenler için minimum bir olasılık eşiği belirler. Bu parametre yalnızca `örnekleme_modu` "on" olduğunda kullanılabilir. Varsayılan değer 0.05'tir. | FLOAT | Hayır | 0.0 ila 1.0 |
| `repetition_penalty` | Tekrarı azaltmak için daha önce oluşturulmuş tokenleri cezalandırır. 1.0 değeri herhangi bir ceza uygulamaz. Bu parametre yalnızca `örnekleme_modu` "on" olduğunda kullanılabilir. Varsayılan değer 1.05'tir. | FLOAT | Hayır | 0.0 ila 5.0 |
| `presence_penalty` | Yeni tokenleri, metinde şimdiye kadar görünüp görünmediklerine göre cezalandırarak modelin yeni konular hakkında konuşmasını teşvik eder. Bu parametre yalnızca `örnekleme_modu` "on" olduğunda kullanılabilir. Varsayılan değer 0.0'dır. | FLOAT | Hayır | 0.0 ila 5.0 |
| `seed` | Örnekleme "on" olduğunda tekrarlanabilir sonuçlar için rastgele sayı üretecini başlatmak için kullanılan bir sayı. Varsayılan değer 0'dır. | INT | Hayır | 0 ila 18446744073709551615 |

**Not:** `temperature`, `top_k`, `top_p`, `min_p`, `repetition_penalty`, `presence_penalty` ve `seed` parametreleri yalnızca `sampling_mode` "on" olarak ayarlandığında düğüm arayüzünde etkin ve görünür olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `oluşturulan_metin` | Model tarafından giriş istemi ve isteğe bağlı görsel, video veya ses temel alınarak oluşturulan metin. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerate/tr.md)

---
**Source fingerprint (SHA-256):** `dc6868bd7ebb63c485a4346113834f845416d7359759b2d428525398bdedf343`
