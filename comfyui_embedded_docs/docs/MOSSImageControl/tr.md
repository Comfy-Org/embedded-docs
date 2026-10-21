# MOSS-Image Color/Depth Control

MOSS-Image renk/derinlik kontrol adaptörünün renk bölgesi ve derinlik haritalarını koşullandırmaya ekler. Pozitif ve negatif koşullandırmaları, bir VAE'yi ve haritalardan birini veya ikisini bağlayın: haritalar latentlere kodlanır, bir renk/derinlik kontrol sinyalinde birleştirilir ve seçtiğiniz örnekleme bölümü için koşullandırmaya eklenir. Bir LoRA yükleyici aracılığıyla yüklenen bir MOSS-Image kontrol adaptörüyle birlikte kullanın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `positive` | Kontrol sinyalinin ekleneceği pozitif koşullandırma. | CONDITIONING | Evet | N/A |
| `negative` | Kontrol sinyalinin ekleneceği negatif koşullandırma. | CONDITIONING | Evet | N/A |
| `vae` | Haritaları latentlere kodlamak için kullanılan VAE. | VAE | Evet | N/A |
| `color_map` | Çıktı boyutunda, her bölge için tek bir düz renk. Renkler yalnızca bölge kimlikleridir. | IMAGE | Hayır | N/A |
| `depth_map` | Çıktı boyutunda derinlik haritası; yakın olan beyazdır. | IMAGE | Hayır | N/A |
| `strength` | Haritaların görüntü token'larına katkısını ölçekler. 0.0, harita olmamasıyla aynıdır; 1.0, eğitilmiş güçtür (varsayılan: 1.0). | FLOAT | Evet | 0.0 ile 10.0 arası (adım: 0.01) |
| `start_percent` | Kontrolün başladığı örnekleme yüzdesi (varsayılan: 0.0). | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.001) |
| `end_percent` | Kontrolün bittiği örnekleme yüzdesi. Erken bitirmek düzeni ve derinliği korurken kalan adımlar şekilleri gevşetir (varsayılan: 1.0). | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.001) |

**Not:** `color_map` ve `depth_map`'ten en az birini bağlayın; ikisi de yoksa düğüm koşullandırmaları değiştirmeden döndürür. Eksik harita sıfırlarla değiştirilir, bu nedenle yalnızca renk ve yalnızca derinlik kurulumlarının ikisi de çalışır. İki harita boyut olarak farklıysa, küçük olan diğerinin boyutuna ölçeklenir. Bu düğüm ComfyUI'de deneysel olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | Kontrol sinyali eklenmiş pozitif koşullandırma. | CONDITIONING |
| `negative` | Kontrol sinyali eklenmiş negatif koşullandırma. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MOSSImageControl/tr.md)

---
**Source fingerprint (SHA-256):** `c4a40c76f26237408e47cb9f683c13bccc3507bd775bec1b89919947a308c115`
