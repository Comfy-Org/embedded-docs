> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityStableImageUltraNode/tr.md)

İstem ve çözünürlük temelinde görüntüleri eşzamanlı olarak oluşturur. Bu düğüm, Stability AI'nin Stable Image Ultra modelini kullanarak görüntüler oluşturur, metin isteminizi işler ve belirtilen en-boy oranı ve stile sahip karşılık gelen bir görüntü üretir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | - | Çıktı görüntüsünde görmek istediğiniz şey. Öğeleri, renkleri ve konuları net bir şekilde tanımlayan güçlü, betimleyici bir istem daha iyi sonuçlara yol açacaktır. Belirli bir kelimenin ağırlığını kontrol etmek için `(kelime:ağırlık)` biçimini kullanın; burada `kelime` ağırlığını kontrol etmek istediğiniz kelime, `ağırlık` ise 0 ile 1 arasında bir değerdir. Örneğin: `Gökyüzü canlı bir (mavi:0.3) ve (yeşil:0.8) renkteydi` ifadesi, mavi ve yeşil ama maviden daha çok yeşil olan bir gökyüzünü ifade eder. |
| `aspect_ratio` | COMBO | Evet | Birden fazla seçenek mevcut | Oluşturulan görüntünün en-boy oranı. |
| `style_preset` | COMBO | Hayır | Birden fazla seçenek mevcut | İsteğe bağlı olarak oluşturulan görüntünün istediğiniz stili. |
| `seed` | INT | Evet | 0-4294967294 | Gürültüyü oluşturmak için kullanılan rastgele tohum değeri. |
| `image` | IMAGE | Hayır | - | İsteğe bağlı girdi görüntüsü. |
| `negative_prompt` | STRING | Hayır | - | Çıktı görüntüsünde görmek istemediğiniz şeyleri açıklayan bir metin parçası. Bu gelişmiş bir özelliktir. |
| `image_denoise` | FLOAT | Hayır | 0.0-1.0 | Girdi görüntüsünün gürültü giderme seviyesi; 0.0 girdiyle aynı görüntüyü verir, 1.0 ise hiç görüntü sağlanmamış gibi davranır. Varsayılan: 0.5 |

**Not:** Bir girdi görüntüsü sağlanmadığında, `image_denoise` parametresi otomatik olarak devre dışı bırakılır.

## Çıktılar

| Çıktı Adı | Veri Türı | Açıklama |
|-------------|-----------|-------------|
| `output` | IMAGE | Girdi parametrelerine dayalı olarak oluşturulan görüntü. |