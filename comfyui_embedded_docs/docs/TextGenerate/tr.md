# TextGenerate

TextGenerate düğümü, kullanıcının istemine dayalı metin oluşturmak için bir CLIP modeli kullanır. Metin oluşturmayı yönlendirmek üzere isteğe bağlı olarak görselleri, videoyu veya sesi ek bağlam olarak kullanabilir. Çıktının uzunluğunu kontrol edebilir, desteklenen modeller için bir düşünme modunu etkinleştirebilir ve çeşitli ayarlarla rastgele örnekleme kullanıp kullanmayacağınızı ya da örnekleme olmadan metin oluşturup oluşturmayacağınızı seçebilirsiniz.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `örnekleme_modu` | Metin oluşturma sırasında rastgele örneklemenin kullanılıp kullanılmayacağını kontrol eder. "on" olarak ayarlandığında ek örnekleme parametreleri kullanılabilir hale gelir. "off" olarak ayarlandığında düğüm rastgele örnekleme olmadan metin oluşturur. | DYNAMIC_COMBO | Evet | `"on"`<br>`"off"` |
| `clip` | İstemi tokenize etmek ve metin oluşturmak için kullanılan CLIP modeli. | CLIP | Evet | N/A |
| `istem` | Oluşturmayı yönlendiren metin istemi. Bu alan birden çok satırı ve dinamik istemleri destekler. Varsayılan değer boş bir dizedir. | STRING | Evet | N/A |
| `görsel` | Oluşturulan metni etkilemek için metin istemiyle birlikte kullanılabilen isteğe bağlı bir görsel. | IMAGE | Hayır | N/A |
| `video` | Görüntü yığını olarak video kareleri. 24 FPS olduğu varsayılır; dahili olarak 1 FPS'ye alt örneklenir. | IMAGE | Hayır | N/A |
| `ses` | Oluşturulan metni etkilemek için metin istemiyle birlikte kullanılabilen isteğe bağlı bir ses girdisi. | AUDIO | Hayır | N/A |
| `maks_uzunluk` | Modelin oluşturacağı maksimum token sayısı. Varsayılan değer 512'dir. | INT | Evet | 1 - 32768 |
| `düşünme` | Model destekliyorsa düşünme modunda çalışır. Varsayılan değer False'tur. | BOOLEAN | Hayır | True veya False |
| `use_default_template` | Modelde varsa yerleşik sistem istemini/şablonunu kullanır. Varsayılan değer True'dur. Bu gelişmiş bir parametredir. | BOOLEAN | Hayır | True veya False |
| `mtp` | Checkpoint'in çoklu token tahmini başlığıyla spekülatif kod çözme. MTP ağırlıkları olmadan etkisi yoktur. `"auto"` taslak derinliğini uyarlar, `"2"` ile `"5"` arası sabitler. Örneklenen çıktı doğru dağılımda kalır ancak aynı `seed` için MTP olmayan çıktıdan farklıdır (varsayılan: `"auto"`). | COMBO | Hayır | `"auto"`<br>`"off"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"` |
| `system_prompt` | Modelin sohbet şablonundaki sistem istemini değiştirir. Varsayılan şablon kullanılmadığında yok sayılır. Düğümde yazmak yerine bir STRING girdisi bağlayın (varsayılan: boş). | STRING | Hayır | N/A |

### Örnekleme Parametreleri (`sampling_mode` "on" olduğunda)

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `temperature` | Çıktının rastgeleliğini kontrol eder. Düşük değerler çıktıyı daha öngörülebilir, yüksek değerler daha yaratıcı yapar. Varsayılan değer 0.7'dir. | FLOAT | Evet | 0.01 - 2.0 |
| `top_k` | Örnekleme havuzunu en olası sonraki K token ile sınırlar. 0 değeri bu filtreyi devre dışı bırakır. Varsayılan değer 64'tür. | INT | Evet | 0 - 1000 |
| `top_p` | Çekirdek örnekleme kullanır: kümülatif olasılığı bu değere ulaşan en olası tokenların en küçük kümesini tutar. Varsayılan değer 0.95'tir. | FLOAT | Evet | 0.0 - 1.0 |
| `min_p` | Tokenların dikkate alınması için minimum olasılık eşiği belirler. Varsayılan değer 0.05'tir. | FLOAT | Evet | 0.0 - 1.0 |
| `repetition_penalty` | Tekrarı azaltmak için zaten oluşturulmuş tokenları cezalandırır. 1.0 değeri hiçbir ceza uygulamaz. Varsayılan değer 1.05'tir. | FLOAT | Evet | 0.0 - 5.0 |
| `seed` | Yinelenebilir sonuçlar için rastgele sayı üretecini başlatmak üzere kullanılan sayı. Varsayılan değer 0'dır. | INT | Evet | 0 - 18446744073709551615 |
| `presence_penalty` | Şimdiye kadar metinde görünüp görünmediklerine göre yeni tokenları cezalandırır ve modeli yeni konular hakkında konuşmaya teşvik eder. Varsayılan değer 0.0'dır. | FLOAT | Hayır | 0.0 - 5.0 |

**Not:** Yukarıdaki örnekleme parametreleri yalnızca `sampling_mode` "on" olarak ayarlandığında etkindir ve düğüm arayüzünde görünür. `sampling_mode` "off" olarak ayarlandığında hiçbir örnekleme parametresi kullanılamaz ve düğüm rastgele örnekleme olmadan metin oluşturur.

**Not:** Üretilen metin bir akıl yürütme bloğu içerdiğinde (metin `<think>` ile başlıyorsa veya istem bununla bitiyorsa), akıl yürütme ayrı olarak döndürülür: `generated_text` yanıtı, `thinking` ise açılış etiketi çıkarılmış akıl yürütmeyi taşır. Aksi durumda `generated_text` modelin ürettiği her şeyi taşır ve `thinking` boş olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `generated_text` | Model tarafından giriş istemine ve isteğe bağlı görsel, video veya sese dayalı olarak oluşturulan metin; akıl yürütme bloğu `thinking` çıktısına ayrılır. | STRING |
| `thinking` | Modelin ürettiği akıl yürütme bloğu; açılış `<think>` etiketi çıkarılmıştır. Model akıl yürütme bloğu üretmediyse boştur. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerate/tr.md)

---
**Source fingerprint (SHA-256):** `80813781c06dfb0c3b59ee72c8bd6ebced69a4de8152de916ebc15153a0757fa`
