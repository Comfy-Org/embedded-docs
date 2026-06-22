# Bria Görüntü Düzenleme

Bria FIBO Görüntü Düzenleme düğümü, bir metin talimatı kullanarak mevcut bir görüntüyü değiştirmenize olanak tanır. Görüntüyü ve isteminizi, isteğinize göre görüntünün yeni, düzenlenmiş bir sürümünü oluşturmak için FIBO modelini kullanan Bria API'sine gönderir. Düzenlemeleri belirli bir alanla sınırlamak için bir maske de sağlayabilirsiniz.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Görüntü düzenleme için kullanılacak model sürümü. | COMBO | Evet | `"FIBO"` |
| `görüntü` | Düzenlemek istediğiniz giriş görüntüsü. | IMAGE | Evet | - |
| `istem` | Görüntünün nasıl düzenleneceğini açıklayan metin talimatı (varsayılan: boş). | STRING | Hayır | - |
| `negatif_istem` | Düzenlenmiş görüntüde görünmesini istemediğiniz şeyleri açıklayan metin (varsayılan: boş). | STRING | Hayır | - |
| `yapılandırılmış_istem` | JSON formatında yapılandırılmış düzenleme istemini içeren bir dize. Hassas, programatik kontrol için normal istem yerine bunu kullanın (varsayılan: boş). | STRING | Hayır | - |
| `tohum` | Rastgele oluşturmayı başlatmak için kullanılan, tekrarlanabilir sonuçlar sağlayan bir sayı (varsayılan: 1). | INT | Evet | 1 ila 2147483647 |
| `yönlendirme_ölçeği` | Oluşturulan görüntünün istemi ne kadar yakından takip edeceğini kontrol eder. Daha yüksek bir değer, daha güçlü bir bağlılıkla sonuçlanır (varsayılan: 3,0). | FLOAT | Evet | 3,0 ila 5,0 |
| `adımlar` | Modelin gerçekleştireceği gürültü giderme adımı sayısı (varsayılan: 50). | INT | Evet | 20 ila 50 |
| `denetleme` | İçerik denetimini etkinleştirir veya devre dışı bırakır. `"true"` seçilmesi, istem içeriği, görsel giriş ve görsel çıktı için ek denetim seçeneklerini ortaya çıkarır. | DYNAMICCOMBO | Evet | `"false"`<br>`"true"` |
| `maske` | İsteğe bağlı bir maske görüntüsü. Sağlanırsa, düzenlemeler yalnızca görüntünün maskelenmiş alanlarına uygulanır. | MASK | Hayır | - |

**Önemli Kısıtlamalar:**

* `prompt` veya `structured_prompt` girişlerinden en az birini sağlamalısınız. İkisi de aynı anda boş olamaz.
* Tam olarak bir `image` girişi gereklidir.
* `moderation` parametresi `"true"` olarak ayarlandığında, üç ek boolean girişi kullanılabilir hale gelir: `prompt_content_moderation` (varsayılan: false), `visual_input_moderation` (varsayılan: false) ve `visual_output_moderation` (varsayılan: true).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `yapılandırılmış_istem` | Bria API'si tarafından döndürülen düzenlenmiş görüntü. | IMAGE |
| `yapılandırılmış_istem` | Düzenleme işlemi sırasında kullanılan veya oluşturulan yapılandırılmış istem. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageEditNode/tr.md)

---
**Source fingerprint (SHA-256):** `30148261f43f5bfd14339f5ff1ec250381a615cc05c67eee21b0a2423ebe349d`
