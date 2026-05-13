> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageEditNode/tr.md)

Bria FIBO Görüntü Düzenleme düğümü, bir metin talimatı kullanarak mevcut bir görüntüyü değiştirmenize olanak tanır. Görüntüyü ve isteminizi, isteğinize göre görüntünün yeni, düzenlenmiş bir sürümünü oluşturmak için FIBO modelini kullanan Bria API'sine gönderir. Düzenlemeleri belirli bir alanla sınırlamak için bir maske de sağlayabilirsiniz.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `"FIBO"` | Görüntü düzenleme için kullanılacak model sürümü. |
| `görüntü` | IMAGE | Evet | - | Düzenlemek istediğiniz giriş görüntüsü. |
| `istem` | STRING | Hayır | - | Görüntünün nasıl düzenleneceğini açıklayan metin talimatı (varsayılan: boş). |
| `negatif_istem` | STRING | Hayır | - | Düzenlenmiş görüntüde görünmesini istemediğiniz şeyleri açıklayan metin (varsayılan: boş). |
| `yapılandırılmış_istem` | STRING | Hayır | - | JSON formatında yapılandırılmış düzenleme istemini içeren bir dize. Hassas, programatik kontrol için normal istem yerine bunu kullanın (varsayılan: boş). |
| `tohum` | INT | Evet | 1 ila 2147483647 | Rastgele oluşturmayı başlatmak için kullanılan, tekrarlanabilir sonuçlar sağlayan bir sayı (varsayılan: 1). |
| `yönlendirme_ölçeği` | FLOAT | Evet | 3,0 ila 5,0 | Oluşturulan görüntünün istemi ne kadar yakından takip edeceğini kontrol eder. Daha yüksek bir değer, daha güçlü bir bağlılıkla sonuçlanır (varsayılan: 3,0). |
| `adımlar` | INT | Evet | 20 ila 50 | Modelin gerçekleştireceği gürültü giderme adımı sayısı (varsayılan: 50). |
| `denetleme` | DYNAMICCOMBO | Evet | `"false"`<br>`"true"` | İçerik denetimini etkinleştirir veya devre dışı bırakır. `"true"` seçilmesi, istem içeriği, görsel giriş ve görsel çıktı için ek denetim seçeneklerini ortaya çıkarır. |
| `maske` | MASK | Hayır | - | İsteğe bağlı bir maske görüntüsü. Sağlanırsa, düzenlemeler yalnızca görüntünün maskelenmiş alanlarına uygulanır. |

**Önemli Kısıtlamalar:**

* `prompt` veya `structured_prompt` girişlerinden en az birini sağlamalısınız. İkisi de aynı anda boş olamaz.
* Tam olarak bir `image` girişi gereklidir.
* `moderation` parametresi `"true"` olarak ayarlandığında, üç ek boolean girişi kullanılabilir hale gelir: `prompt_content_moderation` (varsayılan: false), `visual_input_moderation` (varsayılan: false) ve `visual_output_moderation` (varsayılan: true).

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `yapılandırılmış_istem` | IMAGE | Bria API'si tarafından döndürülen düzenlenmiş görüntü. |
| `yapılandırılmış_istem` | STRING | Düzenleme işlemi sırasında kullanılan veya oluşturulan yapılandırılmış istem. |

---
**Source fingerprint (SHA-256):** `30148261f43f5bfd14339f5ff1ec250381a615cc05c67eee21b0a2423ebe349d`
