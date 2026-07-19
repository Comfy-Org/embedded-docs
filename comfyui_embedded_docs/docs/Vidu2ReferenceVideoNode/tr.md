# Vidu2 Referans ile Videoya Üretim

Vidu2 Referans-Görüntüden-Video Oluşturma düğümü, bir metin istemi ve birden fazla referans görüntüden video oluşturur. Her biri kendi referans görüntü kümesine sahip en fazla yedi özne tanımlayabilir ve bunlara istemde `@subject{subject_id}` kullanarak başvurabilirsiniz. Düğüm, yapılandırılabilir süre, en-boy oranı ve hareket ile video oluşturur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video oluşturma için kullanılacak AI modeli. | COMBO | Evet | `"viduq2"` |
| `konular` | Her özne için en fazla 3 referans görüntü sağlayın (tüm özneler için toplam 7 görüntü). İstemlerde `@subject{subject_id}` ile bunlara başvurun. | AUTOGROW | Evet | Yok |
| `istem` | Video oluşturmayı yönlendirmek için kullanılan metin açıklaması. `ses` parametresi etkinleştirildiğinde, video bu isteme dayalı olarak oluşturulan konuşma ve arka plan müziği içerecektir. | STRING | Evet | Yok |
| `ses` | Etkinleştirildiğinde, video isteme dayalı olarak oluşturulan konuşma ve arka plan müziği içerecektir (varsayılan: `False`). | BOOLEAN | Hayır | Yok |
| `süre` | Oluşturulan videonun saniye cinsinden uzunluğu (varsayılan: `5`). | INT | Hayır | 1 ila 10 |
| `tohum` | Tekrarlanabilir sonuçlar için oluşturmanın rastgeleliğini kontrol etmek için kullanılan sayı (varsayılan: `1`). | INT | Hayır | 0 ila 2147483647 |
| `en-boy_oranı` | Video çerçevesinin şekli. | COMBO | Hayır | `"16:9"`<br>`"9:16"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `çözünürlük` | Çıktı videosunun piksel çözünürlüğü. | COMBO | Hayır | `"720p"`<br>`"1080p"` |
| `hareket_genliği` | Çerçevedeki nesnelerin hareket genliğini kontrol eder. | COMBO | Hayır | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` |

**Kısıtlamalar:**

* `prompt` 1 ila 2000 karakter arasında olmalıdır.
* Birden fazla özne tanımlayabilirsiniz, ancak tüm özneler arasında toplam referans görüntü sayısı 7'yi geçmemelidir.
* Her bir özne en fazla 3 referans görüntüye sahip olabilir.
* Her referans görüntünün genişlik-yükseklik oranı 1:4 ile 4:1 arasında olmalıdır.
* Her referans görüntü, hem genişlik hem de yükseklik olarak en az 128 piksel olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2ReferenceVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `3e02b05a0e374442a6ca4ce6a3dbc182b4059e19b5ed7dfc2794e036de7beffd`
