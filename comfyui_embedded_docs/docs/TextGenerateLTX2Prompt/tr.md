> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/tr.md)

TextGenerateLTX2Prompt düğümü, metin üretimi düğümünün özelleştirilmiş bir sürümüdür. Kullanıcının metin girdisini alır ve belirli sistem talimatlarıyla otomatik olarak biçimlendirerek, geliştirme veya tamamlama amacıyla bir dil modeline gönderir. Düğüm iki modda çalışabilir: yalnızca metin veya görsel referanslı olup, her durum için farklı sistem yönergeleri kullanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-----------|
| `clip` | CLIP | Evet | | Metin kodlama için kullanılan CLIP modeli. |
| `prompt` | STRING | Evet | | Kullanıcıdan alınan ve geliştirilecek veya tamamlanacak ham metin girdisi. |
| `max_length` | INT | Evet | | Dil modelinin üretmesine izin verilen maksimum token sayısı. |
| `sampling_mode` | COMBO | Evet | `"greedy"`<br>`"top_k"`<br>`"top_p"`<br>`"temperature"` | Metin üretimi sırasında bir sonraki tokeni seçmek için kullanılan örnekleme stratejisi. |
| `image` | IMAGE | Hayır | | İsteğe bağlı bir girdi görseli. Sağlandığında, düğüm görsel bağlamı için bir yer tutucu içeren farklı bir sistem yönergesi kullanır. |
| `thinking` | BOOLEAN | Hayır | | Etkinleştirildiğinde, model nihai yanıttan önce akıl yürütme sürecini çıktı olarak verir. |
| `use_default_template` | BOOLEAN | Hayır | | Etkinleştirildiğinde, düğüm biçimlendirme için varsayılan sohbet şablonunu kullanır. |
| `video` | VIDEO | Hayır | | Üretim için ek bağlam olarak kullanılabilecek isteğe bağlı bir video girdisi. |
| `audio` | AUDIO | Hayır | | Üretim için ek bağlam olarak kullanılabilecek isteğe bağlı bir ses girdisi. |

**Not:** Düğümün davranışı, `image` girdisinin varlığına bağlı olarak değişir. Bir görsel sağlanırsa, oluşturulan yönerge görselden videoya görevi için biçimlendirilir. Görsel sağlanmazsa, biçimlendirme metinden videoya görevi için yapılır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | STRING | Dil modeli tarafından oluşturulan, geliştirilmiş veya tamamlanmış metin dizisi. |

---
**Source fingerprint (SHA-256):** `a3daa0a376a53b9c5613238092cc1289d4c358c7c74b12a6e311681de550d1f8`
