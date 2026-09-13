# OpenAI ChatGPT Gelişmiş Seçenekler

OpenAIChatConfig düğümü, OpenAI Chat Node'un yanıtları nasıl oluşturduğunu kontrol eden gelişmiş seçenekleri tanımlar. Kesme stratejisini ayarlamanıza, çıktı token sayısını sınırlamanıza, özel talimatlar sağlamanıza ve modelin yanıtlamadan önce ne kadar akıl yürütme çabası uygulayacağını seçmenize olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `truncation` | Model yanıtı için kullanılacak kesme stratejisi. auto: Bu yanıtın ve önceki yanıtların bağlamı modelin bağlam pencere boyutunu aşarsa, model konuşmanın ortasındaki girdi öğelerini bırakarak yanıtı bağlam penceresine sığacak şekilde kısaltır. disabled: Bir model yanıtı modelin bağlam pencere boyutunu aşacaksa, istek 400 hatasıyla başarısız olur (varsayılan: "auto") | COMBO | Evet | "auto"<br>"disabled" |
| `max_output_tokens` | Bir yanıt için üretilebilecek token sayısı üst sınırı; görünür çıktı token'ları ve akıl yürütme token'ları dahil (varsayılan: 4096) | INT | Hayır | 16 ile 16384 |
| `instructions` | Modelin yanıtı nasıl oluşturacağına ilişkin talimatlar (çok satırlı girdi desteklenir) | STRING | Hayır | - |
| `reasoning_effort` | Modelin yanıtlamadan önce ne kadar akıl yürüttüğü. "default" seçimi modele bırakır. Desteklenen seviyeler modele göre farklılık gösterir: GPT-6 Astra low-max, GPT-5.6 none-max (minimal yok), GPT-5.5 none-xhigh, GPT-5.5 Pro medium-xhigh, GPT-5 minimal-high, o-series low-high; GPT-4.1'de akıl yürütme yoktur. Desteklenmeyen seviyeler, istek gönderilmeden önce reddedilir. (varsayılan: "default") | COMBO | Hayır | "default"<br>"none"<br>"minimal"<br>"low"<br>"medium"<br>"high"<br>"xhigh"<br>"max" |

Not: `top_p` ve `temperature` API spesifikasyonunda özellik olarak listelense de tüm modeller tarafından desteklenmez ve bu nedenle girdi olarak sunulmaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `OPENAI_CHAT_CONFIG` | Belirtilen gelişmiş ayarları içeren ve OpenAI Chat Node'larıyla kullanılacak yapılandırma nesnesi | OPENAI_CHAT_CONFIG |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/tr.md)

---
**Source fingerprint (SHA-256):** `37d18a13b9d5bb36359603e5bab5918e7fea200ac552ea8439fff1488a88263c`
