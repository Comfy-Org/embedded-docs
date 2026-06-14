# SCAIL2ColoredMask

Bu düğüm, SAM3 takip verilerini, WanSCAILToVideo düğümü tarafından kullanılan renkli maskelere dönüştürür. Sürüş pozu videosundan ve isteğe bağlı olarak bir referans görüntüden gelen takip verilerini işleyerek, her iki çıktıda da takip edilen her kişiye tutarlı renkler atar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|---------|--------|
| `driving_track_data` | Sürüş pozu videosunun SAM3 takibi. pose_video_mask çıktısına dönüştürülecektir. | SAM3_TRACK_DATA | Evet | - |
| `ref_track_data` | Referans görüntünün SAM3 takibi. | SAM3_TRACK_DATA | Hayır | - |
| `object_indices` | Dahil edilecek kişi indekslerinin virgülle ayrılmış listesi (örn. '0,2,3'). Hem referans hem de poz videosu maskelerine uygulanır. Boş = tümü. | STRING | Evet | - |
| `sort_by` | Palet renklerinin takip edilen nesnelere atanma sırası (her kimliğin aynı rengi koruması için hem referans hem de poz videosuna uygulanır). left_to_right = en soldaki nesne (ilk kare merkez noktasına göre) ilk rengi alır; area = en büyük nesne (ilk kare maske alanına göre) ilk rengi alır; none = SAM3'ün sırasını korur. (varsayılan: "left_to_right") | COMBO | Evet | `"none"`<br>`"left_to_right"`<br>`"area"` |
| `replacement_mode` | False = Animasyon Modu (pose_video_mask siyah arka plana, reference_image_mask beyaz arka plana sahiptir). True = Değiştirme Modu (pose_video_mask beyaz arka plana, reference_image_mask siyah arka plana sahiptir). (varsayılan: False) | BOOLEAN | Evet | False<br>True |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `pose_video_mask` | Sürüş pozu videosu takip verilerinden oluşturulan renkli maske. Arka plan rengi replacement_mode ayarını takip eder. | IMAGE |
| `reference_image_mask` | Referans görüntü takip verilerinden oluşturulan renkli maske. Model kuralı gereği her zaman siyah arka planla oluşturulur. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SCAIL2ColoredMask/tr.md)

---
**Source fingerprint (SHA-256):** `c9f6d87410b8bd4082ffb06ef1cf973829566ed222be643db3528cbc241d3c14`
