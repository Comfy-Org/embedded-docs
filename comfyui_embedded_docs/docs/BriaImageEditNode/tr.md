# Bria Görüntü Düzenleme

Bria FIBO Image Edit düğümü, mevcut bir görseli metin talimatı kullanarak değiştirmenize olanak tanır. Görseli ve isteminizi, isteğinize göre görselin yeni ve düzenlenmiş bir sürümünü oluşturmak için FIBO modelini kullanan Bria API'sine gönderir. Ayrıca düzenlemeleri belirli bir alanla sınırlamak için bir maske de sağlayabilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Görsel düzenleme için kullanılacak model sürümü. | COMBO | Evet | `"FIBO"` |
| `görüntü` | Düzenlemek istediğiniz giriş görseli. | IMAGE | Evet | - |
| `istem` | Görseli düzenlemek için talimat (varsayılan: boş). | STRING | Evet | - |
| `negatif_istem` | Düzenlenmiş görselde görünmesini istemediğiniz şeyleri tanımlayan metin (varsayılan: boş). | STRING | Evet | - |
| `yapılandırılmış_istem` | JSON formatında yapılandırılmış düzenleme istemini içeren bir dize. Hassas, programatik kontrol için normal istem yerine bunu kullanın (varsayılan: boş). | STRING | Evet | - |
| `tohum` | Rastgele üretimi başlatmak için kullanılan ve tekrarlanabilir sonuçları garanti eden bir sayı (varsayılan: 1). | INT | Evet | 1 ile 2147483647 arası |
| `yönlendirme_ölçeği` | Daha yüksek değer, görselin istemi daha yakından takip etmesini sağlar (varsayılan: 3.0). | FLOAT | Evet | 3.0 ile 5.0 arası |
| `adımlar` | Modelin gerçekleştireceği gürültü giderme adımı sayısı (varsayılan: 50). | INT | Evet | 20 ile 50 arası |
| `denetleme` | Moderasyon ayarları. `"true"` seçildiğinde, istem içeriği, görsel girdi ve görsel çıktı için ek moderasyon seçenekleri görüntülenir. | DYNAMIC_COMBO | Evet | `"false"`<br>`"true"` |
| `maske` | Atlanırsa, düzenleme görselin tamamına uygulanır. | MASK | Hayır | - |

**Önemli Kısıtlamalar:**

- `prompt` veya `structured_prompt` girdilerinden en az birini sağlamalısınız. İkisi de boş olamaz.
- `moderation` parametresi `"true"` olarak ayarlandığında, üç ek boole girdisi kullanılabilir: `prompt_content_moderation` (varsayılan: false), `visual_input_moderation` (varsayılan: false) ve `visual_output_moderation` (varsayılan: true).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Bria API'si tarafından döndürülen düzenlenmiş görsel. | IMAGE |
| `yapılandırılmış_istem` | Düzenleme sürecinde kullanılan veya oluşturulan yapılandırılmış istem. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageEditNode/tr.md)

---
**Source fingerprint (SHA-256):** `e66aaa563a82407408f25b289011a491c8b158822fc2db8912daf73731750081`
