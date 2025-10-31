> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/tr.md)

ModelSamplingSD3 düğümü, bir modele Stable Diffusion 3 örnekleme parametrelerini uygular. Modelin örnekleme davranışını, örnekleme dağılımı özelliklerini kontrol eden shift parametresini ayarlayarak değiştirir. Düğüm, belirtilen örnekleme konfigürasyonu uygulanmış giriş modelinin değiştirilmiş bir kopyasını oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | SD3 örnekleme parametrelerinin uygulanacağı giriş modeli |
| `shift` | FLOAT | Evet | 0.0 - 100.0 | Örnekleme shift parametresini kontrol eder (varsayılan: 3.0) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | SD3 örnekleme parametreleri uygulanmış değiştirilmiş model |