> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingMotionControl/tr.md)

Kling Motion Control düğümü, referans bir görüntü ve metin istemiyle tanımlanan bir karaktere, referans bir videodaki hareket, ifade ve kamera hareketlerini uygulayarak bir video oluşturur. Karakterin nihai yönünün referans videodan mı yoksa referans görüntüden mi geleceğini kontrol etmenizi sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `istem` | STRING | Evet | Yok | İstenen videonun metin açıklaması. Maksimum uzunluk 2500 karakterdir. |
| `referans_görsel` | IMAGE | Evet | Yok | Canlandırılacak karakterin görüntüsü. Minimum boyutlar 340x340 pikseldir. En-boy oranı 1:2,5 ile 2,5:1 arasında olmalıdır. |
| `referans_video` | VIDEO | Evet | Yok | Karakterin hareketini ve ifadesini yönlendirmek için kullanılan bir hareket referans videosu. Minimum boyutlar 340x340 piksel, maksimum boyutlar 3850x3850 pikseldir. Süre sınırları `karakter_yönelimi` ayarına bağlıdır. |
| `orijinal_sesi_koru` | BOOLEAN | Hayır | Yok | Referans videodaki orijinal sesin çıktıda korunup korunmayacağını belirler. Varsayılan `True` değeridir. |
| `karakter_yönelimi` | COMBO | Hayır | `"video"`<br>`"image"` | Karakterin bakış yönünün/yöneliminin nereden geldiğini kontrol eder. `"video"`: hareketler, ifadeler, kamera hareketleri ve yönelim, hareket referans videosunu takip eder (diğer detaylar istem aracılığıyla). `"image"`: hareketler ve ifadeler hala hareket referans videosunu takip eder, ancak karakter yönelimi referans görüntüyle eşleşir (kamera/diğer detaylar istem aracılığıyla). |
| `mod` | COMBO | Hayır | `"pro"`<br>`"std"` | Kullanılacak oluşturma modu. |
| `model` | COMBO | Hayır | `"kling-v3"`<br>`"kling-v2-6"` | Kullanılacak Kling model sürümü. Varsayılan `"kling-v2-6"` değeridir. |

**Kısıtlamalar:**

* `character_orientation` `"video"` olarak ayarlandığında `reference_video` süresi 3 ila 30 saniye arasında olmalıdır.
* `character_orientation` `"image"` olarak ayarlandığında `reference_video` süresi 3 ila 10 saniye arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | VIDEO | Karakterin referans videodaki hareketi gerçekleştirdiği oluşturulan video. |

---
**Source fingerprint (SHA-256):** `4159b10496e85ae93f522865494e9bc99ba08bda00df1601bca2314e61fb32df`
