# ModelMergeKrea2

Bu düğüm, iki modeli iç bileşenlerini ince taneli bir düzeyde harmanlayarak birleştirir ve her modelin belirli kısımlarının nihai sonucu ne kadar etkileyeceğini kontrol etmenizi sağlar. İki giriş modelini alarak ve mimarilerinin farklı bölümlerine ayrı harmanlama oranları uygulayarak çalışır.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model1` | Birleştirilecek ilk model | MODEL | Evet | - |
| `model2` | Birleştirilecek ikinci model | MODEL | Evet | - |
| `first.` | İlk katman bloğu için harmanlama oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `tmlp.` | Zaman MLP bloğu için harmanlama oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `txtmlp.` | Metin MLP bloğu için harmanlama oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `tproj.` | Zaman projeksiyon bloğu için harmanlama oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `txtfusion.layerwise_blocks.0.` | İlk metin füzyonu katmanlı blok için harmanlama oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `txtfusion.layerwise_blocks.1.` | İkinci metin füzyonu katmanlı blok için harmanlama oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `txtfusion.projector.` | Metin füzyonu projektör bloğu için harmanlama oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `txtfusion.refiner_blocks.0.` | İlk metin füzyonu iyileştirici blok için harmanlama oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `txtfusion.refiner_blocks.1.` | İkinci metin füzyonu iyileştirici blok için harmanlama oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `blocks.0.` ile `blocks.27.` arası | 28 ana bloğun her biri için harmanlama oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |
| `last.` | Son blok için harmanlama oranı (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası (adım: 0.01) |

Her harmanlama oranı, o belirli bileşen için `model2`'nin ne kadar kullanılacağını kontrol eder; 0.0 yalnızca `model1` kullanılacağı, 1.0 yalnızca `model2` kullanılacağı ve aradaki değerler ağırlıklı bir harmanlama oluşturacağı anlamına gelir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `MODEL` | Belirtilen oranlara göre iki giriş modelinin harmanlanmasıyla elde edilen birleştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeKrea2/tr.md)

---
**Source fingerprint (SHA-256):** `ece35524f77fd906dc3109a0818d4d7d3986ec9debb518fd04893048843d7e88`
