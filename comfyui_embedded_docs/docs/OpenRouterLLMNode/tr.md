## Genel Bakış

OpenRouter LLM düğümü, OpenRouter hizmeti aracılığıyla sunulan, özenle seçilmiş popüler dil modellerine bir metin istemi gönderir ve oluşturulan metin yanıtını döndürür. xAI, DeepSeek, Qwen, Mistral, Z.AI (GLM), Moonshot (Kimi) ve Perplexity Sonar gibi sağlayıcılardan gelen modelleri destekler ve isteğe bağlı olarak isteğe resim veya video ekleyebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `prompt` | Modele gönderilen metin girişi. | STRING | Evet | Yok |
| `model` | Yanıtı oluşturmak için kullanılan OpenRouter modeli. | STRING | Evet | Birden çok seçenek mevcut (aşağıdaki nota bakın) |
| `seed` | Örnekleme için tohum değeri. 0 olarak ayarlandığında atlanır. Çoğu model bunu yalnızca bir ipucu olarak kabul eder. (varsayılan: 0) | INT | Evet | 0 ile 2147483647 arası |
| `system_prompt` | Modelin davranışını belirleyen temel talimatlar. (varsayılan: "") | STRING | Hayır | Yok |

**`model` parametresi hakkında not:** Mevcut model seçenekleri dinamik olarak oluşturulur ve farklı yeteneklere sahip modeller içerebilir. Bazı modeller, muhakeme çabası, web araması veya resim/video girişleri gibi ek özellikleri destekler. Düğüm, sağlanan resim veya video sayısının modelin desteklediği maksimum sayıyı aşmadığını doğrular.

**`seed` parametresi hakkında not:** `seed` parametresi "control_after_generate" (oluşturma sonrası kontrol) davranışına sahiptir; yani kullanıcının pencere öğesi ayarlarına bağlı olarak her düğüm yürütmesinden sonra otomatik olarak değişecek şekilde (örneğin, rastgele, artımlı veya sabit) ayarlanabilir.

**`system_prompt` hakkında not:** Bu parametre isteğe bağlıdır ve kullanıcı arayüzünde gelişmiş bir parametre olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | OpenRouter modelinden oluşturulan metin yanıtı. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterLLMNode/tr.md)

---
**Source fingerprint (SHA-256):** `24757e36bf2356cc1805a6f071db88ca455e17944695672f19845a4cd1826c8a`
