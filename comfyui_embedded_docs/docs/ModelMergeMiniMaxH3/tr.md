# Model Merge MiniMax H3

İki uyumlu MiniMax H3 modelini bileşen bazında, mimarinin her bir parçası için ayrı bir oranla birleştirin. Bir oranı yükseltmek, o bileşenin daha fazlasını `model2`'den alır; böylece bir modelin patch projeksiyonlarını ve iyileştirme bloklarını korurken transformatör bloklarını başka bir modelle değiştirebilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `model1` | İlk MiniMax H3 modeli, her bileşenin alındığı temel (varsayılan ağırlık, `model2`'nin kullanılmadığı yerlerde geçerlidir). | MODEL | Evet | - |
| `model2` | Karıştırdığınız bileşenleri sağlayan ikinci MiniMax H3 modeli. | MODEL | Evet | - |
| `video_patch_proj.` | Video patch projeksiyonu için `model2` payı (varsayılan: 1.0). | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `audio_patch_proj.` | Ses patch projeksiyonu için `model2` payı (varsayılan: 1.0). | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `condition_proj.` | Koşullandırma projeksiyonu için `model2` payı (varsayılan: 1.0). | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `time_embedder.` | Zaman gömücü için `model2` payı (varsayılan: 1.0). | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `token_refiner.blocks.0.` | İlk token iyileştirici blok için `model2` payı (varsayılan: 1.0). | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `token_refiner.blocks.1.` | İkinci token iyileştirici blok için `model2` payı (varsayılan: 1.0). | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `token_refiner.final_norm.` | Token iyileştirici son normalizasyonu için `model2` payı (varsayılan: 1.0). | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `blocks.0.` through `blocks.49.` | 50 transformatör bloğunun her biri için `model2` payı, blok başına bir widget (varsayılan: 1.0). | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `final_layer.norm.` | Son katman normalizasyonu için `model2` payı (varsayılan: 1.0). | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `final_layer.adaln_proj.` | Son uyarlanabilir normalizasyon projeksiyonu için `model2` payı (varsayılan: 1.0). | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `final_layer.video_out.` | Video çıktı katmanı için `model2` payı (varsayılan: 1.0). | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `final_layer.audio_out.` | Ses çıktı katmanı için `model2` payı (varsayılan: 1.0). | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |

0.0 oranı, o bileşeni tamamen `model1`'den korur ve 1.0, onu tamamen `model2`'den alır; aradaki değerler ikisini karıştırır. Oran taşımayan tensörler, örneğin normalizasyon istatistikleri, her zaman `model1`'den gelir. Her iki girdi de aynı mimariye sahip MiniMax H3 modelleri olmalıdır, aksi takdirde birleştirme, çalışmayan bir model üretir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `MODEL` | Birleştirilmiş MiniMax H3 modeli. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeMiniMaxH3/tr.md)

---
**Source fingerprint (SHA-256):** `4fea4e588d16a8396c68aa071a59e671a2a0c645734606be6d7e221986ba88bd`
