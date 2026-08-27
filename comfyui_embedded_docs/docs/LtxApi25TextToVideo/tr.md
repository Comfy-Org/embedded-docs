# LTX 2.5 Metinden Videoya

LTX 2.5 Text To Video, LTX 2.5 modelini kullanarak metin açıklamasından profesyonel kalitede videolar üreten bir API düğümüdür. Bir istem sağlarsınız ve model seviyesi, süre, çözünürlük, kare hızı ve ses ekleyip eklememe gibi üretim ayarlarını seçersiniz; düğüm görevi LTX API'ye gönderir ve ortaya çıkan videoyu döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video üretimi için kullanılacak LTX 2.5 model seviyesi. | STRING | Evet | "LTX-2.5 (Fast)"<br>"LTX-2.5 (Pro)" |
| `süre` | Oluşturulan videonun uzunluğu. | INT | Evet | Integer |
| `çözünürlük` | Videonun çıktı çözünürlüğü. Kullanılabilir seçenekler seçilen `model`e bağlıdır. | STRING | Evet | "LTX-2.5 (Fast)" ile:<br>"1280x720"<br>"720x1280"<br>"1920x1080"<br>"1080x1920"<br>"2560x1440"<br>"1440x2560"<br>"3840x2160"<br>"2160x3840"<br>"LTX-2.5 (Pro)" ile:<br>"1280x720"<br>"720x1280"<br>"1920x1080"<br>"1080x1920" |
| `fps` | Oluşturulan videonun kare hızı (varsayılan: 25). | INT | Hayır | Integer |
| `ses_oluştur` | Video ile birlikte ses üretilip üretilmeyeceği (varsayılan: True). | BOOLEAN | Hayır | True<br>False |
| `prompt` | Oluşturulacak videonun metin açıklaması. En fazla 10.000 karakter içeren boş olmayan bir istem gereklidir (varsayılan: ""). | STRING | Evet | 1 ile 10000 characters |
| `tohum` | Tekrarlanabilir üretim için kullanılan Seed değeri (varsayılan: 42). | INT | Hayır | Integer |

Not: Kullanılabilir `model.resolution` seçenekleri seçilen `model`e bağlıdır. "LTX-2.5 (Fast)" 2160x3840'e kadar çözünürlükleri desteklerken, "LTX-2.5 (Pro)" 1920x1080'e kadar çözünürlükleri destekler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | LTX API tarafından döndürülen, iş akışında daha fazla kullanıma hazır oluşturulmuş video. Ses üretimi etkinleştirildiyse, video eşzamanlı ses içerir. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25TextToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `02e131116fb0760cce2cea1e9bc49fa16dd7e4e296903fef5e44b7942b6e84c9`
