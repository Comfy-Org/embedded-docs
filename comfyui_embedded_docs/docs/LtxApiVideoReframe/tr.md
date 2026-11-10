# LTX Video Reframe

Bir videoyu yeni bir çözünürlük ve en-boy oranına yeniden çerçeveler. Orijinal videonun dışındaki alan, içeriğiyle eşleşecek şekilde oluşturulur; böylece dikey bir klip yatay hale gelebilir veya bunun tersi olabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `video` | Yeniden çerçevelenecek video; en fazla 60 saniye ve 1800 kare, her bir kenarı 64 ile 4096 piksel arasında. | VIDEO | Evet | - |
| `resolution` | Çıktı boyutu ve en-boy oranı; 720p veya 1080p. Varsayılan: `"(1080p) 1080x1920 (9:16)"`. | COMBO | Evet | `"(720p) 720x720 (1:1)"`<br>`"(720p) 720x900 (4:5)"`<br>`"(720p) 900x720 (5:4)"`<br>`"(720p) 720x1280 (9:16)"`<br>`"(720p) 1280x720 (16:9)"`<br>`"(1080p) 1080x1080 (1:1)"`<br>`"(1080p) 1080x1350 (4:5)"`<br>`"(1080p) 1350x1080 (5:4)"`<br>`"(1080p) 1080x1920 (9:16)"`<br>`"(1080p) 1920x1080 (16:9)"` |
| `placement` | Orijinal videonun yeni çerçevede nerede konumlandığını belirler. Video her zaman çerçevenin bir kenarını doldurur; bu nedenle bir çapa onu yalnızca diğer kenar boyunca hareket ettirir. Varsayılan: `"center"`. | DYNAMIC_COMBO | Evet | `"center"`<br>`"top"`<br>`"bottom"`<br>`"left"`<br>`"right"`<br>`"custom"` |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar `seed` değerinden bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Hayır | 0 ile 4294967295 arası |

### Yerleştirme "custom" Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `x` | Çıktı genişliğinin bir oranı olarak videonun sol kenarı. Varsayılan: 0.25. | FLOAT | Hayır | 0.0 ile 0.99 arası (adım: 0.01) |
| `y` | Çıktı yüksekliğinin bir oranı olarak videonun üst kenarı. Varsayılan: 0.25. | FLOAT | Hayır | 0.0 ile 0.99 arası (adım: 0.01) |
| `width` | Çıktı genişliğinin bir oranı olarak videonun genişliği; yükseklik videonun en-boy oranını izler. Video çerçevenin içinde kalmalıdır ve en fazla 2 kat büyütülebilir. Varsayılan: 0.5. | FLOAT | Hayır | 0.01 ile 1.0 arası (adım: 0.01) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Yeniden çerçevelenmiş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApiVideoReframe/tr.md)

---
**Source fingerprint (SHA-256):** `85fcce4a8054fa8faf0085a55510ee09bce89afd1cf9f19d6ea45105549f2656`
