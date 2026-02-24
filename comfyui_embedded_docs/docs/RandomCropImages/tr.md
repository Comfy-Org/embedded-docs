> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomCropImages/tr.md)

Random Crop Images düğümü, her bir girdi görüntüsünden rastgele bir dikdörtgen bölüm seçer ve bunu belirtilen genişlik ve yüksekliğe kırpar. Bu, genellikle eğitim görüntülerinin çeşitlemelerini oluşturmak için veri artırma amacıyla kullanılır. Kırpma için rastgele konum, bir `seed` değeri tarafından belirlenir, böylece aynı kırpma işlemi tekrarlanabilir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Kırpılacak görüntü. |
| `width` | INT | Hayır | 1 - 8192 | Kırpma alanının genişliği (varsayılan: 512). |
| `height` | INT | Hayır | 1 - 8192 | Kırpma alanının yüksekliği (varsayılan: 512). |
| `seed` | INT | Hayır | 0 - 18446744073709551615 | Kırpmanın rastgele konumunu kontrol etmek için kullanılan bir sayı (varsayılan: 0). |

**Not:** `width` ve `height` parametreleri, girdi görüntüsünün boyutlarından küçük veya ona eşit olmalıdır. Belirtilen bir boyut görüntünün boyutundan büyükse, kırpma işlemi görüntünün sınırlarıyla sınırlandırılacaktır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Rastgele kırpma uygulandıktan sonra elde edilen görüntü. |
