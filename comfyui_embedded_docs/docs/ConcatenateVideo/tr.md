# ConcatenateVideo

Birden çok video segmentini, bağlanma sırasını koruyarak tek bir videoda birleştirir. Uyumlu kodlanmış girdiler, kod çözülmeden birleştirilir ve orijinal sesin yerini alacak isteğe bağlı ayrı bir ses parçası sağlanabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `videos` | Girdi sırasına göre birleştirilecek video segmentleri. 1 ile 100 arasında video bağlayın; her video `video_1`, `video_2` vb. etiketli ayrı bir girdi yuvası olarak görünür. | VIDEO | Evet | 1 ile 100 segment |
| `codec` | Video tensörlerini kodlamak için kullanılan codec. Auto, H.264 kullanır; uyumlu, önceden kodlanmış girdiler değişmeden kalır. Varsayılan: "auto" | COMBO | Evet | `"auto"`<br>Diğer seçenekler kullanılabilir video codec türleri tarafından tanımlanır. |
| `complete_audio` | Birleştirilmiş video için isteğe bağlı tam ses parçası. Girdi videolarının taşıdığı sesin üzerine yazar. | AUDIO | Hayır | N/A |

**Not:** `videos` girdisi 1 ile 100 arasında video segmenti kabul eder. `complete_audio` sağlanırsa, tüm girdi videolarının sesinin yerini alır. `codec` "auto" olarak ayarlandığında, uyumlu kodlanmış girdiler kod çözülmeden birleştirilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Birleştirilmiş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConcatenateVideo/tr.md)

---
**Source fingerprint (SHA-256):** `f591aecb83754127e1c86ed0488548f9e7d99f3559c95a1c86c55fa5d430713d`
