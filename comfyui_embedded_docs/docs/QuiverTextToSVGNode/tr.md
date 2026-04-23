> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverTextToSVGNode/tr.md)

# QuiverTextToSVGDüğümü

Quiver Metin SVG Düğümü, Quiver AI modellerini kullanarak bir metin açıklamasından Ölçeklenebilir Vektör Grafiği (SVG) görüntüsü oluşturur. İsteğe bağlı olarak referans görseller ve stil talimatları sağlayarak oluşturma sürecini yönlendirebilirsiniz.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | Yok | İstenen SVG çıktısının metin açıklaması. Bu, ne oluşturulacağına dair ana talimattır. |
| `instructions` | STRING | Hayır | Yok | Ek stil veya biçimlendirme yönergeleri. Bu, isteğe bağlı, gelişmiş bir parametredir. |
| `reference_images` | IMAGE | Hayır | Yok | Oluşturmayı yönlendirmek için en fazla 4 referans görseli. Bu isteğe bağlı bir girdidir. |
| `model` | COMBO | Evet | Birden fazla seçenek mevcut | SVG oluşturma için kullanılacak model. Mevcut seçenekler Quiver API tarafından belirlenir. |
| `seed` | INT | Evet | 0 ile 2147483647 arası | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; gerçek sonuçlar tohum değerinden bağımsız olarak deterministik değildir. Varsayılan: 0. |

**Not:** `reference_images` girdisi en fazla 4 görsel kabul eder. Daha fazlası sağlanırsa, düğüm hata verecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `SVG` | SVG | Oluşturulan Ölçeklenebilir Vektör Grafiği (SVG) görüntüsü. |