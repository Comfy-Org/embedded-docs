# OpenRouter LLM

OpenRouter LLM düğümü, OpenRouter hizmeti aracılığıyla sunulan özenle seçilmiş bir dizi popüler dil modeline bir metin istemi gönderir ve oluşturulan metin yanıtını döndürür. Anthropic (Claude), OpenAI (GPT), Google (Gemini), xAI (Grok), DeepSeek, Qwen, Mistral, Z.AI (GLM), Moonshot (Kimi) ve Perplexity Sonar modellerini destekler ve isteğe bağlı olarak görselleri veya videoları referans girdileri olarak ekleyebilir.

## Girdiler

`model` seçicide bir model seçildiğinde, düğüm seçilen modelin yeteneklerine bağlı olarak ortak girdilerin üzerinde modele özgü widget'ları gösterir — akıl yürütme çabası, web arama boyutu ve/veya referans medya yuvaları.

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Modele metin girdisi. | STRING | Evet | Yok |
| `model` | Yanıtı oluşturmak için kullanılan OpenRouter modeli. | DYNAMIC_COMBO | Evet | Birden fazla seçenek mevcut (aşağıdaki model bölümlerine bakın) |
| `seed` | Örnekleme için tohum (seed). Atlamak için 0 olarak ayarlayın. Çoğu model bunu yalnızca bir ipucu olarak ele alır. (varsayılan: 0) | INT | Evet | 0 ile 2147483647 arası |
| `system_prompt` | Modelin davranışını belirleyen temel talimatlar. (varsayılan: "") | STRING | Hayır | Yok |

### Anthropic Claude Modelleri Girdileri

Şu modellerde ortaktır: `anthropic/claude-opus-5`, `anthropic/claude-opus-4.8`, `anthropic/claude-opus-4.7`, `anthropic/claude-fable-5`, `anthropic/claude-sonnet-5` ve `anthropic/claude-haiku-4.5`.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Akıl yürütme çabası. 'off' akıl yürütmeyi tamamen devre dışı bırakır. (varsayılan: "off") | COMBO | Hayır | "off"<br>"low"<br>"medium"<br>"high" |

Bu modeller en fazla 20 referans görselini destekler (bkz. Referans Girdileri).

### OpenAI GPT Modelleri Girdileri

Şu modellerde ortaktır: `openai/gpt-5.6-sol-pro`, `openai/gpt-5.6-sol`, `openai/gpt-5.6-terra-pro`, `openai/gpt-5.6-terra`, `openai/gpt-5.6-luna-pro`, `openai/gpt-5.6-luna`, `openai/gpt-5.5-pro` ve `openai/gpt-5.5`.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Akıl yürütme çabası. 'off' akıl yürütmeyi tamamen devre dışı bırakır. (varsayılan: "off") | COMBO | Hayır | "off"<br>"low"<br>"medium"<br>"high" |

Bu modeller en fazla 20 referans görselini destekler (bkz. Referans Girdileri).

### Google Gemini 3.5 Flash Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Akıl yürütme çabası. 'off' akıl yürütmeyi tamamen devre dışı bırakır. (varsayılan: "off") | COMBO | Hayır | "off"<br>"low"<br>"medium"<br>"high" |

Bu model en fazla 20 referans görselini ve en fazla 4 referans videosunu destekler (bkz. Referans Girdileri).

### xAI Grok Modelleri Girdileri

Şu modellerde ortaktır: `x-ai/grok-4.5`, `x-ai/grok-4.20` ve `x-ai/grok-4.3`.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Akıl yürütme çabası. 'off' akıl yürütmeyi tamamen devre dışı bırakır. (varsayılan: "off") | COMBO | Hayır | "off"<br>"low"<br>"medium"<br>"high" |

Bu modeller en fazla 20 referans görselini destekler (bkz. Referans Girdileri).

### DeepSeek Modelleri Girdileri

Şu modellerde ortaktır: `deepseek/deepseek-v4-pro`, `deepseek/deepseek-v4-flash` ve `deepseek/deepseek-v3.2`.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Akıl yürütme çabası. 'off' akıl yürütmeyi tamamen devre dışı bırakır. (varsayılan: "off") | COMBO | Hayır | "off"<br>"low"<br>"medium"<br>"high" |

Yalnızca metin modelleri — referans görseli veya videosu yok.

### Qwen 3.6 Max Preview Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Akıl yürütme çabası. 'off' akıl yürütmeyi tamamen devre dışı bırakır. (varsayılan: "off") | COMBO | Hayır | "off"<br>"low"<br>"medium"<br>"high" |

Yalnızca metin modeli — referans görseli veya videosu yok.

### Qwen 3.6 Plus ve Qwen 3.6 Flash Girdileri

Şu modellerde ortaktır: `qwen/qwen3.6-plus` ve `qwen/qwen3.6-flash`.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Akıl yürütme çabası. 'off' akıl yürütmeyi tamamen devre dışı bırakır. (varsayılan: "off") | COMBO | Hayır | "off"<br>"low"<br>"medium"<br>"high" |

Bu modeller en fazla 10 referans görselini ve en fazla 4 referans videosunu destekler (bkz. Referans Girdileri).

### Mistral Large 2512 Girdileri

Profile özgü girdi bulunmuyor (standart profil). Bu model en fazla 8 referans görselini destekler (bkz. Referans Girdileri).

### Mistral Medium 3.5 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Akıl yürütme çabası. 'off' akıl yürütmeyi tamamen devre dışı bırakır. (varsayılan: "off") | COMBO | Hayır | "off"<br>"low"<br>"medium"<br>"high" |

Bu model en fazla 8 referans görselini destekler (bkz. Referans Girdileri).

### Z.AI GLM Modelleri Girdileri

Şu modellerde ortaktır: `z-ai/glm-4.6` ve `z-ai/glm-5`.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Akıl yürütme çabası. 'off' akıl yürütmeyi tamamen devre dışı bırakır. (varsayılan: "off") | COMBO | Hayır | "off"<br>"low"<br>"medium"<br>"high" |

Yalnızca metin modelleri — referans görseli veya videosu yok.

### Moonshot Kimi K3 ve K2.6 Girdileri

Şu modellerde ortaktır: `moonshotai/kimi-k3` ve `moonshotai/kimi-k2.6`.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Akıl yürütme çabası. 'off' akıl yürütmeyi tamamen devre dışı bırakır. (varsayılan: "off") | COMBO | Hayır | "off"<br>"low"<br>"medium"<br>"high" |

Bu modeller en fazla 10 referans görselini destekler (bkz. Referans Girdileri).

### Moonshot Kimi K2 Thinking Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Akıl yürütme çabası. 'off' akıl yürütmeyi tamamen devre dışı bırakır. (varsayılan: "off") | COMBO | Hayır | "off"<br>"low"<br>"medium"<br>"high" |

Yalnızca metin modeli — referans görseli veya videosu yok.

### Perplexity Sonar Pro Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `search_context_size` | Ne kadar web arama bağlamı alınacağı. Daha büyük = daha gerçeklere dayanan ancak daha yavaş/pahalı. (varsayılan: "medium") | COMBO | Hayır | "low"<br>"medium"<br>"high" |

Yalnızca metin modeli — referans görseli veya videosu yok.

### Perplexity Sonar Reasoning Pro ve Sonar Deep Research Girdileri

Şu modellerde ortaktır: `perplexity/sonar-reasoning-pro` ve `perplexity/sonar-deep-research`.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `search_context_size` | Ne kadar web arama bağlamı alınacağı. Daha büyük = daha gerçeklere dayanan ancak daha yavaş/pahalı. (varsayılan: "medium") | COMBO | Hayır | "low"<br>"medium"<br>"high" |
| `reasoning_effort` | Akıl yürütme çabası. 'off' akıl yürütmeyi tamamen devre dışı bırakır. (varsayılan: "off") | COMBO | Hayır | "off"<br>"low"<br>"medium"<br>"high" |

Yalnızca metin modelleri — referans görseli veya videosu yok.

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | İsteğe bağlı referans görsel(ler)i, URL olarak gönderilir. Genişletilebilir yuva: 1..N görsel girdisini bağlayın (`image_1`, `image_2`, ...); sayı sınırı seçilen modele bağlıdır (bkz. model bölümleri). | IMAGE | Hayır | 0 ile 20 arası (modele bağlı: 8, 10 veya 20) |
| `videos` | İsteğe bağlı referans video(lar)ı, URL olarak gönderilir. Genişletilebilir yuva: 1..N video girdisini bağlayın (`video_1`, `video_2`, ...); sayı sınırı seçilen modele bağlıdır (bkz. model bölümleri). | VIDEO | Hayır | 0 ile 4 arası (modele bağlı) |

**Notlar:**

- **Kullanılabilir modeller:** Kullanılabilir model seçenekleri dinamik olarak oluşturulur ve farklı yeteneklere sahip modelleri içerir. 34 modelin tam listesi şu şekildedir:
  - Anthropic: `anthropic/claude-opus-5`, `anthropic/claude-opus-4.8`, `anthropic/claude-opus-4.7`, `anthropic/claude-fable-5`, `anthropic/claude-sonnet-5`, `anthropic/claude-haiku-4.5`
  - OpenAI: `openai/gpt-5.6-sol-pro`, `openai/gpt-5.6-sol`, `openai/gpt-5.6-terra-pro`, `openai/gpt-5.6-terra`, `openai/gpt-5.6-luna-pro`, `openai/gpt-5.6-luna`, `openai/gpt-5.5-pro`, `openai/gpt-5.5`
  - Google: `google/gemini-3.5-flash`
  - xAI: `x-ai/grok-4.5`, `x-ai/grok-4.20`, `x-ai/grok-4.3`
  - DeepSeek: `deepseek/deepseek-v4-pro`, `deepseek/deepseek-v4-flash`, `deepseek/deepseek-v3.2`
  - Qwen: `qwen/qwen3.6-max-preview`, `qwen/qwen3.6-plus`, `qwen/qwen3.6-flash`
  - Mistral: `mistralai/mistral-large-2512`, `mistralai/mistral-medium-3-5`
  - Z.AI: `z-ai/glm-4.6`, `z-ai/glm-5`
  - Moonshot: `moonshotai/kimi-k3`, `moonshotai/kimi-k2.6`, `moonshotai/kimi-k2-thinking`
  - Perplexity: `perplexity/sonar-pro`, `perplexity/sonar-reasoning-pro`, `perplexity/sonar-deep-research`

- **Görsel ve video kısıtlamaları:** Referans görsellerinin ve videolarının maksimum sayısı seçilen modele bağlıdır. Sağlanan toplam görsel veya video sayısı modelin sınırını aşarsa düğüm bir hata verir. Görsel veya video desteği olmayan modeller, ilgili referans yuvalarını göstermez.

- **Akıl yürütme davranışı:** `reasoning_effort` "off" dışında bir değere ayarlandığında, istek sağlayıcıdan akıl yürütme izini döndürmeden dahili olarak akıl yürütmesini ister.

- **Tohum (seed) davranışı:** `seed` parametresi "control_after_generate" davranışına sahiptir; yani kullanıcının widget ayarlarına bağlı olarak her düğüm yürütmesinden sonra otomatik olarak değişecek şekilde (örn. rastgeleleştir, artır veya sabit) ayarlanabilir.

- **Sistem istemi:** `system_prompt` parametresi isteğe bağlıdır ve kullanıcı arayüzünde gelişmiş bir parametre olarak işaretlenmiştir.

- **Hata durumları:** Düğüm; boşluklar temizlendikten sonra istem boşsa, OpenRouter bir hata döndürürse, seçilen model yanıt vermeyi reddederse veya yanıt hiçbir seçenek ya da mesaj içermiyorsa bir hata verir. Düğümdeki fiyat rozeti, seçilen modele göre 1K token başına yaklaşık maliyet tahminini gösterir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | OpenRouter modelinden üretilen metin yanıtı. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterLLMNode/tr.md)

---
**Source fingerprint (SHA-256):** `534ab9ecc12e35a23a4d8f3e10f4f82d95db8e902ac8a2f2ee0ea68246516f62`
