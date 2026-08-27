# TextGenerate

TextGenerate düğümü, kullanıcının istemine dayalı olarak metin oluşturmak için bir CLIP modeli kullanır. Metin oluşturmayı yönlendirmek için isteğe bağlı olarak görseller, video veya sesi ek bağlam olarak kullanabilir. Çıktının uzunluğunu kontrol edebilir, desteklenen modeller için düşünme modunu etkinleştirebilir ve çeşitli ayarlarla rastgele örnekleme kullanmayı veya örnekleme olmadan metin oluşturmayı seçebilirsiniz.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `örnekleme_modu` | Metin oluşturma sırasında rastgele örneklemenin kullanılıp kullanılmadığını kontrol eder. "on" olarak ayarlandığında ek örnekleme parametreleri kullanılabilir hale gelir. "off" olarak ayarlandığında düğüm, rastgele örnekleme olmadan metin oluşturur. | DYNAMIC_COMBO | Evet | `"on"`<br>`"off"` |
| `clip` | İstemi belirteçlere ayırmak ve metin oluşturmak için kullanılan CLIP modeli. | CLIP | Evet | N/A |
| `istem` | Üretimi yönlendiren metin istemi. Bu alan birden çok satırı ve dinamik istemleri destekler. Varsayılan değer boş bir dizedir. | STRING | Evet | N/A |
| `görsel` | Metin istemiyle birlikte üretilen metni etkilemek için kullanılabilen isteğe bağlı bir görsel. | IMAGE | Hayır | N/A |
| `video` | Görüntü topluluğu olarak video kareleri. 24 FPS olduğu varsayılır; dahili olarak 1 FPS'ye alt örneklenir. | IMAGE | Hayır | N/A |
| `ses` | Metin istemiyle birlikte üretilen metni etkilemek için kullanılabilen isteğe bağlı bir ses girdisi. | AUDIO | Hayır | N/A |
| `maks_uzunluk` | Modelin üreteceği maksimum belirteç (token) sayısı. Varsayılan değer 512'dir. | INT | Evet | 1 ile 32768 |
| `düşünme` | Model destekliyorsa düşünme modunda çalışır. Varsayılan değer False'tır. | BOOLEAN | Hayır | True or False |
| `use_default_template` | Modelde varsa yerleşik sistem istemini/şablonunu kullanır. Varsayılan değer True'dur. Bu bir gelişmiş parametredir. | BOOLEAN | Hayır | True or False |

### Örnekleme Parametreleri (`sampling_mode` "on" olduğunda)

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `temperature` | Çıktının rastgeleliğini kontrol eder. Düşük değerler çıktıyı daha öngörülebilir yapar, yüksek değerler daha yaratıcı yapar. Varsayılan değer 0.7'dir. | FLOAT | Evet | 0.01 ile 2.0 |
| `top_k` | Örnekleme havuzunu en olası sonraki K belirteçle sınırlar. 0 değeri bu filtreyi devre dışı bırakır. Varsayılan değer 64'tür. | INT | Evet | 0 ile 1000 |
| `top_p` | Nükleus örneklemesi kullanır ve seçenekleri kümülatif olasılığı bu değerden düşük olan belirteçlerle sınırlar. Varsayılan değer 0.95'tir. | FLOAT | Evet | 0.0 ile 1.0 |
| `min_p` | Dikkate alınacak belirteçler için minimum olasılık eşiği belirler. Varsayılan değer 0.05'tir. | FLOAT | Evet | 0.0 ile 1.0 |
| `repetition_penalty` | Tekrarı azaltmak için daha önce üretilmiş belirteçleri cezalandırır. 1.0 değeri ceza uygulamaz. Varsayılan değer 1.05'tir. | FLOAT | Evet | 0.0 ile 5.0 |
| `seed` | Tekrarlanabilir sonuçlar için rastgele sayı üretecini başlatmak amacıyla kullanılan bir sayı. Varsayılan değer 0'dır. | INT | Evet | 0 ile 18446744073709551615 |
| `presence_penalty` | Yeni belirteçleri, metinde şimdiye kadar görünüp görünmediklerine göre cezalandırarak modeli yeni konular hakkında konuşmaya teşvik eder. Varsayılan değer 0.0'dır. | FLOAT | Hayır | 0.0 ile 5.0 |

**Not:** Yukarıdaki örnekleme parametreleri, yalnızca `sampling_mode` "on" olarak ayarlandığında düğüm arayüzünde etkin ve görünürdür. `sampling_mode` "off" olarak ayarlandığında hiçbir örnekleme parametresi mevcut değildir ve düğüm, rastgele örnekleme olmadan metin oluşturur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `oluşturulan_metin` | Modelin girdi istemine ve isteğe bağlı görsel, video veya ses girdisine dayalı olarak ürettiği metin. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerate/tr.md)

---
**Source fingerprint (SHA-256):** `6274a2db7c9a963304daf6df494b2b20879155e918d73429fd2ce7f3b5b9da02`
