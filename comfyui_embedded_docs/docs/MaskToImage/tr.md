> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskToImage/tr.md)

`MaskToImage` düğümü, bir maskeyi görüntü formatına dönüştürmek için tasarlanmıştır. Bu dönüşüm, maskelerin görüntü olarak görselleştirilmesine ve daha fazla işlenmesine olanak tanıyarak, maske tabanlı işlemler ile görüntü tabanlı uygulamalar arasında bir köprü oluşturur.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `maske`    | `MASK`      | Maske girdisi, dönüşüm işlemi için temel teşkil eder ve görüntü formatına dönüştürülecek kaynak veri olarak hizmet eder. Bu girdi, ortaya çıkan görüntünün şeklini ve içeriğini belirler. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | Çıktı, girdi maskesinin bir görüntü temsilidir ve görsel incelemeye ve daha fazla görüntü tabanlı manipülasyona olanak tanır. |