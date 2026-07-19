# PiD Koşullandırma

## Genel Bakış

Bir gizli görüntüyü ve bozulma sigma değerini CONDITIONING verisine ekler. Bu, PiD (Pixel-in-Detail) kod çözme veya ölçeklendirme için kullanılır ve işleme öncesinde gizli görüntünün ne kadar bozulacağını kontrol etmenizi sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Gizli görüntü ve bozulma sigmasının ekleneceği koşullandırma verisi. | CONDITIONING | Evet | - |
| `latent` | Koşullandırmaya eklenecek gizli görüntü (VAEEncode veya bir KSampler'dan). | LATENT | Evet | - |
| `latent_format` | Gizli görüntünün formatı. Flux1 ve Flux2 gizli görüntüleri kanal boyutundan otomatik olarak algılanır. SD3 manuel olarak seçilmelidir (varsayılan: "flux"). | COMBO | Evet | `"flux"`<br>`"sd3"` |
| `degrade_sigma` | Uygulanacak bozulma miktarı. 0, temiz bir gizli görüntü anlamına gelir. Bozulmuş gizli görüntü çıktılarını gidermek için bu değeri artırın (varsayılan: 0,0). | FLOAT | Evet | 0,0 ila 1,0 (adım: 0,01) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CONDITIONING` | Gizli görüntü ve bozulma sigma değerlerinin eklendiği orijinal koşullandırma verisi. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `7c8de543629c2299fc2c1e035e433dfc249af594773a77e65c69dde67eb104d7`
