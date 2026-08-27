# Diffusers Yükleyici

DiffusersLoader düğümü, diffusers formatında kaydedilmiş önceden eğitilmiş modelleri yükler. `model_index.json` dosyası içeren dizinler için yapılandırılmış `diffusers` klasörlerini tarar, birini seçmenizi sağlar ve bunu pipeline'da kullanılan MODEL, CLIP ve VAE bileşenleri olarak yükler. Bu düğüm kullanımdan kaldırılmıştır, ancak Hugging Face diffusers modelleriyle uyumluluk için kullanılabilir durumda tutulmaktadır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_yolu` | Yüklenecek diffusers model dizininin yolu. Düğüm, geçerli modeller için yapılandırılmış diffusers klasörlerini otomatik olarak tarar ve mevcut seçenekleri listeler. | COMBO | Evet | Birden fazla seçenek mevcut<br>(diffusers klasörlerinden otomatik doldurulur) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|-------------|-----------|
| MODEL | Diffusers formatından yüklenen model bileşeni. | MODEL |
| CLIP | Diffusers formatından yüklenen CLIP model bileşeni. | CLIP |
| VAE | Diffusers formatından yüklenen VAE (Variational Autoencoder) bileşeni. | VAE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/tr.md)

---
**Source fingerprint (SHA-256):** `75238342d05eac7528f981a2d4544accb6053891cd078a77751cc838054225d4`
