> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerPadKeyframesList/tr.md)

## Genel Bakış

Bu düğüm, bir dizi görüntüyü ve isteğe bağlı bir ses parçasını alarak, bunları belirtilen sayıda dolgulu parçaya böler. Video oluşturma için anahtar kare dizileri hazırlamak üzere tasarlanmıştır; burada her parça tutarlı bir uzunluğa dolgulanır ve hangi karelerin geçerli olduğunu belirtmek için karşılık gelen bir maske oluşturulur.

## Girdiler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `görseller` | IMAGE | Evet | Yok | Parçalara ayrılacak giriş görüntü dizisi. |
| `segment_uzunluğu` | INT | Evet | 1 ila 10000 | Kare cinsinden her parçanın uzunluğu (varsayılan: 149). |
| `segment_sayısı` | INT | Evet | 1 ila 100 | Liste olarak yayınlanacak dolgulu parça sayısı (varsayılan: 1). |
| `ses` | AUDIO | Hayır | Yok | Yayınlanan her parça için dilimlenecek ses. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `anahtar_kare_maskeleri` | IMAGE | Her parça için bir tane olmak üzere dolgulu anahtar kare dizilerinin listesi. |
| `ses_segmenti` | MASK | Her parça için geçerli kareleri belirten maskelerin listesi. |
| `audio_segment` | AUDIO | Her video parçası için bir tane olmak üzere ses parçalarının listesi. |

---
**Source fingerprint (SHA-256):** `c6a3ddca3fd61fcdb287fecb6969796eebd65e70f1174abdab57912586d27d00`
