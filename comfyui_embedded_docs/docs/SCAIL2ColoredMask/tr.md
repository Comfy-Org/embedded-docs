# SCAIL-2 Renkli Maske Oluştur

Bu düğüm, SAM3 izleme verilerini WanSCAILToVideo düğümü tarafından kullanılan renkli maskelere dönüştürür. Bir yönlendirici poz videosundan ve isteğe bağlı olarak bir referans görüntüden gelen izleme verilerini işler; her iki çıktıda da izlenen her kişiye tutarlı renkler atar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `driving_track_data` | Yönlendirici poz videosunun SAM3 izlemesi. `pose_video_mask` çıktısına dönüştürülecektir. | SAM3_TRACK_DATA | Evet | - |
| `ref_track_data` | Referans görüntü(ler)in SAM3 izlemesi (nesne başına bir kimlik, toplu iş sırasına göre renklendirilir) veya referans öznenin düz bir MASK'ı (tek bir kimlik olarak işlenir). | SAM3_TRACK_DATA veya MASK | Hayır | - |
| `nesne_indeksleri` | Dahil edilecek kişi indekslerinin virgülle ayrılmış listesi (örn. '0,2,3'). Hem referans hem de poz videosu maskelerine uygulanır. Boş = tümü. (varsayılan: "") | STRING | Evet | - |
| `sırala` | Palet renklerinin izlenen nesnelere atanma sırası (hem referansa hem de poz videosuna uygulanır, böylece her kimlik aynı rengi korur). Daha önceki karelerde görünen nesneler her zaman önce gelir; bir kare içinde left_to_right = en soldaki nesne (ilk görünümdeki ağırlık merkezine göre) ilk rengi alır, area = en büyük nesne (ilk görünümdeki maske alanına göre) ilk rengi alır; none = SAM3'ün sırasını korur. (varsayılan: "left_to_right") | COMBO | Evet | `"none"`<br>`"left_to_right"`<br>`"area"` |
| `değiştirme_modu` | False = Animasyon Modu (pose_video_mask siyah arka plana sahiptir, reference_image_mask beyaz arka plana sahiptir). True = Değiştirme Modu (pose_video_mask beyaz arka plana sahiptir, reference_image_mask siyah arka plana sahiptir). (varsayılan: False) | BOOLEAN | Evet | False<br>True |

Not: `object_indices` yalnızca virgülle ayrılmış rakamları kabul eder; sayısal olmayan girdiler ve aralık dışı indeksler yok sayılır. `ref_track_data` sağlanmadığında, `reference_image_mask` çıktısı referans arka plan rengi kullanılarak düz bir dolgu olur (Animasyon Modunda beyaz, Değiştirme Modunda siyah).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `pose_video_mask` | Yönlendirici poz videosu izleme verilerinden oluşturulan renkli maske. Arka plan rengi replacement_mode ayarına uyar. | IMAGE |
| `reference_image_mask` | Referans görüntü izleme verilerinden oluşturulan renkli maske. Değiştirme Modunda arka plan siyah, Animasyon Modunda beyazdır. Referans verisi sağlanmazsa, referans arka plan rengiyle eşleşen düz bir dolgu döndürür. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SCAIL2ColoredMask/tr.md)

---
**Source fingerprint (SHA-256):** `ce0669ad0ed3c76cc18ef0ee7b620f5aa6eaa1e5b96c189941c0a5b744c3351f`
