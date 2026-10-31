# MiniMax H3 Max Lip Sync

Bu düğüm, hareketsiz bir görüntüyü, sağlanan ses parçasına göre ağız hareketlerini takip edecek şekilde canlandırır. Görüntü ve ses yüklenir, Hailuo 03 Max dudak senkronizasyonu işi yoklanır ve konuşan video seçtiğiniz çözünürlükte geri döner. Çıktı videosu, sesin süresi kadar uzundur.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video oluşturmak için kullanılacak model. | DYNAMIC_COMBO | Evet | "MiniMax H3 Max" |

### MiniMax H3 Max Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Canlandırılacak görüntü, en az 256x256 piksel. En-boy oranı 0,4 ile 2,5 arasında olmalıdır. | IMAGE | Evet | Tek görüntü |
| `audio` | Dudak senkronizasyonu yapılacak ses, 5 ile 899 saniye uzunluğunda. | AUDIO | Evet | 5–899 saniye |
| `resolution` | Çıktı çözünürlüğü (varsayılan: "768P"). En-boy oranı, görüntüye en yakın desteklenen orandır. | COMBO | Evet | "480P"<br>"768P"<br>"1080P"<br>"2K" |
| `transcription` | Sesi, dudak senkronizasyonuna kılavuzluk etmesi için yazıya döker (varsayılan: false). | BOOLEAN | Hayır | true<br>false |
| `seed` | Rastgele tohum. Aynı tohumla yapılan aynı istek benzer, ancak birebir aynı olduğu garanti edilmeyen sonuçlar verir (varsayılan: 42). | INT | Evet | 0–2147483647 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Konuşan video, girdi sesi kadar uzundur. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxLipSyncNode/tr.md)

---
**Source fingerprint (SHA-256):** `0af4166f9f3237cacc3506d6c6544c0374a330cf998f8bd2ef1f4f7162e2f9ab`
