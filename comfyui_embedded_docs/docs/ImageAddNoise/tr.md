> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageAddNoise/tr.md)

ImageAddNoise düğümü, bir giriş görüntüsüne rastgele gürültü ekler. Tutarlı gürültü desenleri oluşturmak için belirli bir rastgele tohum kullanır ve gürültü etkisinin yoğunluğunu kontrol etmeye olanak tanır. Ortaya çıkan görüntü, girişle aynı boyutları korur ancak eklenen görsel doku ile birlikte.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Gürültü eklenecek giriş görüntüsü |
| `seed` | INT | Evet | 0 ile 18446744073709551615 | Gürültü oluşturmak için kullanılan rastgele tohum (varsayılan: 0) |
| `strength` | FLOAT | Evet | 0.0 ile 1.0 | Gürültü etkisinin yoğunluğunu kontrol eder (varsayılan: 0.5) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Üzerine gürültü eklenmiş çıktı görüntüsü |