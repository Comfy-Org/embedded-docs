> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2ReferenceVideoNode/tr.md)

Vidu2 Referans-Görüntüden-Video Oluşturma düğümü, bir metin istemi ve birden fazla referans görüntüden video oluşturur. Her biri kendi referans görüntü kümesine sahip en fazla yedi özne tanımlayabilir ve bunlara istemde `@subject{subject_id}` kullanarak başvurabilirsiniz. Düğüm, yapılandırılabilir süre, en-boy oranı ve hareket ile video oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `"viduq2"` | Video oluşturma için kullanılacak AI modeli. |
| `konular` | AUTOGROW | Evet | Yok | Her özne için en fazla 3 referans görüntü sağlayın (tüm özneler için toplam 7 görüntü). İstemlerde `@subject{subject_id}` ile bunlara başvurun. |
| `istem` | STRING | Evet | Yok | Video oluşturmayı yönlendirmek için kullanılan metin açıklaması. `ses` parametresi etkinleştirildiğinde, video bu isteme dayalı olarak oluşturulan konuşma ve arka plan müziği içerecektir. |
| `ses` | BOOLEAN | Hayır | Yok | Etkinleştirildiğinde, video isteme dayalı olarak oluşturulan konuşma ve arka plan müziği içerecektir (varsayılan: `False`). |
| `süre` | INT | Hayır | 1 ila 10 | Oluşturulan videonun saniye cinsinden uzunluğu (varsayılan: `5`). |
| `tohum` | INT | Hayır | 0 ila 2147483647 | Tekrarlanabilir sonuçlar için oluşturmanın rastgeleliğini kontrol etmek için kullanılan sayı (varsayılan: `1`). |
| `en-boy_oranı` | COMBO | Hayır | `"16:9"`<br>`"9:16"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` | Video çerçevesinin şekli. |
| `çözünürlük` | COMBO | Hayır | `"720p"`<br>`"1080p"` | Çıktı videosunun piksel çözünürlüğü. |
| `hareket_genliği` | COMBO | Hayır | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` | Çerçevedeki nesnelerin hareket genliğini kontrol eder. |

**Kısıtlamalar:**

* `prompt` 1 ila 2000 karakter arasında olmalıdır.
* Birden fazla özne tanımlayabilirsiniz, ancak tüm özneler arasında toplam referans görüntü sayısı 7'yi geçmemelidir.
* Her bir özne en fazla 3 referans görüntüye sahip olabilir.
* Her referans görüntünün genişlik-yükseklik oranı 1:4 ile 4:1 arasında olmalıdır.
* Her referans görüntü, hem genişlik hem de yükseklik olarak en az 128 piksel olmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video dosyası. |

---
**Source fingerprint (SHA-256):** `3e02b05a0e374442a6ca4ce6a3dbc182b4059e19b5ed7dfc2794e036de7beffd`
