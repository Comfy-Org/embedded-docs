> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftTextToVectorNode/tr.md)

İstem ve çözünürlük temelinde SVG'yi eşzamanlı olarak oluşturur. Bu düğüm, metin istemlerini Recraft API'sine göndererek vektör çizimler oluşturur ve oluşturulan SVG içeriğini döndürür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `istem` | STRING | Evet | - | Görsel oluşturma için istem. (varsayılan: "") |
| `alt_stil` | COMBO | Evet | Birden fazla seçenek mevcut | Oluşturma için kullanılacak belirli çizim stili. Seçenekler RecraftStyleV3'te mevcut olan vektör çizim alt stilleri tarafından belirlenir. |
| `boyut` | COMBO | Evet | Birden fazla seçenek mevcut | Oluşturulan görselin boyutu. (varsayılan: 1024x1024) |
| `n` | INT | Evet | 1-6 | Oluşturulacak görsel sayısı. (varsayılan: 1, min: 1, maks: 6) |
| `tohum` | INT | Evet | 0-18446744073709551615 | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum; gerçek sonuçlar tohuma bakılmaksızın belirleyici değildir. (varsayılan: 0, min: 0, maks: 18446744073709551615) |
| `negatif_istem` | STRING | Hayır | - | Bir görselde istenmeyen öğelerin isteğe bağlı metin açıklaması. (varsayılan: "") |
| `recraft_kontrolleri` | CONTROLS | Hayır | - | Recraft Kontroller düğümü aracılığıyla oluşturma üzerinde isteğe bağlı ek kontroller. |

**Not:** `seed` parametresi yalnızca düğümün ne zaman yeniden çalıştırılacağını kontrol eder ancak oluşturma sonuçlarını belirleyici hale getirmez.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `SVG` | SVG | SVG formatında oluşturulan vektör çizimi |