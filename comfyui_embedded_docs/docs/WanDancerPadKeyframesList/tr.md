## Genel Bakış

Bu düğüm, bir dizi görüntüyü ve isteğe bağlı bir ses parçasını alarak, bunları belirtilen sayıda dolgulu parçaya böler. Video oluşturma için anahtar kare dizileri hazırlamak üzere tasarlanmıştır; burada her parça tutarlı bir uzunluğa dolgulanır ve hangi karelerin geçerli olduğunu belirtmek için karşılık gelen bir maske oluşturulur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `görseller` | Parçalara ayrılacak giriş görüntü dizisi. | IMAGE | Evet | Yok |
| `segment_uzunluğu` | Kare cinsinden her parçanın uzunluğu (varsayılan: 149). | INT | Evet | 1 ila 10000 |
| `segment_sayısı` | Liste olarak yayınlanacak dolgulu parça sayısı (varsayılan: 1). | INT | Evet | 1 ila 100 |
| `ses` | Yayınlanan her parça için dilimlenecek ses. | AUDIO | Hayır | Yok |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `anahtar_kare_dizileri` | Her parça için bir tane olmak üzere dolgulu anahtar kare dizilerinin listesi. | IMAGE |
| `anahtar_kare_maskeleri` | Her parça için geçerli kareleri belirten maskelerin listesi. | MASK |
| `ses_segmenti` | Her video parçası için bir tane olmak üzere ses parçalarının listesi. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerPadKeyframesList/tr.md)

---
**Source fingerprint (SHA-256):** `c6a3ddca3fd61fcdb287fecb6969796eebd65e70f1174abdab57912586d27d00`
