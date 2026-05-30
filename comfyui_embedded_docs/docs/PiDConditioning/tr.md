> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/tr.md)

## Genel Bakış

Bir gizli görüntüyü ve bozulma sigma değerini CONDITIONING verisine ekler. Bu, PiD (Pixel-in-Detail) kod çözme veya ölçeklendirme için kullanılır ve işleme öncesinde gizli görüntünün ne kadar bozulacağını kontrol etmenizi sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `pozitif` | CONDITIONING | Evet | - | Gizli görüntü ve bozulma sigmasının ekleneceği koşullandırma verisi. |
| `latent` | LATENT | Evet | - | Koşullandırmaya eklenecek gizli görüntü (VAEEncode veya bir KSampler'dan). |
| `latent_format` | COMBO | Evet | `"flux"`<br>`"sd3"` | Gizli görüntünün formatı. Flux1 ve Flux2 gizli görüntüleri kanal boyutundan otomatik olarak algılanır. SD3 manuel olarak seçilmelidir (varsayılan: "flux"). |
| `degrade_sigma` | FLOAT | Evet | 0,0 ila 1,0 (adım: 0,01) | Uygulanacak bozulma miktarı. 0, temiz bir gizli görüntü anlamına gelir. Bozulmuş gizli görüntü çıktılarını gidermek için bu değeri artırın (varsayılan: 0,0). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Gizli görüntü ve bozulma sigma değerlerinin eklendiği orijinal koşullandırma verisi. |

---
**Source fingerprint (SHA-256):** `7c8de543629c2299fc2c1e035e433dfc249af594773a77e65c69dde67eb104d7`
