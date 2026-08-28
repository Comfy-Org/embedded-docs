# Trellis2UpsampleStage

Bu düğüm, ilk şekil aşaması örnekleme geçişinde üretilen 512 çözünürlüklü şekil latentini alır, bunu daha yüksek bir hedef çözünürlüğe ölçekler ve ikinci şekil aşaması örnekleme geçişi için gereken koşullandırma ve latent hazırlar. Koşullandırmaya aşama başına meta veriler ekler, böylece model bunu üretim sırasında kullanabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `positive` | Yukarı örnekleme aşaması şekil meta verilerinin eklendiği pozitif koşullandırma. | CONDITIONING | Evet | |
| `negative` | Yukarı örnekleme aşaması şekil meta verilerinin eklendiği negatif koşullandırma. | CONDITIONING | Evet | |
| `shape_latent` | İlk şekil aşaması KSampler'ından çıkan 512 çözünürlüklü şekil latent çıktısı. | LATENT | Evet | |
| `vae` | Şekil latentini yüksek çözünürlüklü seyrek koordinatlara çözmek için kullanılan Trellis2 VAE. | VAE | Evet | |
| `target_resolution` | Yukarı örneklenmiş şeklin voxel çözünürlüğü. Daha yüksek = daha fazla detay, daha fazla VRAM. Varsayılan: 1024. | INT | Evet | 1024 - 2048 (step 128) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | Yukarı örnekleme aşaması şekil meta verileri eklenmiş pozitif koşullandırma. | CONDITIONING |
| `negative` | Yukarı örnekleme aşaması şekil meta verileri eklenmiş negatif koşullandırma. | CONDITIONING |
| `latent` | Hedef çözünürlükte ikinci şekil aşaması örnekleme geçişi için hazırlanmış, yukarı örneklenmiş koordinatları ve çözünürlük meta verilerini taşıyan sıfır dolgulu latent. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2UpsampleStage/tr.md)

---
**Source fingerprint (SHA-256):** `0582579bfab487718d69789de508a5ec243d98a0e06ad7165c406154a64677d6`
