# BriaGenFill

Bu düğüm, Bria API'sini kullanarak bir görüntünün maskeli bir bölgesinde nesneler veya sahne oluşturur. Görüntüyü ve maskeyi yükler, istemi Bria üretken dolgu hizmetine gönderir, işlemin tamamlanmasını bekler ve düzenlenmiş görüntüyü döndürür. Bu, ücretli bir API işlemidir (istek başına US$0.0429).
## Girişler

### Ortak Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|---|---|---|---|---|
| `image` | Düzenlenecek girdi görüntüsü. | IMAGE | Evet | - |
| `mask` | Beyaz alanlar oluşturulan içerikle doldurulur, siyah alanlar korunur. Maske gönderilmeden önce ikili hale getirilir; bu nedenle kısmen boyanmış alanlar beyaz sayılır. Görüntüyle aynı en-boy oranına sahip olmalıdır. | MASK | Evet | - |
| `prompt` | Maskeli bölgede ne oluşturulacağının açıklaması. En az 1 karakter içermelidir. | STRING | Evet | - |
| `negative_prompt` | Oluşturulan sonuçta kaçınılması gereken içeriği tanımlayan bir istem. Boş bırakılırsa API'ye gönderilmez. | STRING | Evet | - |
| `refine_prompt` | Daha iyi sonuçlar için istemi otomatik olarak ayarlar; istemi tam olarak yazıldığı gibi kullanmak için devre dışı bırakın. (varsayılan: true) | BOOLEAN | Evet | true<br>false |
| `seed` | Üretim süreci için tohum. (varsayılan: 42) | INT | Evet | 1 to 2147483647 |
| `moderation` | İstek için moderasyon ayarları. "true" olarak ayarlandığında, aşağıda açıklanan iç içe moderasyon seçenekleri uygulanır. (varsayılan: "false") | DYNAMIC_COMBO | Evet | "false"<br>"true" |

### Moderasyon Girişleri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|---|---|---|---|---|
| `prompt_content_moderation` | İsteme içerik moderasyonu uygular. (varsayılan: false) | BOOLEAN | Hayır | true<br>false |
| `visual_input_moderation` | Giriş görüntüsüne içerik moderasyonu uygular. (varsayılan: false) | BOOLEAN | Hayır | true<br>false |
| `visual_output_moderation` | Çıkış görüntüsüne içerik moderasyonu uygular. (varsayılan: false) | BOOLEAN | Hayır | true<br>false |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|---|---|---|
| `image` | The resulting image with the masked region filled by the generated content. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaGenFill/tr.md)

---
**Source fingerprint (SHA-256):** `0d9babfa5e14c03f73d2b5befbd1c5cd1f5ffc685a0d7ccb3db09cfec51ba4fa`
