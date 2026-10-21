# VEED Clean Audio (in Video)

VEED ile bir videodaki konuşmanın arka plan gürültüsünü kaldırın. Yalnızca ses parçası değişir: görüntü, çözünürlük ve kare hızı olduğu gibi kalırken ses parçası temizlenmiş 48 kHz mono konuşma ile değiştirilir. Her dildeki konuşma için tasarlanmıştır; müzik ve ses efektleri korunmak yerine kaldırılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `video` | Konuşma içeren bir ses parçasına sahip, 30 dakikadan kısa video. Videonun bir ses kanalı olmalıdır. | VIDEO | Evet | 1799 saniyeye kadar |
| `strength` | Konuşma altında ne kadar gürültünün kaldırılacağı. Daha düşük değer, sesin arkasında daha fazla ortam tonu bırakır; kelimeler arasındaki duraklamalar her zaman tamamen temizlenir ve varsayılanın üzerindeki değerler çok az değişiklik yapar. (varsayılan: 0.874) | FLOAT | Evet | 0.0 ila 1.0 (adım 0.001) |
| `loudness` | Konuşma ses yüksekliğinin normalleştirilip normalleştirilmeyeceği. `"normalize"`, bunu `target_lufs` değerine ayarlar; `"keep input level"` seviyeyi olduğu gibi bırakır. Bir seçenek belirlemek, parametrelerini gösterir. (varsayılan: `"normalize"`) | DYNAMIC_COMBO | Evet | `"normalize"`<br>`"keep input level"` |
| `target_lufs` | Temizlenmiş konuşmanın LUFS cinsinden entegre ses yüksekliği. Tepe değerler -1.1 dBTP ile sınırlandırılır, bu nedenle yüksek hedefler erken durur (tipik konuşma için yaklaşık -15 LUFS). `loudness` değeri `"normalize"` olduğunda kullanılabilir (varsayılan: -19.0). | FLOAT | Evet | -40.0 ila -8.0 (adım 0.1) |

Klip 1799 saniyeden uzun olduğunda ve videoda ses kanalı olmadığında düğüm hata vererek durur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `VIDEO` | Ses parçası temizlenmiş konuşma ile değiştirilmiş giriş videosu. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedCleanVideoAudioNode/tr.md)

---
**Source fingerprint (SHA-256):** `b8ff533f3ce45691cccd3449596252b0216178fdef0e7e728ccccbc9a8712217`
