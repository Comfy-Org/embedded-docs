> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLIGENTextBoxApply/tr.md)

`GLIGENTextBoxApply` düğümü, metin tabanlı koşullandırmayı bir üretken modelin girdisine entegre etmek için tasarlanmıştır. Özellikle metin kutusu parametrelerini uygulayarak ve bunları bir CLIP modeli kullanarak kodlayarak çalışır. Bu süreç, koşullandırmayı mekansal ve metinsel bilgilerle zenginleştirerek daha hassas ve bağlam bilincine sahip bir üretim sağlar.

## Girişler

| Parametre            | Comfy veri türü  | Açıklama |
|----------------------|--------------------|-------------|
| `conditioning_to`     | `CONDITIONING`     | Metin kutusu parametrelerinin ve kodlanmış metin bilgisinin ekleneceği başlangıç koşullandırma girdisini belirtir. Yeni koşullandırma verilerini entegre ederek nihai çıktının belirlenmesinde önemli bir rol oynar. |
| `clip`               | `CLIP`             | Sağlanan metni, üretken model tarafından kullanılabilecek bir formata kodlamak için kullanılan CLIP modelidir. Metinsel bilgiyi uyumlu bir koşullandırma formatına dönüştürmek için gereklidir. |
| `gligen_textbox_model` | `GLIGEN`         | Metin kutusunu oluşturmak için kullanılacak belirli GLIGEN model yapılandırmasını temsil eder. Metin kutusunun istenen özelliklere göre oluşturulmasını sağlamak için önemlidir. |
| `text`               | `STRING`           | Kodlanacak ve koşullandırmaya entegre edilecek metin içeriğidir. Üretken modele rehberlik eden anlamsal bilgiyi sağlar. |
| `width`              | `INT`              | Metin kutusunun piksel cinsinden genişliğidir. Oluşturulan görüntü içindeki metin kutusunun mekansal boyutunu tanımlar. |
| `height`             | `INT`              | Metin kutusunun piksel cinsinden yüksekliğidir. Genişliğe benzer şekilde, oluşturulan görüntü içindeki metin kutusunun mekansal boyutunu tanımlar. |
| `x`                  | `INT`              | Oluşturulan görüntü içindeki metin kutusunun sol üst köşesinin x koordinatıdır. Metin kutusunun yatay konumunu belirtir. |
| `y`                  | `INT`              | Oluşturulan görüntü içindeki metin kutusunun sol üst köşesinin y koordinatıdır. Metin kutusunun dikey konumunu belirtir. |

## Çıktılar

| Parametre            | Comfy veri türü  | Açıklama |
|----------------------|--------------------|-------------|
| `conditioning`        | `CONDITIONING`     | Orijinal koşullandırma verileri ile yeni eklenen metin kutusu parametrelerini ve kodlanmış metin bilgisini içeren zenginleştirilmiş koşullandırma çıktısıdır. Üretken modele bağlam bilincine sahip çıktılar üretmede rehberlik etmek için kullanılır. |