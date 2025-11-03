> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JoinImageWithAlpha/tr.md)

Bu düğüm, kompozitleme işlemleri için tasarlanmıştır ve özellikle bir görüntüyü karşılık gelen alfa maskesiyle birleştirerek tek bir çıktı görüntüsü oluşturur. Görsel içeriği şeffaflık bilgisiyle etkili bir şekilde birleştirerek, belirli alanların şeffaf veya yarı şeffaf olduğu görüntülerin oluşturulmasını sağlar.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `görüntü`   | `IMAGE`     | Alfa maskesiyle birleştirilecek ana görsel içerik. Şeffaflık bilgisi olmayan görüntüyü temsil eder. |
| `alfa`   | `MASK`      | İlgili görüntünün şeffaflığını tanımlayan alfa maskesi. Görüntünün hangi kısımlarının şeffaf veya yarı şeffaf olması gerektiğini belirlemek için kullanılır. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `görüntü`   | `IMAGE`     | Çıktı, girdi görüntüsünü alfa maskesiyle birleştiren ve görsel içeriğe şeffaflık bilgisi katılmış tek bir görüntüdür. |