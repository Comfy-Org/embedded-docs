# ModelÖrneklemeSD3

The ModelSamplingSD3 düğümü, bir modele Stable Diffusion 3 örnekleme parametrelerini uygular. Modelin örnekleme davranışını, örnekleme dağılımı özelliklerini kontrol eden `shift` parametresini ayarlayarak değiştirir. Düğüm, belirtilen örnekleme yapılandırması uygulanmış girdi modelinin değiştirilmiş bir kopyasını oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | SD3 örnekleme parametrelerinin uygulanacağı girdi modeli | MODEL | Evet | - |
| `kaydırma` | Örnekleme shift parametresini kontrol eder (varsayılan: 3.0) | FLOAT | Evet | 0.0 - 100.0 (adım: 0.01) |

Not: Düğüm, `shift` değerini sabit bir dahili çarpan olan 1000 ile uygular. Orijinal modelde bir gürültü ölçeği ayarı varsa, değiştirilmiş modelde korunur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | SD3 örnekleme parametreleri uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/tr.md)

---
**Source fingerprint (SHA-256):** `46d44786422c2efea78c1fe7e1183cebc9bf51d4f13861da04d5a974b5b6da7d`
