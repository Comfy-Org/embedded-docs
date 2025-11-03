> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleCreativeNode/tr.md)

Görüntüyü minimum değişikliklerle 4K çözünürlüğe yükseltir. Bu düğüm, orijinal içeriği korurken ve ince yaratıcı detaylar eklerken görüntü çözünürlüğünü geliştirmek için Stability AI'nin yaratıcı yükseltme teknolojisini kullanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `görüntü` | IMAGE | Evet | - | Yükseltilecek giriş görüntüsü |
| `istem` | STRING | Evet | - | Çıktı görüntüsünde görmek istedikleriniz. Öğeleri, renkleri ve konuları net bir şekilde tanımlayan güçlü, betimleyici bir prompt daha iyi sonuçlara yol açacaktır. (varsayılan: boş dize) |
| `yaratıcılık` | FLOAT | Evet | 0.1-0.5 | Başlangıç görüntüsü tarafından ağır şekilde koşullandırılmayan ek detaylar oluşturma olasılığını kontrol eder. (varsayılan: 0.3) |
| `stil_önayarı` | COMBO | Evet | Birden fazla seçenek mevcut | İsteğe bağlı olarak oluşturulan görüntünün istediğiniz tarzı. Seçenekler arasında Stability AI'den çeşitli stil ön ayarları bulunur. |
| `tohum` | INT | Evet | 0-4294967294 | Gürültü oluşturmak için kullanılan rastgele tohum değeri. (varsayılan: 0) |
| `negatif_istem` | STRING | Hayır | - | Çıktı görüntüsünde görmek *istemediklerinizin* anahtar kelimeleri. Bu gelişmiş bir özelliktir. (varsayılan: boş dize) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `görüntü` | IMAGE | 4K çözünürlükte yükseltilmiş görüntü |