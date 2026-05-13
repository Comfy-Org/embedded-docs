> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetDefaultAndCombine/tr.md)

Bu düğüm, birincil koşullandırma girdisini varsayılan bir koşullandırma girdisiyle kanca tabanlı bir sistem kullanarak birleştirir. İki koşullandırma kaynağını tek bir çıktıda birleştirerek, birincil koşullandırma eksik olduğunda varsayılan koşullandırmanın yedek veya temel görevi görmesini sağlar.

## Girdiler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `cond` | CONDITIONING | Gerekli | - | - | İşlenecek ve birleştirilecek birincil koşullandırma girdisi |
| `cond_DEFAULT` | CONDITIONING | Gerekli | - | - | Birincil koşullandırma ile birleştirilecek varsayılan koşullandırma verisi |
| `hooks` | HOOKS | İsteğe bağlı | - | - | Koşullandırma verisinin nasıl işleneceğini ve birleştirileceğini kontrol eden isteğe bağlı kanca yapılandırması |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Birincil ve varsayılan koşullandırma girdilerinin birleştirilmesiyle elde edilen birleşik koşullandırma verisi |

---
**Source fingerprint (SHA-256):** `5e6c95f454c7e262878cc362c6b199e01abff10f803c81afe6e76a317c30d039`
