> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/tr.md)

OpenAIChatConfig düğümü, OpenAI Chat Node için ek yapılandırma seçenekleri ayarlamaya olanak tanır. Modelin yanıtları nasıl oluşturacağını kontrol eden, kesme davranışı, çıktı uzunluk sınırları ve özel talimatlar dahil olmak üzere gelişmiş ayarlar sağlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `truncation` | COMBO | Evet | `"auto"`<br>`"disabled"` | Model yanıtı için kullanılacak kesme stratejisi. auto: Bu yanıtın ve öncekilerin bağlamı modelin bağlam penceresi boyutunu aşarsa, model, konuşmanın ortasındaki girdi öğelerini atarak yanıtı bağlam penceresine sığacak şekilde kesecektir. disabled: Bir model yanıtı, bir model için bağlam penceresi boyutunu aşacaksa, istek 400 hatasıyla başarısız olur (varsayılan: "auto") |
| `max_output_tokens` | INT | Hayır | 16-16384 | Görünür çıktı token'ları dahil olmak üzere, bir yanıt için oluşturulabilecek token sayısı için bir üst sınır (varsayılan: 4096) |
| `instructions` | STRING | Hayır | - | Model yanıtı için ek talimatlar (çok satırlı girdi desteklenir) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `OPENAI_CHAT_CONFIG` | OPENAI_CHAT_CONFIG | OpenAI Chat Node'ları ile kullanım için belirtilen ayarları içeren yapılandırma nesnesi |