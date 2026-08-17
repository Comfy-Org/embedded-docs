# OpenAI ChatGPT

Bu düğüm, bir OpenAI modelinden metin yanıtları üretir. Metin isteminizi (ve isteğe bağlı olarak görselleri veya dosyaları) bir OpenAI modeline gönderir ve üretilen metin yanıtını döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Modele gönderilen ve yanıt üretmek için kullanılan metin girdileri (varsayılan: boş) | STRING | Evet | - |
| `persist_context` | Bu parametre kullanımdan kaldırılmıştır ve hiçbir etkisi yoktur (varsayılan: False) | BOOLEAN | Evet | - |
| `model` | Yanıtı üretmek için kullanılan model (varsayılan: `gpt-5`) | COMBO | Evet | `gpt-5.6-sol`<br>`gpt-5.6-terra`<br>`gpt-5.6-luna`<br>`gpt-5.5-pro`<br>`gpt-5.5`<br>`gpt-5`<br>`gpt-5-mini`<br>`gpt-5-nano`<br>`gpt-4.1`<br>`gpt-4.1-mini`<br>`gpt-4.1-nano`<br>`o4-mini`<br>`o3`<br>`o1-pro`<br>`o1` |
| `images` | Model için bağlam olarak kullanılacak isteğe bağlı görseller. Birden fazla görsel eklemek için Batch Images düğümünü kullanabilirsiniz | IMAGE | Hayır | - |
| `files` | Model için bağlam olarak kullanılacak isteğe bağlı dosyalar. OpenAI Chat Input Files düğümünden girişleri kabul eder | OPENAI_INPUT_FILES | Hayır | - |
| `advanced_options` | Model için isteğe bağlı yapılandırma. OpenAI Chat Advanced Options düğümünden girişleri kabul eder | OPENAI_CHAT_CONFIG | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output_text` | OpenAI modeli tarafından üretilen metin yanıtı | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/tr.md)

---
**Source fingerprint (SHA-256):** `25bb3648a4e1ea5668486375153ac4c96b542082c88958d4f62b93adf1db5b2a`
