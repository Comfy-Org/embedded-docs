> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEqualizer3Band/tr.md)

Ses Ekolayzeri (3 Bant) düğümü, bir ses dalga formunun bas, orta ve tiz frekanslarını ayarlamanızı sağlar. Bas için alçak raf, orta için tepe filtre ve tiz için yüksek raf olmak üzere üç ayrı filtre uygular. Her bant, kazanç, frekans ve bant genişliği ayarlarıyla bağımsız olarak kontrol edilebilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Evet | - | Dalga formu ve örnekleme hızını içeren giriş ses verisi. |
| `low_gain_dB` | FLOAT | Hayır | -24.0 ila 24.0 | Düşük frekanslar (Bas) için kazanç. Pozitif değerler yükseltir, negatif değerler kısar. (varsayılan: 0.0) |
| `low_freq` | INT | Hayır | 20 ila 500 | Alçak raf filtresi için Hertz (Hz) cinsinden kesim frekansı. (varsayılan: 100) |
| `mid_gain_dB` | FLOAT | Hayır | -24.0 ila 24.0 | Orta frekanslar için kazanç. Pozitif değerler yükseltir, negatif değerler kısar. (varsayılan: 0.0) |
| `mid_freq` | INT | Hayır | 200 ila 4000 | Orta tepe filtresi için Hertz (Hz) cinsinden merkez frekansı. (varsayılan: 1000) |
| `mid_q` | FLOAT | Hayır | 0.1 ila 10.0 | Orta tepe filtresi için Q faktörü (bant genişliği). Daha düşük değerler daha geniş bir bant, daha yüksek değerler daha dar bir bant oluşturur. (varsayılan: 0.707) |
| `high_gain_dB` | FLOAT | Hayır | -24.0 ila 24.0 | Yüksek frekanslar (Tiz) için kazanç. Pozitif değerler yükseltir, negatif değerler kısar. (varsayılan: 0.0) |
| `high_freq` | INT | Hayır | 1000 ila 15000 | Yüksek raf filtresi için Hertz (Hz) cinsinden kesim frekansı. (varsayılan: 5000) |

**Not:** `low_gain_dB`, `mid_gain_dB` ve `high_gain_dB` parametreleri yalnızca değerleri sıfır olmadığında uygulanır. Bir kazanç 0.0 olarak ayarlanırsa, ilgili filtre aşaması atlanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `audio` | AUDIO | Ekolayzır uygulanmış, değiştirilmiş dalga formunu ve orijinal örnekleme hızını içeren işlenmiş ses verisi. |

---
**Source fingerprint (SHA-256):** `7aeaec2959f1af6144e46d8e6c558a16193669846923df1db23ae9d47e5cc173`
