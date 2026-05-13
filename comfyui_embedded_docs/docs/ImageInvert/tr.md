> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageInvert/tr.md)

`ImageInvert` düğümü, bir görüntünün renklerini tersine çevirmek, yani her pikselin renk değerini renk tekerleğindeki tamamlayıcı rengine dönüştürmek için tasarlanmıştır. Bu işlem, negatif görüntüler oluşturmak veya renk tersine çevirme gerektiren görsel efektler için kullanışlıdır.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | 'image' parametresi, tersine çevrilecek giriş görüntüsünü temsil eder. Renkleri tersine çevrilecek hedef görüntüyü belirtmek için kritiktir; düğümün yürütülmesini ve tersine çevirme işleminin görsel sonucunu etkiler. |

## Çıkışlar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | Çıktı, giriş görüntüsünün tersine çevrilmiş bir sürümüdür; her pikselin renk değeri, tamamlayıcı rengine dönüştürülmüştür. |