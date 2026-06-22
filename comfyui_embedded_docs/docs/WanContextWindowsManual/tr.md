# WAN Bağlam Pencereleri (Manuel)

WAN Bağlam Pencereleri (Manuel) düğümü, 2 boyutlu işleme sahip WAN benzeri modeller için bağlam pencerelerini manuel olarak yapılandırmanıza olanak tanır. Pencere uzunluğunu, örtüşmeyi, zamanlama yöntemini ve birleştirme tekniğini belirterek örnekleme sırasında özel bağlam penceresi ayarları uygular. Bu, modelin farklı bağlam bölgelerinde bilgiyi nasıl işlediği üzerinde hassas kontrol sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Örnekleme sırasında bağlam pencerelerinin uygulanacağı model. | MODEL | Evet | - |
| `bağlam_uzunluğu` | Bağlam penceresinin uzunluğu (varsayılan: 81). | INT | Evet | 1 ila 1048576 |
| `bağlam_örtüşmesi` | Bağlam penceresinin örtüşme miktarı (varsayılan: 30). | INT | Evet | 0 ila 1048576 |
| `bağlam_çizelgesi` | Bağlam penceresinin adım aralığı. | COMBO | Evet | `"static_standard"`<br>`"uniform_standard"`<br>`"uniform_looped"`<br>`"batched"` |
| `bağlam_adımı` | Bağlam penceresinin adım aralığı; yalnızca tekdüze zamanlamalar için geçerlidir (varsayılan: 1). | INT | Evet | 1 ila 1048576 |
| `kapalı_döngü` | Bağlam penceresi döngüsünün kapatılıp kapatılmayacağı; yalnızca döngülü zamanlamalar için geçerlidir (varsayılan: False). | BOOLEAN | Evet | - |
| `birleştirme_yöntemi` | Bağlam pencerelerini birleştirmek için kullanılacak yöntem (varsayılan: "pyramid"). | COMBO | Evet | `"pyramid"`<br>`"gaussian"`<br>`"average"`<br>`"overlap"` |
| `freenoise` | FreeNoise gürültü karıştırmanın uygulanıp uygulanmayacağı; pencere karışımını iyileştirir (varsayılan: False). | BOOLEAN | Evet | - |

**Not:** `context_stride` parametresi yalnızca tekdüze zamanlamaları etkiler ve `closed_loop` yalnızca döngülü zamanlamalar için geçerlidir. Bağlam uzunluğu ve örtüşme değerleri, işleme sırasında minimum geçerli değerlerin sağlanması için otomatik olarak ayarlanır. `fuse_method` parametresi artık yalnızca "pyramid" değil, ek seçenekler de içermektedir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Uygulanan bağlam penceresi yapılandırmasına sahip model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/tr.md)

---
**Source fingerprint (SHA-256):** `33e539f1e6647a6a2bc98fadc357a25279b0900746f5b3d568e2782cdb770258`
