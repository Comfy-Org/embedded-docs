# PhotoMakerKodlama

PhotoMakerEncode düğümü, görüntü oluşturma için koşullandırma verileri oluşturmak amacıyla bir referans görüntüyü bir metin istemiyle birleştirir. Metin "photomaker" sözcüğünü içerdiğinde, düğüm PhotoMaker modelini kullanarak referans görüntünün görsel kimliğini istemdeki bu konuma koşullandırmaya ekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `photomaker` | Referans görüntüyü işlemek ve görüntü tabanlı gömme vektörleri oluşturmak için kullanılan PhotoMaker modeli | PHOTOMAKER | Evet | - |
| `görüntü` | Koşullandırma için görsel özellikleri sağlayan referans görüntü | IMAGE | Evet | - |
| `clip` | Metin tokenizasyonu ve metin kodlaması için kullanılan CLIP modeli | CLIP | Evet | - |
| `metin` | Koşullandırma oluşturma için metin istemi. Çok satırlı metin ve dinamik istemleri destekler (varsayılan: "photograph of photomaker") | STRING | Evet | Herhangi bir metin |

**Not:** Metin, bağımsız bir sözcük olarak "photomaker" içerdiğinde, düğüm bu sözcüğü kodlanmış istemden çıkarır ve referans görüntünün kimliğini PhotoMaker modelini kullanarak bu konuma uygular. Metinde "photomaker" bulunmazsa, düğüm görüntü etkisi olmadan standart metin koşullandırması döndürür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Görüntü oluşturmayı yönlendiren metin ve görüntü gömme vektörlerini, CLIP metin kodlayıcısının havuzlanmış (pooled) çıktısıyla birlikte içeren koşullandırma verileri | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerEncode/tr.md)

---
**Source fingerprint (SHA-256):** `490a90c504ade253c2bb055e0efb1eb015ba6d7faf8f2370cac188871f678986`
