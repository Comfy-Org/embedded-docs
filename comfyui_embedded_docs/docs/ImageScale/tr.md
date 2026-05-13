> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScale/tr.md)

ImageScale düğümü, görüntüleri belirli boyutlara yeniden boyutlandırmak için tasarlanmış olup, çeşitli büyütme yöntemleri ve yeniden boyutlandırılan görüntüyü kırpma olanağı sunar. Görüntü büyütme ve kırpma işlemlerinin karmaşıklığını soyutlayarak, kullanıcı tanımlı parametrelere göre görüntü boyutlarını değiştirmek için basit bir arayüz sağlar.

## Girişler

| Parametre        | Veri Türü      | Açıklama                                                                                                                                                                                                 |
|------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `görüntü`          | `IMAGE`        | Büyütülecek giriş görüntüsü. Bu parametre, düğümün işleyişinin merkezinde yer alır ve yeniden boyutlandırma dönüşümlerinin uygulandığı birincil veri olarak hizmet eder. Çıktı görüntüsünün kalitesi ve boyutları, orijinal görüntünün özelliklerinden doğrudan etkilenir. |
| `büyütme_yöntemi` | COMBO[STRING]  | Görüntüyü büyütmek için kullanılan yöntemi belirtir. Yöntem seçimi, büyütülmüş görüntünün kalitesini ve özelliklerini etkileyerek, yeniden boyutlandırılmış çıktıdaki görsel doğruluğu ve olası yapaylıkları etkileyebilir. |
| `genişlik`          | `INT`          | Büyütülmüş görüntü için hedef genişlik. Bu parametre, çıktı görüntüsünün boyutlarını doğrudan etkileyerek yeniden boyutlandırma işleminin yatay ölçeğini belirler.                                          |
| `yükseklik`         | `INT`          | Büyütülmüş görüntü için hedef yükseklik. Bu parametre, çıktı görüntüsünün boyutlarını doğrudan etkileyerek yeniden boyutlandırma işleminin dikey ölçeğini belirler.                                          |
| `kırp`           | COMBO[STRING]  | Büyütülmüş görüntünün kırpılıp kırpılmayacağını ve nasıl kırpılacağını belirler; devre dışı kırpma veya merkezden kırpma seçenekleri sunar. Bu, belirtilen boyutlara uyması için potansiyel olarak kenarları kaldırarak görüntünün nihai kompozisyonunu etkiler. |

## Çıktılar

| Parametre | Veri Türü | Açıklama                                                                 |
|-----------|-----------|--------------------------------------------------------------------------|
| `görüntü`   | `IMAGE`   | Daha ileri işleme veya görselleştirme için hazır, büyütülmüş (ve isteğe bağlı olarak kırpılmış) görüntü. |