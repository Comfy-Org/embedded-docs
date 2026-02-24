> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToDialogue/tr.md)

ElevenLabs Metinden Diyaloğa düğümü, metinden çoklu konuşmacılı bir ses diyaloğu oluşturur. Farklı metin satırları ve her katılımcı için ayrı sesler belirterek bir konuşma oluşturmanıza olanak tanır. Düğüm, diyalog isteğini ElevenLabs API'sine gönderir ve oluşturulan sesi döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `stability` | FLOAT | Hayır | 0.0 - 1.0 | Ses kararlılığı. Düşük değerler daha geniş bir duygusal aralık sağlar, yüksek değerler daha tutarlı ancak potansiyel olarak monoton bir konuşma üretir. (varsayılan: 0.5) |
| `apply_text_normalization` | COMBO | Hayır | `"auto"`<br>`"on"`<br>`"off"` | Metin normalleştirme modu. 'auto' sistemi karar vermeye bırakır, 'on' her zaman normalleştirme uygular, 'off' atlar. |
| `model` | COMBO | Hayır | `"eleven_v3"` | Diyalog oluşturmak için kullanılacak model. |
| `inputs` | DYNAMICCOMBO | Evet | `"1"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` | Diyalog girişi sayısı. Bir sayı seçmek, o kadar metin ve ses giriş alanı oluşturacaktır. |
| `language_code` | STRING | Hayır | - | ISO-639-1 veya ISO-639-3 dil kodu (örn., 'en', 'es', 'fra'). Otomatik algılama için boş bırakın. (varsayılan: boş) |
| `seed` | INT | Hayır | 0 - 4294967295 | Tekrarlanabilirlik için tohum değeri. (varsayılan: 1) |
| `output_format` | COMBO | Hayır | `"mp3_44100_192"`<br>`"opus_48000_192"` | Ses çıktı formatı. |

**Not:** `inputs` parametresi dinamiktir. Bir sayı (örn., "3") seçtiğinizde, düğüm üç adet karşılık gelen `text` ve `voice` giriş alanı görüntüleyecektir (örn., `text1`, `voice1`, `text2`, `voice2`, `text3`, `voice3`). Her `text` alanı en az bir karakter içermelidir.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `audio` | AUDIO | Seçilen çıktı formatında oluşturulan çoklu konuşmacılı diyalog sesi. |