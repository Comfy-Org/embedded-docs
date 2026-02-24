> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageDeduplication/tr.md)

Bu düğüm, bir grup görselden kopya veya çok benzer görselleri kaldırır. Her görsel için algısal bir hash (görsel içeriğine dayalı basit bir sayısal parmak izi) oluşturarak ve bunları karşılaştırarak çalışır. Hash değerleri belirlenen bir eşik değerinden daha benzer olan görseller kopya olarak kabul edilir ve filtrelenir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Evet | - | Kopyaları temizlenecek görsel grubu. |
| `similarity_threshold` | FLOAT | Hayır | 0.0 - 1.0 | Benzerlik eşiği (0-1). Daha yüksek değer daha benzer anlamına gelir. Bu eşiğin üzerindeki görseller kopya olarak kabul edilir. (varsayılan: 0.95) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `images` | IMAGE | Kopyaları kaldırılmış, filtrelenmiş görsel listesi. |
