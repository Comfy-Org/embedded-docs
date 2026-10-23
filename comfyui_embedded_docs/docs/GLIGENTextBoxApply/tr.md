# GLIGENMetinKutusuUygula

`GLIGENTextBoxApply` düğümü, metin tabanlı koşullandırmayı bir üretken modelin girdisine entegre etmek için tasarlanmıştır. Özellikle metin kutusu parametrelerini uygulayarak ve bunları bir CLIP modeli kullanarak kodlayarak çalışır. Bu süreç, koşullandırmayı mekansal ve metinsel bilgilerle zenginleştirerek daha hassas ve bağlam bilincine sahip bir üretim sağlar.

## Girişler

| Parametre | Açıklama | Comfy veri türü |
| --- | --- | --- |
| `hedef_koşullandırma` | Metin kutusu parametrelerinin ve kodlanmış metin bilgisinin ekleneceği başlangıç koşullandırma girdisini belirtir. Yeni koşullandırma verilerini entegre ederek nihai çıktının belirlenmesinde önemli bir rol oynar. | `CONDITIONING` |
| `clip` | Sağlanan metni, üretken model tarafından kullanılabilecek bir formata kodlamak için kullanılan CLIP modelidir. Metinsel bilgiyi uyumlu bir koşullandırma formatına dönüştürmek için gereklidir. | `CLIP` |
| `gligen_metinkutusu_modeli` | Metin kutusunu oluşturmak için kullanılacak belirli GLIGEN model yapılandırmasını temsil eder. Metin kutusunun istenen özelliklere göre oluşturulmasını sağlamak için önemlidir. | `GLIGEN` |
| `metin` | Kodlanacak ve koşullandırmaya entegre edilecek metin içeriğidir. Üretken modele rehberlik eden anlamsal bilgiyi sağlar. | `STRING` |
| `genişlik` | Metin kutusunun piksel cinsinden genişliğidir. Oluşturulan görüntü içindeki metin kutusunun mekansal boyutunu tanımlar. | `INT` |
| `yükseklik` | Metin kutusunun piksel cinsinden yüksekliğidir. Genişliğe benzer şekilde, oluşturulan görüntü içindeki metin kutusunun mekansal boyutunu tanımlar. | `INT` |
| `x` | Oluşturulan görüntü içindeki metin kutusunun sol üst köşesinin x koordinatıdır. Metin kutusunun yatay konumunu belirtir. | `INT` |
| `y` | Oluşturulan görüntü içindeki metin kutusunun sol üst köşesinin y koordinatıdır. Metin kutusunun dikey konumunu belirtir. | `INT` |

## Çıktılar

| Parametre | Açıklama | Comfy veri türü |
| --- | --- | --- |
| `conditioning` | Orijinal koşullandırma verileri ile yeni eklenen metin kutusu parametrelerini ve kodlanmış metin bilgisini içeren zenginleştirilmiş koşullandırma çıktısıdır. Üretken modele bağlam bilincine sahip çıktılar üretmede rehberlik etmek için kullanılır. | `CONDITIONING` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLIGENTextBoxApply/tr.md)
