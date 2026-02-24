> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/tr.md)

Topaz Image Enhance düğümü, sektör standardında yükseltme ve görüntü iyileştirme sağlar. Tek bir girdi görüntüsünü, kaliteyi, detayı ve çözünürlüğü iyileştirmek için bulut tabanlı bir AI modeli kullanarak işler. Düğüm, yaratıcı rehberlik, konu odaklama ve yüz koruma seçenekleri de dahil olmak üzere, iyileştirme süreci üzerinde ayrıntılı kontrol sunar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `"Reimagine"` | Görüntü iyileştirme için kullanılacak AI modeli. |
| `image` | IMAGE | Evet | - | İyileştirilecek girdi görüntüsü. Yalnızca tek bir görüntü desteklenir. |
| `prompt` | STRING | Hayır | - | Yaratıcı yükseltme rehberliği için isteğe bağlı bir metin istemi (varsayılan: boş). |
| `subject_detection` | COMBO | Hayır | `"All"`<br>`"Foreground"`<br>`"Background"` | İyileştirmenin görüntünün hangi kısmına odaklanacağını kontrol eder (varsayılan: "All"). |
| `face_enhancement` | BOOLEAN | Hayır | - | Görüntüde yüzler varsa onları iyileştirmek için etkinleştirin (varsayılan: True). |
| `face_enhancement_creativity` | FLOAT | Hayır | 0.0 - 1.0 | Yüz iyileştirme için yaratıcılık seviyesini ayarlar (varsayılan: 0.0). |
| `face_enhancement_strength` | FLOAT | Hayır | 0.0 - 1.0 | İyileştirilmiş yüzlerin arka plana göre ne kadar keskin olacağını kontrol eder (varsayılan: 1.0). |
| `crop_to_fill` | BOOLEAN | Hayır | - | Varsayılan olarak, çıktı en-boy oranı farklı olduğunda görüntüye siyah çubuklar eklenir. Bunun yerine görüntüyü çıktı boyutlarını dolduracak şekilde kırpmak için etkinleştirin (varsayılan: False). |
| `output_width` | INT | Hayır | 0 - 32000 | Çıktı görüntüsünün istenen genişliği. 0 değeri, genellikle orijinal boyuta veya belirtilmişse `output_height` değerine dayalı olarak otomatik hesaplanacağı anlamına gelir (varsayılan: 0). |
| `output_height` | INT | Hayır | 0 - 32000 | Çıktı görüntüsünün istenen yüksekliği. 0 değeri, genellikle orijinal boyuta veya belirtilmişse `output_width` değerine dayalı olarak otomatik hesaplanacağı anlamına gelir (varsayılan: 0). |
| `creativity` | INT | Hayır | 1 - 9 | İyileştirmenin genel yaratıcılık seviyesini kontrol eder (varsayılan: 3). |
| `face_preservation` | BOOLEAN | Hayır | - | Görüntüdeki öznelerin yüz kimliğini korur (varsayılan: True). |
| `color_preservation` | BOOLEAN | Hayır | - | Girdi görüntüsünün orijinal renklerini korur (varsayılan: True). |

**Not:** Bu düğüm yalnızca tek bir girdi görüntüsünü işleyebilir. Birden fazla görüntüden oluşan bir grup sağlamak hata ile sonuçlanacaktır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | İyileştirilmiş çıktı görüntüsü. |
