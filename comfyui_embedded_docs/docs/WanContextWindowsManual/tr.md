> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/tr.md)

WAN Context Windows (Manual) düğümü, 2 boyutlu işleme yeteneğine sahip WAN benzeri modeller için bağlam pencerelerini manuel olarak yapılandırmanıza olanak tanır. Örnekleme sırasında pencere uzunluğu, örtüşme, zamanlama yöntemi ve füzyon tekniğini belirterek özel bağlam penceresi ayarları uygular. Bu, modelin farklı bağlam bölgeleri boyunca bilgiyi nasıl işlediği üzerinde hassas kontrol sağlar.

## Girdiler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Örnekleme sırasında bağlam pencerelerinin uygulanacağı model. |
| `context_length` | INT | Evet | 1 - 1048576 | Bağlam penceresinin uzunluğu (varsayılan: 81). |
| `context_overlap` | INT | Evet | 0 - 1048576 | Bağlam penceresinin örtüşme miktarı (varsayılan: 30). |
| `context_schedule` | COMBO | Evet | "static_standard"<br>"uniform_standard"<br>"uniform_looped"<br>"batched" | Bağlam penceresinin adım aralığı. |
| `context_stride` | INT | Evet | 1 - 1048576 | Bağlam penceresinin adım aralığı; sadece uniform zamanlamalar için geçerlidir (varsayılan: 1). |
| `closed_loop` | BOOLEAN | Evet | - | Bağlam penceresi döngüsünün kapatılıp kapatılmayacağı; sadece döngülü zamanlamalar için geçerlidir (varsayılan: False). |
| `fuse_method` | COMBO | Evet | "pyramid" | Bağlam pencerelerini birleştirmek için kullanılacak yöntem (varsayılan: "pyramid"). |

**Not:** `context_stride` parametresi sadece uniform zamanlamaları etkiler ve `closed_loop` sadece döngülü zamanlamalar için geçerlidir. Bağlam uzunluğu ve örtüşme değerleri, işleme sırasında minimum geçerli değerleri sağlamak için otomatik olarak ayarlanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Uygulanan bağlam penceresi yapılandırmasına sahip model. |