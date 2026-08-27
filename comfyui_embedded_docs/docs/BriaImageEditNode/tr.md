# Bria Görüntü Düzenleme

Bria FIBO Image Edit düğümü, mevcut bir görüntüyü metin talimatı kullanarak düzenler. Görüntüyü ve isteminizi Bria API'sine gönderir; burada FIBO modeli düzenlenmiş bir sürüm oluşturur. İsteğe bağlı bir maske, değişiklikleri belirli bir alanla sınırlayabilir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Görüntü düzenleme için kullanılacak model sürümü. | COMBO | Evet | `"FIBO"` |
| `görüntü` | Düzenlemek istediğiniz giriş görüntüsü. | IMAGE | Evet | - |
| `istem` | Görüntüyü düzenleme talimatı (varsayılan: boş). | STRING | Evet | - |
| `negatif_istem` | Düzenlenmiş görüntüde görünmesini istemediğiniz şeyleri tanımlayan metin (varsayılan: boş). | STRING | Evet | - |
| `yapılandırılmış_istem` | JSON formatında yapılandırılmış düzenleme istemini içeren bir dize. Hassas, programatik kontrol için normal istem yerine bunu kullanın (varsayılan: boş). | STRING | Evet | - |
| `tohum` | Rastgele üretimi başlatmak için kullanılan ve tekrarlanabilir sonuçlar sağlayan bir sayı (varsayılan: 1). | INT | Evet | 1 ila 2147483647 |
| `yönlendirme_ölçeği` | Daha yüksek değer, görüntünün istemi daha yakından takip etmesini sağlar (varsayılan: 3). | FLOAT | Evet | 3.0 ila 5.0 |
| `adımlar` | Model tarafından gerçekleştirilen gürültü giderme adımı sayısı (varsayılan: 50). | INT | Evet | 20 ila 50 |
| `denetleme` | Moderasyon ayarları. `"true"` seçilmesi ek moderasyon seçeneklerini ortaya çıkarır. | DYNAMIC_COMBO | Evet | `"false"`<br>`"true"` |
| `maske` | Atlanırsa, düzenleme görüntünün tamamına uygulanır. | MASK | Hayır | - |

### Moderasyon Girdileri

`moderation` `"true"` olarak ayarlandığında, şu ek girdiler kullanılabilir hale gelir:

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt_content_moderation` | İstem metninin uygunsuz içerik için denetlenip denetlenmeyeceği (varsayılan: false). | BOOLEAN | Hayır | `true`<br>`false` |
| `visual_input_moderation` | Giriş görüntüsünün uygunsuz içerik için denetlenip denetlenmeyeceği (varsayılan: false). | BOOLEAN | Hayır | `true`<br>`false` |
| `visual_output_moderation` | Düzenlenmiş çıktı görüntüsünün uygunsuz içerik için denetlenip denetlenmeyeceği (varsayılan: true). | BOOLEAN | Hayır | `true`<br>`false` |

**Önemli Kısıtlamalar:**

- `prompt` veya `structured_prompt` alanlarından en az biri boş olmamalıdır. İkisi de boşsa, düğüm bir hata verir.
- `moderation` `"true"` olarak ayarlandığında, yukarıdaki üç moderasyon girdisi gösterilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Bria API tarafından döndürülen düzenlenmiş görüntü. | IMAGE |
| `yapılandırılmış_istem` | Düzenleme sürecinde kullanılan veya oluşturulan yapılandırılmış istem. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageEditNode/tr.md)

---
**Source fingerprint (SHA-256):** `e66aaa563a82407408f25b289011a491c8b158822fc2db8912daf73731750081`
