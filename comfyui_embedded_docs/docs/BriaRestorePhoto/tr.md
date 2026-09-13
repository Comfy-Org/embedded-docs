# BriaRestorePhoto

Bu düğüm, eski veya hasarlı fotoğrafları Bria API'si aracılığıyla onarır. Gren, çizik ve bulanıklığı giderir, yaşa bağlı renk sapmalarını nötralize eder, karton montajlarını ve stüdyo kenarlıklarını kırpabilir ve yüzleri yeniden çizer. Sonuç yaklaşık 1 megapikselde yeniden oluşturulur, bu nedenle girdiyle piksel hizalı değildir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Onarılacak fotoğraf. Yüklemeden önce alfa kanalı kaldırılır. | IMAGE | Evet | - |
| `moderation` | İstek için moderasyon ayarları. `"true"` seçildiğinde iki ek boolean anahtar görünür; `"false"` seçildiğinde hiçbir moderasyon bayrağı gönderilmez. Varsayılan: `"false"`. | DYNAMIC_COMBO | Evet | `"false"`<br>`"true"` |

### Moderasyon Girdileri

Bu girdiler yalnızca `moderation` `"true"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | Girdi görüntüsünde görsel içerik moderasyonunu etkinleştirir. Varsayılan: false. | BOOLEAN | Hayır | true<br>false |
| `visual_output_moderation` | Çıktı görüntüsünde görsel içerik moderasyonunu etkinleştirir. Varsayılan: false. | BOOLEAN | Hayır | true<br>false |

**Not:** Düğüm tüm kareyi yaklaşık 1 megapikselde yeniden oluşturur; bu nedenle sonuç girdiyle piksel hizalı değildir. Görüntüyü büyütmek için bu düğüm yerine Bria Increase Resolution düğümünü kullanın.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-----------|-----------|
| `IMAGE` | Bria tarafından döndürülen onarılmış fotoğraf. | IMAGE |
| `structured_prompt` | Düzenlenen görüntünün yapılandırılmış açıklaması; Bria FIBO Image Edit ile sonraki bir düzenleme için. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRestorePhoto/tr.md)

---
**Source fingerprint (SHA-256):** `387ec3e049464f185e27f79d160ade2a4170ab238853064c008892d84523fa68`
