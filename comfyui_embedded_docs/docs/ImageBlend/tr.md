> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBlend/tr.md)

`ImageBlend` düğümü, belirtilen bir karıştırma modu ve karıştırma faktörüne göre iki görüntüyü birbirine karıştırmak için tasarlanmıştır. Normal, çarpma, ekran, kaplama, yumuşak ışık ve fark gibi çeşitli karıştırma modlarını destekleyerek çok yönlü görüntü işleme ve birleştirme tekniklerine olanak tanır. Bu düğüm, iki görüntü katmanı arasındaki görsel etkileşimi ayarlayarak bileşik görüntüler oluşturmak için gereklidir.

## Girişler

| Alan           | Veri Türü    | Açıklama                                                                       |
|----------------|--------------|--------------------------------------------------------------------------------|
| `image1`       | `IMAGE`      | Karıştırılacak ilk görüntü. Karıştırma işlemi için temel katman görevi görür. |
| `image2`       | `IMAGE`      | Karıştırılacak ikinci görüntü. Karıştırma moduna bağlı olarak ilk görüntünün görünümünü değiştirir. |
| `blend_factor` | `FLOAT`      | Karışımdaki ikinci görüntünün ağırlığını belirler. Daha yüksek bir karıştırma faktörü, ortaya çıkan karışımda ikinci görüntüye daha fazla ön plana çıkarır. |
| `blend_mode`   | COMBO[STRING] | İki görüntüyü karıştırma yöntemini belirtir. Her biri benzersiz bir görsel efekt üreten normal, çarpma, ekran, kaplama, yumuşak ışık ve fark gibi modları destekler. |

## Çıkışlar

| Alan    | Veri Türü | Açıklama                                                              |
|---------|-----------|------------------------------------------------------------------------|
| `image` | `IMAGE`   | Belirtilen karıştırma modu ve faktörüne göre iki giriş görüntüsünün karıştırılmasıyla elde edilen sonuç görüntüsü. |