# ConditioningSetDefaultAndCombine

Bu düğüm, birincil koşullandırma girdisini varsayılan bir koşullandırma girdisiyle kanca tabanlı bir sistem kullanarak birleştirir. İki koşullandırma kaynağını tek bir çıktıda birleştirerek, birincil koşullandırma eksik olduğunda varsayılan koşullandırmanın yedek veya temel görevi görmesini sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Girdi Türü | Varsayılan | Aralık |
| --- | --- | --- | --- | --- | --- |
| `cond` | İşlenecek ve birleştirilecek birincil koşullandırma girdisi | CONDITIONING | Gerekli | - | - |
| `cond_DEFAULT` | Birincil koşullandırma ile birleştirilecek varsayılan koşullandırma verisi | CONDITIONING | Gerekli | - | - |
| `hooks` | Koşullandırma verisinin nasıl işleneceğini ve birleştirileceğini kontrol eden isteğe bağlı kanca yapılandırması | HOOKS | İsteğe bağlı | - | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Birincil ve varsayılan koşullandırma girdilerinin birleştirilmesiyle elde edilen birleşik koşullandırma verisi | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetDefaultAndCombine/tr.md)

---
**Source fingerprint (SHA-256):** `5e6c95f454c7e262878cc362c6b199e01abff10f803c81afe6e76a317c30d039`
