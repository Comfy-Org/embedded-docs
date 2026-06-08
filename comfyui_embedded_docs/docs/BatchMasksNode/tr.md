Topluluk Maskeleme düğümü, birden fazla bireysel maske girdisini tek bir toplulukta birleştirir. Değişken sayıda maske girdisi alır ve bunları tek bir toplu maske tensörü olarak çıktılar, böylece sonraki düğümlerde maskelerin toplu olarak işlenmesine olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `mask_0` | İlk maske girdisi. | MASK | Evet | - |
| `mask_1` | İkinci maske girdisi. | MASK | Evet | - |
| `mask_2` ile `mask_49` arası | Ek isteğe bağlı maske girdileri. Düğüm, toplamda en az 2 ve en fazla 50 maske kabul edebilir. | MASK | Hayır | - |

**Not:** Bu düğüm, otomatik büyüyen bir girdi şablonu kullanır. En az iki maske (`mask_0` ve `mask_1`) bağlamanız gerekir. Toplam 50 maske için en fazla 48 isteğe bağlı maske girdisi daha (`mask_2` ile `mask_49` arası) ekleyebilirsiniz. Bağlanan tüm maskeler tek bir toplulukta birleştirilecektir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Tüm girdi maskelerini üst üste istiflenmiş halde içeren tek bir toplu maske. | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchMasksNode/tr.md)

---
**Source fingerprint (SHA-256):** `8eb7a2a2d8108b619387b049d92348b8e9fc6d5e94e78c856c8520b88cdf77f2`
