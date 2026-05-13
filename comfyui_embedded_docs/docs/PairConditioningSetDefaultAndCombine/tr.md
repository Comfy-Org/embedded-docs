> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetDefaultAndCombine/tr.md)

**PairConditioningSetDefaultAndCombine** düğümü, varsayılan koşullandırma değerlerini ayarlar ve bunları giriş koşullandırma verileriyle birleştirir. Pozitif ve negatif koşullandırma girdilerini varsayılan karşılıklarıyla birlikte alır, ardından bunları ComfyUI'nin kanca sistemi aracılığıyla işleyerek varsayılan değerleri içeren nihai koşullandırma çıktılarını üretir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `positive` | CONDITIONING | Evet | - | İşlenecek birincil pozitif koşullandırma girdisi |
| `negative` | CONDITIONING | Evet | - | İşlenecek birincil negatif koşullandırma girdisi |
| `positive_DEFAULT` | CONDITIONING | Evet | - | Yedek olarak kullanılacak varsayılan pozitif koşullandırma değerleri |
| `negative_DEFAULT` | CONDITIONING | Evet | - | Yedek olarak kullanılacak varsayılan negatif koşullandırma değerleri |
| `hooks` | HOOKS | Hayır | - | Özel işleme mantığı için isteğe bağlı kanca grubu |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `positive` | CONDITIONING | Varsayılan değerlerin eklendiği işlenmiş pozitif koşullandırma |
| `negative` | CONDITIONING | Varsayılan değerlerin eklendiği işlenmiş negatif koşullandırma |

---
**Source fingerprint (SHA-256):** `dfa47d0fe02e81db8b68d20ae9b765c2518773f4f7fc8caf774cb870267dbb21`
