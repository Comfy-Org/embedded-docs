# OpenAI ChatGPT Gelişmiş Seçenekler

OpenAIChatConfig düğümü, OpenAI Chat Düğümü'nün yanıtları nasıl ürettiğini kontrol eden gelişmiş seçenekleri tanımlar. Kırpma stratejisini ayarlamanıza, çıktı tokenlarının sayısını sınırlamanıza, özel yönergeler sağlamanıza ve modelin yanıtlamadan önce ne kadar akıl yürütme çabası uygulayacağını seçmenize olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `kırpma` | Model yanıtı için kullanılacak kırpma stratejisi. auto: Bu yanıtın ve önceki yanıtların bağlamı modelin bağlam penceresi boyutunu aşarsa, model konuşmanın ortasındaki girdi öğelerini çıkararak yanıtı bağlam penceresine sığacak şekilde kırpar. disabled: Bir model yanıtı modelin bağlam penceresi boyutunu aşacaksa, istek 400 hatasıyla başarısız olur (varsayılan: "auto") | COMBO | Evet | "auto"<br>"disabled" |
| `maksimum_çıktı_tokenları` | Bir yanıt için üretilebilecek token sayısı üst sınırı; görünür çıktı tokenları ve akıl yürütme tokenları dahildir (varsayılan: 4096) | INT | Hayır | 16 - 16384 |
| `talimatlar` | Modelin yanıtı nasıl üreteceğine ilişkin yönergeler (çok satırlı girdi desteklenir) | STRING | Hayır | - |
| `reasoning_effort` | Modelin yanıtlamadan önce ne kadar akıl yürüteceği. "default" seçimi modele bırakır. Desteklenen seviyeler modele göre farklılık gösterir: GPT-6 Astra low-max, GPT-6 Sol/Luna ve GPT-5.6 none-max (minimal yok), GPT-5.5 none-xhigh, GPT-5.5 Pro medium-xhigh, GPT-5 minimal-high, o-series low-high; GPT-4.1 akıl yürütmeyi desteklemez. Desteklenmeyen seviyeler istek gönderilmeden önce reddedilir. (varsayılan: "default") | COMBO | Hayır | "default"<br>"none"<br>"minimal"<br>"low"<br>"medium"<br>"high"<br>"xhigh"<br>"max" |

Not: `top_p` ve `temperature` API belirtiminde özellik olarak listelense de tüm modeller için desteklenmez ve bu nedenle girdi olarak sunulmaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `OPENAI_CHAT_CONFIG` | Belirtilen gelişmiş ayarları içeren yapılandırma nesnesi; OpenAI Chat Düğümleri ile kullanım içindir | OPENAI_CHAT_CONFIG |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/tr.md)

---
**Source fingerprint (SHA-256):** `4237ad464230c464223c184eab38c7d707a29ba5f47da04c2ec2034cd4347207`
