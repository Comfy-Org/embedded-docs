# Recraft Görüntüden Görüntüye

Bu düğüm, mevcut bir görüntüyü bir metin istemine ve bir güç ayarına göre değiştirir. Görüntüyü Recraft V3 API'sine gönderir ve istemi takip eden, güç değerine bağlı olarak orijinal görüntüye az çok benzeyen yeni bir görüntü döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntü` | Değiştirilecek giriş görüntüsü. Bir görüntü grubu sağlandığında, her görüntü ayrı ayrı işlenir. | IMAGE | Evet | - |
| `istem` | Görüntü oluşturma için istem. Varsayılan: boş dize. Maksimum uzunluk: 1000 karakter. | STRING | Evet | - |
| `n` | Oluşturulacak görüntü sayısı. Varsayılan: 1. | INT | Evet | 1-6 |
| `güç` | Orijinal görüntüyle farkı tanımlar; [0, 1] aralığında olmalıdır; burada 0 neredeyse aynı, 1 ise çok düşük benzerlik anlamına gelir. Varsayılan: 0.5. | FLOAT | Evet | 0.0-1.0 (adım: 0.01) |
| `tohum` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum; gerçek sonuçlar tohumdan bağımsız olarak deterministik değildir. Varsayılan: 0. | INT | Evet | 0-18446744073709551615 |
| `recraft_stili` | Görüntü oluşturma için isteğe bağlı stil seçimi. Sağlanmazsa varsayılan olarak `realistic_image` kullanılır. | STYLEV3 | Hayır | - |
| `negatif_istem` | Görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması. Varsayılan: boş dize. Bir giriş soketi olarak sağlanır. | STRING | Hayır | - |
| `recraft_kontrolleri` | Recraft Controls düğümü aracılığıyla oluşturma üzerinde isteğe bağlı ek kontroller. | CONTROLS | Hayır | - |

**Not:** `seed` parametresi yalnızca düğümün yeniden yürütülmesini tetikler ancak deterministik sonuçları garanti etmez. `strength` parametresi dahili olarak 2 ondalık basamağa yuvarlanır. `prompt` doğrulanır ve 1000 karakteri aşmamalıdır. Boş bir `negative_prompt`, negatif istem yok olarak değerlendirilir. `recraft_style` sağlanmazsa düğüm varsayılan olarak `realistic_image` stiline geçer. Infinite Style Library'den bir `style_id` kullanırsanız, bunun bir Vector art stili olmadığından emin olun; çünkü bu, düğümün görüntü yerine SVG verisi almasına ve hata oluşmasına neden olabilir. Giriş `image` bir grup olduğunda, gruptaki her görüntü ayrı ayrı işlenir ve tüm sonuçlar birlikte döndürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Giriş görüntüsü, istem ve güç ayarına göre oluşturulan görüntü(ler). | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageToImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `1932e55d1dc392e6bd42a0bd29f5aaba44b65997b597648a927fba38a27c90ad`
