# MiniMax H3 Max Recast

Recast, bir videodaki kişileri referans fotoğraflardaki kişilerle değiştirir; kaynak klibin hareketini, kamerasını, kesmelerini ve sesini korur. Video yüklenir, Hailuo 03 Max işi yoklanır ve recast videosu seçtiğiniz çözünürlükte geri döner.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video oluşturmada kullanılacak model. | DYNAMIC_COMBO | Evet | "MiniMax H3 Max" |

### MiniMax H3 Max Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `video` | Kaynak video, 5 ila 30 saniye uzunluğunda; her çekim 15 saniye veya daha kısa olmalıdır. En-boy oranı 0.4 ile 2.5 arasında olmalıdır. | VIDEO | Evet | 5 ila 30 saniye |
| `reference_images` | Büyütülebilir yuva: 1 ila 4 fotoğraf bağlayın (`image_1`...`image_4`), her yeni kişi için bir tane, en az 256x256 piksel. Varsayılan olarak videodaki ana kişileri soldan sağa değiştirirler. | IMAGE | Evet | 1 ila 4 görsel |
| `prompt` | İsteğe bağlı. Kimin kime dönüşeceği veya başka nelerin korunacağı ya da değiştirileceği. Fotoğraflara `@Image1`..`@Image4` olarak başvurun, örneğin "adam @Image2 olur". | STRING | Evet | 0 ila 2000 karakter |
| `resolution` | Çıktı videosunun çözünürlüğü (varsayılan: "768P"). | COMBO | Evet | "768P"<br>"1080P" |
| `enhance_realism` | Daha doğal cilt dokuları ve yeni kişilerin sahneye daha iyi karışması (varsayılan: false). | BOOLEAN | Hayır | true<br>false |
| `seed` | Rastgele tohum. Aynı tohumla yapılan aynı istek benzer, ancak aynı olduğu garanti edilmeyen sonuçlar verir (varsayılan: 42). | INT | Evet | 0 ila 4294967295 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Yeni kişilerin yerleştirildiği recast videosu. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxRecastNode/tr.md)

---
**Source fingerprint (SHA-256):** `a9e6f9edf12653f9f361992a097d1d57e7ba14b3e7dd20008b0e022cabc14c1b`
