> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/tr.md)

TextGenerateLTX2Prompt düğümü, bir metin oluşturma düğümünün özelleştirilmiş bir versiyonudur. Kullanıcının metin istemini alır ve onu bir dil modeline geliştirme veya tamamlama için göndermeden önce belirli sistem talimatlarıyla otomatik olarak biçimlendirir. Düğüm, her bir durum için farklı sistem istemleri kullanarak iki modda çalışabilir: yalnızca metin veya bir görsel referansı ile.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Evet | | Metin kodlaması için kullanılan CLIP modeli. |
| `prompt` | STRING | Evet | | Kullanıcıdan gelen, geliştirilecek veya tamamlanacak ham metin girişi. |
| `max_length` | INT | Evet | | Dil modelinin oluşturmasına izin verilen maksimum token sayısı. |
| `sampling_mode` | COMBO | Evet | `"greedy"`<br>`"top_k"`<br>`"top_p"`<br>`"temperature"` | Metin oluşturma sırasında bir sonraki token'ı seçmek için kullanılan örnekleme stratejisi. |
| `image` | IMAGE | Hayır | | İsteğe bağlı bir giriş görseli. Sağlandığında, düğüm görsel bağlamı için bir yer tutucu içeren farklı bir sistem istemi kullanır. |

**Not:** Düğümün davranışı, `image` girişinin varlığına göre değişir. Bir görsel sağlanırsa, oluşturulan istem bir görselden-videoya görevi için biçimlendirilir. Görsel sağlanmazsa, biçimlendirme metinden-videoya görevi için yapılır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | STRING | Dil modeli tarafından oluşturulan, geliştirilmiş veya tamamlanmış metin dizisi. |