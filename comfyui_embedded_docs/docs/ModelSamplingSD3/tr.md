> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/tr.md)

ModelSamplingSD3 düğümü, bir modele Stable Diffusion 3 örnekleme parametrelerini uygular. Kaydırma parametresini ayarlayarak modelin örnekleme davranışını değiştirir; bu parametre, örnekleme dağılım özelliklerini kontrol eder. Düğüm, belirtilen örnekleme yapılandırması uygulanmış giriş modelinin değiştirilmiş bir kopyasını oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `model` | MODEL | Evet | - | SD3 örnekleme parametrelerinin uygulanacağı giriş modeli |
| `shift` | FLOAT | Evet | 0.0 - 100.0 | Örnekleme kaydırma parametresini kontrol eder (varsayılan: 3.0) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `model` | MODEL | SD3 örnekleme parametreleri uygulanmış değiştirilmiş model |

---
**Source fingerprint (SHA-256):** `aa2172d578badffb0a728308b0d3aae4d048db074336963965264d5e512a0d93`
