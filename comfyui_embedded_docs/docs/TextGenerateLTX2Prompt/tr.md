# TextGenerateLTX2Prompt

TextGenerateLTX2Prompt düğümü, kısa bir kullanıcı istemini LTX-2 serisi video modelleriyle video üretmeye uygun ayrıntılı, görsel-işitsel bir açıklamaya genişletir. Göreve özgü sistem talimatlarını otomatik olarak ekler, biçimlendirilmiş istemi bir dil modeline gönderir ve geliştirilmiş metni döndürür. İsteğe bağlı bir referans görüntü sağlandığında düğüm, görüntüden videoya moduna geçer ve istemi bu görüntünün içeriğinden başlayarak genişletir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Metin kodlama için kullanılan CLIP modeli. Düğüm, eşleşen talimatları seçmek için modelin tokenizer adını kontrol eder: Gemma 4 tabanlı modeller LTX-2.4 biçimini kullanır, diğer modeller ise LTX-2 (Gemma 3) biçimini kullanır. | CLIP | Evet |  |
| `istem` | Ayrıntılı bir video üretim istemine genişletilecek sahneyi veya kavramı açıklayan ham metin girdisi. | STRING | Evet |  |
| `maksimum_uzunluk` | Dil modelinin üretmesine izin verilen maksimum token sayısı. | INT | Evet |  |
| `örnekleme_modu` | Metin üretimi sırasında bir sonraki tokeni seçmek için kullanılan örnekleme stratejisi. | COMBO | Evet | `"greedy"`<br>`"top_k"`<br>`"top_p"`<br>`"temperature"` |
| `görsel` | Videonun ilk karesi olarak kullanılan isteğe bağlı giriş görüntüsü. Sağlandığında düğüm, görüntüden videoya moduna geçer ve kullanıcı istemini görüntünün içeriğine göre genişleten bir sistem istemi kullanır. | IMAGE | Hayır |  |
| `düşünme` | Etkinleştirildiğinde modelin yanıtlamadan önce akıl yürütmesi istenir. Döndürülen çıktıdan tüm akıl yürütme bloğu kaldırılır (varsayılan: False). | BOOLEAN | Hayır |  |
| `use_default_template` | Etkinleştirildiğinde düğüm, biçimlendirme için varsayılan sohbet şablonunu kullanır (varsayılan: True). | BOOLEAN | Hayır |  |
| `video` | Üretim için ek bağlam olarak kullanılabilecek isteğe bağlı video girdisi. | VIDEO | Hayır |  |
| `ses` | Üretim için ek bağlam olarak kullanılabilecek isteğe bağlı ses girdisi. | AUDIO | Hayır |  |

**Not:** Düğümün davranışı girdilerine göre değişir:

- Bir `image` sağlanırsa, üretilen istem, istemin görüntünün içeriğine göre nasıl genişletileceğini açıklayan bir sistem istemi kullanılarak görüntüden videoya görevi için biçimlendirilir. Görüntü sağlanmazsa, biçimlendirme, istemi ayrıntılı bir video üretim açıklamasına genişleten bir sistem istemi kullanılarak metinden videoya görevi için yapılır.
- CLIP tokenizer adı "gemma4" içeriyorsa düğüm, LTX-2.4 sistem istemlerini ve Gemma 4 sohbet biçimini kullanır. Aksi takdirde LTX-2 (Gemma 3) sistem istemlerini ve sohbet biçimini kullanır.
- Bir Gemma 4 modeliyle `thinking` etkinleştirildiğinde model, akıl yürütme kanalında açılır; devre dışı bırakıldığında model doğrudan nihai yanıt kanalında açılır. Gemma 4 olmayan modellerde `thinking`, alttaki üretim adımına aktarılır.
- Dil modeli, akıl yürütme blokları kaldırıldıktan sonra kullanılabilir metin üretmezse düğüm bunun yerine özgün `prompt` değerini döndürür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Dil modeli tarafından üretilen, tüm akıl yürütme blokları kaldırılmış geliştirilmiş video üretim istemi. Sonuç boşsa özgün kullanıcı istemi döndürülür. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/tr.md)

---
**Source fingerprint (SHA-256):** `8f524ea60a247217dde8a1edaf7a689e253ae05acc9eb52ad47b91e879dba1df`
