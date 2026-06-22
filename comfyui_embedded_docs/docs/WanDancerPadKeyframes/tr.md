# WanDancerPadKeyframes

## Genel Bakış

Bu düğüm, daha uzun bir video oluşturma sürecinin belirli bir bölümü için bir dizi ana kare hazırlar. Bir grup girdi görüntüsü ve bir ses parçası alır, ses süresine göre tam videonun sahip olması gereken toplam kare sayısını hesaplar ve ardından girdi görüntülerini seçilen bölüm boyunca ana kareler olarak dağıtır, kalan kısımları boş karelerle doldurur. Ayrıca bu bölüm için sesin ilgili kısmını çıkarır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görseller` | Ana kareler olarak dağıtılacak girdi görüntüleri. | IMAGE | Evet | Görüntü grubu |
| `segment_uzunluğu` | Bu bölümün kare cinsinden uzunluğu (varsayılan: 149). | INT | Evet | 1 ila 10000 |
| `segment_indeksi` | Bu bölümün hangi bölüm olduğu (0 ilk, 1 ikinci, vb., varsayılan: 0). | INT | Evet | 0 ila 100 |
| `ses` | Toplam çıktı karelerini hesaplamak ve bölüm sesini çıkarmak için kullanılacak ses. | AUDIO | Evet | Ses verisi |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `anahtar_kare_maskesi` | Belirtilen bölüm için doldurulmuş ana kare dizisi. | IMAGE |
| `ses_segmenti` | Geçerli kareleri gösteren maske (ana kare konumları için 1, doldurulmuş konumlar için 0). | MASK |
| `audio_segment` | Bu video bölümü için ses bölümü. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerPadKeyframes/tr.md)

---
**Source fingerprint (SHA-256):** `5a104b45faaa870727d4c45e6327e7233110b40dc5a13515a29e5f14de2050e0`
