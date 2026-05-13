> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscale/tr.md)

LatentUpscale düğümü, görüntülerin gizli (latent) temsillerini büyütmek için tasarlanmıştır. Çıktı görüntüsünün boyutlarının ve büyütme yönteminin ayarlanmasına olanak tanıyarak, gizli görüntülerin çözünürlüğünü artırmada esneklik sağlar.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `örnekler` | `LATENT`    | Büyütülecek görüntünün gizli temsili. Bu parametre, büyütme işleminin başlangıç noktasını belirlemek için çok önemlidir. |
| `büyütme_yöntemi` | COMBO[STRING] | Gizli görüntüyü büyütmek için kullanılan yöntemi belirtir. Farklı yöntemler, büyütülmüş görüntünün kalitesini ve özelliklerini etkileyebilir. |
| `genişlik`   | `INT`       | Büyütülmüş görüntünün istenen genişliği. 0 olarak ayarlanırsa, en boy oranını korumak için yüksekliğe göre hesaplanır. |
| `yükseklik`  | `INT`       | Büyütülmüş görüntünün istenen yüksekliği. 0 olarak ayarlanırsa, en boy oranını korumak için genişliğe göre hesaplanır. |
| `kırp`    | COMBO[STRING] | Büyütülmüş görüntünün nasıl kırpılacağını belirler; bu, çıktının son görünümünü ve boyutlarını etkiler. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Görüntünün büyütülmüş gizli temsili; daha fazla işleme veya oluşturma için hazırdır. |