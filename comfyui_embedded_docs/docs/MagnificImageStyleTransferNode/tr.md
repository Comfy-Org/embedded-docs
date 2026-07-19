# Magnific Görüntü Stil Transferi

Bu belge, yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme öneriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageStyleTransferNode/en.md)

Bu düğüm, referans görselinizin görsel stilini giriş görselinize uygular. Görselleri işlemek için harici bir yapay zeka hizmeti kullanarak, stil aktarımının gücünü ve orijinal görselin yapısının korunmasını kontrol etmenize olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Stil aktarımının uygulanacağı görsel. | IMAGE | Evet | - |
| `reference_image` | Stilin çıkarılacağı referans görsel. | IMAGE | Evet | - |
| `prompt` | Stil aktarımına yön vermek için isteğe bağlı bir metin istemi. | STRING | Hayır | - |
| `style_strength` | Stil gücünün yüzdesi (varsayılan: 100). | INT | Hayır | 0 ile 100 |
| `structure_strength` | Orijinal görselin yapısını korur (varsayılan: 50). | INT | Hayır | 0 ile 100 |
| `flavor` | Stil aktarımı çeşnisi. | COMBO | Hayır | "faithful"<br>"gen_z"<br>"psychedelia"<br>"detaily"<br>"clear"<br>"donotstyle"<br>"donotstyle_sharp" |
| `engine` | İşleme motoru seçimi. | COMBO | Hayır | "balanced"<br>"definio"<br>"illusio"<br>"3d_cartoon"<br>"colorful_anime"<br>"caricature"<br>"real"<br>"super_real"<br>"softy" |
| `portrait_mode` | Yüz iyileştirmeleri için portre modunu etkinleştirin. | COMBO | Hayır | "disabled"<br>"enabled" |
| `portrait_style` | Portre görsellerine uygulanan görsel stil. Bu girdi yalnızca `portrait_mode` "enabled" olarak ayarlandığında kullanılabilir. | COMBO | Hayır | "standard"<br>"pop"<br>"super_pop" |
| `portrait_beautifier` | Portrelerde yüz güzelleştirme yoğunluğu. Bu girdi yalnızca `portrait_mode` "enabled" olarak ayarlandığında kullanılabilir. | COMBO | Hayır | "none"<br>"beautify_face"<br>"beautify_face_max" |
| `fixed_generation` | Devre dışı bırakıldığında, her üretimin bir miktar rastgelelik getirmesi beklenir ve bu da daha çeşitli sonuçlara yol açar (varsayılan: True). | BOOLEAN | Hayır | - |

**Kısıtlamalar:**

* Tam olarak bir adet `image` ve bir adet `reference_image` gereklidir.
* Her iki görselin de en boy oranı 1:3 ile 3:1 arasında olmalıdır.
* Her iki görselin de minimum yükseklik ve genişliği 160 piksel olmalıdır.
* `portrait_style` ve `portrait_beautifier` parametreleri yalnızca `portrait_mode` "enabled" olarak ayarlandığında etkin ve zorunludur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Stil aktarımı uygulandıktan sonra elde edilen sonuç görseli. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageStyleTransferNode/tr.md)

---
**Source fingerprint (SHA-256):** `4ae400183618953c369d089d39b878f0a24592967c29d779c577fb8b7339dea8`
