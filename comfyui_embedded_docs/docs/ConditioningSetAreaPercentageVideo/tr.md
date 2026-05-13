> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentageVideo/tr.md)

ConditioningSetAreaPercentageVideo düğümü, video üretimi için belirli bir alan ve zamansal bölge tanımlayarak koşullandırma verilerini değiştirir. Koşullandırmanın uygulanacağı alanın konumunu, boyutunu ve süresini, genel boyutlara göre yüzde değerleri kullanarak ayarlamanıza olanak tanır. Bu, üretimi bir video dizisinin belirli bölümlerine odaklamak için kullanışlıdır.

## Girişler

| Parametre | Veri Türü | Giriş Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `koşullandırma` | CONDITIONING | Gerekli | - | - | Değiştirilecek koşullandırma verileri |
| `genişlik` | FLOAT | Gerekli | 1.0 | 0.0 - 1.0 | Toplam genişliğin yüzdesi olarak alanın genişliği |
| `yükseklik` | FLOAT | Gerekli | 1.0 | 0.0 - 1.0 | Toplam yüksekliğin yüzdesi olarak alanın yüksekliği |
| `zamansal` | FLOAT | Gerekli | 1.0 | 0.0 - 1.0 | Toplam video uzunluğunun yüzdesi olarak alanın zamansal süresi |
| `x` | FLOAT | Gerekli | 0.0 | 0.0 - 1.0 | Alanın yatay başlangıç konumu (yüzde olarak) |
| `y` | FLOAT | Gerekli | 0.0 | 0.0 - 1.0 | Alanın dikey başlangıç konumu (yüzde olarak) |
| `z` | FLOAT | Gerekli | 0.0 | 0.0 - 1.0 | Video zaman çizelgesinin yüzdesi olarak alanın zamansal başlangıç konumu |
| `güç` | FLOAT | Gerekli | 1.0 | 0.0 - 10.0 | Tanımlanan alan içindeki koşullandırmaya uygulanan güç çarpanı |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `koşullandırma` | CONDITIONING | Belirtilen alan ve güç ayarları uygulanmış değiştirilmiş koşullandırma verileri |

---
**Source fingerprint (SHA-256):** `72d4bef4f8ddc4765cf69863f7ad03d34992f0ff30a963dbe2dc1b7d69815410`
