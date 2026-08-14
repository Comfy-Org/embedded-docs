# BriaGenFill

Bu düğüm, Bria API'sini kullanarak bir görüntünün maskeli bölgesi içinde nesneler veya manzaralar oluşturur. Görüntüyü ve maskeyi yükler, istemi Bria üretken doldurma hizmetine gönderir, işlemin tamamlanmasını bekler ve düzenlenmiş görüntüyü döndürür. Bu ücretli bir API işlemidir (istek başına US$0.0429).

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Düzenlenecek giriş görüntüsü. | IMAGE | Evet | - |
| `mask` | Beyaz alanlar oluşturulan içerikle doldurulur, siyah alanlar korunur. Maske gönderilmeden önce ikili hale getirilir, bu nedenle kısmen boyanmış alanlar beyaz sayılır. Görüntü ile aynı en-boy oranına sahip olmalıdır. | MASK | Evet | - |
| `prompt` | Maskeli bölgenin içinde ne oluşturulacağına dair açıklama. En az 1 karakter içermelidir. | STRING | Evet | - |
| `negative_prompt` | Oluşturulan sonuçta kaçınılması gereken içeriği tanımlayan bir istem. Boş bırakılırsa API'ye gönderilmez. | STRING | Evet | - |
| `refine_prompt` | Daha iyi sonuçlar için istemi otomatik olarak ayarlar; istemi tam olarak yazıldığı gibi kullanmak için devre dışı bırakın. (varsayılan: true) | BOOLEAN | Evet | true<br>false |
| `seed` | Oluşturma süreci için tohum (seed). (varsayılan: 42) | INT | Evet | 1 ile 2147483647 arası |
| `moderation` | İstek için moderasyon ayarları. "true" olarak ayarlandığında, aşağıda açıklanan iç içe moderasyon seçenekleri uygulanır. (varsayılan: "false") | COMBO | Evet | "false"<br>"true" |

Not: `prompt` boş olmamalıdır ve `mask`, `image` ile aynı en-boy oranına sahip olmalıdır.

`moderation` "true" olarak ayarlandığında, aşağıdaki iç içe boolean seçenekler kullanılabilir:
- `prompt_content_moderation` (varsayılan: false): İsteme içerik moderasyonu uygular.
- `visual_input_moderation` (varsayılan: false): Giriş görüntüsüne içerik moderasyonu uygular.
- `visual_output_moderation` (varsayılan: false): Çıktı görüntüsüne içerik moderasyonu uygular.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Maskeli bölgenin oluşturulan içerikle doldurulduğu sonuç görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaGenFill/tr.md)

---
**Source fingerprint (SHA-256):** `0d9babfa5e14c03f73d2b5befbd1c5cd1f5ffc685a0d7ccb3db09cfec51ba4fa`
