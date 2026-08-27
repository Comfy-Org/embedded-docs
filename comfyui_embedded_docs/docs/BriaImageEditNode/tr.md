# Bria Görüntü Düzenleme

Bria FIBO Image Edit düğümü, mevcut bir görseli metin talimatı kullanarak değiştirmenize olanak tanır. Görseli ve isteminizi, isteğinize göre görselin yeni ve düzenlenmiş bir sürümünü oluşturmak için FIBO modelini kullanan Bria API'sine gönderir. Ayrıca düzenlemeleri belirli bir alanla sınırlamak için bir maske de sağlayabilirsiniz.
## Girişler

### Ortak Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|---|---|---|---|---|
| `model` | Görsel düzenleme için kullanılacak model sürümü. | COMBO | Evet | `"FIBO"` |
| `image` | Düzenlemek istediğiniz giriş görseli. | IMAGE | Evet | - |
| `prompt` | Görseli düzenlemek için talimat (varsayılan: boş). | STRING | Evet | - |
| `negative_prompt` | Düzenlenmiş görselde görünmesini istemediğiniz şeyleri tanımlayan metin (varsayılan: boş). | STRING | Evet | - |
| `structured_prompt` | JSON formatında yapılandırılmış düzenleme istemini içeren bir dize. Hassas, programatik kontrol için normal istem yerine bunu kullanın (varsayılan: boş). | STRING | Evet | - |
| `seed` | Rastgele üretimi başlatmak için kullanılan ve tekrarlanabilir sonuçları garanti eden bir sayı (varsayılan: 1). | INT | Evet | 1 to 2147483647 |
| `guidance_scale` | Daha yüksek değer, görselin istemi daha yakından takip etmesini sağlar (varsayılan: 3.0). | FLOAT | Evet | 3.0 to 5.0 |
| `steps` | Modelin gerçekleştireceği gürültü giderme adımı sayısı (varsayılan: 50). | INT | Evet | 20 to 50 |
| `moderation` | Moderasyon ayarları. `"true"` seçildiğinde, istem içeriği, görsel girdi ve görsel çıktı için ek moderasyon seçenekleri görüntülenir. | DYNAMIC_COMBO | Evet | `"false"`<br>`"true"` |
| `mask` | Atlanırsa, düzenleme görselin tamamına uygulanır. | MASK | Hayır | - |

### Moderasyon Girişleri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|---|---|---|---|---|
| `prompt_content_moderation` | prompt_content_moderation (varsayılan: false) | BOOLEAN | Hayır | `true`<br>`false` |
| `visual_input_moderation` | visual_input_moderation (varsayılan: false) | BOOLEAN | Hayır | `true`<br>`false` |
| `visual_output_moderation` | visual_output_moderation (varsayılan: true) | BOOLEAN | Hayır | `true`<br>`false` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|---|---|---|
| `IMAGE` | The edited image returned by the Bria API. | IMAGE |
| `yapılandırılmış_istem` | The structured prompt used or generated during the editing process. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageEditNode/tr.md)

---
**Source fingerprint (SHA-256):** `e66aaa563a82407408f25b289011a491c8b158822fc2db8912daf73731750081`
