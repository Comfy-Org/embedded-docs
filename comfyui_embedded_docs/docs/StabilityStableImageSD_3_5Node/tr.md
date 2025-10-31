> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityStableImageSD_3_5Node/tr.md)

Bu düğüm, Stability AI'nin Stable Diffusion 3.5 modelini kullanarak görüntüleri senkronize bir şekilde oluşturur. Metin prompt'larına dayalı görüntüler oluşturur ve ayrıca girdi olarak sağlandığında mevcut görüntüleri değiştirebilir. Düğüm, çıktıyı özelleştirmek için çeşitli en-boy oranlarını ve stil ön ayarlarını destekler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | - | Çıktı görüntüsünde görmek istediğiniz şey. Öğeleri, renkleri ve konuları net bir şekilde tanımlayan güçlü, betimleyici bir prompt daha iyi sonuçlara yol açacaktır. (varsayılan: boş string) |
| `model` | COMBO | Evet | Birden fazla seçenek mevcut | Oluşturma için kullanılacak Stable Diffusion 3.5 modeli. |
| `aspect_ratio` | COMBO | Evet | Birden fazla seçenek mevcut | Oluşturulan görüntünün en-boy oranı. (varsayılan: 1:1 oranı) |
| `style_preset` | COMBO | Hayır | Birden fazla seçenek mevcut | İsteğe bağlı olarak oluşturulan görüntünün istediğiniz stili. |
| `cfg_scale` | FLOAT | Evet | 1.0 - 10.0 | Difüzyon sürecinin prompt metnine ne kadar sıkı bir şekilde bağlı kaldığı (daha yüksek değerler görüntünüzü prompt'unuza daha yakın tutar). (varsayılan: 4.0) |
| `seed` | INT | Evet | 0 - 4294967294 | Gürültü oluşturmak için kullanılan rastgele seed değeri. (varsayılan: 0) |
| `image` | IMAGE | Hayır | - | Görüntüden-görüntüye oluşturma için isteğe bağlı girdi görüntüsü. |
| `negative_prompt` | STRING | Hayır | - | Çıktı görüntüsünde görmek istemediğiniz şeylerin anahtar kelimeleri. Bu gelişmiş bir özelliktir. (varsayılan: boş string) |
| `image_denoise` | FLOAT | Hayır | 0.0 - 1.0 | Girdi görüntüsünün gürültü giderme seviyesi; 0.0 girdiyle aynı görüntüyü verir, 1.0 ise hiç görüntü sağlanmamış gibi davranır. (varsayılan: 0.5) |

**Not:** Bir `image` sağlandığında, düğüm görüntüden-görüntüye oluşturma moduna geçer ve `aspect_ratio` parametresi otomatik olarak girdi görüntüsünden belirlenir. Hiç `image` sağlanmadığında, `image_denoise` parametresi dikkate alınmaz.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Oluşturulan veya değiştirilen görüntü. |