ConditioningSetAreaPercentageVideo düğümü, video üretimi için belirli bir alan ve zamansal bölge tanımlayarak koşullandırma verilerini değiştirir. Koşullandırmanın uygulanacağı alanın konumunu, boyutunu ve süresini, genel boyutlara göre yüzde değerleri kullanarak ayarlamanıza olanak tanır. Bu, üretimi bir video dizisinin belirli bölümlerine odaklamak için kullanışlıdır.

## Girişler

| Parametre | Açıklama | Veri Türü | Giriş Türü | Varsayılan | Aralık |
| --- | --- | --- | --- | --- | --- |
| `koşullandırma` | Değiştirilecek koşullandırma verileri | CONDITIONING | Gerekli | - | - |
| `genişlik` | Toplam genişliğin yüzdesi olarak alanın genişliği | FLOAT | Gerekli | 1.0 | 0.0 - 1.0 |
| `yükseklik` | Toplam yüksekliğin yüzdesi olarak alanın yüksekliği | FLOAT | Gerekli | 1.0 | 0.0 - 1.0 |
| `zamansal` | Toplam video uzunluğunun yüzdesi olarak alanın zamansal süresi | FLOAT | Gerekli | 1.0 | 0.0 - 1.0 |
| `x` | Alanın yatay başlangıç konumu (yüzde olarak) | FLOAT | Gerekli | 0.0 | 0.0 - 1.0 |
| `y` | Alanın dikey başlangıç konumu (yüzde olarak) | FLOAT | Gerekli | 0.0 | 0.0 - 1.0 |
| `z` | Video zaman çizelgesinin yüzdesi olarak alanın zamansal başlangıç konumu | FLOAT | Gerekli | 0.0 | 0.0 - 1.0 |
| `güç` | Tanımlanan alan içindeki koşullandırmaya uygulanan güç çarpanı | FLOAT | Gerekli | 1.0 | 0.0 - 10.0 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `koşullandırma` | Belirtilen alan ve güç ayarları uygulanmış değiştirilmiş koşullandırma verileri | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentageVideo/tr.md)

---
**Source fingerprint (SHA-256):** `72d4bef4f8ddc4765cf69863f7ad03d34992f0ff30a963dbe2dc1b7d69815410`
