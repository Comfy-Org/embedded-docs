# Video Listesini Karıştır

Bu düğüm, bir video listesi alır ve bunları rastgele yeniden sıralar. Karıştırmanın tekrarlanabilir olması için rastgele bir tohum kullanır; bu nedenle aynı tohum her zaman aynı çıktı sırasını üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|---------|--------|
| `videos` | Karıştırılacak video listesi. | VIDEO | Evet | Video girdi listesi |
| `seed` | Karıştırma için rastgele tohum (varsayılan: 0). | INT | Hayır | 0 ile 18446744073709551615 arası |
Not: tohum değeri kullanılmadan önce 4294967295 (2^32 - 1) modülüne indirgenir. Sonuç olarak, 4294967295'in katı kadar farklı olan tohumlar aynı çıktı sırasını üretir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `videos` | Rastgele sırada karıştırılmış video listesi. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleVideoDataset/tr.md)

---
**Source fingerprint (SHA-256):** `0bd32b664197d3bbd4c53f65e29ef38fba836579f07f05cb7fb85f3b8a1024ac`
