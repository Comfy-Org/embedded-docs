> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerate/tr.md)

TextGenerate düğümü, kullanıcının istemine dayalı metin oluşturmak için bir CLIP modeli kullanır. İsteğe bağlı olarak, metin oluşturmayı yönlendirmek için görsel bir referans olarak bir görüntü kullanabilir. Çıktının uzunluğunu kontrol edebilir ve çeşitli ayarlarla rastgele örnekleme kullanıp kullanmayacağınızı veya örnekleme olmadan metin oluşturmayı seçebilirsiniz.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Evet | Yok | İstemi tokenize etmek ve metin oluşturmak için kullanılan CLIP modeli. |
| `prompt` | STRING | Evet | Yok | Oluşturmayı yönlendiren metin istemi. Bu alan çoklu satırları ve dinamik istemleri destekler. Varsayılan değer boş bir dizidir. |
| `image` | IMAGE | Hayır | Yok | Oluşturulan metni etkilemek için metin istemiyle birlikte kullanılabilecek isteğe bağlı bir görüntü. |
| `max_length` | INT | Evet | 1 - 2048 | Modelin oluşturacağı maksimum token sayısı. Varsayılan değer 256'dır. |
| `sampling_mode` | COMBO | Evet | `"on"`<br>`"off"` | Metin oluşturma sırasında rastgele örnekleme kullanılıp kullanılmayacağını kontrol eder. "on" olarak ayarlandığında, örneklemeyi kontrol etmek için ek parametreler kullanılabilir hale gelir. Varsayılan değer "on"dur. |
| `temperature` | FLOAT | Hayır | 0.01 - 2.0 | Çıktının rastgeleliğini kontrol eder. Düşük değerler çıktıyı daha tahmin edilebilir, yüksek değerler daha yaratıcı yapar. Bu parametre yalnızca `sampling_mode` "on" olduğunda kullanılabilir. Varsayılan değer 0.7'dir. |
| `top_k` | INT | Hayır | 0 - 1000 | Örnekleme havuzunu, bir sonraki en olası K token ile sınırlar. 0 değeri bu filtreyi devre dışı bırakır. Bu parametre yalnızca `sampling_mode` "on" olduğunda kullanılabilir. Varsayılan değer 64'tür. |
| `top_p` | FLOAT | Hayır | 0.0 - 1.0 | Çekirdek örneklemesi kullanır, seçenekleri birikimli olasılığı bu değerden küçük olan token'larla sınırlar. Bu parametre yalnızca `sampling_mode` "on" olduğunda kullanılabilir. Varsayılan değer 0.95'tir. |
| `min_p` | FLOAT | Hayır | 0.0 - 1.0 | Token'ların değerlendirilmesi için minimum bir olasılık eşiği belirler. Bu parametre yalnızca `sampling_mode` "on" olduğunda kullanılabilir. Varsayılan değer 0.05'tir. |
| `repetition_penalty` | FLOAT | Hayır | 0.0 - 5.0 | Tekrarı azaltmak için daha önce oluşturulmuş token'ları cezalandırır. 1.0 değeri ceza uygulamaz. Bu parametre yalnızca `sampling_mode` "on" olduğunda kullanılabilir. Varsayılan değer 1.05'tir. |
| `seed` | INT | Hayır | 0 - 18446744073709551615 | Örnekleme "on" olduğunda tekrarlanabilir sonuçlar için rastgele sayı üretecini başlatmakta kullanılan bir sayı. Varsayılan değer 0'dır. |

**Not:** `temperature`, `top_k`, `top_p`, `min_p`, `repetition_penalty` ve `seed` parametreleri yalnızca `sampling_mode` "on" olarak ayarlandığında düğüm arayüzünde aktif ve görünür durumdadır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `generated_text` | STRING | Model tarafından girdi istemine ve isteğe bağlı görüntüye dayalı olarak oluşturulan metin. |