> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrowMask/tr.md)

`GrowMask` düğümü, belirli bir maskenin boyutunu genişletmek veya daraltmak ve isteğe bağlı olarak köşelere sivrilen bir efekt uygulamak için tasarlanmıştır. Bu işlevsellik, görüntü işleme görevlerinde maske sınırlarını dinamik olarak ayarlamak için çok önemlidir ve ilgi alanı üzerinde daha esnek ve hassas bir kontrol sağlar.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `maske`    | MASK        | Değiştirilecek giriş maskesi. Bu parametre, düğümün işleyişinin merkezinde yer alır ve maskenin genişletildiği veya daraltıldığı temel görevi görür. |
| `genişlet`  | INT         | Maske değişikliğinin büyüklüğünü ve yönünü belirler. Pozitif değerler maskenin genişlemesine neden olurken, negatif değerler daralmaya yol açar. Bu parametre, maskenin nihai boyutunu doğrudan etkiler. |
| `sivri_köşeler` | BOOLEAN    | `True` olarak ayarlandığında, değişiklik sırasında maskenin köşelerine sivrilen bir efekt uygulayan bir boolean bayrağıdır. Bu seçenek, daha yumuşak geçişler ve görsel olarak hoş sonuçlar sağlar. |

## Çıkışlar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `maske`    | MASK        | Belirtilen genişletme/daraltma ve isteğe bağlı sivrilen köşe efekti uygulandıktan sonraki değiştirilmiş maske. |