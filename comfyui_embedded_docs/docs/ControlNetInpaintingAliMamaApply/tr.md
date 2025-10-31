> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/tr.md)

ControlNetInpaintingAliMamaApply düğümü, pozitif ve negatif koşullandırmayı bir kontrol görüntüsü ve maske ile birleştirerek boyama görevleri için ControlNet koşullandırması uygular. Girdi görüntüsünü ve maskeyi işleyerek, üretim sürecini yönlendiren ve görüntünün hangi alanlarının boyanacağı üzerinde hassas kontrol sağlayan değiştirilmiş koşullandırma oluşturur. Düğüm, ControlNet'in etkisini üretim sürecinin farklı aşamalarında ince ayar yapmak için güç ayarlaması ve zamanlama kontrollerini destekler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Evet | - | Üretimi istenen içeriğe yönlendiren pozitif koşullandırma |
| `negative` | CONDITIONING | Evet | - | Üretimi istenmeyen içerikten uzaklaştıran negatif koşullandırma |
| `control_net` | CONTROL_NET | Evet | - | Üretim üzerinde ek kontrol sağlayan ControlNet modeli |
| `vae` | VAE | Evet | - | Görüntüleri kodlamak ve kodunu çözmek için kullanılan VAE (Varyasyonel Otokodlayıcı) |
| `image` | IMAGE | Evet | - | ControlNet için kontrol kılavuzu olarak hizmet veren girdi görüntüsü |
| `mask` | MASK | Evet | - | Görüntünün hangi alanlarının boyanması gerektiğini tanımlayan maske |
| `strength` | FLOAT | Evet | 0.0 - 10.0 | ControlNet etkisinin gücü (varsayılan: 1.0) |
| `start_percent` | FLOAT | Evet | 0.0 - 1.0 | ControlNet etkisinin üretim sırasında başladığı başlangıç noktası (yüzde olarak) (varsayılan: 0.0) |
| `end_percent` | FLOAT | Evet | 0.0 - 1.0 | ControlNet etkisinin üretim sırasında durduğu bitiş noktası (yüzde olarak) (varsayılan: 1.0) |

**Not:** ControlNet'te `concat_mask` etkinleştirildiğinde, maske ters çevrilir ve işlemeden önce görüntüye uygulanır ve maske, ControlNet'e gönderilen ek birleştirme verilerine dahil edilir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Boyama için ControlNet uygulanmış değiştirilmiş pozitif koşullandırma |
| `negative` | CONDITIONING | Boyama için ControlNet uygulanmış değiştirilmiş negatif koşullandırma |