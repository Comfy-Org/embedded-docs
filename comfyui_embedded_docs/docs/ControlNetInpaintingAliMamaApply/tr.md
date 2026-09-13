# ControlNetInpaintingAliMamaUygula

ControlNetInpaintingAliMamaApply düğümü, pozitif ve negatif koşullandırmayı bir kontrol görüntüsü ve maskeyle birleştirerek inpainting görevleri için ControlNet koşullandırması uygular. Üretim sürecine yön vermek için giriş görüntüsünü ve maskeyi işleyerek, görüntünün hangi alanlarının inpaint edileceği üzerinde kontrol sağlayan değiştirilmiş koşullandırma oluşturur. Düğüm, üretim sürecinin farklı aşamalarında ControlNet'in etkisini ince ayarlamak için güç ayarı ve zamanlama kontrollerini destekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Üretimi istenen içeriğe yönlendiren pozitif koşullandırma | CONDITIONING | Evet | - |
| `negative` | Üretimi istenmeyen içerikten uzaklaştıran negatif koşullandırma | CONDITIONING | Evet | - |
| `control_net` | Üretim üzerinde ek kontrol sağlayan ControlNet modeli | CONTROL_NET | Evet | - |
| `vae` | Görüntüleri kodlamak ve kodunu çözmek için kullanılan VAE (Variational Autoencoder) | VAE | Evet | - |
| `image` | ControlNet için kontrol rehberi olarak hizmet eden giriş görüntüsü | IMAGE | Evet | - |
| `mask` | Görüntünün hangi alanlarının inpaint edileceğini tanımlayan maske | MASK | Evet | - |
| `strength` | ControlNet etkisinin gücü (varsayılan: 1.0, adım: 0.01) | FLOAT | Evet | 0.0 ile 10.0 |
| `start_percent` | Gelişmiş parametre. Üretim sırasında ControlNet etkisinin başladığı anın başlangıç noktası (yüzde olarak) (varsayılan: 0.0, adım: 0.001) | FLOAT | Evet | 0.0 ile 1.0 |
| `end_percent` | Gelişmiş parametre. Üretim sırasında ControlNet etkisinin durduğu anın bitiş noktası (yüzde olarak) (varsayılan: 1.0, adım: 0.001) | FLOAT | Evet | 0.0 ile 1.0 |

**Not:** ControlNet'te `concat_mask` etkinleştirildiğinde, maske ters çevrilir ve işleme öncesinde görüntüye uygulanır; ters çevrilmiş maske, ControlNet'e gönderilen ek birleştirme verisine dahil edilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Inpainting için ControlNet uygulanmış değiştirilmiş pozitif koşullandırma | CONDITIONING |
| `negative` | Inpainting için ControlNet uygulanmış değiştirilmiş negatif koşullandırma | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/tr.md)

---
**Source fingerprint (SHA-256):** `307b55c7b4936826b9e4424c172248fa4b41921c2362de724e5cfa2f1c25de68`
