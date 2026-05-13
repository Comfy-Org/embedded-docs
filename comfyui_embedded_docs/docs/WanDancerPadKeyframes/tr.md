> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerPadKeyframes/tr.md)

## Genel Bakış

Bu düğüm, daha uzun bir video oluşturma sürecinin belirli bir bölümü için bir dizi ana kare hazırlar. Bir grup girdi görüntüsü ve bir ses parçası alır, ses süresine göre tam videonun sahip olması gereken toplam kare sayısını hesaplar ve ardından girdi görüntülerini seçilen bölüm boyunca ana kareler olarak dağıtır, kalan kısımları boş karelerle doldurur. Ayrıca bu bölüm için sesin ilgili kısmını çıkarır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `görseller` | IMAGE | Evet | Görüntü grubu | Ana kareler olarak dağıtılacak girdi görüntüleri. |
| `segment_uzunluğu` | INT | Evet | 1 ila 10000 | Bu bölümün kare cinsinden uzunluğu (varsayılan: 149). |
| `segment_indeksi` | INT | Evet | 0 ila 100 | Bu bölümün hangi bölüm olduğu (0 ilk, 1 ikinci, vb., varsayılan: 0). |
| `ses` | AUDIO | Evet | Ses verisi | Toplam çıktı karelerini hesaplamak ve bölüm sesini çıkarmak için kullanılacak ses. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `anahtar_kare_maskesi` | IMAGE | Belirtilen bölüm için doldurulmuş ana kare dizisi. |
| `ses_segmenti` | MASK | Geçerli kareleri gösteren maske (ana kare konumları için 1, doldurulmuş konumlar için 0). |
| `audio_segment` | AUDIO | Bu video bölümü için ses bölümü. |

---
**Source fingerprint (SHA-256):** `5a104b45faaa870727d4c45e6327e7233110b40dc5a13515a29e5f14de2050e0`
