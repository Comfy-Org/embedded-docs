# OpenAI ChatGPT

Bu düğüm, OpenAI'nin GPT modelleriyle metin yanıtları üretir. Bir metin istemi ve isteğe bağlı olarak bağlam sağlayan görseller veya dosyalar gönderir ve yanıtı bir dize olarak döndürür. Tüm ayarlar `model` seçicisinin içinde bulunur: bir model seçildiğinde o modelin kendi `reasoning_effort` seviyeleri, token sınırı, seed değeri ve sistem istemi gösterilir; böylece ayrı bir yapılandırma düğümüne gerek kalmaz. Bu düğüm, kaynak kodunda artık kullanımdan kaldırılmış olarak işaretlenen eski OpenAI ChatGPT düğümünün yerini alır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Yanıtı oluşturmak için kullanılan model. Her model, desteklediği `reasoning_effort` seviyelerini sunar (varsayılan: `"gpt-6.2-sol"`). | DYNAMIC_COMBO | Evet | `"gpt-6.2-sol"`<br>`"gpt-6.2-astra"`<br>`"gpt-6-astra"`<br>`"gpt-6.1-sol"`<br>`"gpt-6.1-terra"`<br>`"gpt-6-sol"`<br>`"gpt-6-luna"`<br>`"gpt-5.6-sol"`<br>`"gpt-5.6-terra"`<br>`"gpt-5.6-luna"`<br>`"gpt-5.5-pro"`<br>`"gpt-5.5"` |
| `prompt` | Modele verilen metin girdisi (varsayılan: boş dize). | STRING | Evet | - |
| `images` | Genişletilebilir yuva: 1..16 öğe bağlayın (`image_1`, `image_2`, ...). Model için bağlam olarak kullanılan isteğe bağlı görsel(ler). | IMAGE | Hayır | 0 ile 16 görsel arası |
| `files` | Model için bağlam olarak kullanılan isteğe bağlı dosya(lar). OpenAI ChatGPT Input Files düğümünden girdileri kabul eder. | OPENAI_INPUT_FILES | Hayır | - |
| `reasoning_effort` | Modelin yanıt vermeden önce ne kadar akıl yürüteceği. Daha yüksek seviyeler daha fazla token kullanır ve daha uzun sürer. Sunulan seviyeler seçilen modele bağlıdır (varsayılan: `"medium"`, `gpt-5.5-pro` için `"high"`). | COMBO | Evet | Aşağıdaki model başına listeye bakın |
| `max_output_tokens` | Üretilecek maksimum token sayısı; reasoning token'ları dahil. Düşük bir değer, yüksek bir `reasoning_effort` ile birlikte yanıt için yer bırakmayabilir (varsayılan: 32768). | INT | Evet | 16 ile 128000 arası |
| `seed` | Seed, düğümün yeniden çalışması gerekip gerekmediğini kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir (varsayılan: 42). | INT | Evet | 0 ile 2147483647 arası |
| `system_prompt` | Modelin davranışını belirleyen temel talimatlar (varsayılan: boş dize). | STRING | Hayır | - |

### Model başına akıl yürütme çabası seviyeleri

- `gpt-6.2-sol`, `gpt-6.2-astra`, `gpt-6-astra`, `gpt-6.1-sol`: `"low"`, `"medium"`, `"high"`, `"xhigh"`, `"max"`, varsayılan `"medium"`.
- `gpt-6.1-terra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`: `"none"`, `"low"`, `"medium"`, `"high"`, `"xhigh"`, `"max"`, varsayılan `"medium"`.
- `gpt-5.5-pro`: `"medium"`, `"high"`, `"xhigh"`, varsayılan `"high"`.
- `gpt-5.5`: `"none"`, `"low"`, `"medium"`, `"high"`, `"xhigh"`, varsayılan `"medium"`.

### Davranışla ilgili notlar

- Yalnızca yanıt metni döndürülür. Modelin düşünürken yorum aşamasında yaydığı mesajlar atlanır.
- Yanıt yazılmadan önce token bütçesi tükenirse düğüm, `max_output_tokens` değerini artırmanızı söyleyen bir hata verir.
- Görseller kendi çözünürlüklerinde ve API'nin otomatik ayrıntı düzeyiyle gönderilir; bu nedenle büyük görseller daha fazla token kullanır.
- Her istek OpenAI tarafında saklanır ve döndürülen metin, yanıt parçalarını yeni satırlarla birleştirir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | OpenAI modeli tarafından oluşturulan metin yanıtı. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNodeV2/tr.md)

---
**Source fingerprint (SHA-256):** `129c13a6c7b76d142c0a23234ab5e707a1dd39a99055974277d46a39593aa7ba`
