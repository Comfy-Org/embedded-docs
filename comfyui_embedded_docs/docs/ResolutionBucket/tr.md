> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionBucket/tr.md)

Bu düğüm, bir liste gizli görüntüyü ve bunlara karşılık gelen koşullandırma verilerini çözünürlüklerine göre düzenler. Aynı yükseklik ve genişliğe sahip öğeleri gruplandırarak, her bir benzersiz çözünürlük için ayrı toplu işlemler oluşturur. Bu işlem, modellerin aynı boyuttaki birden fazla öğeyi birlikte işlemesine olanak tanıdığı için, verimli eğitim için veri hazırlamada kullanışlıdır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `latents` | LATENT | Evet | Yok | Çözünürlüğe göre gruplanacak gizli sözlüklerin listesi. |
| `conditioning` | CONDITIONING | Evet | Yok | Koşullandırma listelerinin listesi (gizli görüntü listesi uzunluğuyla eşleşmeli). |

**Not:** `latents` listesindeki öğe sayısı, `conditioning` listesindeki öğe sayısıyla tam olarak eşleşmelidir. Her bir gizli sözlük bir grup örnek içerebilir ve karşılık gelen koşullandırma listesi, o grup için eşleşen sayıda koşullandırma öğesi içermelidir.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `latents` | LATENT | Toplu işlenmiş gizli sözlüklerin listesi, her çözünürlük grubu için bir tane. |
| `conditioning` | CONDITIONING | Koşullandırma listelerinin listesi, her çözünürlük grubu için bir tane. |
