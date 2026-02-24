> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToVectorNode/tr.md)

Recraft V4 Metinden Vektöre düğümü, bir metin açıklamasından Ölçeklenebilir Vektör Grafikleri (SVG) illüstrasyonları oluşturur. Görüntü oluşturma için Recraft V4 veya Recraft V4 Pro modelini kullanmak üzere harici bir API'ye bağlanır. Düğüm, girdiğiniz komuta dayalı olarak bir veya daha fazla SVG görüntüsü çıktılar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | Yok | Görüntü oluşturma komutu. Maksimum 10.000 karakter. |
| `negative_prompt` | STRING | Hayır | Yok | Bir görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması. |
| `model` | COMBO | Evet | `"recraftv4"`<br>`"recraftv4_pro"` | Oluşturma için kullanılacak model. Bir model seçmek, mevcut `size` seçeneklerini değiştirir. |
| `size` | COMBO | Evet | `recraftv4` için: `"1024x1024"`, `"1152x896"`, `"896x1152"`, `"1216x832"`, `"832x1216"`, `"1344x768"`, `"768x1344"`, `"1536x640"`, `"640x1536"`<br>`recraftv4_pro` için: `"2048x2048"`, `"2304x1792"`, `"1792x2304"`, `"2432x1664"`, `"1664x2432"`, `"2688x1536"`, `"1536x2688"`, `"3072x1280"`, `"1280x3072"` | Oluşturulan görüntünün boyutu. Mevcut seçenekler seçilen `model`'e bağlıdır. Varsayılan, `recraftv4` için `"1024x1024"` ve `recraftv4_pro` için `"2048x2048"`'dir. |
| `n` | INT | Evet | 1 - 6 | Oluşturulacak görüntü sayısı (varsayılan: 1). |
| `seed` | INT | Evet | 0 - 18446744073709551615 | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirlemek için tohum; gerçek sonuçlar tohumdan bağımsız olarak belirleyici değildir. |
| `recraft_controls` | CUSTOM | Hayır | Yok | Recraft Kontrolleri düğümü aracılığıyla oluşturma üzerinde isteğe bağlı ek kontroller. |

**Not:** `size` parametresi, mevcut seçenekleri seçilen `model`'e göre değişen dinamik bir girdidir. `seed` değeri, harici API'den tekrarlanabilir sonuçlar garanti etmez.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | SVG | Oluşturulan Ölçeklenebilir Vektör Grafikleri (SVG) görüntüsü/görüntüleri. |