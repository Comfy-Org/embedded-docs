# BriaEraseForeground

Bu düğüm, bir görüntünün ön planını Bria ile kaldırır ve yerine yeni bir arka plan oluşturur. Bria'nın ön plan olarak tanımladığı her şey kaldırılır, yalnızca insanlar değil; dokunulmamış pikseller korunur. Sonuç, 1 megapiksele yakın standart bir boyutta yeniden oluşturulur.

Bu, Bria'nın hizmeti üzerinde çalışan ücretli bir API düğümüdür, bu nedenle her çalıştırmada Comfy API kimlik bilgileriniz kullanılır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Ön planı kaldırılan ve yerine oluşturulmuş bir arka plan konulan görüntü. Yalnızca renk kanalları gönderilir; varsa alfa kanalı yüklemeden önce atılır. | IMAGE | Evet | - |
| `moderation` | Moderasyon ayarları. Görüntüyü moderasyon bayrakları olmadan göndermek için `"false"` seçeneğini veya aşağıdaki içerik moderasyonu anahtarlarını göstermek için `"true"` seçeneğini seçin. Varsayılan: `"false"`. | DYNAMIC_COMBO | Evet | `"false"`<br>`"true"` |

### `"false"` Girdileri

Ek girdi yoktur. İstek, içerik moderasyonu bayrakları olmadan gönderilir.

### `"true"` Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | Girdi görüntüsünde içerik moderasyonunu etkinleştirir. Varsayılan: false. | BOOLEAN | Evet | true<br>false |
| `visual_output_moderation` | Oluşturulan çıktı görüntüsünde içerik moderasyonunu etkinleştirir. Varsayılan: false. | BOOLEAN | Evet | true<br>false |

### Notlar

- Çıktı, 1 megapiksele yakın standart bir boyutta yeniden oluşturulur; bu nedenle döndürülen görüntünün boyutları girdiden farklı olabilir.
- Bu düğüm ücretli bir API düğümüdür; her çalıştırma yaklaşık 0.0572 USD tutar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Ön planı silinmiş ve yerine yeni oluşturulmuş bir arka plan konulmuş girdi görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraseForeground/tr.md)

---
**Source fingerprint (SHA-256):** `4d8c3c5eed97c648b1191ec41931c97caa17e98a8edd1c054ed63e80cc671b05`
