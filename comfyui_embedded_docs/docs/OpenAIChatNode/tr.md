> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/tr.md)

Bu düğüm, bir OpenAI modelinden metin yanıtları oluşturur. Metin istemleri göndererek ve oluşturulan yanıtları alarak AI modeliyle konuşma yapmanıza olanak tanır. Düğüm, önceki bağlamı hatırlayabildiği çok turlu konuşmaları destekler ve ayrıca model için ek bağlam olarak görselleri ve dosyaları işleyebilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | - | Model için metin girişleri, bir yanıt oluşturmak için kullanılır (varsayılan: boş) |
| `persist_context` | BOOLEAN | Evet | - | Çok turlu konuşma için çağrılar arasında sohbet bağlamını sürdürür (varsayılan: True) |
| `model` | COMBO | Evet | Birden fazla OpenAI modeli mevcut | Yanıt oluşturmak için kullanılacak OpenAI modeli |
| `images` | IMAGE | Hayır | - | Model için bağlam olarak kullanılacak isteğe bağlı görsel(ler). Birden fazla görsel eklemek için Batch Images düğümünü kullanabilirsiniz (varsayılan: None) |
| `files` | OPENAI_INPUT_FILES | Hayır | - | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). OpenAI Chat Input Files düğümünden girişleri kabul eder (varsayılan: None) |
| `advanced_options` | OPENAI_CHAT_CONFIG | Hayır | - | Model için isteğe bağlı yapılandırma. OpenAI Chat Advanced Options düğümünden girişleri kabul eder (varsayılan: None) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output_text` | STRING | OpenAI modeli tarafından oluşturulan metin yanıtı |