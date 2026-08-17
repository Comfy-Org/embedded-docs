# ModelÖrneklemeSD3

ModelSamplingSD3 düğümü, bir modele Stable Diffusion 3 örnekleme parametrelerini uygular. Shift parametresini ayarlayarak modelin örnekleme davranışını değiştirir; bu parametre, örnekleme dağılım özelliklerini kontrol eder. Düğüm, belirtilen örnekleme yapılandırması uygulanmış girdi modelinin değiştirilmiş bir kopyasını oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | SD3 örnekleme parametrelerinin uygulanacağı girdi modeli | MODEL | Evet | - |
| `shift` | Örnekleme shift parametresini kontrol eder (varsayılan: 3.0) | FLOAT | Evet | 0.0 - 100.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | SD3 örnekleme parametreleri uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/tr.md)

---
**Source fingerprint (SHA-256):** `46d44786422c2efea78c1fe7e1183cebc9bf51d4f13861da04d5a974b5b6da7d`
