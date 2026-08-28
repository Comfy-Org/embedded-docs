# TextGenerateLTX2Prompt

The TextGenerateLTX2Prompt düğümü, kısa bir kullanıcı istemini LTX-2 video modeli serisiyle video oluşturmaya uygun, ayrıntılı bir görsel-işitsel açıklamaya genişletir. Göreve özel sistem talimatlarını otomatik olarak ekler, biçimlendirilmiş istemi bir dil modeline gönderir ve geliştirilmiş metni döndürür. İsteğe bağlı bir referans görüntü sağlandığında düğüm, görüntüden videoya moduna geçer ve istemi o görüntünün içeriğinden başlayarak genişletir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Metin kodlama için kullanılan CLIP modeli. Düğüm, eşleşen talimatları seçmek için modelin tokenleştirici adını kontrol eder: Gemma 4 tabanlı modeller LTX-2.4 biçimini kullanırken, diğer modeller LTX-2 (Gemma 3) biçimini kullanır. | CLIP | Evet |  |
| `istem` | Ayrıntılı bir video oluşturma istemine genişletilecek sahneyi veya kavramı tanımlayan ham metin girişi. | STRING | Evet |  |
| `maksimum_uzunluk` | Dil modelinin üretmesine izin verilen maksimum token sayısı. | INT | Evet |  |
| `örnekleme_modu` | Metin üretimi sırasında bir sonraki tokeni seçmek için kullanılan örnekleme stratejisi. | COMBO | Evet | `"greedy"`<br>`"top_k"`<br>`"top_p"`<br>`"temperature"` |
| `görsel` | Videonun ilk karesi olarak kullanılan isteğe bağlı giriş görüntüsü. Sağlandığında düğüm, görüntüden videoya moduna geçer ve kullanıcı istemini görüntünün içeriğine göre genişleten bir sistem istemi kullanır. | IMAGE | Hayır |  |
| `düşünme` | Etkinleştirildiğinde modele, yanıt vermeden önce akıl yürütmesi talimatı verilir. Akıl yürütme bloğu döndürülen çıktıdan kaldırılır (varsayılan: False). | BOOLEAN | Hayır |  |
| `use_default_template` | Etkinleştirildiğinde düğüm, biçimlendirme için varsayılan sohbet şablonunu kullanır (varsayılan: True). | BOOLEAN | Hayır |  |
| `video` | Oluşturma için ek bağlam olarak kullanılabilen isteğe bağlı video girişi. | VIDEO | Hayır |  |
| `ses` | Oluşturma için ek bağlam olarak kullanılabilen isteğe bağlı ses girişi. | AUDIO | Hayır |  |

**Not:** Düğümün davranışı girdilerine göre değişir:

- Bir `image` sağlanırsa, oluşturulan istem, görüntünün içeriğine dayalı olarak istemin nasıl genişletileceğini açıklayan bir sistem istemi kullanılarak görüntüden videoya görevi için biçimlendirilir. Görüntü sağlanmazsa, biçimlendirme, istemi ayrıntılı bir video oluşturma açıklamasına genişleten bir sistem istemi kullanılarak metinden videoya görevi içindir.
- CLIP tokenleştiricisinin adı "gemma4" içeriyorsa, düğüm LTX-2.4 sistem istemlerini ve Gemma 4 sohbet biçimini kullanır. Aksi takdirde, LTX-2 (Gemma 3) sistem istemlerini ve sohbet biçimini kullanır.
- Dil modeli, akıl yürütme blokları kaldırıldıktan sonra kullanılabilir bir metin üretmezse, düğüm bunun yerine orijinal `prompt` değerini döndürür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `üretilen_metin` | Dil modeli tarafından üretilen, akıl yürütme bloğu kaldırılmış gelişmiş video oluşturma istemi. Sonuç boşsa, orijinal kullanıcı istemi döndürülür. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/tr.md)

---
**Source fingerprint (SHA-256):** `8f524ea60a247217dde8a1edaf7a689e253ae05acc9eb52ad47b91e879dba1df`
