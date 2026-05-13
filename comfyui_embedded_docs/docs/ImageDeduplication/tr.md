> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageDeduplication/tr.md)

Bu düğüm, bir gruptaki yinelenen veya çok benzer görselleri kaldırır. Her görsel için algısal bir karma (görsel içeriğine dayalı basit bir sayısal parmak izi) oluşturarak ve bunları karşılaştırarak çalışır. Karmaları belirlenen bir eşik değerinden daha benzer olan görseller yinelenen olarak kabul edilir ve filtrelenir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `görseller` | IMAGE | Evet | - | Yinelenenleri kaldırmak için işlenecek görsel grubu. |
| `benzerlik_eşiği` | FLOAT | Hayır | 0.0 - 1.0 | Benzerlik eşiği (0-1). Daha yüksek değer daha benzer anlamına gelir. Bu eşiğin üzerindeki görseller yinelenen olarak kabul edilir. (varsayılan: 0.95) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `görseller` | IMAGE | Yinelenenlerin kaldırıldığı filtrelenmiş görsel listesi. |

---
**Source fingerprint (SHA-256):** `8904f9dee4ca911821e76d2317983cbc230c4821a9ee7876180bd7dbe42b9a54`
