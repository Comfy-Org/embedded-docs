> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEqualizer3Band/tr.md)

Ses Ekolayzır (3-Bant) düğümü, bir ses dalga formunun bas, orta ve tiz frekanslarını ayarlamanıza olanak tanır. Üç ayrı filtre uygular: bas için bir alçak raf filtresi, orta frekanslar için bir tepe filtresi ve tizler için bir yüksek raf filtresi. Her bant, kazanç, frekans ve bant genişliği ayarlarıyla bağımsız olarak kontrol edilebilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Evet | - | Dalga formunu ve örnekleme hızını içeren giriş ses verisi. |
| `low_gain_dB` | FLOAT | Hayır | -24.0 ile 24.0 | Düşük frekanslar (Bas) için kazanç. Pozitif değerler yükseltir, negatif değerler keser. (varsayılan: 0.0) |
| `low_freq` | INT | Hayır | 20 ile 500 | Alçak raf filtresi için kesim frekansı, Hertz (Hz) cinsinden. (varsayılan: 100) |
| `mid_gain_dB` | FLOAT | Hayır | -24.0 ile 24.0 | Orta frekanslar için kazanç. Pozitif değerler yükseltir, negatif değerler keser. (varsayılan: 0.0) |
| `mid_freq` | INT | Hayır | 200 ile 4000 | Orta tepe filtresi için merkez frekansı, Hertz (Hz) cinsinden. (varsayılan: 1000) |
| `mid_q` | FLOAT | Hayır | 0.1 ile 10.0 | Orta tepe filtresi için Q faktörü (bant genişliği). Düşük değerler daha geniş bir bant oluşturur, yüksek değerler daha dar bir bant oluşturur. (varsayılan: 0.707) |
| `high_gain_dB` | FLOAT | Hayır | -24.0 ile 24.0 | Yüksek frekanslar (Tiz) için kazanç. Pozitif değerler yükseltir, negatif değerler keser. (varsayılan: 0.0) |
| `high_freq` | INT | Hayır | 1000 ile 15000 | Yüksek raf filtresi için kesim frekansı, Hertz (Hz) cinsinden. (varsayılan: 5000) |

**Not:** `low_gain_dB`, `mid_gain_dB` ve `high_gain_dB` parametreleri yalnızca değerleri sıfır olmadığında uygulanır. Bir kazanç 0.0 olarak ayarlanırsa, ilgili filtre aşaması atlanır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `audio` | AUDIO | Ekolayzır uygulanmış, değiştirilmiş dalga formunu ve orijinal örnekleme hızını içeren işlenmiş ses verisi. |