> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleDataset/tr.md)

**Shuffle Dataset** düğümü, bir görüntü listesi alır ve bunların sırasını rastgele değiştirir. Rastgeleliği kontrol etmek için bir `seed` değeri kullanır, böylece aynı karıştırma sırasının tekrar üretilebilmesini sağlar. Bu, bir veri kümesindeki görüntülerin işlenmeden önce sırasını rastgele hale getirmek için kullanışlıdır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Evet | - | Karıştırılacak görüntü listesi. |
| `seed` | INT | Hayır | 0 - 18446744073709551615 | Rastgele tohum değeri. 0 değeri, her seferinde farklı bir karıştırma üretecektir. (varsayılan: 0) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `images` | IMAGE | Aynı görüntü listesi, ancak yeni, rastgele karıştırılmış bir sırada. |
