Bu düğüm, birleştirme işlemleri için tasarlanmıştır; özellikle bir görüntüyü, karşılık gelen alfa maskesiyle birleştirerek tek bir çıktı görüntüsü üretir. Görsel içeriği şeffaflık bilgisiyle etkili bir şekilde birleştirerek, belirli alanların şeffaf veya yarı şeffaf olduğu görüntülerin oluşturulmasını sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | Alfa maskesiyle birleştirilecek ana görsel içerik. Şeffaflık bilgisi olmayan görüntüyü temsil eder. | `IMAGE` |
| `alfa` | İlgili görüntünün şeffaflığını tanımlayan alfa maskesi. Görüntünün hangi bölümlerinin şeffaf veya yarı şeffaf olması gerektiğini belirlemek için kullanılır. | `MASK` |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | Çıktı, giriş görüntüsünü alfa maskesiyle birleştiren ve şeffaflık bilgisini görsel içeriğe dahil eden tek bir görüntüdür. | `IMAGE` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JoinImageWithAlpha/tr.md)
