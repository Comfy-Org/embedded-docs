> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DeprecatedCheckpointLoader/tr.md)

CheckpointLoader düğümü, gelişmiş yükleme işlemleri için tasarlanmış olup özellikle model kontrol noktalarını konfigürasyonlarıyla birlikte yüklemeyi amaçlar. Modelin başlatılması ve çalıştırılması için gerekli olan model bileşenlerinin, belirtilen dizinlerden konfigürasyonlar ve kontrol noktaları dahil olmak üzere alınmasını sağlar.

## Girdiler

| Parametre    | Veri Tipi | Açıklama |
|--------------|-----------|----------|
| `config_name` | COMBO[STRING] | Kullanılacak konfigürasyon dosyasının adını belirtir. Modelin parametrelerini ve ayarlarını belirlemede kritik öneme sahiptir, modelin davranışını ve performansını etkiler. |
| `ckpt_name`  | COMBO[STRING] | Yüklenecek kontrol noktası dosyasının adını belirtir. Bu, başlatılan modelin durumunu doğrudan etkileyerek başlangıç ağırlıklarını ve yanlılıklarını etkiler. |

## Çıktılar

| Parametre | Veri Tipi | Açıklama |
|-----------|-----------|----------|
| `model`   | MODEL     | Kontrol noktasından yüklenen, daha fazla işlem veya çıkarım için hazır olan birincil modeli temsil eder. |
| `clip`    | CLIP      | Kontrol noktasından yüklenen, mevcut ve talep edilmişse CLIP model bileşenini sağlar. |
| `vae`     | VAE       | Kontrol noktasından yüklenen, mevcut ve talep edilmişse VAE model bileşenini sunar. |