# FreeU

FreeU düğümü, görüntü oluşturma kalitesini artırmak için bir modelin çıktı bloklarına frekans alanı değişiklikleri uygular. Farklı kanal gruplarını ölçeklendirerek ve belirli özellik haritalarına Fourier filtresi uygulayarak çalışır; bu, üretim süreci sırasında modelin davranışı üzerinde ince ayarlı kontrol sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | FreeU değişikliklerinin uygulanacağı model | MODEL | Evet | - |
| `b1` | model_channels × 4 kanallı özellik haritalarına uygulanan backbone ölçekleme faktörü (varsayılan: 1,1). Gelişmiş ayar olarak işaretlenmiştir. | FLOAT | Evet | 0.0 - 10.0 |
| `b2` | model_channels × 2 kanallı özellik haritalarına uygulanan backbone ölçekleme faktörü (varsayılan: 1,2). Gelişmiş ayar olarak işaretlenmiştir. | FLOAT | Evet | 0.0 - 10.0 |
| `s1` | model_channels × 4 kanallı özellik haritalarına uygulanan atlamalı bağlantı ölçekleme faktörü (varsayılan: 0,9). Gelişmiş ayar olarak işaretlenmiştir. | FLOAT | Evet | 0.0 - 10.0 |
| `s2` | model_channels × 2 kanallı özellik haritalarına uygulanan atlamalı bağlantı ölçekleme faktörü (varsayılan: 0,2). Gelişmiş ayar olarak işaretlenmiştir. | FLOAT | Evet | 0.0 - 10.0 |

Not: FreeU ayarlamaları yalnızca kanal sayısı model_channels × 4 olan (`b1` ve `s1` kullanılarak) veya model_channels × 2 olan (`b2` ve `s2` kullanılarak) özellik haritalarına uygulanır. Fourier filtresi, atlamalı bağlantı özellik haritalarının yalnızca merkezi düşük frekanslı bölgesini (eşik değeri 1) ölçeklendirir; diğer tüm frekans bileşenleri değişmeden kalır. Dört ölçekleme parametresinin tümü 0,0 ile 10,0 arasında 0,01 adımlarla değer kabul eder.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | FreeU yamaları uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/tr.md)

---
**Source fingerprint (SHA-256):** `7f7bd34964218ed16c9e58caa446d0c1e69f116607334df4a114cdc4adaf047f`
