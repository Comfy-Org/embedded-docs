# ControlNetInpaintingAliMamaUygula

Bu düğüm, pozitif ve negatif koşullandırmayı bir kontrol görüntüsü ve maske ile birleştirerek inpainting görevleri için ControlNet koşullandırması uygular. Görüntüyü ve maskeyi işleyerek üretim sürecini yönlendiren değiştirilmiş koşullandırma oluşturur ve hangi alanların yeniden boyanacağı üzerinde hassas kontrol sağlar. Düğüm ayrıca, üretim sırasında ControlNet'in etkisini ayarlamak için güç ve zamanlama kontrollerini de destekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Üretimi istenen içeriğe yönlendiren pozitif koşullandırma. | CONDITIONING | Evet | - |
| `negative` | Üretimi istenmeyen içerikten uzaklaştıran negatif koşullandırma. | CONDITIONING | Evet | - |
| `control_net` | Üretim üzerinde ek kontrol sağlayan ControlNet modeli. | CONTROL_NET | Evet | - |
| `vae` | Görüntüleri kodlamak ve kodunu çözmek için kullanılan VAE. | VAE | Evet | - |
| `image` | ControlNet için kontrol rehberi olarak kullanılan giriş görüntüsü. | IMAGE | Evet | - |
| `mask` | Görüntünün hangi alanlarının yeniden boyanacağını tanımlayan maske. | MASK | Evet | - |
| `strength` | ControlNet etkisinin gücü (varsayılan: 1.0). | FLOAT | Evet | 0.0 - 10.0 |
| `start_percent` | Gelişmiş seçenek. ControlNet etkisinin başladığı üretim sürecinin oranı (varsayılan: 0.0). | FLOAT | Evet | 0.0 - 1.0 |
| `end_percent` | Gelişmiş seçenek. ControlNet etkisinin bittiği üretim sürecinin oranı (varsayılan: 1.0). | FLOAT | Evet | 0.0 - 1.0 |

**Not:** Seçili ControlNet'te `concat_mask` etkinleştirildiğinde, maske değerleri ters çevrilir (1 - mask), ters çevrilmiş maskenin yeniden boyutlandırılmış bir sürümü görüntüye uygulanır ve ters çevrilmiş maske, ControlNet'e iletilen ek birleştirme verilerine dahil edilir. `concat_mask` devre dışıysa, `mask` girdisi kullanılmaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Inpainting için ControlNet uygulanmış değiştirilmiş pozitif koşullandırma. | CONDITIONING |
| `negative` | Inpainting için ControlNet uygulanmış değiştirilmiş negatif koşullandırma. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/tr.md)

---
**Source fingerprint (SHA-256):** `307b55c7b4936826b9e4424c172248fa4b41921c2362de724e5cfa2f1c25de68`
