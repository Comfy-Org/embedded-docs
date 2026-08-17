# Bağlam Pencereleri (Manuel)

The Context Windows (Manual) düğümü, örnekleme sırasında modeller için bağlam pencerelerini manuel olarak yapılandırmanıza olanak tanır. Belirtilen uzunluk, örtüşme ve zamanlama düzenlerine sahip örtüşen bağlam bölümleri oluşturarak verileri yönetilebilir parçalar halinde işlerken bölümler arasında süreklilik sağlar. Bu düğüm, gürültü karıştırma, koşullandırma koruma, gürültü latenti koruma ve nedensel pencere düzeltmeleri dahil olmak üzere bağlam pencerelerinin nasıl uygulanacağını kontrol etmek için gelişmiş seçenekler sunar.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Örnekleme sırasında bağlam pencerelerinin uygulanacağı model. | MODEL | Evet | - |
| `context_length` | Bağlam penceresinin uzunluğu (varsayılan: 16). | INT | Hayır | 1+ |
| `context_overlap` | Bağlam penceresinin örtüşme miktarı (varsayılan: 4). | INT | Hayır | 0+ |
| `context_schedule` | Bağlam pencereleri için adıma bağlı zamanlama algoritması (varsayılan: STATIC_STANDARD). | COMBO | Hayır | `"STATIC_STANDARD"`<br>`"UNIFORM_STANDARD"`<br>`"UNIFORM_LOOPED"`<br>`"BATCHED"` |
| `context_stride` | Bağlam penceresinin adım uzunluğu; yalnızca tekdüze zamanlamalar için geçerlidir (varsayılan: 1). | INT | Hayır | 1+ |
| `closed_loop` | Bağlam penceresi döngüsünün kapatılıp kapatılmayacağı; yalnızca döngülü zamanlamalar için geçerlidir (varsayılan: False). | BOOLEAN | Hayır | - |
| `fuse_method` | Bağlam pencerelerini birleştirmek için kullanılacak yöntem (varsayılan: PYRAMID). | COMBO | Hayır | `"PYRAMID"`<br>`"LIST_STATIC"` |
| `dim` | Bağlam pencerelerinin uygulanacağı boyut (varsayılan: 0). | INT | Hayır | 0-5 |
| `freenoise` | FreeNoise gürültü karıştırmanın uygulanıp uygulanmayacağı, pencere harmanlamasını iyileştirir (varsayılan: False). | BOOLEAN | Hayır | - |
| `cond_retain_index_list` | Her pencere için koşullandırma tensörlerinde korunacak latent indekslerin listesi. Concat tarzı I2V modelleri için (örn. Wan I2V, HunyuanVideo I2V, Cosmos I2V, SVD) kodlanmış başlangıç görüntüsü c_concat koşullandırma kanallarında bulunur; bunun '0' olarak ayarlanması, bu başlangıç görüntüsü içeriğini her pencerenin alt konum 0'ında koruyacaktır (varsayılan: ""). | STRING | Hayır | - |
| `split_conds_to_windows` | ConditionCombine tarafından oluşturulan birden çok koşullandırmanın, bölge indeksine göre her pencereye bölünüp bölünmeyeceği (varsayılan: False). | BOOLEAN | Hayır | - |
| `latent_retain_index_list` | Her pencere için gürültü latenti içinde korunacak latent indekslerin listesi. Referans içeriğin (örn. bir başlangıç görüntüsü) ayrı koşullandırma kanalları yerine doğrudan gürültü latenti içinde bulunduğu iş akışları için kullanın (örn. LTXV, AnimateDiff gibi yerinde I2V). `cond_retain_index_list`'ten bağımsızdır (varsayılan: ""). | STRING | Hayır | - |
| `causal_window_fix` | 0 indeksli olmayan bağlam pencerelerine nedensel düzeltme çerçevesi eklenip eklenmeyeceği (varsayılan: True). | BOOLEAN | Hayır | - |

**Parametre Kısıtlamaları:**

- `context_stride` yalnızca tekdüze zamanlamalar seçildiğinde kullanılır
- `closed_loop` yalnızca döngülü zamanlamalar için geçerlidir
- `dim` 0 ile 5 arasında (dahil) olmalıdır
- `cond_retain_index_list`, virgülle ayrılmış bir tamsayı indeks listesi olarak bir dize bekler (örn. "0,1,2")
- `latent_retain_index_list`, virgülle ayrılmış bir tamsayı indeks listesi olarak bir dize bekler (örn. "0,1,2") ve `cond_retain_index_list`'ten bağımsızdır

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
| --- | --- | --- |
| `model` | Örnekleme sırasında bağlam pencereleri uygulanmış model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/tr.md)

---
**Source fingerprint (SHA-256):** `39dc39ece3d3c10c13ca8c4b85af4fbbebbcaba8a019145a6d4727c3df7b302b`
