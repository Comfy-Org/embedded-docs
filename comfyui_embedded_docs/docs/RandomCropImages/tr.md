Rastgele Kırpma Görselleri düğümü, her bir giriş görselinden rastgele bir dikdörtgen bölüm seçer ve bunu belirtilen genişlik ve yüksekliğe kırpar. Bu işlem, genellikle eğitim görsellerinde çeşitlilik oluşturmak için veri artırma amacıyla kullanılır. Kırpma için rastgele konum, bir tohum değeri tarafından belirlenir ve aynı kırpmanın tekrar üretilebilmesini sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Kırpılacak görsel. | IMAGE | Evet | - |
| `width` | Kırpma alanının genişliği (varsayılan: 512). | INT | Hayır | 1 - 8192 |
| `height` | Kırpma alanının yüksekliği (varsayılan: 512). | INT | Hayır | 1 - 8192 |
| `seed` | Kırpmanın rastgele konumunu kontrol etmek için kullanılan sayı (varsayılan: 0). | INT | Hayır | 0 - 18446744073709551615 |

**Not:** `width` ve `height` parametreleri, giriş görselinin boyutlarından küçük veya eşit olmalıdır. Belirtilen bir boyut görselden daha büyükse, kırpma görselin sınırıyla sınırlandırılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `images` | Rastgele kırpma uygulandıktan sonra elde edilen görsel. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomCropImages/tr.md)

---
**Source fingerprint (SHA-256):** `bc4aca8cc63bde28fee906a92463b73436ba48ba69d7c1ff13881ac900e252a8`
