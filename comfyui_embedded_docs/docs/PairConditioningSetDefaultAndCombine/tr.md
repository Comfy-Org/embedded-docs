# PairConditioningSetDefaultAndCombine

**PairConditioningSetDefaultAndCombine** düğümü, varsayılan koşullandırma değerlerini ayarlar ve bunları giriş koşullandırma verileriyle birleştirir. Pozitif ve negatif koşullandırma girdilerini varsayılan karşılıklarıyla birlikte alır, ardından bunları ComfyUI'nin kanca sistemi aracılığıyla işleyerek varsayılan değerleri içeren nihai koşullandırma çıktılarını üretir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | İşlenecek birincil pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `negative` | İşlenecek birincil negatif koşullandırma girdisi | CONDITIONING | Evet | - |
| `positive_DEFAULT` | Yedek olarak kullanılacak varsayılan pozitif koşullandırma değerleri | CONDITIONING | Evet | - |
| `negative_DEFAULT` | Yedek olarak kullanılacak varsayılan negatif koşullandırma değerleri | CONDITIONING | Evet | - |
| `hooks` | Özel işleme mantığı için isteğe bağlı kanca grubu | HOOKS | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Varsayılan değerlerin eklendiği işlenmiş pozitif koşullandırma | CONDITIONING |
| `negative` | Varsayılan değerlerin eklendiği işlenmiş negatif koşullandırma | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetDefaultAndCombine/tr.md)

---
**Source fingerprint (SHA-256):** `dfa47d0fe02e81db8b68d20ae9b765c2518773f4f7fc8caf774cb870267dbb21`
