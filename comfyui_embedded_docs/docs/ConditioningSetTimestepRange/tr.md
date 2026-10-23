# KoşullandırmaZamanAdımıAralığıAyarla

Bu düğüm, belirli bir zaman adımı aralığı ayarlayarak koşullandırmanın zamansal yönünü ayarlamak için tasarlanmıştır. Koşullandırma sürecinin başlangıç ve bitiş noktaları üzerinde hassas kontrol sağlayarak daha hedefli ve verimli bir üretim yapılmasına olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Koşullandırma girişi, üretim sürecinin mevcut durumunu temsil eder. Bu düğüm, belirli bir zaman adımı aralığı belirleyerek bu durumu değiştirir. | CONDITIONING |
| `başlangıç` | Başlangıç parametresi, zaman adımı aralığının başlangıcını toplam üretim sürecinin yüzdesi olarak belirtir. Koşullandırma etkilerinin ne zaman başlayacağı üzerinde ince ayar yapılmasını sağlar. | `FLOAT` |
| `bitiş` | Bitiş parametresi, zaman adımı aralığının bitiş noktasını yüzde olarak tanımlar. Koşullandırma etkilerinin süresi ve sonlanması üzerinde hassas kontrol sağlar. | `FLOAT` |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Çıktı, belirtilen zaman adımı aralığı uygulanmış, daha sonraki işlemlere veya üretime hazır, değiştirilmiş koşullandırmadır. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetTimestepRange/tr.md)
