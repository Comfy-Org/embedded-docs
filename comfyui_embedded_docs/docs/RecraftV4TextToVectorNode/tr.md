Recraft V4 Metinden Vektöre düğümü, bir metin açıklamasından Ölçeklenebilir Vektör Grafikleri (SVG) çizimleri oluşturur. Görüntü oluşturma için Recraft V4 veya Recraft V4 Pro modelini kullanmak üzere harici bir API'ye bağlanır. Düğüm, isteminize bağlı olarak bir veya daha fazla SVG görüntüsü çıktısı verir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `prompt` | Görüntü oluşturma için istem. Maksimum 10.000 karakter. | STRING | Evet | Yok |
| `negative_prompt` | Görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması. | STRING | Hayır | Yok |
| `model` | Oluşturma için kullanılacak model. Bir model seçmek, mevcut `size` seçeneklerini değiştirir. | COMBO | Evet | `"recraftv4"`<br>`"recraftv4_pro"` |
| `size` | Oluşturulan görüntünün boyutu. Mevcut seçenekler seçilen `model`'e bağlıdır. `recraftv4` için varsayılan `"1024x1024"`, `recraftv4_pro` için varsayılan `"2048x2048"`'dir. | COMBO | Evet | `recraftv4` için: `"1024x1024"`, `"1152x896"`, `"896x1152"`, `"1216x832"`, `"832x1216"`, `"1344x768"`, `"768x1344"`, `"1536x640"`, `"640x1536"`<br>`recraftv4_pro` için: `"2048x2048"`, `"2304x1792"`, `"1792x2304"`, `"2432x1664"`, `"1664x2432"`, `"2688x1536"`, `"1536x2688"`, `"3072x1280"`, `"1280x3072"` |
| `n` | Oluşturulacak görüntü sayısı (varsayılan: 1). | INT | Evet | 1 ila 6 |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar tohum değerinden bağımsız olarak deterministik değildir. | INT | Evet | 0 ila 18446744073709551615 |
| `recraft_controls` | Recraft Kontrolleri düğümü aracılığıyla oluşturma üzerinde isteğe bağlı ek kontroller. | CUSTOM | Hayır | Yok |

**Not:** `size` parametresi, mevcut seçenekleri seçilen `model`'e göre değişen dinamik bir girdidir. `seed` değeri, harici API'den tekrarlanabilir sonuçları garanti etmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan Ölçeklenebilir Vektör Grafikleri (SVG) görüntüsü/görüntüleri. | SVG |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToVectorNode/tr.md)

---
**Source fingerprint (SHA-256):** `ffab67555923cea29b50ae71e3ffaad13340aead4d01973a70244468fae4420d`
