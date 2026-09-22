# QwenImage21Cache

QwenImage21Cache düğümü, Qwen-Image 2.1 modelinin KV önek önbelleğini yapılandırır: önbelleğe alınan anahtarların ve değerlerin nerede ve hangi hassasiyette saklanacağını. Metin ve referans token'ları bir kez hesaplanır ve örnekleme adımları boyunca yeniden kullanılır; düzenleme iş akışlarındaki hızlanmanın büyük kısmı buradan gelir ve bu düğüm, hız için bellekten ödün vermenize veya önbelleği tamamen devre dışı bırakmanıza olanak tanır. Bu düğüm deneysel olarak işaretlenmiştir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Önek önbelleği yapılandırılan Qwen-Image 2.1 modeli. | MODEL | Evet | - |
| `device` | Önbelleğe alınan anahtarların ve değerlerin nerede saklandığı. `"auto"` (varsayılan) önce kullanılmayan VRAM'i, ardından RAM'i kullanır; `"gpu"` önbelleği VRAM'de saklar; `"cpu"` önbelleği RAM'de saklar ve hesaplama sürerken önceden getirir, bu da hız açısından çok az maliyetlidir; `"off"` öneki her adımda yeniden hesaplar, bu daha yavaştır ancak önbelleği devre dışı bırakmanın tek yoludur. | COMBO | Evet | `"auto"`<br>`"gpu"`<br>`"cpu"`<br>`"off"` |
| `dtype` | Önbelleğin depolama hassasiyeti. `"default"` kayıpsızdır; `"int8"` önbelleği yarıya indirir ve yaklaşık bf16 doğruluğu sunar; `"int4"` önbelleği dörtte birine indirir ancak adım başına hatayı kabaca iki katına çıkarır. | COMBO | Evet | `"default"`<br>`"int8"`<br>`"int4"` |

Önbellek sığmadığında model, diğer dalın yuvasını çıkaracağına öneki yeniden hesaplar; bu nedenle aşırı büyük bir ayar çalışmayı başarısız kılmak yerine hızı düşürür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MODEL` | Önbellek cihazı ve hassasiyeti uygulanmış, örneklemeye hazır model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImage21Cache/tr.md)

---
**Source fingerprint (SHA-256):** `0c10cdb465d1ee4063273ffbb4913def3830f7e329694cd0a2e292d6f3c37ae4`
