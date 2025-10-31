> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleConservativeNode/tr.md)

Görüntüyü minimum değişikliklerle 4K çözünürlüğe yükseltir. Bu düğüm, orijinal içeriği korurken ve yalnızca ince değişiklikler yaparak görüntü çözünürlüğünü artırmak için Stability AI'nin konservatif yükseltme yöntemini kullanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Yükseltilecek giriş görüntüsü |
| `prompt` | STRING | Evet | - | Çıktı görüntüsünde görmek istediğiniz içerik. Öğeleri, renkleri ve konuları net bir şekilde tanımlayan güçlü, betimleyici bir prompt daha iyi sonuçlara yol açacaktır. (varsayılan: boş dize) |
| `creativity` | FLOAT | Evet | 0.2-0.5 | Başlangıç görüntüsü tarafından ağır şekilde koşullandırılmamış ek detaylar oluşturma olasılığını kontrol eder. (varsayılan: 0.35) |
| `seed` | INT | Evet | 0-4294967294 | Gürültü oluşturmak için kullanılan rastgele tohum değeri. (varsayılan: 0) |
| `negative_prompt` | STRING | Hayır | - | Çıktı görüntüsünde görmek istemediğiniz içeriklerin anahtar kelimeleri. Bu gelişmiş bir özelliktir. (varsayılan: boş dize) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | 4K çözünürlükte yükseltilmiş görüntü |