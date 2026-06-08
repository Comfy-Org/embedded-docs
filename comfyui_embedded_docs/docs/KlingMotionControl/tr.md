Kling Motion Control düğümü, referans bir görüntü ve metin istemiyle tanımlanan bir karaktere, referans bir videodaki hareket, ifade ve kamera hareketlerini uygulayarak bir video oluşturur. Karakterin nihai yönünün referans videodan mı yoksa referans görüntüden mi geleceğini kontrol etmenizi sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `istem` | İstenen videonun metin açıklaması. Maksimum uzunluk 2500 karakterdir. | STRING | Evet | Yok |
| `referans_görsel` | Canlandırılacak karakterin görüntüsü. Minimum boyutlar 340x340 pikseldir. En-boy oranı 1:2,5 ile 2,5:1 arasında olmalıdır. | IMAGE | Evet | Yok |
| `referans_video` | Karakterin hareketini ve ifadesini yönlendirmek için kullanılan bir hareket referans videosu. Minimum boyutlar 340x340 piksel, maksimum boyutlar 3850x3850 pikseldir. Süre sınırları `karakter_yönelimi` ayarına bağlıdır. | VIDEO | Evet | Yok |
| `orijinal_sesi_koru` | Referans videodaki orijinal sesin çıktıda korunup korunmayacağını belirler. Varsayılan `True` değeridir. | BOOLEAN | Hayır | Yok |
| `karakter_yönelimi` | Karakterin bakış yönünün/yöneliminin nereden geldiğini kontrol eder. `"video"`: hareketler, ifadeler, kamera hareketleri ve yönelim, hareket referans videosunu takip eder (diğer detaylar istem aracılığıyla). `"image"`: hareketler ve ifadeler hala hareket referans videosunu takip eder, ancak karakter yönelimi referans görüntüyle eşleşir (kamera/diğer detaylar istem aracılığıyla). | COMBO | Hayır | `"video"`<br>`"image"` |
| `mod` | Kullanılacak oluşturma modu. | COMBO | Hayır | `"pro"`<br>`"std"` |
| `model` | Kullanılacak Kling model sürümü. Varsayılan `"kling-v2-6"` değeridir. | COMBO | Hayır | `"kling-v3"`<br>`"kling-v2-6"` |

**Kısıtlamalar:**

* `character_orientation` `"video"` olarak ayarlandığında `reference_video` süresi 3 ila 30 saniye arasında olmalıdır.
* `character_orientation` `"image"` olarak ayarlandığında `reference_video` süresi 3 ila 10 saniye arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Karakterin referans videodaki hareketi gerçekleştirdiği oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingMotionControl/tr.md)

---
**Source fingerprint (SHA-256):** `4159b10496e85ae93f522865494e9bc99ba08bda00df1601bca2314e61fb32df`
