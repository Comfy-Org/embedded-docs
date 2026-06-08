Bu düğüm, daha önce diske kaydedilmiş kodlanmış bir eğitim veri kümesini yükler. ComfyUI çıktı dizini içindeki belirtilen bir klasördeki tüm veri parçası dosyalarını arar ve okur, ardından birleştirilmiş gizli vektörleri ve koşullandırma verilerini eğitim iş akışlarında kullanılmak üzere döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `folder_name` | ComfyUI çıktı dizini içinde bulunan, kaydedilmiş veri kümesini içeren klasörün adı (varsayılan: "training_dataset"). | STRING | Evet | Yok |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `latents` | Her bir sözlüğün `"samples"` anahtarına sahip bir tensör içerdiği, gizli sözlüklerin listesi. | LATENT |
| `conditioning` | Her bir iç listenin ilgili bir örnek için koşullandırma verileri içerdiği, koşullandırma listelerinin listesi. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadTrainingDataset/tr.md)

---
**Source fingerprint (SHA-256):** `0a07c97e2c6a32f77cd21ea7dbdd33e06fad82285696b88122fef369307e133d`
