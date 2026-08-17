# Boş Flux 2 Latent

EmptyFlux2LatentImage düğümü boş bir latent temsili oluşturur. Sıfırlarla dolu bir tensör üretir; bu tensör, Flux modelinin gürültü giderme süreci için bir başlangıç noktası görevi görür. Latent boyutları, girdi genişliği ve yüksekliğine göre belirlenir ve 16 kat küçültülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `width` | Oluşturulacak son görüntünün genişliği. Latent genişliği bu değerin 16'ya bölünmesiyle elde edilir. Varsayılan değer 1024'tür. | INT | Evet | 16 ila 16384 |
| `height` | Oluşturulacak son görüntünün yüksekliği. Latent yüksekliği bu değerin 16'ya bölünmesiyle elde edilir. Varsayılan değer 1024'tür. | INT | Evet | 16 ila 16384 |
| `batch_size` | Tek bir batch'te oluşturulacak latent örnek sayısı. Varsayılan değer 1'dir. | INT | Hayır | 1 ila 4096 |

**Not:** `width` ve `height` girdileri 16'ya tam bölünebilmelidir; düğüm, latent boyutlarını oluşturmak için bu değerleri dahili olarak 16'ya böler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `samples` | Sıfırlarla dolu bir latent tensör. Şekil: `[batch_size, 128, height // 16, width // 16]`. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyFlux2LatentImage/tr.md)

---
**Source fingerprint (SHA-256):** `f8356568f0ab521a3f246d1f672492e74f9a2f449694961b913bd14a5f0f3878`
