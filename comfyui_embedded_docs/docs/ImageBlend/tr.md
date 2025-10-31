> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBlend/tr.md)

`ImageBlend` düğümü, iki görüntüyü belirli bir karıştırma modu ve karıştırma faktörüne göre birleştirmek için tasarlanmıştır. Normal, çarpma, ekran, kaplama, yumuşak ışık ve fark gibi çeşitli karıştırma modlarını destekleyerek çok yönlü görüntü işleme ve kompozit oluşturma tekniklerine olanak tanır. Bu düğüm, iki görüntü katmanı arasındaki görsel etkileşimi ayarlayarak kompozit görüntüler oluşturmak için gereklidir.

## Girişler

| Alan          | Veri Türü   | Açıklama                                                                       |
|---------------|-------------|---------------------------------------------------------------------------------|
| `görüntü1`      | `IMAGE`     | Birleştirilecek ilk görüntü. Karıştırma işlemi için temel katman görevi görür. |
| `görüntü2`      | `IMAGE`     | Birleştirilecek ikinci görüntü. Karıştırma moduna bağlı olarak, ilk görüntünün görünümünü değiştirir. |
| `karıştırma_faktörü`| `FLOAT`     | İkinci görüntünün karışımdaki ağırlığını belirler. Daha yüksek bir karıştırma faktörü, ortaya çıkan karışımda ikinci görüntüye daha fazla önem verir. |
| `karıştırma_modu`  | COMBO[STRING] | İki görüntünün karıştırılma yöntemini belirtir. Her biri benzersiz bir görsel efekt üreten normal, çarpma, ekran, kaplama, yumuşak ışık ve fark gibi modları destekler. |

## Çıkışlar

| Alan   | Veri Türü | Açıklama                                                              |
|--------|-------------|--------------------------------------------------------------------------|
| `image`| `IMAGE`     | Belirtilen karıştırma modu ve faktörüne göre iki giriş görüntüsünün karıştırılması sonucu oluşan görüntü. |