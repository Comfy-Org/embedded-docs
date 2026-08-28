# GizliYükle

LoadLatent düğümü, girdi dizinindeki .latent dosyalarından önceden kaydedilmiş latent temsilleri yükler. Seçilen dosyadan latent tensör verilerini okur ve latent verileri diğer düğümlerde kullanılmak üzere döndürmeden önce gerekli ölçekleme ayarlarını uygular.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `gizli` | Girdi dizinindeki mevcut dosyalardan hangi .latent dosyasının yükleneceğini seçer | COMBO | Evet | Girdi dizinindeki tüm .latent dosyaları (dinamik liste, alfabetik olarak sıralanmış) |

Not: Mevcut dosyaların listesi dinamik olarak oluşturulur ve yalnızca girdi dizininde bulunan .latent ile biten dosyaları içerir. Seçilen dosya artık mevcut değilse, düğüm bunu geçersiz bir latent dosyası olarak bildirir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Seçilen dosyadan yüklenen latent temsil verilerini bir float tensör olarak döndürür. Dosya `latent_format_version_0` işaretini içermiyorsa, tensör döndürülmeden önce 1/0.18215 ile ölçeklenir; işareti içeren dosyalar saklanan ölçeklerinde döndürülür. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLatent/tr.md)

---
**Source fingerprint (SHA-256):** `0938214361687a3a98e03878b8cbc0240100cbeacc0b157c4a299e59e7728a13`
