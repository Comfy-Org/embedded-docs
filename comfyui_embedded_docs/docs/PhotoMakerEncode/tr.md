# PhotoMakerKodlama

PhotoMakerEncode, bir referans görüntüsünü bir metin istemiyle birleştirerek AI görüntü üretimi için koşullandırma verisi oluşturur. Metin isteminde "photomaker" sözcüğünü arar ve bulduğunda, PhotoMaker modelini kullanarak referans görüntüsünün görsel özelliklerini istemdeki bu konuma uygular.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `photomaker` | Referans görüntüsünün işlenmesi ve görüntü tabanlı yerleştirmelerin (embeddings) oluşturulması için kullanılan PhotoMaker modeli | PHOTOMAKER | Evet | - |
| `image` | Koşullandırma için görsel özellikleri sağlayan referans görüntüsü | IMAGE | Evet | - |
| `clip` | Metin tokenizasyonu ve kodlama için kullanılan CLIP modeli | CLIP | Evet | - |
| `text` | Koşullandırma oluşturma için metin istemi. Birden çok satırı ve dinamik istemleri destekler (varsayılan: "photograph of photomaker") | STRING | Evet | - |

**Not:** Görüntü tabanlı koşullandırmanın uygulanabilmesi için "photomaker" sözcüğünün metin isteminde ayrı bir sözcük olarak görünmesi gerekir (eşleştirme büyük/küçük harfe duyarlıdır). Bu sözcük mevcut olduğunda, görüntünün özellikleri istemdeki bu konuma eklenir. "photomaker" bulunamazsa, düğüm, görüntü etkisi olmadan standart metin koşullandırması döndürür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Görüntü üretimini yönlendirmek için görüntü ve metin yerleştirmelerini (embeddings) içeren koşullandırma verisi ve CLIP metin kodlayıcının havuzlanmış (pooled) çıktısı | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerEncode/tr.md)

---
**Source fingerprint (SHA-256):** `490a90c504ade253c2bb055e0efb1eb015ba6d7faf8f2370cac188871f678986`
