> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageAddNoise/tr.md)

ImageAddNoise düğümü, bir giriş görüntüsüne rastgele gürültü ekler. Tutarlı gürültü desenleri oluşturmak için belirtilen bir rastgele tohum değeri kullanır ve gürültü efektinin yoğunluğunu kontrol etmeye olanak tanır. Ortaya çıkan görüntü, girişle aynı boyutları korur ancak eklenmiş görsel dokuya sahiptir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Gürültü eklenecek giriş görüntüsü |
| `seed` | INT | Evet | 0 - 18446744073709551615 | Gürültü oluşturmak için kullanılan rastgele tohum değeri (varsayılan: 0) |
| `strength` | FLOAT | Evet | 0,0 - 1,0 | Gürültü efektinin yoğunluğunu kontrol eder (varsayılan: 0,5) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `image` | IMAGE | Gürültü eklenmiş çıktı görüntüsü |

---
**Source fingerprint (SHA-256):** `8abfc64500e5ff8fe7589763a07c15d771e9a5a6a61bae9ec4d819be9bf71810`
