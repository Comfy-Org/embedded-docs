# Boş Flux 2 Latent

Empty Flux 2 Latent düğümü, sıfırlarla doldurulmuş boş bir latent temsili oluşturur. Flux modelinin gürültü giderme süreci için başlangıç noktası olarak kullanılır. Latent boyutları, girdi genişliği ve yüksekliğinden alınır ve her biri 16'ya bölünür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `genişlik` | Oluşturulacak nihai görüntünün genişliği. Latent genişliği bu değerin 16'ya bölünmüş hali olacaktır. Varsayılan değer 1024'tür. | INT | Evet | 16 ile 16384 |
| `yükseklik` | Oluşturulacak nihai görüntünün yüksekliği. Latent yüksekliği bu değerin 16'ya bölünmüş hali olacaktır. Varsayılan değer 1024'tür. | INT | Evet | 16 ile 16384 |
| `toplu_boyut` | Tek bir partide oluşturulacak latent örnek sayısı. Varsayılan değer 1'dir. | INT | Hayır | 1 ile 4096 |

**Not:** `width` ve `height` girdileri 16 adımlı kullanır, bu nedenle 16'ya bölünebilir olmalıdır. Bunun nedeni, düğümün latent boyutları oluşturmak için bu değerleri bu faktöre bölmesidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Sıfırlarla doldurulmuş bir latent tensör. Şekli `[batch_size, 128, height // 16, width // 16]` şeklindedir. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyFlux2LatentImage/tr.md)

---
**Source fingerprint (SHA-256):** `f8356568f0ab521a3f246d1f672492e74f9a2f449694961b913bd14a5f0f3878`
