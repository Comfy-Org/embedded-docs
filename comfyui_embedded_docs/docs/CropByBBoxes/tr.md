> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CropByBBoxes/tr.md)

CropByBBoxes düğümü, bir giriş görüntü kümesinden belirli dikdörtgen bölgeleri çıkarır ve yeniden boyutlandırır. Kırpılacak alanı tanımlamak için sağlanan sınırlayıcı kutu koordinatlarını kullanır. Kırpılan bölgeler daha sonra belirtilen bir çıktı boyutuna yeniden boyutlandırılır ve kırpılan alanı esnetme veya orijinal en-boy oranını korumak için doldurma seçenekleri sunar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Kırpılacak giriş görüntü kümesi. |
| `bboxes` | BOUNDINGBOX | Evet | - | Kırpılacak bölgeleri tanımlayan sınırlayıcı kutuların listesi. Bu giriş zorunludur, yani bağlı olmalıdır. |
| `output_width` | INT | Hayır | 64 - 4096 | Her kırpılan alanın yeniden boyutlandırıldığı genişlik (varsayılan: 512). |
| `output_height` | INT | Hayır | 64 - 4096 | Her kırpılan alanın yeniden boyutlandırıldığı yükseklik (varsayılan: 512). |
| `padding` | INT | Hayır | 0 - 1024 | Kırpma işleminden önce sınırlayıcı kutunun her bir kenarına eklenen piksel cinsinden ekstra dolgu (varsayılan: 0). |
| `keep_aspect` | COMBO | Hayır | `"stretch"`<br>`"pad"` | Kırpılan alanın çıktı boyutuna sığması için esnetilip esnetilmeyeceği veya en-boy oranını korumak için siyah piksellerle doldurulup doldurulmayacağı (varsayılan: "stretch"). |

**Not:** Düğüm, her seferinde bir görüntü karesini işler. Tek bir kare için birden fazla sınırlayıcı kutu sağlanırsa, tüm sağlanan kutuların birleşimi (tüm kutuları içeren en küçük dikdörtgen) olan tek bir kırpma bölgesi hesaplar. Hesaplanan bir kırpma bölgesi geçersizse (örneğin, sıfır genişlik veya yükseklik), düğüm görüntünün orta-üst kısmından bir yedek kırpma alanı oluşturur.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Kırpılmış ve yeniden boyutlandırılmış tüm bölgeler, tek bir görüntü kümesinde birleştirilmiştir. |