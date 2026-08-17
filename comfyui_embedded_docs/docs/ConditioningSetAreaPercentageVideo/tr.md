# KoşullandırmaAlanYüzdesiVideo

ConditioningSetAreaPercentageVideo düğümü, video üretimi için belirli bir alan ve zamansal bölge tanımlayarak koşullandırma verilerini değiştirir. Koşullandırmanın uygulanacağı alanın konumunu, boyutunu ve süresini genel boyutlara göre yüzde değerleriyle ayarlamanıza olanak tanır. Bu, üretimi bir video dizisinin belirli bölümlerine odaklamak için kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `conditioning` | Değiştirilecek koşullandırma verileri | CONDITIONING | Evet | - |
| `width` | Alanın genişliğinin toplam genişliğe oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `height` | Alanın yüksekliğinin toplam yüksekliğe oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `temporal` | Alanın zamansal süresinin toplam video uzunluğuna oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `x` | Alanın yatay başlangıç konumu (varsayılan: 0.0) | FLOAT | Evet | 0.0 - 1.0 |
| `y` | Alanın dikey başlangıç konumu (varsayılan: 0.0) | FLOAT | Evet | 0.0 - 1.0 |
| `z` | Alanın video zaman çizelgesindeki zamansal başlangıç konumu (varsayılan: 0.0) | FLOAT | Evet | 0.0 - 1.0 |
| `strength` | Tanımlanan alan içindeki koşullandırmaya uygulanan güç çarpanı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 10.0 |

Not: Tüm boyut ve konum değerleri, genel video boyutlarına ve zaman çizelgesine göre normalleştirilmiş yüzdelerdir (0.0 ila 1.0).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `conditioning` | Belirtilen alan ve güç ayarları uygulanmış değiştirilmiş koşullandırma verileri | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentageVideo/tr.md)

---
**Source fingerprint (SHA-256):** `9c5ddae6a2b1da5907fb52ef625eefb12b0b228fd3bd52c3033b5c4226d76150`
