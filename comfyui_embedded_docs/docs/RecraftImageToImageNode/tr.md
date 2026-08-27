# Recraft Görüntüden Görüntüye

Bu düğüm, mevcut bir görüntüyü metin istemine ve güç parametresine dayalı olarak değiştirir. Girdi görüntüsünü, sağlanan açıklamaya göre dönüştürmek için Recraft V3 API'sini kullanır; orijinal görüntüyle benzerlik, güç ayarı tarafından kontrol edilir.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntü` | Değiştirilecek girdi görüntüsü | IMAGE | Evet | - |
| `istem` | Görüntü üretimi için istem (varsayılan: boş dize, maksimum uzunluk: 1000 karakter) | STRING | Evet | - |
| `n` | Üretilecek görüntü sayısı (varsayılan: 1) | INT | Evet | 1-6 |
| `güç` | Orijinal görüntüyle farkını tanımlar; [0, 1] aralığında olmalıdır; 0 neredeyse aynı, 1 ise çok düşük benzerlik anlamına gelir (varsayılan: 0.5) | FLOAT | Evet | 0.0-1.0 |
| `tohum` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum; gerçek sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0) | INT | Evet | 0-18446744073709551615 |
| `recraft_stili` | Görüntü üretimi için isteğe bağlı stil seçimi. Sağlanmazsa, varsayılan olarak `realistic_image` kullanılır | STYLEV3 | Hayır | - |
| `negatif_istem` | Görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması (varsayılan: boş dize) | STRING | Hayır | - |
| `recraft_kontrolleri` | Recraft Controls düğümü üzerinden üretim üzerinde isteğe bağlı ek kontroller | CONTROLS | Hayır | - |

**Not:** `seed` parametresi yalnızca düğümün yeniden çalıştırılmasını tetikler, ancak deterministik sonuçları garanti etmez. `strength` parametresi dahili olarak 2 ondalık basamağa yuvarlanır. `prompt` doğrulanır ve 1000 karakteri aşmamalıdır. Boş bir `negative_prompt`, negatif istem yok olarak değerlendirilir. `recraft_style` sağlanmazsa, düğüm varsayılan olarak `realistic_image` stilini kullanır. Infinite Style Library'den bir `style_id` kullanıyorsanız, bunun Vektör sanat stili olmadığından emin olun; aksi takdirde düğüm görüntü yerine SVG verisi alabilir ve bu da hataya neden olabilir. Girdi `image` bir batch ise, batch içindeki her görüntü ayrı ayrı işlenir ve tüm sonuçlar birlikte döndürülür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
|-------------|-------------|-----------|
| `image` | Girdi görüntüsüne ve isteme dayalı olarak üretilen görüntü(ler) | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageToImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `1932e55d1dc392e6bd42a0bd29f5aaba44b65997b597648a927fba38a27c90ad`
