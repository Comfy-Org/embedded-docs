# TextGenerate

TextGenerate düğümü, kullanıcının istemine dayalı olarak metin oluşturmak için bir CLIP modeli kullanır. Metin oluşturmayı yönlendirmek için isteğe bağlı olarak görseller, video veya sesi ek bağlam olarak kullanabilir. Çıktının uzunluğunu kontrol edebilir, desteklenen modeller için düşünme modunu etkinleştirebilir ve çeşitli ayarlarla rastgele örnekleme kullanmayı veya örnekleme olmadan metin oluşturmayı seçebilirsiniz.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | İstemi tokenize etmek ve metin oluşturmak için kullanılan CLIP modeli. | CLIP | Evet | N/A |
| `prompt` | Oluşturmayı yönlendiren metin istemi. Bu alan birden çok satırı ve dinamik istemleri destekler. Varsayılan değer boş bir dizedir. | STRING | Evet | N/A |
| `image` | Oluşturulan metni etkilemek için metin istemiyle birlikte kullanılabilen isteğe bağlı bir görsel. | IMAGE | Hayır | N/A |
| `video` | Görüntü topluluğu olarak video kareleri. 24 FPS olduğu varsayılır; dahili olarak 1 FPS'e alt örneklenir. | IMAGE | Hayır | N/A |
| `audio` | Oluşturulan metni etkilemek için metin istemiyle birlikte kullanılabilen isteğe bağlı bir ses girdisi. | AUDIO | Hayır | N/A |
| `max_length` | Modelin oluşturacağı maksimum token sayısı. Varsayılan değer 512'dir. | INT | Evet | 1 to 32768 |
| `sampling_mode` | Metin oluşturma sırasında rastgele örneklemenin kullanılıp kullanılmadığını kontrol eder. "on" olarak ayarlandığında, örneklemeyi kontrol etmek için ek parametreler kullanılabilir hale gelir. Varsayılan "on"dur. | DYNAMIC_COMBO | Evet | "on"<br>"off" |
| `thinking` | Model destekliyorsa düşünme modunda çalışır. Varsayılan değer False'tur. | BOOLEAN | Hayır | True or False |
| `use_default_template` | Modelde varsa yerleşik sistem istemini/şablonunu kullanır. Varsayılan değer True'dır. Bu bir gelişmiş parametredir. | BOOLEAN | Hayır | True or False |

### "on" Girdileri

Aşağıdaki örnekleme parametreleri `sampling_mode` "on" olarak ayarlandığında kullanılabilir:

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `temperature` | Çıktının rastgeleliğini kontrol eder. Düşük değerler çıktıyı daha öngörülebilir yapar, yüksek değerler daha yaratıcı yapar. Varsayılan değer 0.7'dir. | FLOAT | Hayır | 0.01 to 2.0 |
| `top_k` | Örnekleme havuzunu en olası sonraki K token ile sınırlar. 0 değeri bu filtreyi devre dışı bırakır. Varsayılan değer 64'tür. | INT | Hayır | 0 to 1000 |
| `top_p` | Nükleus örneklemesi kullanır, seçimleri kümülatif olasılığı bu değerden düşük olan tokenlerle sınırlar. Varsayılan değer 0.95'tir. | FLOAT | Hayır | 0.0 to 1.0 |
| `min_p` | Tokenlerin dikkate alınması için minimum olasılık eşiği belirler. Varsayılan değer 0.05'tir. | FLOAT | Hayır | 0.0 to 1.0 |
| `repetition_penalty` | Tekrarı azaltmak için daha önce oluşturulmuş tokenleri cezalandırır. 1.0 değeri ceza uygulamaz. Varsayılan değer 1.05'tir. | FLOAT | Hayır | 0.0 to 5.0 |
| `presence_penalty` | Yeni tokenleri, şimdiye kadar metinde görünüp görünmediklerine göre cezalandırır ve modeli yeni konular hakkında konuşmaya teşvik eder. Varsayılan değer 0.0'dır. | FLOAT | Hayır | 0.0 to 5.0 |
| `seed` | Örnekleme "on" iken tekrarlanabilir sonuçlar için rastgele sayı üretecini başlatmak için kullanılan sayı. Varsayılan değer 0'dır. | INT | Hayır | 0 to 18446744073709551615 |

### "off" Girdileri

`sampling_mode` "off" olarak ayarlandığında, ek örnekleme parametresi kullanılamaz ve düğüm rastgele örnekleme olmadan metin oluşturur.

**Not:** `temperature`, `top_k`, `top_p`, `min_p`, `repetition_penalty`, `presence_penalty` ve `seed` parametreleri yalnızca `sampling_mode` "on" olarak ayarlandığında düğüm arayüzünde etkin ve görünürdür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `generated_text` | Modelin girdi istemine ve isteğe bağlı görsel, video veya sese dayalı olarak oluşturduğu metin. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerate/tr.md)

---
**Source fingerprint (SHA-256):** `6274a2db7c9a963304daf6df494b2b20879155e918d73429fd2ce7f3b5b9da02`
