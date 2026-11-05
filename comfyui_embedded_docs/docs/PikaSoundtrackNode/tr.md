# Pika Soundtrack

Bu düğüm, Pika ile bir video için senkronize bir ses parçası oluşturur. Görüntü ve süre korunur; yalnızca ses değiştirilir. İstediğiniz sesi tanımlayın veya görüntüden türetilmesi için talimatı boş bırakın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | Ses parçası oluşturulacak klip. En fazla 10 dakika. | VIDEO | Evet | - |
| `instruction` | Sesin ne olması gerektiği: ses efektleri, ortam sesi, müzik veya stil. Görüntüden türetmek için boş bırakın. Varsayılan: "" (boş dize). | STRING | Evet | 0 ile 10000 karakter arası |
| `seed` | Örnekleme için tohum. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 arası |

**Kısıtlamalar:**

* Girdi videosu 10 dakika veya daha kısa olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Orijinal sesin yerine oluşturulan ses parçasının yer aldığı girdi klibi. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaSoundtrackNode/tr.md)

---
**Source fingerprint (SHA-256):** `9820efec607ba52dbabe5e4fb0862240fb0f0215ce7e72914451823b7e75120b`
