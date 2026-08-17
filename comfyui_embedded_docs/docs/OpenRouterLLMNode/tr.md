# OpenRouter LLM

OpenRouter LLM düğümü, OpenRouter hizmeti üzerinden sunulan özenle seçilmiş bir dil modeli kümesine bir metin istemi (ve isteğe bağlı olarak görsel veya video) gönderir ve üretilen metin yanıtını döndürür. Anthropic (Claude), OpenAI (GPT), Google (Gemini), xAI (Grok), DeepSeek, Qwen, Mistral, Z.AI (GLM), Moonshot (Kimi) ve Perplexity Sonar modellerini destekler; seçilen model desteklediğinde muhakeme çabası ve web arama bağlamı gibi modele özgü seçenekleri gösterir.

## Girdiler

`model` seçici dinamiktir: bir model seçmek, aşağıdaki ortak girdilere ek olarak modele özgü widget'ları (muhakeme çabası, web arama bağlamı, görsel ve video yuvaları) ortaya çıkarır.

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Yanıtı oluşturmak için kullanılan OpenRouter modeli. Bir model seçmek, modele özgü girdilerini ortaya çıkarır (aşağıdaki model bölümlerine bakın). | DYNAMIC_COMBO | Evet | 34 özenle seçilmiş OpenRouter model seçeneği |
| `prompt` | Modele verilen metin girdisi. En az bir boşluk olmayan karakter içermelidir. | STRING | Evet | Çok satırlı metin |
| `seed` | Örnekleme için seed değeri. Atlamak için 0 olarak ayarlayın. Çoğu model bunu yalnızca bir ipucu olarak kabul eder. (varsayılan: 0) | INT | Evet | 0 ile 2147483647 |
| `system_prompt` | Modelin davranışını belirleyen temel talimatlar. (varsayılan: "") | STRING | Hayır | Çok satırlı metin |

**`seed` hakkında not:** Bu parametre "control_after_generate" davranışına sahiptir; yani kullanıcının widget ayarlarına bağlı olarak her düğüm çalıştırmasından sonra otomatik olarak değişecek şekilde ayarlanabilir (örn. rastgeleleştir, artır veya sabit).

**`system_prompt` hakkında not:** Bu parametre isteğe bağlıdır ve kullanıcı arayüzünde gelişmiş parametre olarak işaretlenmiştir.

### Anthropic Claude Girdileri

`anthropic/claude-opus-5`, `anthropic/claude-opus-4.8`, `anthropic/claude-opus-4.7`, `anthropic/claude-fable-5`, `anthropic/claude-sonnet-5` ve `anthropic/claude-haiku-4.5` modellerinde ortaktır.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Muhakeme çabası. 'off' muhakemeyi tamamen devre dışı bırakır. (varsayılan: "off") | COMBO | Hayır | "off"<br>"low"<br>"medium"<br>"high" |

### OpenAI GPT Girdileri

`openai/gpt-5.6-sol-pro`, `openai/gpt-5.6-sol`, `openai/gpt-5.6-terra-pro`, `openai/gpt-5.6-terra`, `openai/gpt-5.6-luna-pro`, `openai/gpt-5.6-luna`, `openai/gpt-5.5-pro` ve `openai/gpt-5.5` modellerinde ortaktır.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Muhakeme çabası. 'off' muhakemeyi tamamen devre dışı bırakır. (varsayılan: "off") | COMBO | Hayır | "off"<br>"low"<br>"medium"<br>"high" |

### Google Gemini 3.5 Flash Girdileri

`google/gemini-3.5-flash` için geçerlidir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Muhakeme çabası. 'off' muhakemeyi tamamen devre dışı bırakır. (varsayılan: "off") | COMBO | Hayır | "off"<br>"low"<br>"medium"<br>"high" |

### xAI Grok Girdileri

`x-ai/grok-4.5`, `x-ai/grok-4.20` ve `x-ai/grok-4.3` modellerinde ortaktır.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Muhakeme çabası. 'off' muhakemeyi tamamen devre dışı bırakır. (varsayılan: "off") | COMBO | Hayır | "off"<br>"low"<br>"medium"<br>"high" |

### DeepSeek Girdileri

`deepseek/deepseek-v4-pro`, `deepseek/deepseek-v4-flash` ve `deepseek/deepseek-v3.2` modellerinde ortaktır.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Muhakeme çabası. 'off' muhakemeyi tamamen devre dışı bırakır. (varsayılan: "off") | COMBO | Hayır | "off"<br>"low"<br>"medium"<br>"high" |

### Qwen 3.6 Plus ve Flash Girdileri

`qwen/qwen3.6-plus` ve `qwen/qwen3.6-flash` modellerinde ortaktır.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Muhakeme çabası. 'off' muhakemeyi tamamen devre dışı bırakır. (varsayılan: "off") | COMBO | Hayır | "off"<br>"low"<br>"medium"<br>"high" |

### Mistral Large 2512 Girdileri

`mistralai/mistral-large-2512` için geçerlidir. Bu model, modele özgü parametre widget'ı eklemez; yalnızca ortak girdiler ve `images` referans yuvası geçerlidir.

### Mistral Medium 3.5 Girdileri

`mistralai/mistral-medium-3-5` için geçerlidir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Muhakeme çabası. 'off' muhakemeyi tamamen devre dışı bırakır. (varsayılan: "off") | COMBO | Hayır | "off"<br>"low"<br>"medium"<br>"high" |

### Moonshot Kimi K3 ve K2.6 Girdileri

`moonshotai/kimi-k3` ve `moonshotai/kimi-k2.6` modellerinde ortaktır.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Muhakeme çabası. 'off' muhakemeyi tamamen devre dışı bırakır. (varsayılan: "off") | COMBO | Hayır | "off"<br>"low"<br>"medium"<br>"high" |

### Perplexity Sonar Pro Girdileri

`perplexity/sonar-pro` için geçerlidir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `search_context_size` | Alınacak web arama bağlamı miktarı. Daha büyük = daha güvenilir ancak daha yavaş/pahalı. (varsayılan: "medium") | COMBO | Hayır | "low"<br>"medium"<br>"high" |

### Perplexity Sonar Reasoning Pro ve Deep Research Girdileri

`perplexity/sonar-reasoning-pro` ve `perplexity/sonar-deep-research` modellerinde ortaktır.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `search_context_size` | Alınacak web arama bağlamı miktarı. Daha büyük = daha güvenilir ancak daha yavaş/pahalı. (varsayılan: "medium") | COMBO | Hayır | "low"<br>"medium"<br>"high" |
| `reasoning_effort` | Muhakeme çabası. 'off' muhakemeyi tamamen devre dışı bırakır. (varsayılan: "off") | COMBO | Hayır | "off"<br>"low"<br>"medium"<br>"high" |

### Yalnızca Muhakeme Modelleri

`qwen/qwen3.6-max-preview`, `z-ai/glm-4.6`, `z-ai/glm-5` ve `moonshotai/kimi-k2-thinking` modellerinde ortaktır.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Muhakeme çabası. 'off' muhakemeyi tamamen devre dışı bırakır. (varsayılan: "off") | COMBO | Hayır | "off"<br>"low"<br>"medium"<br>"high" |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | İsteğe bağlı referans görsel(ler)i — URL olarak gönderilir. Genişletilebilir yuva: N, seçilen modele bağlı olmak üzere `image_1` ile `image_N` arasını bağlayın. | IMAGE | Hayır | 0 ile N görsel (modele bağlı olarak N = 8, 10 veya 20) |
| `videos` | İsteğe bağlı referans video(lar)ı — URL olarak gönderilir. Genişletilebilir yuva: `video_1` ile `video_N` arasını bağlayın. Yalnızca video desteği olan modellerde kullanılabilir. | VIDEO | Hayır | 0 ile 4 video |

**Model yetenekleri ve sınırları hakkında not:**

- Görsel desteği: Anthropic Claude, OpenAI GPT, Google Gemini 3.5 Flash ve xAI Grok modelleri için en fazla 20 görsel; Qwen 3.6 Plus/Flash ve Moonshot Kimi K3/K2.6 için en fazla 10 görsel; Mistral Large 2512 ve Mistral Medium 3.5 için en fazla 8 görsel. DeepSeek, Qwen 3.6 Max Preview, Z.AI GLM, Moonshot Kimi K2 Thinking ve Perplexity Sonar modelleri görsel kabul etmez.
- Video desteği: yalnızca `google/gemini-3.5-flash`, `qwen/qwen3.6-plus` ve `qwen/qwen3.6-flash` modelleri, en fazla 4 video olacak şekilde video kabul eder.
- Seçilen modelin desteklediğinden daha fazla görsel veya video bağlanırsa düğüm bir hata verir.
- `reasoning_effort` "low", "medium" veya "high" olarak ayarlandığında model dahili olarak muhakeme yapar ancak muhakeme izini döndürmez; "off" muhakemeyi tamamen devre dışı bırakır.
- `search_context_size` widget'ı yalnızca Perplexity Sonar modellerinde görünür. `reasoning_effort` ve `search_context_size` widget'ları gelişmiş parametreler olarak işaretlenmiştir.
- Düğüm, seçilen modele bağlı olarak yaklaşık bir fiyat rozeti (1K token başına USD) görüntüler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Seçilen OpenRouter modelinden üretilen metin yanıtı. | STRING |

**Hatalar hakkında not:** OpenRouter bir API hatası, boş bir yanıt (seçenek yok) veya modelden bir ret döndürürse düğüm bir hata verir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterLLMNode/tr.md)

---
**Source fingerprint (SHA-256):** `534ab9ecc12e35a23a4d8f3e10f4f82d95db8e902ac8a2f2ee0ea68246516f62`
