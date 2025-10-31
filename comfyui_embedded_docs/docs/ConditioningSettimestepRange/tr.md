> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetTimestepRange/tr.md)

Bu düğüm, belirli bir zaman adımı aralığı ayarlayarak koşullandırmanın zamansal boyutunu ayarlamak için tasarlanmıştır. Koşullandırma sürecinin başlangıç ve bitiş noktaları üzerinde hassas kontrol sağlayarak, daha hedefli ve verimli üretime olanak tanır.

## Girdiler

| Parametre | Veri Türü | Açıklama |
| --- | --- | --- |
| `CONDITIONING` | CONDITIONING | Koşullandırma girdisi, üretim sürecinin mevcut durumunu temsil eder ve bu düğüm, belirli bir zaman adımı aralığı ayarlayarak bu durumu değiştirir. |
| `start` | `FLOAT` | Başlangıç parametresi, zaman adımı aralığının başlangıcını, toplam üretim sürecinin yüzdesi olarak belirler ve koşullandırma etkilerinin ne zaman başlayacağı üzerinde hassas kontrol sağlar. |
| `end` | `FLOAT` | Bitiş parametresi, zaman adımı aralığının bitiş noktasını yüzde olarak tanımlar ve koşullandırma etkilerinin süresi ve sonlanması üzerinde hassas kontrol sağlar. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
| --- | --- | --- |
| `CONDITIONING` | CONDITIONING | Çıktı, belirtilen zaman adımı aralığı uygulanmış, daha fazla işlem veya üretim için hazır, değiştirilmiş koşullandırmadır. |