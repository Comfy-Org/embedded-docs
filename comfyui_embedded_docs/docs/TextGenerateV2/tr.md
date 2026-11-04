# Generate Text

Generate Text düğümü, bir istemden metin üretmek için bir CLIP modeli kullanır. Eski tek eklemeli düğümden farklı olarak, ek bağlam olarak büyütülebilir görsel, video ve ses dosyası yığınlarını kabul eder; böylece tek bir düğümde tam bir referans kümesini besleyebilirsiniz. Çıktı uzunluğunu, örnekleme kullanılıp kullanılmadığını ve modelin kendi sohbet şablonu ile düşünme modunun uygulanıp uygulanmadığını kontrol edersiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | İstemi tokenize etmek ve metni üretmek için kullanılan CLIP modeli. | CLIP | Evet | - |
| `prompt` | Üretimi yönlendiren istem. Birden çok satırı ve dinamik istemleri destekler (varsayılan: boş dize). | STRING | Evet | - |
| `images` | En fazla 50 görselden oluşan, `image1` ile `image50` arasındaki büyütülebilir grup; model için görsel bağlam olarak kullanılır. | AUTOGROW | Hayır | 0 ile 50 görsel arası |
| `videos` | En fazla 100 video girdisinden oluşan, `video1` ile `video100` arasındaki büyütülebilir grup. Her video, 24 FPS olduğu varsayılan ve dahili olarak 1 FPS'ye alt örneklenen bir kare grubudur. | AUTOGROW | Hayır | 0 ile 100 video arası |
| `audios` | En fazla 100 ses girdisinden oluşan, `audio1` ile `audio100` arasındaki büyütülebilir grup; model için ses bağlamı olarak kullanılır. | AUTOGROW | Hayır | 0 ile 100 ses dosyası arası |
| `max_length` | Üretilecek maksimum token sayısı (varsayılan: 512). | INT | Evet | 1 ile 32768 arası |
| `sampling_mode` | `on` çıktıyı örnekler ve aşağıdaki örnekleme parametrelerini gösterir. `off` rastgele örnekleme olmadan açgözlü üretim yapar. | DYNAMIC_COMBO | Evet | `"on"`<br>`"off"` |
| `thinking` | Model destekliyorsa düşünme modunda çalışır (varsayılan: False). | BOOLEAN | Hayır | True veya False |
| `use_default_template` | Modelde varsa yerleşik sistem istemini veya sohbet şablonunu kullanır (varsayılan: True). Gelişmiş parametre. | BOOLEAN | Hayır | True veya False |
| `mtp` | Checkpoint'in çoklu token tahmini başlığıyla spekülatif kod çözme. MTP ağırlıkları olmadan etkisi yoktur. `"auto"`, taslak derinliğini ve genişliğini gözlenen token eşleşmelerine ve yürütme maliyetine uyarlar; `"2"` ile `"5"` arası sabit bir taslak derinliği belirler; `tree` modları hem genişliği hem de derinliği sabitler. Örneklenen çıktı doğru dağılımda kalır ancak aynı seed için MTP olmayan çıktıdan farklıdır (varsayılan: `"auto"`). | COMBO | Hayır | `"auto"`<br>`"off"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"tree2s1"`<br>`"tree2s2"`<br>`"tree3s1"`<br>`"tree4s1m8"` |
| `system_prompt` | Modelin sohbet şablonundaki sistem istemini değiştirir. Varsayılan şablon kullanılmadığında yok sayılır. Düğümde yazmak yerine bir STRING girdisi bağlayın (varsayılan: boş). | STRING | Hayır | - |

### Örnekleme Parametreleri (`sampling_mode` `"on"` olduğunda)

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `temperature` | Çıktının rastgeleliğini kontrol eder. Düşük değerler çıktıyı daha öngörülebilir, yüksek değerler daha yaratıcı yapar (varsayılan: 0.7). | FLOAT | Evet | 0.01 ile 2.0 arası |
| `top_k` | Örnekleme havuzunu, sonraki en olası K token ile sınırlar. 0 değeri filtreyi devre dışı bırakır (varsayılan: 64). | INT | Evet | 0 ile 1000 arası |
| `top_p` | Çekirdek örnekleme: kümülatif olasılığı bu değere ulaşan en olası token'ların en küçük kümesini korur (varsayılan: 0.95). | FLOAT | Evet | 0.0 ile 1.0 arası |
| `min_p` | Bir token'ın havuzda kalması için ulaşması gereken minimum olasılık (varsayılan: 0.05). | FLOAT | Evet | 0.0 ile 1.0 arası |
| `repetition_penalty` | Tekrarı azaltmak için zaten üretilmiş token'ları cezalandırır. 1.0 değeri herhangi bir ceza uygulamaz (varsayılan: 1.05). | FLOAT | Evet | 0.0 ile 5.0 arası |
| `presence_penalty` | Yeni token'ları, metinde şimdiye kadar görünüp görünmediklerine göre cezalandırarak modeli yeni konulara geçmeye teşvik eder (varsayılan: 0.0). | FLOAT | Evet | 0.0 ile 5.0 arası |
| `seed` | Yeniden üretilebilir sonuçlar için rastgele sayı üreticisini başlatmakta kullanılan sayı (varsayılan: 0). | INT | Evet | 0 ile 18446744073709551615 arası |

**Not:** Yukarıdaki örnekleme parametreleri yalnızca `sampling_mode` `"on"` olduğunda bulunur. `"off"` ile düğüm, rastgele örnekleme olmadan metin üretir ve parametreler gizlenir.

**Not:** Modelin çıktısı `<think>` ile bir akıl yürütme bloğu açtığında düğüm bunu ayırır: `generated_text` yanıtı taşır ve `thinking` açılış etiketi kaldırılmış akıl yürütmeyi taşır. Aksi durumda `generated_text` modelin ürettiği her şeyi taşır ve `thinking` boştur. `max_length` tarafından kesilen akıl yürütme `generated_text` içinde kalır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `generated_text` | Modelin ürettiği metin; varsa akıl yürütme bloğu `thinking` çıktısına ayrılmıştır. | STRING |
| `thinking` | Modelin ürettiği akıl yürütme bloğu; açılış `<think>` etiketi kaldırılmıştır. Model akıl yürütme bloğu üretmediyse boştur. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateV2/tr.md)

---
**Source fingerprint (SHA-256):** `b61210726faa495a342a5eaaebe64f800ec1d2af4e2fc1321d8c3d7c594bd9ca`
