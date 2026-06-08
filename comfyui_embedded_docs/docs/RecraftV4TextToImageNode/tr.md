Bu belge, Recraft V4 veya V4 Pro yapay zeka modellerini kullanarak metin açıklamalarından görseller üretir. İsteğinizi harici bir API'ye gönderir ve oluşturulan görselleri döndürür. Modeli, görsel boyutunu ve oluşturulacak görsel sayısını belirterek çıktıyı kontrol edebilirsiniz.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `prompt` | Görsel oluşturma için istem. Maksimum 10.000 karakter. | STRING | Evet | Yok |
| `negative_prompt` | Görselde istenmeyen öğelerin isteğe bağlı metin açıklaması. | STRING | Hayır | Yok |
| `model` | Oluşturma için kullanılacak model. Bir model seçmek, mevcut görsel boyutlarını belirler. | COMBO | Evet | `"recraftv4"`<br>`"recraftv4_pro"` |
| `size` | Oluşturulan görselin boyutu. Mevcut seçenekler seçilen modele bağlıdır. `recraftv4` için varsayılan "1024x1024" değeridir. `recraftv4_pro` için varsayılan "2048x2048" değeridir. | COMBO | Evet | Modele göre değişir |
| `n` | Oluşturulacak görsel sayısı (varsayılan: 1). | INT | Evet | 1 ila 6 |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar tohum değerinden bağımsız olarak deterministik değildir (varsayılan: 0). | INT | Evet | 0 ila 18446744073709551615 |
| `recraft_controls` | Recraft Kontrolleri düğümü aracılığıyla oluşturma üzerinde isteğe bağlı ek kontroller. | CUSTOM | Hayır | Yok |

**Not:** `size` parametresi, mevcut seçenekleri seçili `model`'e göre değişen dinamik bir girdidir. `seed` değeri, tekrarlanabilir görsel çıktılarını garanti etmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan görsel veya görsel grubu. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `77d549a43aeee670b6c42069654017fb6b202ed83ca330389573b790bad6ae6e`
