> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageMask/tr.md)

LoadImageMask düğümü, belirli bir yoldan görüntüleri ve bunlarla ilişkili maskeleri yüklemek, bunları daha sonraki görüntü işleme veya analiz görevleriyle uyumluluğunu sağlamak için işlemek üzere tasarlanmıştır. Maskeler için alfa kanalı varlığı gibi çeşitli görüntü formatları ve koşullarını ele almaya odaklanır ve görüntüleri standart bir formata dönüştürerek aşağı yönlü işleme hazırlar.

## Girdiler

| Parametre | Veri Tipi | Açıklama |
|-----------|-------------|-------------|
| `görüntü`   | COMBO[STRING] | 'image' parametresi, yüklenecek ve işlenecek görüntü dosyasını belirtir. Maske çıkarımı ve format dönüşümü için kaynak görüntüyü sağlayarak çıktıyı belirlemede çok önemli bir rol oynar. |
| `kanal` | COMBO[STRING] | 'channel' parametresi, maskeyi oluşturmak için kullanılacak olan görüntünün renk kanalını belirtir. Bu, farklı renk kanallarına dayalı maske oluşturmada esneklik sağlayarak düğümün çeşitli görüntü işleme senaryolarındaki kullanışlılığını artırır. |

## Çıktılar

| Parametre | Veri Tipi | Açıklama |
|-----------|-------------|-------------|
| `mask`    | `MASK`      | Bu düğüm, belirtilen görüntü ve kanaldan oluşturulan, görüntü işleme görevlerinde daha fazla işleme uygun standart formatta hazırlanmış maskeyi çıkarır. |