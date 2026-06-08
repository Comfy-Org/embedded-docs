DiffusersLoader düğümü, diffusers formatındaki önceden eğitilmiş modelleri yükler. `model_index.json` dosyası içeren geçerli diffusers model dizinlerini arar ve bunları MODEL, CLIP ve VAE bileşenleri olarak yükleyerek pipeline'da kullanıma sunar. Bu düğüm, kullanımdan kaldırılmış yükleyiciler kategorisinin bir parçasıdır ve Hugging Face diffusers modelleriyle uyumluluk sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model_yolu` | Yüklenecek diffusers model dizininin yolu. Düğüm, yapılandırılmış diffusers klasörlerindeki geçerli diffusers modellerini otomatik olarak tarar ve mevcut seçenekleri listeler. | STRING | Evet | Birden çok seçenek mevcut<br>(diffusers klasörlerinden otomatik doldurulur) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MODEL` | Diffusers formatından yüklenen model bileşeni | MODEL |
| `CLIP` | Diffusers formatından yüklenen CLIP model bileşeni | CLIP |
| `VAE` | Diffusers formatından yüklenen VAE (Değişken Otomatik Kodlayıcı) bileşeni | VAE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/tr.md)

---
**Source fingerprint (SHA-256):** `59be9923ed76d4859d5f7217a802c43297cb5af3d895eb6713edea97a32c3db2`
