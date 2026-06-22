# MediaPipe Yüz Maskesi

## Genel Bakış

Bu düğüm, MediaPipe tarafından algılanan yüz işaret noktalarına dayalı olarak ikili bir maske (siyah beyaz bir görüntü) oluşturur. Algılanan her yüz bölgesi için dolu çokgen şekiller çizer ve bir yığındaki her kare için bir maske üretir. Aynı karede birden fazla yüz algılandığında, maskeleri tek bir maskede birleştirilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `face_landmarks` | Bir MediaPipe yüz algılama düğümünden gelen yüz işaret noktası verileri. | FACE_LANDMARKS | Evet | - |
| `regions` | Maskeye hangi yüz bölgelerinin dahil edileceğini seçer. `"all"`, tüm yüz bölgelerinin (yüz ovali, dudaklar, gözler, irisler) birleşiminden bir maske oluşturur. `"custom"`, her bölgeyi ayrı ayrı açıp kapatmanıza olanak tanır. Varsayılan: `"all"` | COMBO | Evet | `"all"`<br>`"custom"` |

`regions` parametresi `"custom"` olarak ayarlandığında, aşağıdaki ek boolean parametreler kullanılabilir hale gelir:

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `face_oval` | Yüz ovali bölgesini maskeye dahil eder. Varsayılan: True | BOOLEAN | Hayır | True/False |
| `lips` | Dudak bölgesini maskeye dahil eder. Varsayılan: True | BOOLEAN | Hayır | True/False |
| `eyes` | Göz bölgesini maskeye dahil eder. Varsayılan: True | BOOLEAN | Hayır | True/False |
| `irises` | İris bölgesini maskeye dahil eder. Varsayılan: True | BOOLEAN | Hayır | True/False |

**Not:** `"all"` modu kullanıldığında, maske tüm bölgelerin birleşimini içerir. Yüz ovali diğer bölgeleri çevrelediğinden, `"all"` seçeneği etkili bir şekilde yalnızca yüz ovalinin seçilmesiyle aynı sonucu verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MASK` | Yüz bölgelerinin beyaz (değer 1.0) ve arka planın siyah (değer 0.0) olduğu ikili bir maske tensörü. Maske, giriş görüntüsüyle aynı boyutlara sahiptir ve yığındaki her kare için bir maske içerir. | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MediaPipeFaceMask/tr.md)

---
**Source fingerprint (SHA-256):** `92270002a42ed59bc75e676a6881e1899186d3c8a1bb4dd4c0d39b3762b5bb66`
