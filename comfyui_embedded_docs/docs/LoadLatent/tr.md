# GizliYükle

LoadLatent düğümü, daha önce giriş dizininde .latent dosyaları olarak kaydedilmiş latent temsillerini yükler. Seçilen dosyadan latent tensör verilerini okur ve sonuçları diğer düğümlerde kullanılmak üzere döndürmeden önce gerekli ölçekleme ayarlamalarını uygular.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `latent` | Giriş dizinindeki mevcut dosyalar arasından hangi .latent dosyasının yükleneceğini seçer | COMBO | Evet | Giriş dizinindeki tüm .latent dosyaları |

Not: `latent_format_version_0` işaretini içermeyen .latent dosyaları için, yüklenen latent tensörü 1/0.18215 ile çarpılır; böylece ölçeği diğer düğümlerin beklediği biçimle eşleşir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Seçilen dosyadan yüklenen latent temsil verilerini döndürür | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLatent/tr.md)

---
**Source fingerprint (SHA-256):** `0938214361687a3a98e03878b8cbc0240100cbeacc0b157c4a299e59e7728a13`
