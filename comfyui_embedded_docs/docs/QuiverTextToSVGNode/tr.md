> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverTextToSVGNode/tr.md)

Quiver Text to SVG düğümü, Quiver AI modellerini kullanarak bir metin açıklamasından Ölçeklenebilir Vektör Grafiği (SVG) görüntüsü oluşturur. İsteğe bağlı olarak referans görseller ve stil talimatları sağlayarak oluşturma sürecini yönlendirebilirsiniz.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | Yok | İstenen SVG çıktısının metin açıklaması. Ne oluşturulacağına dair ana talimattır. |
| `instructions` | STRING | Hayır | Yok | Ek stil veya biçimlendirme yönergeleri. Bu, isteğe bağlı, ileri düzey bir parametredir. |
| `reference_images` | IMAGE | Hayır | 0 ila 4 görsel | Oluşturmayı yönlendirmek için en fazla 4 referans görsel. Bu isteğe bağlı bir giriştir. |
| `model` | COMBO | Evet | `"Quiver SVG v1"`<br>`"Quiver SVG v1 Max"`<br>`"Quiver SVG v1 Preview"` | SVG oluşturma için kullanılacak model. Mevcut seçenekler Quiver API tarafından belirlenir. |
| `seed` | INT | Evet | 0 ila 2147483647 | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar tohum değerinden bağımsız olarak deterministik değildir. Varsayılan: 0. |

**Not:** `reference_images` girişi en fazla 4 görsel kabul eder. Daha fazlası sağlanırsa, düğüm bir hata verecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `SVG` | SVG | Oluşturulan Ölçeklenebilir Vektör Grafiği (SVG) görüntüsü. |

---
**Source fingerprint (SHA-256):** `634758797a59e5a409424deee808e1d8b5b5852a86eac4bccd7f2634a19fb743`
