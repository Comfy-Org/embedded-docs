# SetModelHooksOnCond

Bu düğüm, koşullandırma verilerine özel kancalar ekleyerek model yürütme sırasında koşullandırma sürecine müdahale etmenize ve bu süreci değiştirmenize olanak tanır. Bir dizi kanca alır ve bunları sağlanan koşullandırma verilerine uygulayarak metinden görüntüye oluşturma iş akışının ileri düzeyde özelleştirilmesini sağlar. Eklenen kancalarla birlikte değiştirilmiş koşullandırma, daha sonraki işlem adımlarında kullanılmak üzere döndürülür.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `conditioning` | Kancaların ekleneceği koşullandırma verileri | CONDITIONING | Evet | - |
| `hooks` | Koşullandırma verilerine uygulanacak kanca tanımları | HOOKS | Evet | - |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `conditioning` | Kancalar eklenmiş değiştirilmiş koşullandırma verileri | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetModelHooksOnCond/tr.md)

---
**Source fingerprint (SHA-256):** `a6e63a3a4d94d1b66a82d449af5ae001e1fc4a04f0f81d9fb5c4f8c13e5bdf8b`
