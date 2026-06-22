# Görüntü Veri Setini Karıştır

Shuffle Dataset düğümü, bir görüntü listesini alır ve sıralarını rastgele değiştirir. Rastgeleliği kontrol etmek için bir tohum değeri kullanır ve aynı karıştırma sırasının tekrar üretilebilmesini sağlar. Bu, işleme başlamadan önce bir veri kümesindeki görüntülerin sırasını rastgele hale getirmek için kullanışlıdır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `images` | Karıştırılacak görüntü listesi. | IMAGE | Evet | - |
| `seed` | Rastgele tohum. 0 değeri her seferinde farklı bir karıştırma üretecektir. (varsayılan: 0) | INT | Hayır | 0 ile 18446744073709551615 arası |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `images` | Aynı görüntü listesi, ancak yeni, rastgele karıştırılmış bir sırada. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleDataset/tr.md)

---
**Source fingerprint (SHA-256):** `0b8442029995bdcedf1df0cb8d27d87aa529fb1021d911ed3016a6a7e788b246`
