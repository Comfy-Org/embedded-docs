> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScale/tr.md)

ImageScale düğümü, görüntüleri belirli boyutlara yeniden boyutlandırmak için tasarlanmış olup, bir dizi yüksek çözünürlüğe yükseltme yöntemi seçeneği ve yeniden boyutlandırılmış görüntüyü kırpma yeteneği sunar. Görüntü yükseltme ve kırpmanın karmaşıklığını soyutlayarak, kullanıcı tanımlı parametrelere göre görüntü boyutlarını değiştirmek için basit bir arayüz sağlar.

## Girdiler

| Parametre       | Veri Tipi    | Açıklama                                                                           |
|-----------------|-------------|---------------------------------------------------------------------------------------|
| `görüntü`         | `IMAGE`     | Yükseltilecek girdi görüntüsü. Bu parametre, düğümün işleyişinde merkezi bir role sahiptir ve yeniden boyutlandırma dönüşümlerinin uygulandığı birincil veri olarak hizmet eder. Çıktı görüntüsünün kalitesi ve boyutları, orijinal görüntünün özelliklerinden doğrudan etkilenir. |
| `büyütme_yöntemi`| COMBO[STRING] | Görüntüyü yükseltmek için kullanılan yöntemi belirtir. Yöntem seçimi, yükseltilmiş görüntünün kalitesini ve özelliklerini etkileyerek, yeniden boyutlandırılmış çıktıdaki görsel doğruluğu ve olası yapay bozulmaları etkiler. |
| `genişlik`         | `INT`       | Yükseltilmiş görüntü için hedef genişlik. Bu parametre, çıktı görüntüsünün boyutlarını doğrudan etkileyerek, yeniden boyutlandırma işleminin yatay ölçeğini belirler. |
| `yükseklik`        | `INT`       | Yükseltilmiş görüntü için hedef yükseklik. Bu parametre, çıktı görüntüsünün boyutlarını doğrudan etkileyerek, yeniden boyutlandırma işleminin dikey ölçeğini belirler. |
| `kırp`          | COMBO[STRING] | Yükseltilmiş görüntünün kırpılıp kırpılmayacağını ve nasıl kırpılacağını belirler; kırpmanın devre dışı bırakılması veya merkezden kırpma seçenekleri sunar. Bu, belirtilen boyutlara sığdırmak için kenarları potansiyel olarak kaldırarak görüntünün nihai kompozisyonunu etkiler. |

## Çıktılar

| Parametre | Veri Tipi | Açıklama |
|-----------|-------------|-------------|
| `görüntü`   | `IMAGE`     | Yükseltilmiş (ve isteğe bağlı olarak kırpılmış) görüntü, daha fazla işleme veya görselleştirmeye hazır. |