PikaScenes v2.2 düğümü, birden fazla görüntüyü birleştirerek tüm giriş görüntülerindeki nesneleri içeren bir video oluşturur. En fazla beş farklı görüntüyü bileşen olarak yükleyebilir ve bunları sorunsuz bir şekilde harmanlayan yüksek kaliteli bir video oluşturabilirsiniz.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `prompt_text` | Oluşturulacak içeriğin metin açıklaması | STRING | Evet | - |
| `negative_prompt` | Oluşturmada kaçınılması gerekenlerin metin açıklaması | STRING | Evet | - |
| `seed` | Oluşturma için rastgele tohum değeri | INT | Evet | - |
| `resolution` | Video için çıktı çözünürlüğü | STRING | Evet | - |
| `duration` | Oluşturulan videonun süresi | INT | Evet | - |
| `ingredients_mode` | Bileşenleri birleştirme modu (varsayılan: "creative") | STRING | Hayır | "creative"<br>"precise" |
| `aspect_ratio` | En boy oranı (genişlik / yükseklik) (varsayılan: 1.778) | FLOAT | Hayır | 0.4 - 2.5 |
| `image_ingredient_1` | Video oluşturmak için bileşen olarak kullanılacak görüntü | IMAGE | Hayır | - |
| `image_ingredient_2` | Video oluşturmak için bileşen olarak kullanılacak görüntü | IMAGE | Hayır | - |
| `image_ingredient_3` | Video oluşturmak için bileşen olarak kullanılacak görüntü | IMAGE | Hayır | - |
| `image_ingredient_4` | Video oluşturmak için bileşen olarak kullanılacak görüntü | IMAGE | Hayır | - |
| `image_ingredient_5` | Video oluşturmak için bileşen olarak kullanılacak görüntü | IMAGE | Hayır | - |

**Not:** En fazla 5 görüntü bileşeni sağlayabilirsiniz, ancak video oluşturmak için en az bir görüntü gereklidir. Düğüm, nihai video kompozisyonunu oluşturmak için sağlanan tüm görüntüleri kullanacaktır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Tüm giriş görüntülerini birleştiren oluşturulmuş video | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaScenesV2_2/tr.md)

---
**Source fingerprint (SHA-256):** `dda8f10a58527c2b9037744f59f30821cdde37ad23427b856ba5e699a05acafd`
