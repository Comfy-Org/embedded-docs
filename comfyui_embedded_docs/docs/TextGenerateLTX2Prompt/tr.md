TextGenerateLTX2Prompt düğümü, metin üretimi düğümünün özelleştirilmiş bir sürümüdür. Kullanıcının metin girdisini alır ve belirli sistem talimatlarıyla otomatik olarak biçimlendirerek, geliştirme veya tamamlama amacıyla bir dil modeline gönderir. Düğüm iki modda çalışabilir: yalnızca metin veya görsel referanslı olup, her durum için farklı sistem yönergeleri kullanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | Metin kodlama için kullanılan CLIP modeli. | CLIP | Evet |  |
| `istem` | Kullanıcıdan alınan ve geliştirilecek veya tamamlanacak ham metin girdisi. | STRING | Evet |  |
| `maksimum_uzunluk` | Dil modelinin üretmesine izin verilen maksimum token sayısı. | INT | Evet |  |
| `örnekleme_modu` | Metin üretimi sırasında bir sonraki tokeni seçmek için kullanılan örnekleme stratejisi. | COMBO | Evet | `"greedy"`<br>`"top_k"`<br>`"top_p"`<br>`"temperature"` |
| `görsel` | İsteğe bağlı bir girdi görseli. Sağlandığında, düğüm görsel bağlamı için bir yer tutucu içeren farklı bir sistem yönergesi kullanır. | IMAGE | Hayır |  |
| `düşünme` | Etkinleştirildiğinde, model nihai yanıttan önce akıl yürütme sürecini çıktı olarak verir. | BOOLEAN | Hayır |  |
| `use_default_template` | Etkinleştirildiğinde, düğüm biçimlendirme için varsayılan sohbet şablonunu kullanır. | BOOLEAN | Hayır |  |
| `video` | Üretim için ek bağlam olarak kullanılabilecek isteğe bağlı bir video girdisi. | VIDEO | Hayır |  |
| `ses` | Üretim için ek bağlam olarak kullanılabilecek isteğe bağlı bir ses girdisi. | AUDIO | Hayır |  |

**Not:** Düğümün davranışı, `image` girdisinin varlığına bağlı olarak değişir. Bir görsel sağlanırsa, oluşturulan yönerge görselden videoya görevi için biçimlendirilir. Görsel sağlanmazsa, biçimlendirme metinden videoya görevi için yapılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `üretilen_metin` | Dil modeli tarafından oluşturulan, geliştirilmiş veya tamamlanmış metin dizisi. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/tr.md)

---
**Source fingerprint (SHA-256):** `a3daa0a376a53b9c5613238092cc1289d4c358c7c74b12a6e311681de550d1f8`
