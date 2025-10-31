> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLIGENTextBoxApply/tr.md)

`GLIGENTextBoxApply` düğümü, metin tabanlı koşullandırmayı bir üretken modelin girdisine entegre etmek üzere tasarlanmıştır; özellikle metin kutusu parametrelerini uygulayarak ve bunları bir CLIP modeli kullanarak kodlayarak çalışır. Bu süreç, koşullandırmayı mekansal ve metinsel bilgilerle zenginleştirerek daha hassas ve bağlamdan haberdar üretimi kolaylaştırır.

## Girdiler

| Parametre           | Comfy dtype        | Açıklama |
|---------------------|--------------------|-------------|
| `hedef_koşullandırma`   | `CONDITIONING`     | Metin kutusu parametrelerinin ve kodlanmış metin bilgisinin ekleneceği başlangıç koşullandırma girdisini belirtir. Yeni koşullandırma verilerini entegre ederek nihai çıktının belirlenmesinde kritik bir rol oynar. |
| `clip`              | `CLIP`             | Sağlanan metni, üretken model tarafından kullanılabilecek bir formata kodlamak için kullanılan CLIP modelidir. Metin bilgisini uyumlu bir koşullandırma formatına dönüştürmek için gereklidir. |
| `gligen_metinkutusu_modeli` | `GLIGEN`        | Metin kutusunu oluşturmak için kullanılacak spesifik GLIGEN model konfigürasyonunu temsil eder. Metin kutusunun istenen özelliklere göre oluşturulmasını sağlamak için çok önemlidir. |
| `metin`              | `STRING`           | Kodlanacak ve koşullandırmaya entegre edilecek metin içeriğidir. Üretken modeli yönlendiren anlamsal bilgiyi sağlar. |
| `genişlik`             | `INT`              | Metin kutusunun piksel cinsinden genişliğidir. Oluşturulan görüntü içindeki metin kutusunun mekansal boyutunu tanımlar. |
| `yükseklik`            | `INT`              | Metin kutusunun piksel cinsinden yüksekliğidir. Genişliğe benzer şekilde, oluşturulan görüntü içindeki metin kutusunun mekansal boyutunu tanımlar. |
| `x`                 | `INT`              | Metin kutusunun oluşturulan görüntü içindeki sol üst köşesinin x koordinatıdır. Metin kutusunun yatay konumunu belirtir. |
| `y`                 | `INT`              | Metin kutusunun oluşturulan görüntü içindeki sol üst köşesinin y koordinatıdır. Metin kutusunun dikey konumunu belirtir. |

## Çıktılar

| Parametre           | Comfy dtype        | Açıklama |
|---------------------|--------------------|-------------|
| `conditioning`      | `CONDITIONING`     | Orijinal koşullandırma verilerinin yanı sıra yeni eklenen metin kutusu parametrelerini ve kodlanmış metin bilgisini içeren zenginleştirilmiş koşullandırma çıktısıdır. Üretken modelin bağlamdan haberdar çıktılar üretmesine rehberlik etmek için kullanılır. |