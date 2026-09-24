# OpenAI ChatGPT

Bu düğüm, bir OpenAI modelinden metin yanıtları üretir. Metin isteminizi ve isteğe bağlı olarak görselleri veya dosyaları bir OpenAI modeline gönderir ve üretilen metin yanıtını döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `komut` | Modele gönderilen ve bir yanıt oluşturmak için kullanılan metin girdileri (varsayılan: boş dize). | STRING | Evet | - |
| `bağlamı_sürdür` | Bu parametre kullanımdan kaldırılmıştır ve hiçbir etkisi yoktur (varsayılan: False). | BOOLEAN | Evet | - |
| `model` | Yanıtı oluşturmak için kullanılan model (varsayılan: `gpt-5`) | COMBO | Evet | `gpt-6-astra`<br>`gpt-6-sol`<br>`gpt-6-luna`<br>`gpt-5.6-sol`<br>`gpt-5.6-terra`<br>`gpt-5.6-luna`<br>`gpt-5.5-pro`<br>`gpt-5.5`<br>`gpt-5`<br>`gpt-5-mini`<br>`gpt-5-nano`<br>`gpt-4.1`<br>`gpt-4.1-mini`<br>`gpt-4.1-nano`<br>`o4-mini`<br>`o3`<br>`o1-pro`<br>`o1` |
| `görseller` | Model için bağlam olarak kullanılacak isteğe bağlı görsel(ler). Birden fazla görsel eklemek için Batch Images düğümünü kullanabilirsiniz. | IMAGE | Hayır | - |
| `dosyalar` | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). OpenAI Chat Input Files düğümünden girdileri kabul eder. | OPENAI_INPUT_FILES | Hayır | - |
| `gelişmiş_seçenekler` | Model için isteğe bağlı yapılandırma. OpenAI Chat Advanced Options düğümünden girdileri kabul eder. | OPENAI_CHAT_CONFIG | Hayır | - |

Not: Bir akıl yürütme eforu ayarlayan bir `advanced_options` yapılandırması bağlandığında, seçilen `model` bu efor değerini desteklemelidir. Örneğin, gpt-4.1 model ailesi herhangi bir akıl yürütme eforunu desteklemez; `gpt-6-sol` ve `gpt-6-luna` none, low, medium, high, xhigh ve max değerlerini destekler; `gpt-5.5` none, low, medium, high ve xhigh değerlerini destekler; `gpt-5.5-pro` ise medium, high ve xhigh değerlerini destekler. Akıl yürütme eforu seçilen model tarafından desteklenmiyorsa düğüm hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output_text` | OpenAI modeli tarafından oluşturulan metin yanıtı. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/tr.md)

---
**Source fingerprint (SHA-256):** `46b4558f1368191e2b4eb68f79e098f289c9eb80e1e05f7a516123c098295f2b`
