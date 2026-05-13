> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskToImage/tr.md)

`MaskToImage` düğümü, bir maskeyi görüntü formatına dönüştürmek için tasarlanmıştır. Bu dönüşüm, maskelerin görselleştirilmesine ve görüntü olarak daha ileri düzeyde işlenmesine olanak tanıyarak, maske tabanlı işlemler ile görüntü tabanlı uygulamalar arasında bir köprü kurulmasını sağlar.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `mask`    | `MASK`      | Maske girişi, dönüşüm süreci için gereklidir ve görüntü formatına dönüştürülecek kaynak veri olarak işlev görür. Bu giriş, elde edilecek görüntünün şeklini ve içeriğini belirler. |

## Çıkışlar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | Çıkış, giriş maskesinin bir görüntü temsilidir; görsel inceleme ve daha ileri düzeyde görüntü tabanlı işlemler yapılmasına olanak tanır. |