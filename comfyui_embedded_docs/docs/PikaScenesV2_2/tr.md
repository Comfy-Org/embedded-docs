> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaScenesV2_2/tr.md)

PikaScenes v2.2 düğümü, birden fazla görüntüyü birleştirerek tüm girdi görüntülerindeki nesneleri içeren bir video oluşturur. Beş farklı görüntüyü bileşen olarak yükleyebilir ve bunları sorunsuz bir şekilde harmanlayan yüksek kaliteli bir video oluşturabilirsiniz.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `istem_metni` | STRING | Evet | - | Oluşturulacak içeriğin metin açıklaması |
| `negatif_istem` | STRING | Evet | - | Oluşturmada kaçınılacak unsurların metin açıklaması |
| `tohum` | INT | Evet | - | Oluşturma için rastgele tohum değeri |
| `çözünürlük` | STRING | Evet | - | Video için çıktı çözünürlüğü |
| `süre` | INT | Evet | - | Oluşturulan videonun süresi |
| `malzemeler_modu` | COMBO | Hayır | "creative"<br>"precise" | Bileşenleri birleştirme modu (varsayılan: "creative") |
| `en_boy_oranı` | FLOAT | Hayır | 0.4 - 2.5 | En-boy oranı (genişlik / yükseklik) (varsayılan: 1.778) |
| `görüntü_malzemesi_1` | IMAGE | Hayır | - | Video oluşturmak için bileşen olarak kullanılacak görüntü |
| `görüntü_malzemesi_2` | IMAGE | Hayır | - | Video oluşturmak için bileşen olarak kullanılacak görüntü |
| `görüntü_malzemesi_3` | IMAGE | Hayır | - | Video oluşturmak için bileşen olarak kullanılacak görüntü |
| `görüntü_malzemesi_4` | IMAGE | Hayır | - | Video oluşturmak için bileşen olarak kullanılacak görüntü |
| `görüntü_malzemesi_5` | IMAGE | Hayır | - | Video oluşturmak için bileşen olarak kullanılacak görüntü |

**Not:** En fazla 5 adet görüntü bileşeni sağlayabilirsiniz, ancak bir video oluşturmak için en az bir görüntü gereklidir. Düğüm, son video kompozisyonunu oluşturmak için sağlanan tüm görüntüleri kullanacaktır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Tüm girdi görüntülerini birleştiren oluşturulmuş video |