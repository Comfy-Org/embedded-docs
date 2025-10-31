> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentageVideo/tr.md)

ConditioningSetAreaPercentageVideo düğümü, video üretimi için belirli bir alan ve zamansal bölge tanımlayarak koşullandırma verilerini değiştirir. Koşullandırmanın uygulanacağı alanın konumunu, boyutunu ve süresini genel boyutlara göre yüzde değerleri kullanarak ayarlamanıza olanak tanır. Bu, üretimi bir video dizisinin belirli bölümlerine odaklamak için kullanışlıdır.

## Girdiler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `koşullandırma` | CONDITIONING | Gerekli | - | - | Değiştirilecek koşullandırma verisi |
| `genişlik` | FLOAT | Gerekli | 1.0 | 0.0 - 1.0 | Alanın genişliği, toplam genişliğin yüzdesi olarak |
| `yükseklik` | FLOAT | Gerekli | 1.0 | 0.0 - 1.0 | Alanın yüksekliği, toplam yüksekliğin yüzdesi olarak |
| `zamansal` | FLOAT | Gerekli | 1.0 | 0.0 - 1.0 | Alanın zamansal süresi, toplam video uzunluğunun yüzdesi olarak |
| `x` | FLOAT | Gerekli | 0.0 | 0.0 - 1.0 | Alanın yatay başlangıç konumu, yüzde olarak |
| `y` | FLOAT | Gerekli | 0.0 | 0.0 - 1.0 | Alanın dikey başlangıç konumu, yüzde olarak |
| `z` | FLOAT | Gerekli | 0.0 | 0.0 - 1.0 | Alanın zamansal başlangıç konumu, video zaman çizelgesinin yüzdesi olarak |
| `güç` | FLOAT | Gerekli | 1.0 | 0.0 - 10.0 | Tanımlanan alan içindeki koşullandırmaya uygulanan güç çarpanı |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `koşullandırma` | CONDITIONING | Belirtilen alan ve güç ayarları uygulanmış olarak değiştirilmiş koşullandırma verisi |