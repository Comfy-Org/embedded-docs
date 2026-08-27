# ControlNetInpaintingAliMamaUygula

ControlNetInpaintingAliMamaApply düğümü, pozitif ve negatif koşullandırmayı bir kontrol görüntüsü ve maskesiyle birleştirerek inpainting görevleri için ControlNet koşullandırması uygular. Girdi görüntüsünü ve maskesini işleyerek üretim sürecini yönlendiren değiştirilmiş koşullandırma oluşturur ve görüntünün hangi alanlarına inpainting uygulanacağı üzerinde hassas kontrol sağlar. Düğüm, üretim sürecinin farklı aşamalarında ControlNet'in etkisini ince ayarlamak için güç ayarı ve zamanlama kontrollerini destekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Üretimi istenen içeriğe yönlendiren pozitif koşullandırma | CONDITIONING | Evet | - |
| `negatif` | Üretimi istenmeyen içerikten uzaklaştıran negatif koşullandırma | CONDITIONING | Evet | - |
| `kontrol_ağı` | Üretim üzerinde ek kontrol sağlayan ControlNet modeli | CONTROL_NET | Evet | - |
| `vae` | Görüntüleri kodlamak ve kodunu çözmek için kullanılan VAE (Varyasyonel Otomatik Kodlayıcı) | VAE | Evet | - |
| `görüntü` | ControlNet için kontrol rehberliği görevi gören girdi görüntüsü | IMAGE | Evet | - |
| `maske` | Görüntünün hangi alanlarına inpainting uygulanacağını tanımlayan maske | MASK | Evet | - |
| `güç` | ControlNet efektinin gücü (varsayılan: 1.0, adım: 0.01) | FLOAT | Evet | 0.0 ile 10.0 |
| `başlangıç_yüzdesi` | Gelişmiş parametre. ControlNet etkisinin üretim sırasında başladığı nokta (yüzde olarak) (varsayılan: 0.0, adım: 0.001) | FLOAT | Evet | 0.0 ile 1.0 |
| `bitiş_yüzdesi` | Gelişmiş parametre. ControlNet etkisinin üretim sırasında durduğu nokta (yüzde olarak) (varsayılan: 1.0, adım: 0.001) | FLOAT | Evet | 0.0 ile 1.0 |

**Not:** ControlNet'te `concat_mask` etkinleştirildiğinde, maske ters çevrilir ve işlemeden önce görüntüye uygulanır; ayrıca ters çevrilmiş maske, ControlNet'e gönderilen ek birleştirme verilerine dahil edilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Inpainting için ControlNet uygulanmış değiştirilmiş pozitif koşullandırma | CONDITIONING |
| `negatif` | Inpainting için ControlNet uygulanmış değiştirilmiş negatif koşullandırma | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/tr.md)

---
**Source fingerprint (SHA-256):** `307b55c7b4936826b9e4424c172248fa4b41921c2362de724e5cfa2f1c25de68`
