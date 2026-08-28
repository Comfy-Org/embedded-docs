# FreeU

FreeU düğümü, görüntü üretim kalitesini artırmak için bir modelin çıktı bloklarına frekans alanı değişiklikleri uygular. Farklı kanal gruplarını ölçekleyerek ve belirli özellik haritalarına Fourier filtrelemesi uygulayarak çalışır; bu sayede üretim süreci sırasında modelin davranışı üzerinde ince ayarlı kontrol sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | FreeU değişikliklerinin uygulanacağı model | MODEL | Evet | - |
| `b1` | model_channels × 4 özellikleri için omurga ölçekleme faktörü (varsayılan: 1.1) | FLOAT | Evet | 0.0 - 10.0 |
| `b2` | model_channels × 2 özellikleri için omurga ölçekleme faktörü (varsayılan: 1.2) | FLOAT | Evet | 0.0 - 10.0 |
| `s1` | model_channels × 4 özellikleri için atlama bağlantısı ölçekleme faktörü (varsayılan: 0.9) | FLOAT | Evet | 0.0 - 10.0 |
| `s2` | model_channels × 2 özellikleri için atlama bağlantısı ölçekleme faktörü (varsayılan: 0.2) | FLOAT | Evet | 0.0 - 10.0 |

Not: FreeU ayarlamaları yalnızca kanal sayısı model_channels × 4 (`b1` ve `s1` kullanılarak) veya model_channels × 2 (`b2` ve `s2` kullanılarak) olan özellik haritalarına uygulanır. Fourier filtresi, atlama bağlantısı özellik haritalarının yalnızca merkezi düşük frekanslı bölgesini ölçekler; diğer tüm frekans bileşenleri değişmeden kalır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | FreeU yamaları uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/tr.md)

---
**Source fingerprint (SHA-256):** `7f7bd34964218ed16c9e58caa446d0c1e69f116607334df4a114cdc4adaf047f`
