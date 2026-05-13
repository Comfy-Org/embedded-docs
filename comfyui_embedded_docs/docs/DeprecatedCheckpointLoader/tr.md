> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DeprecatedCheckpointLoader/tr.md)

CheckpointLoader düğümü, gelişmiş yükleme işlemleri için tasarlanmış olup, özellikle model kontrol noktalarını ve bunların yapılandırmalarını yükler. Belirtilen dizinlerden yapılandırmalar ve kontrol noktaları dahil olmak üzere, üretken modelleri başlatmak ve çalıştırmak için gerekli model bileşenlerinin alınmasını kolaylaştırır.

## Girişler

| Parametre | Veri Türü | Açıklama |
|--------------|--------------|-------------|
| `config_name` | COMBO[STRING] | Kullanılacak yapılandırma dosyasının adını belirtir. Bu, modelin parametrelerini ve ayarlarını belirlemek için çok önemlidir ve modelin davranışını ve performansını etkiler. |
| `ckpt_name`  | COMBO[STRING] | Yüklenecek kontrol noktası dosyasının adını belirtir. Bu, başlatılan modelin durumunu doğrudan etkiler ve ilk ağırlıklarını ve sapmalarını etkiler. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `model`   | MODEL     | Kontrol noktasından yüklenen ve daha ileri işlemler veya çıkarım için hazır olan ana modeli temsil eder. |
| `clip`    | CLIP      | Varsa ve talep edilirse, kontrol noktasından yüklenen CLIP model bileşenini sağlar. |
| `vae`     | VAE       | Varsa ve talep edilirse, kontrol noktasından yüklenen VAE model bileşenini sağlar. |