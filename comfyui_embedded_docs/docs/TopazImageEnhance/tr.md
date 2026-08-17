# Topaz Görüntü İyileştirme

Topaz Image Enhance düğümü, endüstri standardı ölçekleme ve görüntü iyileştirme sağlar. Tek bir girdi görüntüsünü, kaliteyi, ayrıntıyı ve çözünürlüğü artırmak için bulut tabanlı bir yapay zeka modeli kullanarak işler. Düğüm; yaratıcı yönlendirme, özne odaklama ve yüz koruma seçenekleri dahil olmak üzere iyileştirme süreci üzerinde ayrıntılı kontrol sunar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Görüntü iyileştirme için kullanılacak yapay zeka modeli. | COMBO | Evet | `"Reimagine"` |
| `image` | İyileştirilecek girdi görüntüsü. Yalnızca tek bir görüntü desteklenir. | IMAGE | Evet | - |
| `prompt` | Yaratıcı ölçekleme yönlendirmesi için isteğe bağlı metin istemi (varsayılan: boş). | STRING | Hayır | - |
| `subject_detection` | İyileştirmenin görüntünün hangi bölümüne odaklanacağını kontrol eder (varsayılan: "All"). | COMBO | Hayır | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `face_enhancement` | İşleme sırasında varsa yüzleri iyileştirir (varsayılan: True). | BOOLEAN | Hayır | - |
| `face_enhancement_creativity` | Yüz iyileştirme için yaratıcılık düzeyini ayarlar (varsayılan: 0.0). | FLOAT | Hayır | 0.0 - 1.0 |
| `face_enhancement_strength` | İyileştirilmiş yüzlerin arka plana göre ne kadar keskin olduğunu kontrol eder (varsayılan: 1.0). | FLOAT | Hayır | 0.0 - 1.0 |
| `crop_to_fill` | Varsayılan olarak, çıktı en-boy oranı farklı olduğunda görüntü letterbox biçiminde (siyah bantlı) sunulur. Etkinleştirildiğinde, çıktı boyutlarını doldurmak için görüntüyü kırpar (varsayılan: False). | BOOLEAN | Hayır | - |
| `output_width` | Sıfır değeri otomatik hesaplanacağı anlamına gelir (genellikle orijinal boyut veya belirtilmişse output_height) (varsayılan: 0). | INT | Hayır | 0 - 32000 |
| `output_height` | Sıfır değeri, orijinalle aynı yükseklikte veya çıktı genişliğinde çıktı anlamına gelir (varsayılan: 0). | INT | Hayır | 0 - 32000 |
| `creativity` | İyileştirmenin genel yaratıcılık düzeyini kontrol eder (varsayılan: 3). | INT | Hayır | 1 - 9 |
| `face_preservation` | Öznelerin yüz kimliğini korur (varsayılan: True). | BOOLEAN | Hayır | - |
| `color_preservation` | Orijinal renkleri korur (varsayılan: True). | BOOLEAN | Hayır | - |

**Not:** Bu düğüm yalnızca tek bir girdi görüntüsünü işleyebilir. Birden fazla görüntü içeren bir grup sağlanması hataya neden olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | İyileştirilmiş çıktı görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/tr.md)

---
**Source fingerprint (SHA-256):** `a4b622ced661dd1dd1c57d4536359874d2203c8d4064c76fa684b9935e265085`
