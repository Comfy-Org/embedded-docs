> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaScenesV2_2/tr.md)

PikaScenes v2.2 düğümü, birden fazla görüntüyü birleştirerek tüm girdi görüntülerindeki nesneleri içeren bir video oluşturur. Beş farklı görüntüyü bileşen olarak yükleyebilir ve bunları sorunsuz bir şekilde harmanlayan yüksek kaliteli bir video oluşturabilirsiniz.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt_text` | STRING | Evet | - | Oluşturulacak içeriğin metin açıklaması |
| `negative_prompt` | STRING | Evet | - | Oluşturmada kaçınılacak unsurların metin açıklaması |
| `seed` | INT | Evet | - | Oluşturma için rastgele tohum değeri |
| `resolution` | STRING | Evet | - | Video için çıktı çözünürlüğü |
| `duration` | INT | Evet | - | Oluşturulan videonun süresi |
| `ingredients_mode` | COMBO | Hayır | "creative"<br>"precise" | Bileşenleri birleştirme modu (varsayılan: "creative") |
| `aspect_ratio` | FLOAT | Hayır | 0.4 - 2.5 | En-boy oranı (genişlik / yükseklik) (varsayılan: 1.778) |
| `image_ingredient_1` | IMAGE | Hayır | - | Video oluşturmak için bileşen olarak kullanılacak görüntü |
| `image_ingredient_2` | IMAGE | Hayır | - | Video oluşturmak için bileşen olarak kullanılacak görüntü |
| `image_ingredient_3` | IMAGE | Hayır | - | Video oluşturmak için bileşen olarak kullanılacak görüntü |
| `image_ingredient_4` | IMAGE | Hayır | - | Video oluşturmak için bileşen olarak kullanılacak görüntü |
| `image_ingredient_5` | IMAGE | Hayır | - | Video oluşturmak için bileşen olarak kullanılacak görüntü |

**Not:** En fazla 5 adet görüntü bileşeni sağlayabilirsiniz, ancak bir video oluşturmak için en az bir görüntü gereklidir. Düğüm, son video kompozisyonunu oluşturmak için sağlanan tüm görüntüleri kullanacaktır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Tüm girdi görüntülerini birleştiren oluşturulmuş video |