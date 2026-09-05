# ComfyCloudMageFlowTurboTextToImageNode

Bu Comfy Cloud düğümü, Mage-Flow Turbo iş akışını (`mage-flow-turbo/text-to-image`) kullanarak bir metin isteminden görüntü üretir. Mage-Flow modelinin damıtılmış bir sürümünü çalıştırır; bu sürüm, cfg değeri 1 iken görüntüyü 4 adımda üretir ve tam bir Mage-Flow geçişinin GPU süresinin yaklaşık yedide birini alır. Bu da onu hızlı yineleme için tasarlanmış varyant haline getirir.

## Girdiler

Düğüm sınıfının kendisi, mevcut kaynakta girdi widget'ları bildirmez; girdi şeması, tanımı kaynak anlık görüntüsünde bulunmayan ortak temel sınıf `_ComfyCloudMageFlowNode` sınıfından devralınır. Düğüm özetine ve metinden görüntüye iş akışı adına dayanarak, düğüm, üretilecek görüntüyü tanımlayan bir metin istemi alır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Üretilecek görüntüyü tanımlayan metin istemi. Tam parametre adı, devralınan `_ComfyCloudMageFlowNode` temel şeması tarafından belirlenir ve bu etiketten farklı olabilir. | STRING | Evet | Free text |

Not: Sağlanan kaynakta bulunmayan, devralınan temel düğüm tanımında ek girdi parametreleri mevcut olabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Metin isteminden üretilen görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMageFlowTurboTextToImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `8d867a0c906028597ef52c75f5c9a994fdc00211c7aae410ffca8204943f0c34`
