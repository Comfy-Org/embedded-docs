> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageToImageNode/tr.md)

Bu düğüm, bir metin istemi ve güç parametresine dayanarak mevcut bir görüntüyü değiştirir. Giriş görüntüsünü sağlanan açıklamaya göre dönüştürmek için Recraft API'sini kullanır ve güç ayarına bağlı olarak orijinal görüntüyle belirli bir benzerliği korur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `görüntü` | IMAGE | Evet | - | Değiştirilecek giriş görüntüsü |
| `istem` | STRING | Evet | - | Görüntü oluşturma için istem (varsayılan: "", maksimum uzunluk: 1000 karakter) |
| `n` | INT | Evet | 1-6 | Oluşturulacak görüntü sayısı (varsayılan: 1) |
| `güç` | FLOAT | Evet | 0.0-1.0 | Orijinal görüntüyle olan farkı tanımlar, [0, 1] aralığında olmalıdır; 0 neredeyse aynı, 1 ise çok düşük benzerlik anlamına gelir (varsayılan: 0.5) |
| `tohum` | INT | Evet | 0-18446744073709551615 | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0) |
| `recraft_stili` | STYLEV3 | Hayır | - | Görüntü oluşturma için isteğe bağlı stil seçimi. Sağlanmazsa, varsayılan olarak `realistic_image` kullanılır |
| `negatif_istem` | STRING | Hayır | - | Görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması (varsayılan: "") |
| `recraft_kontrolleri` | CONTROLS | Hayır | - | Recraft Kontrolleri düğümü aracılığıyla oluşturma üzerinde isteğe bağlı ek kontroller |

**Not:** `seed` parametresi yalnızca düğümün yeniden yürütülmesini tetikler ancak deterministik sonuçları garanti etmez. Güç parametresi dahili olarak 2 ondalık basamağa yuvarlanır. İstem doğrulanır ve 1000 karakteri geçmemelidir. `recraft_style` sağlanmazsa, düğüm varsayılan olarak `realistic_image` stilini kullanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `görüntü` | IMAGE | Giriş görüntüsü ve isteme dayalı olarak oluşturulan görüntü(ler) |

---
**Source fingerprint (SHA-256):** `e47ab70e77186e62c253c976cdd7942cfb949ba6461914d2b4341f3eca8e14aa`
