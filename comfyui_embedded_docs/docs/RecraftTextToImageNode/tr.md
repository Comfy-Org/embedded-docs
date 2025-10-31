> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftTextToImageNode/tr.md)

İstem ve çözünürlük temelinde senkronize olarak görüntü oluşturur. Bu düğüm, metin açıklamalarından belirtilen boyutlar ve stil seçenekleriyle görüntüler oluşturmak için Recraft API'sına bağlanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `istem` | STRING | Evet | - | Görüntü oluşturma için istem. (varsayılan: "") |
| `boyut` | COMBO | Evet | "1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" | Oluşturulan görüntünün boyutu. (varsayılan: "1024x1024") |
| `n` | INT | Evet | 1-6 | Oluşturulacak görüntü sayısı. (varsayılan: 1) |
| `tohum` | INT | Evet | 0-18446744073709551615 | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar tohum değerinden bağımsız olarak belirsizdir. (varsayılan: 0) |
| `recraft_stili` | COMBO | Hayır | Birden fazla seçenek mevcut | Görüntü oluşturma için isteğe bağlı stil seçimi. |
| `negatif_istem` | STRING | Hayır | - | Bir görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması. (varsayılan: "") |
| `recraft_kontrolleri` | COMBO | Hayır | Birden fazla seçenek mevcut | Recraft Kontroller düğümü aracılığıyla oluşturma üzerinde isteğe bağlı ek kontroller. |

**Not:** `seed` parametresi yalnızca düğümün ne zaman yeniden çalıştırılacağını kontrol eder, ancak görüntü oluşturma sürecini belirleyici hale getirmez. Gerçek çıktı görüntüleri aynı tohum değeriyle bile değişiklik gösterecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Tensor çıktısı olarak oluşturulan görüntü(ler). |