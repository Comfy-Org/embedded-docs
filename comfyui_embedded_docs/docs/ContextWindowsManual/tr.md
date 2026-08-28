# Bağlam Pencereleri (Manuel)

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Örnekleme sırasında bağlam pencerelerinin uygulanacağı model. | MODEL | Evet | - |
| `bağlam uzunluğu` | Bağlam penceresinin uzunluğu (varsayılan: 16). | INT | Evet | 1+ |
| `bağlam örtüşmesi` | Bağlam penceresinin örtüşme miktarı (varsayılan: 4). | INT | Evet | 0+ |
| `bağlam çizelgesi` | Bağlam pencereleri için adıma bağlı zamanlama algoritması (varsayılan: STATIC_STANDARD). | COMBO | Evet | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` |
| `bağlam adımı` | Bağlam penceresinin adım uzunluğu; yalnızca tekdüze (uniform) zamanlamalar için geçerlidir (varsayılan: 1). | INT | Evet | 1+ |
| `kapalı döngü` | Bağlam penceresi döngüsünün kapatılıp kapatılmayacağı; yalnızca döngülü (looped) zamanlamalar için geçerlidir (varsayılan: False). | BOOLEAN | Evet | - |
| `birleştirme yöntemi` | Bağlam pencerelerini birleştirmek için kullanılacak yöntem (varsayılan: PYRAMID). | COMBO | Evet | Statik birleştirme yöntemleri (bkz. `ContextFuseMethods.LIST_STATIC`) |
| `boyut` | Bağlam pencerelerinin uygulanacağı boyut (varsayılan: 0). | INT | Evet | 0-5 |
| `serbest_gürültü` | FreeNoise gürültü karıştırmanın uygulanıp uygulanmayacağı; pencere karışımını iyileştirir (varsayılan: False). | BOOLEAN | Evet | - |
| `cond_retain_index_list` | Her pencere için koşullandırma tensörlerinde saklanacak latent indekslerinin listesi. Concat tarzı I2V modelleri (örn. Wan I2V, HunyuanVideo I2V, Cosmos I2V, SVD) için kodlanmış başlangıç görüntüsü c_concat koşullandırma kanallarında bulunur; bunun '0' olarak ayarlanması, başlangıç görüntüsü içeriğini her pencerenin 0 alt konumunda saklar (varsayılan: ""). | STRING | Hayır | - |
| `split_conds_to_windows` | ConditionCombine tarafından oluşturulan birden fazla koşullandırmanın bölge indeksine göre her pencereye bölünüp bölünmeyeceği (varsayılan: False). | BOOLEAN | Hayır | - |
| `latent_retain_index_list` | Gürültü latentinin kendisinde her pencere için saklanacak latent indekslerinin listesi. Referans içeriğin (örn. bir başlangıç görüntüsü) ayrı koşullandırma kanalları yerine doğrudan gürültü latentinde bulunduğu iş akışları için kullanın (örn. LTXV, AnimateDiff gibi yerinde/inplace tarzı I2V). `cond_retain_index_list`'ten bağımsızdır (varsayılan: ""). | STRING | Hayır | - |
| `causal_window_fix` | 0 indeksli olmayan bağlam pencerelerine nedensel düzeltme çerçevesi eklenip eklenmeyeceği (varsayılan: True). | BOOLEAN | Hayır | - |

**Parametre Kısıtlamaları:**

- `context_stride` yalnızca tekdüze bir zamanlama seçildiğinde kullanılır (`UNIFORM_STANDARD` veya `UNIFORM_LOOPED`).
- `closed_loop` yalnızca döngülü zamanlamalar için geçerlidir (`UNIFORM_LOOPED`).
- `dim` 0 ile 5 arasında (dahil) olmalıdır.
- `cond_retain_index_list` ve `latent_retain_index_list`, bir dize olarak virgülle ayrılmış tam sayı indeksleri bekler (örn. "0,1,2").
- `latent_retain_index_list`, `cond_retain_index_list`'ten bağımsızdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Bağlam pencereleri örnekleme sırasında uygulanmış model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/tr.md)

---
**Source fingerprint (SHA-256):** `39dc39ece3d3c10c13ca8c4b85af4fbbebbcaba8a019145a6d4727c3df7b302b`
