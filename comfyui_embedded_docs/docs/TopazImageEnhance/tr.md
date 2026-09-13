# Topaz Görüntü İyileştirme

Topaz Image Enhance düğümü, endüstri standardında büyütme ve görüntü iyileştirme sağlar. Kaliteyi, ayrıntıyı ve çözünürlüğü artırmak için bulut tabanlı bir yapay zeka modeli kullanarak tek bir girdi görüntüsünü işler. Düğüm, yaratıcı yönlendirme, özne odağı ve yüz koruma seçenekleri dahil olmak üzere iyileştirme süreci üzerinde ince ayarlı kontrol sunar.

Bu düğüm eski bir sürümdür ve arayüzde kullanımdan kaldırılmış olarak işaretlenmiştir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Görüntü iyileştirme için kullanılacak yapay zeka modeli. | COMBO | Evet | `"Reimagine"` |
| `görüntü` | İyileştirilecek girdi görüntüsü. Yalnızca bir görüntü desteklenir. | IMAGE | Evet | - |
| `istem` | Yaratıcı büyütme yönlendirmesi için isteğe bağlı metin istemi (varsayılan: boş). | STRING | Hayır | - |
| `konu_tespiti` | İyileştirmenin görüntünün hangi bölümüne odaklanacağını kontrol eder (varsayılan: "All"). | COMBO | Hayır | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `yüz_iyileştirme` | İşleme sırasında yüzleri (varsa) iyileştirir (varsayılan: True). | BOOLEAN | Hayır | - |
| `yüz_iyileştirme_yaratıcılığı` | Yüz iyileştirme için yaratıcılık düzeyini ayarlar (varsayılan: 0.0). | FLOAT | Hayır | 0.0 - 1.0 |
| `yüz_iyileştirme_gücü` | İyileştirilmiş yüzlerin arka plana göre ne kadar keskin olacağını kontrol eder (varsayılan: 1.0). | FLOAT | Hayır | 0.0 - 1.0 |
| `doldurmak_için_kırp` | Varsayılan olarak, çıktı en-boy oranı farklı olduğunda görüntüye letterbox uygulanır. Görüntüyü çıktı boyutlarını dolduracak şekilde kırpmak için etkinleştirin (varsayılan: False). | BOOLEAN | Hayır | - |
| `çıktı_genişliği` | Sıfır değeri otomatik olarak hesaplanacağı anlamına gelir (genellikle özgün boyut veya belirtilmişse output_height olur) (varsayılan: 0). | INT | Hayır | 0 - 32000 |
| `çıktı_yüksekliği` | Sıfır değeri, özgün yükseklik veya çıktı genişliğiyle aynı yükseklikte çıktı vermek anlamına gelir (varsayılan: 0). | INT | Hayır | 0 - 32000 |
| `yaratıcılık` | İyileştirmenin genel yaratıcılık düzeyini kontrol eder (varsayılan: 3). | INT | Hayır | 1 - 9 |
| `yüz_koruma` | Öznelerin yüz kimliğini korur (varsayılan: True). | BOOLEAN | Hayır | - |
| `renk_koruma` | Orijinal renkleri korur (varsayılan: True). | BOOLEAN | Hayır | - |

**Not:** Bu düğüm yalnızca tek bir girdi görüntüsünü işleyebilir. Birden çok görüntüden oluşan bir toplu iş sağlamak hataya neden olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | İyileştirilmiş çıktı görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/tr.md)

---
**Source fingerprint (SHA-256):** `1a0e708cdea9ec4f92f7f3aaabbdeea06a8fdab2f91a45ad2dea15f2bc2e8fa3`
