> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerPadKeyframes/tr.md)

## Genel Bakış

Bu düğüm, daha uzun bir video oluşturma sürecinin belirli bir bölümü için bir ana kare dizisi hazırlar. Giriş görüntülerinden oluşan bir grubu ve bir ses parçasını alır, ses süresine göre tam videonun sahip olması gereken toplam kare sayısını hesaplar ve ardından giriş görüntülerini seçilen bölüm boyunca ana kareler olarak dağıtır, kalan kısımları boş karelerle doldurur. Ayrıca bu bölüm için sesin karşılık gelen kısmını çıkarır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Evet | Görüntü grubu | Ana kareler olarak dağıtılacak giriş görüntüleri. |
| `segment_length` | INT | Evet | 1 ila 10000 | Bu bölümün kare cinsinden uzunluğu (varsayılan: 149). |
| `segment_index` | INT | Evet | 0 ila 100 | Bu bölümün hangi bölüm olduğu (0 ilk, 1 ikinci, vb., varsayılan: 0). |
| `audio` | AUDIO | Evet | Ses verisi | Toplam çıktı kare sayısını hesaplamak ve bölüm sesini çıkarmak için kullanılacak ses. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `keyframes_sequence` | IMAGE | Belirtilen bölüm için doldurulmuş ana kare dizisi. |
| `keyframes_mask` | MASK | Geçerli kareleri gösteren maske (ana kare konumları için 1, doldurulmuş konumlar için 0). |
| `audio_segment` | AUDIO | Bu video bölümü için ses bölümü. |