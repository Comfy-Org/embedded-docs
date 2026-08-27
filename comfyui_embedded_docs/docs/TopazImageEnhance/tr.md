# Topaz Görüntü İyileştirme

Topaz Image Enhance düğümü, endüstri standardında büyütme (upscaling) ve görüntü iyileştirme sağlar. Bulut tabanlı bir yapay zeka modeli kullanarak tek bir girdi görüntüsünü işler; kaliteyi, detayı ve çözünürlüğü artırır. Düğüm; yaratıcı rehberlik, konu odağı ve yüz koruma seçenekleri dahil olmak üzere iyileştirme süreci üzerinde hassas kontrol sunar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Görüntü iyileştirme için kullanılacak yapay zeka modeli. | COMBO | Evet | `"Reimagine"` |
| `görüntü` | İyileştirilecek girdi görüntüsü. Yalnızca tek bir görüntü desteklenir. | IMAGE | Evet | - |
| `istem` | Yaratıcı büyütme rehberliği için isteğe bağlı metin istemi (varsayılan: boş). | STRING | Hayır | - |
| `konu_tespiti` | İyileştirmenin görüntünün hangi bölümüne odaklanacağını kontrol eder (varsayılan: "All"). | COMBO | Hayır | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `yüz_iyileştirme` | İşleme sırasında yüzleri (varsa) iyileştirir (varsayılan: True). | BOOLEAN | Hayır | - |
| `yüz_iyileştirme_yaratıcılığı` | Yüz iyileştirme için yaratıcılık seviyesini ayarlar (varsayılan: 0.0). | FLOAT | Hayır | 0.0 - 1.0 |
| `yüz_iyileştirme_gücü` | İyileştirilmiş yüzlerin arka plana göre ne kadar keskin olduğunu kontrol eder (varsayılan: 1.0). | FLOAT | Hayır | 0.0 - 1.0 |
| `doldurmak_için_kırp` | Varsayılan olarak, çıktı en-boy oranı farklı olduğunda görüntüye letterbox uygulanır. Görüntüyü çıktı boyutlarını dolduracak şekilde kırpmak için etkinleştirin (varsayılan: False). | BOOLEAN | Hayır | - |
| `çıktı_genişliği` | Sıfır değeri otomatik hesaplama anlamına gelir (genellikle orijinal boyut veya belirtilmişse `output_height` boyutu kullanılır) (varsayılan: 0). | INT | Hayır | 0 - 32000 |
| `çıktı_yüksekliği` | Sıfır değeri, orijinal görüntüyle aynı yükseklikte veya `output_width` ile aynı yükseklikte çıktı vermek anlamına gelir (varsayılan: 0). | INT | Hayır | 0 - 32000 |
| `yaratıcılık` | İyileştirmenin genel yaratıcılık seviyesini kontrol eder (varsayılan: 3). | INT | Hayır | 1 - 9 |
| `yüz_koruma` | Konuların yüz kimliğini korur (varsayılan: True). | BOOLEAN | Hayır | - |
| `renk_koruma` | Orijinal renkleri korur (varsayılan: True). | BOOLEAN | Hayır | - |

**Not:** Bu düğüm yalnızca tek bir girdi görüntüsünü işleyebilir. Birden fazla görüntü içeren bir grup (batch) sağlamak hataya neden olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | İyileştirilmiş çıktı görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/tr.md)

---
**Source fingerprint (SHA-256):** `1a0e708cdea9ec4f92f7f3aaabbdeea06a8fdab2f91a45ad2dea15f2bc2e8fa3`
