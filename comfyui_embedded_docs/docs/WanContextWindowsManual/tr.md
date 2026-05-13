> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/tr.md)

WAN Bağlam Pencereleri (Manuel) düğümü, 2 boyutlu işleme sahip WAN benzeri modeller için bağlam pencerelerini manuel olarak yapılandırmanıza olanak tanır. Pencere uzunluğunu, örtüşmeyi, zamanlama yöntemini ve birleştirme tekniğini belirterek örnekleme sırasında özel bağlam penceresi ayarları uygular. Bu, modelin farklı bağlam bölgelerinde bilgiyi nasıl işlediği üzerinde hassas kontrol sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Örnekleme sırasında bağlam pencerelerinin uygulanacağı model. |
| `context_length` | INT | Evet | 1 ila 1048576 | Bağlam penceresinin uzunluğu (varsayılan: 81). |
| `context_overlap` | INT | Evet | 0 ila 1048576 | Bağlam penceresinin örtüşme miktarı (varsayılan: 30). |
| `context_schedule` | COMBO | Evet | `"static_standard"`<br>`"uniform_standard"`<br>`"uniform_looped"`<br>`"batched"` | Bağlam penceresinin adım aralığı. |
| `context_stride` | INT | Evet | 1 ila 1048576 | Bağlam penceresinin adım aralığı; yalnızca tekdüze zamanlamalar için geçerlidir (varsayılan: 1). |
| `closed_loop` | BOOLEAN | Evet | - | Bağlam penceresi döngüsünün kapatılıp kapatılmayacağı; yalnızca döngülü zamanlamalar için geçerlidir (varsayılan: False). |
| `fuse_method` | COMBO | Evet | `"pyramid"`<br>`"gaussian"`<br>`"average"`<br>`"overlap"` | Bağlam pencerelerini birleştirmek için kullanılacak yöntem (varsayılan: "pyramid"). |
| `freenoise` | BOOLEAN | Evet | - | FreeNoise gürültü karıştırmanın uygulanıp uygulanmayacağı; pencere karışımını iyileştirir (varsayılan: False). |

**Not:** `context_stride` parametresi yalnızca tekdüze zamanlamaları etkiler ve `closed_loop` yalnızca döngülü zamanlamalar için geçerlidir. Bağlam uzunluğu ve örtüşme değerleri, işleme sırasında minimum geçerli değerlerin sağlanması için otomatik olarak ayarlanır. `fuse_method` parametresi artık yalnızca "pyramid" değil, ek seçenekler de içermektedir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Uygulanan bağlam penceresi yapılandırmasına sahip model. |

---
**Source fingerprint (SHA-256):** `33e539f1e6647a6a2bc98fadc357a25279b0900746f5b3d568e2782cdb770258`
