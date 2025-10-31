> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrowMask/tr.md)

`GrowMask` düğümü, bir maskenin boyutunu genişletmek veya daraltmak için tasarlanmıştır ve isteğe bağlı olarak köşelere kademeli bir efekt uygulayabilir. Bu işlevsellik, görüntü işleme görevlerinde maske sınırlarını dinamik olarak ayarlamak için çok önemlidir ve ilgilenilen alan üzerinde daha esnek ve hassas kontrol sağlar.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `mask`    | MASK        | Değiştirilecek giriş maskesi. Bu parametre, düğümün işlemi için merkezi bir öneme sahiptir ve maskenin genişletilmesi veya daraltılması için temel oluşturur. |
| `expand`  | INT         | Maske değişikliğinin büyüklüğünü ve yönünü belirler. Pozitif değerler maskenin genişlemesine, negatif değerler ise daralmasına neden olur. Bu parametre, maskenin nihai boyutunu doğrudan etkiler. |
| `tapered_corners` | BOOLEAN    | True olarak ayarlandığında, maske değiştirilirken köşelere kademeli bir efekt uygulayan bir boolean bayrağı. Bu seçenek, daha yumuşak geçişler ve görsel olarak daha hoş sonuçlar sağlar. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `mask`    | MASK        | Belirtilen genişletme/daraltma ve isteğe bağlı kademeli köşe efektinin uygulanmasından sonra değiştirilmiş maske. |