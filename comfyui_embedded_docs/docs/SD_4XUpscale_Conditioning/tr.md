# SD_4X_Büyütme_Koşullandırma

SD_4XUpscale_Conditioning düğümü, difüzyon modellerini kullanarak görüntüleri ölçek büyütmek için koşullandırma verilerini hazırlar. Girdi görüntülerini ve koşullandırma verilerini alır, ardından ölçekleme ve gürültü artırımı uygulayarak ölçek büyütme sürecini yönlendiren modifiye koşullandırma oluşturur. Düğüm, ölçek büyütülmüş boyutlar için latent temsillerle birlikte hem pozitif hem de negatif koşullandırma çıktısı verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `görüntüler` | Ölçek büyütülecek girdi görüntüleri | IMAGE | Evet | - |
| `pozitif` | Üretimi istenen içeriğe yönlendiren pozitif koşullandırma verileri | CONDITIONING | Evet | - |
| `negatif` | Üretimi istenmeyen içerikten uzaklaştıran negatif koşullandırma verileri | CONDITIONING | Evet | - |
| `ölçek_oranı` | Girdi görüntülerine uygulanan ölçekleme faktörü (varsayılan: 4.0) | FLOAT | Hayır | 0.0 - 10.0 |
| `gürültü_artırımı` | Ölçek büyütme işlemi sırasında eklenecek gürültü miktarı (varsayılan: 0.0) | FLOAT | Hayır | 0.0 - 1.0 |

Not: `noise_augmentation` gelişmiş bir parametredir ve düğüm arayüzünde "Gelişmiş" (Advanced) geçişi altında gösterilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Ölçek büyütme bilgisi uygulanmış modifiye pozitif koşullandırma | CONDITIONING |
| `negatif` | Ölçek büyütme bilgisi uygulanmış modifiye negatif koşullandırma | CONDITIONING |
| `gizli` | Ölçek büyütülmüş boyutlarla eşleşen boş latent temsili | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/tr.md)

---
**Source fingerprint (SHA-256):** `f215e890bd86f42d4da9c6f575fc92e65844e2e2056c5610310d8089e5d61902`
