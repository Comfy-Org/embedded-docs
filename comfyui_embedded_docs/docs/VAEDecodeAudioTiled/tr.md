# VAE Sesini Çöz (Döşemeli)

Bu düğüm, Varyasyonel Otomatik Kodlayıcı (VAE) kullanarak sıkıştırılmış bir ses temsilini (gizli örnekler) tekrar bir ses dalga formuna dönüştürür. Verileri, bellek kullanımını yönetmek için daha küçük, üst üste binen bölümler (döşemeler) halinde işler; bu da daha uzun ses dizilerinin işlenmesi için uygundur. Kod çözülen ses ayrıca, ses düzeyi seviyesini tutarlı tutmak için normalize edilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `örnekler` | Kod çözülecek sesin sıkıştırılmış gizli temsili. | LATENT | Evet | N/A |
| `vae` | Kod çözme işlemini gerçekleştirmek için kullanılan Varyasyonel Otomatik Kodlayıcı modeli. | VAE | Evet | N/A |
| `döşeme boyutu` | Her bir işleme döşemesinin boyutu. Ses, bellekten tasarruf etmek için bu uzunluktaki bölümler halinde kod çözülür (varsayılan: 512). | INT | Evet | 32 ile 8192 |
| `örtüşme` | Bitişik döşemelerin çakıştığı örnek sayısı. Bu, döşemeler arasındaki sınırlarda oluşan bozulmaları azaltmaya yardımcı olur (varsayılan: 64). | INT | Evet | 0 ile 1024 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Kod çözülen ses dalga formu, örnekleme hızı bilgisi dahil. | AUDIO |

Çıkış örnekleme hızı, girdi `samples` bir örnekleme hızı içerdiğinde oradan alınır; aksi takdirde VAE modelinden okunur (varsayılan: 44100 Hz).

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudioTiled/tr.md)

---
**Source fingerprint (SHA-256):** `5ddedf218ba27ab9f463646c1e5288091172f2d7fae8f2980bb2b5e4d3dca89c`
