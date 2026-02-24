> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingMotionControl/tr.md)

Kling Motion Control düğümü, bir referans videodaki hareketi, ifadeleri ve kamera hareketlerini, bir referans görseli ve metin istemiyle tanımlanan bir karaktere uygulayarak video oluşturur. Karakterin son yöneliminin referans videodan mı yoksa referans görselinden mi geleceğini kontrol etmenizi sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | Yok | İstenilen videonun metin açıklaması. Maksimum uzunluk 2500 karakterdir. |
| `reference_image` | IMAGE | Evet | Yok | Canlandırılacak karakterin bir görseli. Minimum boyutlar 340x340 pikseldir. En-boy oranı 1:2.5 ile 2.5:1 arasında olmalıdır. |
| `reference_video` | VIDEO | Evet | Yok | Karakterin hareketini ve ifadesini yönlendirmek için kullanılan bir hareket referans videosu. Minimum boyutlar 340x340 piksel, maksimum boyutlar 3850x3850 pikseldir. Süre sınırları `character_orientation` ayarına bağlıdır. |
| `keep_original_sound` | BOOLEAN | Hayır | Yok | Referans videosundaki orijinal sesin çıktıda korunup korunmayacağını belirler. Varsayılan değer `True`'dur. |
| `character_orientation` | COMBO | Hayır | `"video"`<br>`"image"` | Karakterin yöneliminin/baktığı yönün nereden geleceğini kontrol eder. `"video"`: hareketler, ifadeler, kamera hareketleri ve yönelim, hareket referans videosunu takip eder. `"image"`: hareketler ve ifadeler hareket referans videosunu takip eder, ancak karakterin yönelimi referans görseliyle eşleşir. |
| `mode` | COMBO | Hayır | `"pro"`<br>`"std"` | Kullanılacak oluşturma modu. |

**Kısıtlamalar:**

* `character_orientation` `"video"` olarak ayarlandığında, `reference_video` süresi 3 ile 30 saniye arasında olmalıdır.
* `character_orientation` `"image"` olarak ayarlandığında, `reference_video` süresi 3 ile 10 saniye arasında olmalıdır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Referans videodaki hareketi gerçekleştiren karakterin bulunduğu oluşturulmuş video. |
