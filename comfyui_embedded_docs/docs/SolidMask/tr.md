> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SolidMask/tr.md)

SolidMask düğümü, tüm alanı boyunca belirtilen değerde tek tip bir maske oluşturur. Belirli boyutlarda ve yoğunlukta maskeler oluşturmak için tasarlanmıştır; çeşitli görüntü işleme ve maskeleme görevlerinde kullanışlıdır.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `değer`   | FLOAT       | Maskenin yoğunluk değerini belirtir; genel görünümünü ve sonraki işlemlerdeki kullanışlılığını etkiler. |
| `genişlik`   | INT         | Oluşturulan maskenin genişliğini belirler; boyutunu ve en-boy oranını doğrudan etkiler. |
| `yükseklik`  | INT         | Oluşturulan maskenin yüksekliğini ayarlar; boyutunu ve en-boy oranını etkiler. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `mask`    | MASK        | Belirtilen boyutlarda ve değerde tek tip bir maske çıktısı verir. |