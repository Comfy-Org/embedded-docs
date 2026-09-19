# TextGenerateLTX2Prompt

TextGenerateLTX2Prompt düğümü, kısa bir kullanıcı istemini LTX-2 serisi video modelleriyle video üretmeye uygun ayrıntılı, görsel-işitsel bir açıklamaya genişletir. Otomatik olarak göreve özgü sistem talimatları ekler, biçimlendirilmiş istemi bir dil modeline gönderir ve geliştirilmiş metni döndürür. İsteğe bağlı bir referans görüntü sağlandığında düğüm görüntüden videoya moduna geçer ve istemi o görüntünün içeriğinden başlayarak genişletir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Metin kodlama için kullanılan CLIP modeli. Düğüm, eşleşen talimatları seçmek için modelin tokenizer adını kontrol eder: Gemma 4 tabanlı modeller LTX-2.4 biçimini kullanır, diğer modeller ise LTX-2 (Gemma 3) biçimini kullanır. | CLIP | Evet | - |
| `istem` | Ayrıntılı bir video üretim istemine genişletilecek sahneyi veya kavramı tanımlayan ham metin girdisi. | STRING | Evet | - |
| `görsel` | Videonun ilk karesi olarak kullanılan isteğe bağlı girdi görüntüsü. Sağlandığında düğüm görüntüden videoya moduna geçer ve kullanıcı istemini görüntünün içeriğine göre genişleten bir sistem istemi kullanır. | IMAGE | Hayır | - |
| `video` | Ek bağlam olarak kullanılan isteğe bağlı video girdisi. Dil modeline görüntü grubu olarak iletilir; 24 FPS olduğu varsayılır ve dahili olarak 1 FPS'ye alt örneklenir. | IMAGE | Hayır | - |
| `ses` | Üretim için ek bağlam olarak kullanılabilen isteğe bağlı ses girdisi. | AUDIO | Hayır | - |
| `maksimum_uzunluk` | Dil modelinin üretebileceği maksimum token sayısı (varsayılan: 512). | INT | Evet | 1 ile 32768 arası |
| `örnekleme_modu` | Metin üretimi sırasında rastgele örnekleme kullanılıp kullanılmayacağını kontrol eder. `"on"` olarak ayarlandığında aşağıdaki örnekleme parametreleri kullanılabilir hale gelir; `"off"` ile düğüm, rastgele örnekleme olmadan metin üretir. | DYNAMIC_COMBO | Evet | `"on"`<br>`"off"` |
| `düşünme` | Etkinleştirildiğinde, modelin yanıtlamadan önce akıl yürütmesi talimatı verilir. Döndürülen çıktıdan tüm akıl yürütme bloğu çıkarılır (varsayılan: False). | BOOLEAN | Hayır | True/False |
| `use_default_template` | Etkinleştirildiğinde, düğüm biçimlendirme için varsayılan sohbet şablonunu kullanır (varsayılan: True). Gelişmiş ayar. | BOOLEAN | Hayır | True/False |
| `mtp` | Checkpoint'in çoklu token tahmini başlığıyla spekülatif kod çözme. MTP ağırlıkları olmadan etkisi yoktur. `"auto"` taslak derinliğini uyarlar, `"2"` ile `"5"` bunu sabitler. Örneklenen çıktı doğru dağılımda kalır ancak aynı seed için MTP olmayan çıktıdan farklıdır (varsayılan: `"auto"`). | COMBO | Hayır | `"auto"`<br>`"off"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"` |

### Örnekleme Parametreleri (`sampling_mode` "on" olduğunda)

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `temperature` | Çıktının rastgeleliğini kontrol eder. Düşük değerler çıktıyı daha öngörülebilir, yüksek değerler daha yaratıcı yapar (varsayılan: 0.7). | FLOAT | Evet | 0.01 ile 2.0 arası |
| `top_k` | Örnekleme havuzunu, olasılığı en yüksek ilk K sonraki token ile sınırlar. 0 değeri bu filtreyi devre dışı bırakır (varsayılan: 64). | INT | Evet | 0 ile 1000 arası |
| `top_p` | Çekirdek örnekleme kullanır: kümülatif olasılığı bu değere ulaşan en olası tokenların en küçük kümesini tutar. (varsayılan: 0.95) | FLOAT | Evet | 0.0 ile 1.0 arası |
| `min_p` | Dikkate alınacak token'lar için minimum olasılık eşiği belirler (varsayılan: 0.05). | FLOAT | Evet | 0.0 ile 1.0 arası |
| `repetition_penalty` | Tekrarı azaltmak için zaten üretilmiş token'ları cezalandırır. 1.0 değeri hiçbir ceza uygulamaz (varsayılan: 1.05). | FLOAT | Evet | 0.0 ile 5.0 arası |
| `seed` | Yeniden üretilebilir sonuçlar için rastgele sayı üretecini başlatmak üzere kullanılan bir sayı (varsayılan: 0). | INT | Evet | 0 ile 18446744073709551615 arası |
| `presence_penalty` | Yeni token'ları, metinde şimdiye kadar görünüp görünmediklerine göre cezalandırır ve modeli yeni konulardan bahsetmeye teşvik eder (varsayılan: 0.0). | FLOAT | Hayır | 0.0 ile 5.0 arası |

**Not:** Yukarıdaki örnekleme parametreleri yalnızca `sampling_mode` "on" olarak ayarlandığında etkindir ve düğüm arayüzünde görünür. "off" olarak ayarlandığında hiçbir örnekleme parametresi kullanılamaz ve düğüm, rastgele örnekleme olmadan metin üretir.

**Not:** Düğümün davranışı girdilerine göre değişir:

- Bir `image` sağlanırsa, üretilen istem, istemin görüntünün içeriğine göre nasıl genişletileceğini açıklayan bir sistem istemi kullanılarak görüntüden videoya görevi için biçimlendirilir. Görüntü sağlanmazsa, biçimlendirme, istemi ayrıntılı bir video üretim açıklamasına genişleten bir sistem istemi kullanılarak metinden videoya görevi için yapılır.
- CLIP tokenizer'ının adı "gemma4" içeriyorsa, düğüm LTX-2.4 sistem istemlerini ve Gemma 4 sohbet biçimini kullanır. Aksi takdirde LTX-2 (Gemma 3) sistem istemlerini ve sohbet biçimini kullanır.
- `thinking`, bir Gemma 4 modeliyle etkinleştirildiğinde model akıl yürütme kanalında açılır; devre dışı bırakıldığında model doğrudan son yanıt kanalında açılır. Gemma 4 olmayan modeller için `thinking`, temel üretim adımına iletilir.
- Dil modeli, akıl yürütme blokları çıkarıldıktan sonra kullanılabilir metin üretmezse, düğüm bunun yerine özgün `prompt` değerini döndürür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `generated_text` | Dil modeli tarafından üretilen, tüm akıl yürütme blokları çıkarılmış geliştirilmiş video üretim istemi. Sonuç boşsa, özgün kullanıcı istemi döndürülür. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/tr.md)

---
**Source fingerprint (SHA-256):** `1da4a388b7c358e5649b4746b9b8d288977ec6fbed3eedc4c8709187c9f7b943`
