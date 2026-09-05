# ComfyCloudFlux2TextToImageNode

Flux 2 dev text-to-image modelini bir Comfy Cloud GPU üzerinde çalıştırır ve üretilen görüntüyü döndürür. `turbo` seçeneği, Turbo LoRA'yı kısa bir zamanlama ile uygulayarak çok daha hızlı bir çalışma sağlar; bunun karşılığında küçük bir kalite kaybı yaşanır. Kapatıldığında, LoRA olmadan tam uzunlukta dev geçişi yapılır. Bu, kredi cinsinden çalışma süresine göre faturalandırılan bir beta düğüm setidir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturulacak görüntüyü tanımlayan metin istemi. Gönderimden önce baştaki ve sondaki boşluklar kaldırılır. | STRING | Evet | 1 ile 4096 karakter arası |
| `seed` | Tekrarlanabilirlik için oluşturulan sonucu kontrol eden rastgele tohum değeri (varsayılan: 42). | INT | Evet | 0 ile 18446744073709551615 arası |
| `aspect_ratio` | Çıktı görüntüsünün en-boy oranı (varsayılan: "1:1"). | COMBO | Evet | "1:1"<br>"3:4"<br>"2:3"<br>"3:2"<br>"4:3"<br>"16:9"<br>"9:16"<br>"21:9" |
| `megapixels` | Toplam piksel bütçesi. 1.0, kare oranda yaklaşık 1024x1024'e karşılık gelir (varsayılan: 1.0). | FLOAT | Evet | 0.1 ile 16.0 arası (adım 0.1) |
| `turbo` | Turbo LoRA'yı kısa bir zamanlama ile çalıştırır; çok daha hızlı bir çalışma karşılığında küçük bir kalite kaybı yaşanır. Kapalı durumda, LoRA olmadan tam dev geçişi yapılır (varsayılan: True). | BOOLEAN | Evet | True / False |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Metin isteminden üretilen ve diğer düğümlere aktarılabilen bir ComfyUI görüntü tensörü olarak döndürülen görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudFlux2TextToImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `1b51a8ab89ae7c355dec4256a1a25a09a15e192c72fc8d1862c652dbdf337fcb`
