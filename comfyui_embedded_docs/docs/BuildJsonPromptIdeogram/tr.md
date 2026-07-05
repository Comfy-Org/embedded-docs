# JSON İstem Oluştur (Ideogram)

Bu düğüm, Ideogram 4 görüntü oluşturma modeli için özel olarak biçimlendirilmiş yapılandırılmış bir JSON istemi oluşturur. Metin talimatlarınızı, stil tercihlerinizi ve renk paletinizi modelin beklediği gerekli JSON yapısında düzenler.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `öğe` | "Sınırlayıcı Kutular Oluştur" düğümünden gelen istem öğeleri. | ARRAY | Evet | - |
| `üst düzey açıklama` | Görüntünün bir veya iki cümlelik isteğe bağlı açıklaması. Güçlü bir şekilde önerilir. (varsayılan: boş) | STRING | Hayır | - |
| `arka plan` | Görüntü arka planı veya ortamının zorunlu açıklaması. (varsayılan: boş) | STRING | Evet | - |
| `stil` | Oluşturulan görüntü için görsel stil kategorisi. (varsayılan: "none") | COMBO | Evet | `"none"`<br>`"photo"`<br>`"art_style"` |
| `photo` | Fotoğrafik çıktılar için kamera veya lens detayları (örn. 35mm, f/1.4, bokeh). Yalnızca stil "photo" olarak ayarlandığında kullanılabilir. (varsayılan: boş) | STRING | Hayır | - |
| `art_style` | Sanat stili açıklaması (örn. düz vektör illüstrasyonu, kalın ana hatlar). Yalnızca stil "art_style" olarak ayarlandığında kullanılabilir. (varsayılan: boş) | STRING | Hayır | - |
| `estetik` | Zorunlu estetik anahtar kelimeler (örn. melankolik, sinematik, doygunluğu azaltılmış). (varsayılan: boş) | STRING | Evet | - |
| `aydınlatma` | Zorunlu aydınlatma açıklaması (örn. altın saat, kenar ışığı, dramatik gölgeler). (varsayılan: boş) | STRING | Evet | - |
| `ortam` | Zorunlu ortam türü (örn. fotoğraf, illüstrasyon, 3d_render, resim, grafik_tasarım). Stil = photo olduğunda, photograph olarak ayarlayın. (varsayılan: boş) | STRING | Evet | - |
| `renk paleti` | Görüntünün baskın renklerini yönlendiren onaltılık renk kodları. En fazla 16 giriş. | COLORS | Hayır | - |

**Not:** `style` parametresi "photo" olarak ayarlandığında, `photo` girişi kullanılabilir hale gelir ve `medium` parametresini "photograph" olarak ayarlamanız gerekir. `style` "art_style" olarak ayarlandığında ise `art_style` girişi kullanılabilir hale gelir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `istem` | Üst düzey açıklama, stil açıklaması (varsa) ve arka plan ile öğeleri içeren kompozisyonel ayrıştırmayı barındıran yapılandırılmış bir JSON sözlüğü. | DICT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BuildJsonPromptIdeogram/tr.md)

---
**Source fingerprint (SHA-256):** `56a045e0c7c19531e6443696c0bdf3946df066d03eea7d2d217b7d92f052592f`
