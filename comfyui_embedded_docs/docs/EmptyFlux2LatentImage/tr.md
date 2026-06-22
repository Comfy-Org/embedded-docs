# Boş Flux 2 Latent

EmptyFlux2LatentImage düğümü, boş bir latent temsil oluşturur. Sıfırlarla doldurulmuş bir tensör üretir; bu tensör, Flux modelinin gürültü giderme işlemi için bir başlangıç noktası görevi görür. Latent boyutları, giriş genişliği ve yüksekliğine göre belirlenir ve 16 kat küçültülür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `genişlik` | Oluşturulacak nihai görüntünün genişliği. Latent genişliği, bu değerin 16'ya bölünmesiyle elde edilir. Varsayılan değer 1024'tür. | INT | Evet | 16 ila 8192 |
| `yükseklik` | Oluşturulacak nihai görüntünün yüksekliği. Latent yüksekliği, bu değerin 16'ya bölünmesiyle elde edilir. Varsayılan değer 1024'tür. | INT | Evet | 16 ila 8192 |
| `toplu_boyut` | Tek bir grupta oluşturulacak latent örneklerinin sayısı. Varsayılan değer 1'dir. | INT | Hayır | 1 ila 4096 |

**Not:** `width` ve `height` girişleri 16'ya tam bölünebilir olmalıdır, çünkü düğüm latent boyutları oluşturmak için bu değerleri dahili olarak 16'ya böler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Sıfırlarla doldurulmuş bir latent tensör. Şekli `[batch_size, 128, height // 16, width // 16]` şeklindedir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyFlux2LatentImage/tr.md)

---
**Source fingerprint (SHA-256):** `e3616ad0e283a318bbe441d84f687883e59ab311e72c5e5edd16ddabde10988e`
