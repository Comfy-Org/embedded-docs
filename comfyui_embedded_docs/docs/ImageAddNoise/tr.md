# ImageAddNoise

ImageAddNoise düğümü, bir giriş görüntüsüne rastgele gürültü ekler. Tutarlı gürültü desenleri oluşturmak için belirtilen rastgele tohumu kullanır ve gürültü etkisinin yoğunluğunun kontrol edilmesine olanak tanır. Ortaya çıkan görüntü, giriş görüntüsüyle aynı boyutları korur ancak eklenmiş görsel dokuya sahip olur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Gürültü eklenecek giriş görüntüsü | IMAGE | Evet | - |
| `seed` | Gürültü oluşturmak için kullanılan rastgele tohum (varsayılan: 0). Bu parametre "control after generate" işlevini destekler. | INT | Evet | 0–18446744073709551615 |
| `strength` | Gürültü etkisinin yoğunluğunu kontrol eder (varsayılan: 0.5, adım: 0.01) | FLOAT | Evet | 0.0–1.0 |

**Not:** Gürültü değerleri görüntüye eklenir ve sonuç 0.0–1.0 aralığına kırpılır. Giriş görüntüsünde alfa kanalı varsa (4 kanal), özgün alfa kanalı değişmeden korunur — gürültü yalnızca renk kanallarına uygulanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Gürültü eklenmiş çıkış görüntüsü | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageAddNoise/tr.md)

---
**Source fingerprint (SHA-256):** `e6b9815e7c075c7ee97c924c22a92dfef6d9c65b97b6e65b0f9e1c96628f39f2`
