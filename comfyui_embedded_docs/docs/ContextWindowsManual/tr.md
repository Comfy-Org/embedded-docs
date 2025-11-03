> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/tr.md)

Context Windows (Manual) düğümü, örnekleme sırasında modeller için bağlam pencerelerini manuel olarak yapılandırmanıza olanak tanır. Verileri yönetilebilir parçalar halinde işlerken parçalar arasında sürekliliği korumak için belirli uzunluk, örtüşme ve zamanlama desenlerine sahip örtüşen bağlam segmentleri oluşturur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Örnekleme sırasında bağlam pencerelerinin uygulanacağı model. |
| `context_length` | INT | Hayır | 1+ | Bağlam penceresinin uzunluğu (varsayılan: 16). |
| `context_overlap` | INT | Hayır | 0+ | Bağlam penceresinin örtüşme miktarı (varsayılan: 4). |
| `context_schedule` | COMBO | Hayır | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` | Bağlam penceresinin adım aralığı. |
| `context_stride` | INT | Hayır | 1+ | Bağlam penceresinin adım aralığı; sadece uniform zamanlamalar için geçerlidir (varsayılan: 1). |
| `closed_loop` | BOOLEAN | Hayır | - | Bağlam penceresi döngüsünün kapatılıp kapatılmayacağı; sadece döngülü zamanlamalar için geçerlidir (varsayılan: False). |
| `fuse_method` | COMBO | Hayır | `PYRAMID`<br>`LIST_STATIC` | Bağlam pencerelerini birleştirmek için kullanılacak yöntem (varsayılan: PYRAMID). |
| `dim` | INT | Hayır | 0-5 | Bağlam pencerelerinin uygulanacağı boyut (varsayılan: 0). |

**Parametre Kısıtlamaları:**

- `context_stride` sadece uniform zamanlamalar seçildiğinde kullanılır
- `closed_loop` sadece döngülü zamanlamalar için geçerlidir
- `dim` 0 ile 5 arasında (dahil) olmalıdır

## Çıktılar

| Çıktı Adı | Veri Türı | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Örnekleme sırasında bağlam pencereleri uygulanmış model. |