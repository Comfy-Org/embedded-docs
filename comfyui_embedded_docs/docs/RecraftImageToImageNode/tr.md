# Recraft Görüntüden Görüntüye

Bu düğüm, bir metin istemi ve güç parametresine dayanarak mevcut bir görüntüyü değiştirir. Giriş görüntüsünü sağlanan açıklamaya göre dönüştürmek için Recraft API'sini kullanır ve güç ayarına bağlı olarak orijinal görüntüyle belirli bir benzerliği korur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | Değiştirilecek giriş görüntüsü | IMAGE | Evet | - |
| `istem` | Görüntü oluşturma için istem (varsayılan: "", maksimum uzunluk: 1000 karakter) | STRING | Evet | - |
| `n` | Oluşturulacak görüntü sayısı (varsayılan: 1) | INT | Evet | 1-6 |
| `güç` | Orijinal görüntüyle olan farkı tanımlar, [0, 1] aralığında olmalıdır; 0 neredeyse aynı, 1 ise çok düşük benzerlik anlamına gelir (varsayılan: 0.5) | FLOAT | Evet | 0.0-1.0 |
| `tohum` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0) | INT | Evet | 0-18446744073709551615 |
| `recraft_stili` | Görüntü oluşturma için isteğe bağlı stil seçimi. Sağlanmazsa, varsayılan olarak `realistic_image` kullanılır | STYLEV3 | Hayır | - |
| `negatif_istem` | Görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması (varsayılan: "") | STRING | Hayır | - |
| `recraft_kontrolleri` | Recraft Kontrolleri düğümü aracılığıyla oluşturma üzerinde isteğe bağlı ek kontroller | CONTROLS | Hayır | - |

**Not:** `seed` parametresi yalnızca düğümün yeniden yürütülmesini tetikler ancak deterministik sonuçları garanti etmez. Güç parametresi dahili olarak 2 ondalık basamağa yuvarlanır. İstem doğrulanır ve 1000 karakteri geçmemelidir. `recraft_style` sağlanmazsa, düğüm varsayılan olarak `realistic_image` stilini kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | Giriş görüntüsü ve isteme dayalı olarak oluşturulan görüntü(ler) | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageToImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `e47ab70e77186e62c253c976cdd7942cfb949ba6461914d2b4341f3eca8e14aa`
