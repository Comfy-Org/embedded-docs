# MiniMax H3 Max Reframe Video

Bu düğüm, bir videoyu yeni bir tuvale yerleştirip çevresindeki alanları oluşturarak yeni bir en-boy oranına uyarlar. Kaynak videonun zamanlaması ve sesi korunur. Özneyi çerçeve dışında bırakmadan yatay bir klibi dikey hâle getirmek veya tam tersini yapmak için kullanın.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video oluşturma için kullanılacak model. | DYNAMIC_COMBO | Evet | "MiniMax H3 Max" |

### MiniMax H3 Max Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `video` | Yeniden çerçevelenecek kaynak video; 0.5 ile 300 saniye arasında. | VIDEO | Evet | 0.5 - 300 saniye |
| `aspect_ratio` | Çıktı tuvalinin en-boy oranı (varsayılan: "9:16"). | COMBO | Evet | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4"<br>"21:9"<br>"9:21" |
| `resolution` | Çıktı videosunun çözünürlüğü (varsayılan: "768P"). | COMBO | Evet | "480P"<br>"768P"<br>"1080P" |
| `prompt` | Oluşturulan çevre alanları için isteğe bağlı yönlendirme. | STRING | Evet | 0 - 50000 karakter |
| `seed` | Rastgele tohum. Aynı tohumla yapılan aynı istek benzer ancak birebir aynı olması garanti edilmeyen sonuçlar verir (varsayılan: 42). | INT | Evet | 0 - 4294967295 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Seçilen en-boy oranında yeniden çerçevelenmiş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxReframeVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `83d780c2fe8c42475d4ad25ad5b318f2a4c135edef9c0ca1ff0d1fd07d90c1c6`
