> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SolidMask/tr.md)

SolidMask düğümü, belirli bir değere sahip düzgün bir maske oluşturur. Belirli boyutlarda ve yoğunlukta maskeler oluşturmak için tasarlanmıştır ve çeşitli görüntü işleme ve maskeleme görevlerinde kullanışlıdır.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `değer`   | FLOAT       | Maskenin yoğunluk değerini belirler ve sonraki işlemlerde genel görünümünü ve kullanışlılığını etkiler. |
| `genişlik`   | INT         | Oluşturulan maskenin genişliğini belirler ve doğrudan boyutunu ve en-boy oranını etkiler. |
| `yükseklik`  | INT         | Oluşturulan maskenin yüksekliğini belirler ve boyutunu ile en-boy oranını etkiler. |

## Çıkışlar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `mask`    | MASK        | Belirtilen boyutlarda ve değerde düzgün bir maske çıktısı verir. |