# Comfy Cloud Flux 2 Metinden Görüntüye [BETA]

Flux 2 dev metinden görüntüye modelini bir Comfy Cloud GPU üzerinde çalıştırır ve oluşturulan görüntüyü döndürür. `turbo` seçeneği, Turbo LoRA'yı kısa bir zamanlamayla uygulayarak biraz kaliteden ödün verip çok daha hızlı bir çalışma sağlar; kapatıldığında LoRA olmadan tam uzunlukta dev geçişi gerçekleştirilir. Bu bir beta düğüm kümesidir ve kredi cinsinden çalışma süresine göre faturalandırılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Oluşturulacak görüntüyü tanımlayan metin istemi. Gönderilmeden önce baştaki ve sondaki boşluklar kaldırılır. | STRING | Evet | 1 ila 4096 karakter |
| `seed` | Yeniden üretilebilirlik için oluşturulan sonucu kontrol eden rastgele tohum (varsayılan: 42). | INT | Evet | 0 ila 18446744073709551615 |
| `aspect_ratio` | Çıktı görüntüsünün en-boy oranı (varsayılan: "1:1"). | COMBO | Evet | "1:1"<br>"3:4"<br>"2:3"<br>"3:2"<br>"4:3"<br>"16:9"<br>"9:16"<br>"21:9" |
| `megapixels` | Toplam piksel bütçesi. 1.0, kare oranda yaklaşık 1024x1024'tür (varsayılan: 1.0). | FLOAT | Evet | 0.1 ila 16.0 (adım 0.1) |
| `turbo` | Turbo LoRA'yı kısa bir zamanlamayla çalıştırır; biraz kaliteden ödün verip çok daha hızlı bir çalışma sağlar. Kapalıyken LoRA olmadan tam dev geçişi çalışır (varsayılan: True). | BOOLEAN | Evet | True / False |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Metin isteminden oluşturulan görüntü; diğer düğümlere aktarılabilen bir ComfyUI görüntü tensörü olarak döndürülür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudFlux2TextToImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `1b51a8ab89ae7c355dec4256a1a25a09a15e192c72fc8d1862c652dbdf337fcb`
