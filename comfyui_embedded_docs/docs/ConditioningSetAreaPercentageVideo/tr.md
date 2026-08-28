# KoşullandırmaAlanYüzdesiVideo

ConditioningSetAreaPercentageVideo düğümü, video oluşturma için belirli bir alan ve zamansal bölge tanımlayarak koşullandırma (conditioning) verilerini değiştirir. Koşullandırmanın uygulandığı alanın konumunu, boyutunu ve süresini ayarlamak için genel boyutlara göre yüzde değerleri kullanır. Bu, oluşturmayı bir video dizisinin belirli bölümlerine odaklamak için kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Değer Aralığı |
|-----------|----------|-----------|---------|---------------|
| `koşullandırma` | Değiştirilecek koşullandırma verileri | CONDITIONING | Evet | - |
| `genişlik` | Alanın genişliği, toplam genişliğin yüzdesi olarak (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım 0.01) |
| `yükseklik` | Alanın yüksekliği, toplam yüksekliğin yüzdesi olarak (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım 0.01) |
| `zamansal` | Alanın zamansal süresi, toplam video uzunluğunun yüzdesi olarak (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 (adım 0.01) |
| `x` | Alanın yatay başlangıç konumu, yüzde olarak (varsayılan: 0.0) | FLOAT | Evet | 0.0 - 1.0 (adım 0.01) |
| `y` | Alanın dikey başlangıç konumu, yüzde olarak (varsayılan: 0.0) | FLOAT | Evet | 0.0 - 1.0 (adım 0.01) |
| `z` | Alanın zamansal başlangıç konumu, video zaman çizelgesinin yüzdesi olarak (varsayılan: 0.0) | FLOAT | Evet | 0.0 - 1.0 (adım 0.01) |
| `güç` | Tanımlanan alan içindeki koşullandırmaya uygulanan güç çarpanı (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 10.0 (adım 0.01) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `conditioning` | Belirtilen alan ve güç ayarları uygulanmış değiştirilmiş koşullandırma verileri | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentageVideo/tr.md)

---
**Source fingerprint (SHA-256):** `9c5ddae6a2b1da5907fb52ef625eefb12b0b228fd3bd52c3033b5c4226d76150`
