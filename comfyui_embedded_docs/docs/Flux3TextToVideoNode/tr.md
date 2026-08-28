# Flux 3 Metinden Videoya

FLUX 3 kullanarak metin isteminden (prompt) eş zamanlı ses içeren bir video üretir. Düğüm, isteminizi FLUX 3 hizmetine gönderir, üretimin tamamlanmasını bekler ve tamamlanan video klibini döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Ne istediğinizi sade bir dille ifade edin; istem, üretimden önce yorumlanır ve genişletilir. Katmanlı ses için ortam sesini, müziği ve konuşmayı ayrı ayrı tanımlayın. (varsayılan: "") | STRING | Evet | Çok satırlı metin |
| `aspect_ratio` | Çıktı en-boy oranı. 'auto', istemden ve girdilerden birini seçer. (varsayılan: "auto") | COMBO | Evet | `"auto"` dahil birden fazla seçenek mevcuttur |
| `duration` | Klibin saniye cinsinden uzunluğu. 'auto', uzunluğu içeriğe göre ayarlar. (varsayılan: "auto") | COMBO | Evet | `"auto"` dahil birden fazla seçenek mevcuttur |
| `resolution` | Çıktı çözünürlüğü. (varsayılan: "720p") | COMBO | Evet | `"720p"`<br>`"1080p"` |
| `generate_audio` | Eş zamanlı ses üret (ortam, konuşma, efektler). Kapalı olduğunda ses parçası olmayan bir video üretilir. (varsayılan: True) | BOOLEAN | Evet | True<br>False |
| `safety_tolerance` | İçerik denetimi toleransı; 0 en katı değerdir. Görsel veya video gönderen istekler, burada ne ayarlarsanız ayarlayın 2 ile sınırlandırılır. (varsayılan: 2) | INT | Evet | 0 ila 4 |
| `seed` | Düğümün yeniden çalışıp çalışmayacağını belirleyen tohum (seed); FLUX 3 kendi tohumunu seçtiğinden, bu değerden bağımsız olarak gerçek sonuçlar deterministik değildir. (varsayılan: 42) | INT | Evet | 0 ila 4294967295 |

Not: `seed` girdisi, arayüzde Control After Generate (Üretim Sonrası Kontrol) denetimlerini içerir. Görüntülenen fiyat, `resolution` ve `duration` değerlerine dayanır: HD (720p) için saniye başına $0.2431, FHD (1080p) için saniye başına $0.4147 ücretlendirilir. Sabit bir süre seçildiğinde klibin tahmini toplam maliyeti gösterilir; `duration` değeri "auto" olduğunda saniye başına ücret gösterilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Üretilen video klibi; `generate_audio` etkinleştirildiğinde eş zamanlı ses içerir. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3TextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `9957c78291c320b1a8a6a9c0edeefae5f1ccc21a6b58f0b39069c2df8decd100`
