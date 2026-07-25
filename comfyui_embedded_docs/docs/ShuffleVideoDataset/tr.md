# Video Listesini Karıştır

Bu düğüm, bir video listesi alır ve bunları rastgele yeniden sıralar. Sıralamanın tekrarlanabilir olmasını sağlamak için rastgele bir tohum kullanır, böylece aynı tohum her zaman aynı çıktı sırasını üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|---------|--------|
| `videos` | Karıştırılacak video listesi. | VIDEO | Evet | Video girdi listesi |
| `seed` | Karıştırma için rastgele tohum (varsayılan: 0). | INT | Hayır | 0 ile 18446744073709551615 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `videos` | Rastgele sırada karıştırılmış video listesi. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleVideoDataset/tr.md)

---
**Source fingerprint (SHA-256):** `0bd32b664197d3bbd4c53f65e29ef38fba836579f07f05cb7fb85f3b8a1024ac`
