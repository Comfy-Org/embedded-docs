# p-h3-image Conditioning

Bu düğüm, p-h3-image ile tek bir durağan görüntü için bir istemi koşullandırmaya ve boş bir latent'e dönüştürür. Görüntü olmadan metinden görüntüye çalışır; görüntüler bağlandığında `image_1` düzenlenen görüntüdür ve diğer yuvalar referans olarak görev yapar; istem bunlara `<Picture 1>`, `<Picture 2>` ve benzeri şekilde atıfta bulunur. Örnekleyicinin, her iki kaydırma değeri de 1.0 olan MiniMax H3 sigma shift düğümüyle yamalanmış bir modele ihtiyacı vardır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | İstemi (varsa referans görüntüler dahil) belirteçleştirmek ve koşullandırmayı kodlamak için kullanılan p-h3-image CLIP modeli. | CLIP | Evet | - |
| `prompt` | Neyin oluşturulacağı veya `image_1` dosyasının nasıl düzenleneceği. Görüntüler bağlıyken kısa bir talimatın başına `Edit <Picture 1>. ` eklenir. Zaten `Edit <Picture` ile başlayan bir talimat veya bir istem yükseltici tarafından üretilen bir düzenleme talimatı, tam olarak yazıldığı gibi kullanılır. | STRING | Evet | - |
| `width` | Piksel cinsinden çıktı genişliği; 32'nin katına yuvarlanır. 0, ölçekleme sonrasında `image_1` genişliğini kullanır veya görüntü bağlı değilken 2912 kullanır (varsayılan: 0). | INT | Evet | 0 ile MAX_RESOLUTION arası |
| `height` | Piksel cinsinden çıktı yüksekliği; 32'nin katına yuvarlanır. 0, ölçekleme sonrasında `image_1` yüksekliğini kullanır veya görüntü bağlı değilken 2912 kullanır (varsayılan: 0). | INT | Evet | 0 ile MAX_RESOLUTION arası |
| `vae` | p-h3-image VAE'si. Bir görüntü yuvası bağlandığı anda gereklidir, çünkü referans latentler bununla kodlanır. | VAE | Hayır | - |
| `images` | `image_1` ile `image_9` arasındaki en fazla 9 görüntüden oluşan büyütülebilir grup. `image_1` düzenlenen görüntüdür, kalan yuvalar referanstır. | AUTOGROW | Hayır | 0 ile 9 görsel arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | p-h3-image örnekleyicisi için koşullandırma. Görüntüler bağlıyken paketlenmiş referans latentleri de taşır. | CONDITIONING |
| `latent` | Tek bir durağan kare için boş latent; modelin beklediği iki ses latentini de içerir. | LATENT |

**Not:** Görüntüler `vae` girdisini gerektirir. Düğümü görüntü bağlıyken ve VAE olmadan çalıştırmak hata verir.

**Not:** Koşullandırma tek bir kareyi kapsar. Video veya ses için bunun yerine MiniMax H3 video düğümlerini kullanın.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PH3ImageConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `f1f5e5b2d3ff9bc2f3b81f3d0dd722e725c7930c6f95bf44ad83bc64357d2fb7`
