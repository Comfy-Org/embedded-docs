> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageInvert/tr.md)

`ImageInvert` düğümü, bir görüntünün renklerini tersine çevirmek için tasarlanmıştır ve etkili bir şekilde her pikselin renk değerini renk tekerleğindeki tamamlayıcı rengine dönüştürür. Bu işlem, negatif görüntüler oluşturmak veya renk ters çevirme gerektiren görsel efektler için kullanışlıdır.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | 'image' parametresi, tersine çevrilecek giriş görüntüsünü temsil eder. Renkleri tersine çevrilecek hedef görüntüyü belirtmek için çok önemlidir, bu da düğümün yürütülmesini ve ters çevirme işleminin görsel sonucunu etkiler. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | Çıktı, giriş görüntüsünün ters çevrilmiş halidir; her pikselin renk değeri tamamlayıcı rengine dönüştürülmüştür. |