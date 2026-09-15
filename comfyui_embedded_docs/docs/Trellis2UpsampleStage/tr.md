# Trellis2 Üst Örnekleme Aşaması

Bu düğüm, 512 çözünürlüklü bir şekil latentini yüksek çözünürlüklü seyrek koordinatlara yükseltir ve hedef çözünürlükte ikinci şekil aşaması örnekleme geçişini hazırlar. Modelin üretim sırasında kullanabilmesi için koşullandırmaya aşama başına meta verileri ekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `positive` | Üst örnekleme aşaması şekil meta verilerinin eklendiği pozitif koşullandırma. | CONDITIONING | Evet | |
| `negative` | Üst örnekleme aşaması şekil meta verilerinin eklendiği negatif koşullandırma. | CONDITIONING | Evet | |
| `shape_latent` | İlk şekil aşaması KSampler'ından alınan 512 çözünürlüklü şekil latent çıktısı. | LATENT | Evet | |
| `vae` | Şekil latentini çözerek yüksek çözünürlüklü seyrek koordinatlar elde etmek için kullanılan Trellis2 VAE. | VAE | Evet | |
| `target_resolution` | Üst örneklenmiş şeklin voksel çözünürlüğü. Daha yüksek = daha fazla ayrıntı, daha fazla VRAM. Varsayılan: 1024. | INT | Evet | 1024 - 2048 (adım: 128) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | Üst örnekleme aşaması şekil meta verileri eklenmiş pozitif koşullandırma. | CONDITIONING |
| `negative` | Üst örnekleme aşaması şekil meta verileri eklenmiş negatif koşullandırma. | CONDITIONING |
| `latent` | İkinci şekil aşaması örnekleme geçişi için hedef çözünürlükte hazırlanmış, üst örneklenmiş koordinatları, örnek başına koordinat sayılarını ve koordinat çözünürlüğü meta verilerini taşıyan sıfırla doldurulmuş latent. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2UpsampleStage/tr.md)

---
**Source fingerprint (SHA-256):** `0582579bfab487718d69789de508a5ec243d98a0e06ad7165c406154a64677d6`
