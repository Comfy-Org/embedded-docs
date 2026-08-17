# Recraft Görüntüden Görüntüye

Bu düğüm, mevcut bir görseli bir metin istemine ve güç parametresine dayanarak değiştirir. Recraft API'yi kullanarak, sağlanan açıklamaya göre girdi görselini dönüştürür ve güç ayarına bağlı olarak orijinal görselle belirli bir benzerlik korur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Değiştirilecek girdi görseli | IMAGE | Evet | - |
| `prompt` | Görsel üretimi için istem (varsayılan: "", maksimum uzunluk: 1000 karakter) | STRING | Evet | - |
| `n` | Üretilecek görsel sayısı (varsayılan: 1) | INT | Evet | 1-6 |
| `strength` | Orijinal görselle farkı tanımlar, [0, 1] aralığında olmalıdır; 0 neredeyse aynı olduğu, 1 ise çok düşük benzerlik olduğu anlamına gelir (varsayılan: 0.5) | FLOAT | Evet | 0.0-1.0 |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar tohum değerinden bağımsız olarak belirleyici değildir (varsayılan: 0) | INT | Evet | 0-18446744073709551615 |
| `recraft_style` | Görsel üretimi için isteğe bağlı stil seçimi. Sağlanmazsa, varsayılan olarak `realistic_image` kullanılır | STYLEV3 | Hayır | - |
| `negative_prompt` | Görselde istenmeyen öğelerin isteğe bağlı metin açıklaması (varsayılan: "") | STRING | Hayır | - |
| `recraft_controls` | Recraft Controls düğümü aracılığıyla üretim üzerinde isteğe bağlı ek kontroller | CONTROLS | Hayır | - |

**Not:** `seed` parametresi yalnızca düğümün yeniden yürütülmesini tetikler, ancak belirleyici sonuçları garanti etmez. Güç parametresi dahili olarak 2 ondalık basamağa yuvarlanır. İstem doğrulanır ve 1000 karakteri aşmamalıdır. `recraft_style` sağlanmazsa, düğüm varsayılan olarak `realistic_image` stilini kullanır. Infinite Style Library'den bir `style_id` kullanıyorsanız, bunun Vector art stili olmadığından emin olun; aksi takdirde düğüm bir görsel yerine SVG verisi alabilir ve bu da hataya neden olabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Girdi görseline ve isteme dayalı olarak üretilen görsel(ler). Her girdi görseli için `n` adet görsel üretilir, böylece toplam çıktı sayısı girdi sayısının `n` ile çarpımına eşittir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageToImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `1932e55d1dc392e6bd42a0bd29f5aaba44b65997b597648a927fba38a27c90ad`
