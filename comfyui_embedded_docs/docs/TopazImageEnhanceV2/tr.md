# Topaz Görüntü İyileştirme

Topaz Image Enhance, Topaz modellerini kullanarak tek bir giriş görüntüsüne endüstri standardı ölçek büyütme ve görüntü iyileştirme uygular. Görüntüyü Topaz API'sine gönderir, seçilen modelle işler ve iyileştirilmiş sonucu döndürür. Üç model arasından seçim yapabilirsiniz: Reimagine, Bloom 2 ve Wonder 3.5.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | İyileştirilecek giriş görüntüsü. Yalnızca bir giriş görüntüsü desteklenir. | IMAGE | Evet | Tek görüntü |
| `model` | Kullanılacak Topaz iyileştirme modeli. Seçilen model, hangi modele özgü ayarların görüneceğini belirler. | DYNAMIC_COMBO | Evet | `"Reimagine"`<br>`"Bloom 2"`<br>`"Wonder 3.5"` |
| `output_width` | Sıfır değeri otomatik olarak hesaplanacağı anlamına gelir (genellikle özgün boyut olur veya belirtilmişse `output_height` ile orantılı olarak ölçeklenir). Wonder 3.5 yalnızca 1x ile 6x arasındaki ölçek büyütme faktörlerini destekler. Bloom 2 ve Wonder 3.5 giriş en-boy oranını korur ve istenen boyutu hedef olarak değerlendirir. (varsayılan: 0) | INT | Hayır | 0 - 32000 |
| `output_height` | Sıfır değeri, özgün yükseklikle aynı yükseklikte çıktı vermek veya belirtilmişse `output_width` ile orantılı olarak ölçeklenmek anlamına gelir. Wonder 3.5 yalnızca 1x ile 6x arasındaki ölçek büyütme faktörlerini destekler. Bloom 2 ve Wonder 3.5 giriş en-boy oranını korur ve istenen boyutu hedef olarak değerlendirir. (varsayılan: 0) | INT | Hayır | 0 - 32000 |

### Reimagine Girdileri

Bu ayarlar `model` parametresi `"Reimagine"` olarak ayarlandığında geçerlidir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Yaratıcı ölçek büyütme yönlendirmesi için isteğe bağlı metin istemi. (varsayılan: "") | STRING | Evet | Herhangi bir metin |
| `creativity` | İyileştirme için yaratıcılık düzeyi. (varsayılan: 3) | INT | Evet | 1 - 9 |
| `subject_detection` | Konu algılama modu (gelişmiş). | COMBO | Evet | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `face_enhancement` | İşleme sırasında yüzleri (varsa) iyileştirir. (varsayılan: True) | BOOLEAN | Evet | true<br>false |
| `face_enhancement_creativity` | Yüz iyileştirme için yaratıcılık düzeyini ayarlar. (varsayılan: 0.0) | FLOAT | Evet | 0.0 - 1.0 |
| `face_enhancement_strength` | İyileştirilmiş yüzlerin arka plana göre ne kadar keskin olduğunu kontrol eder. (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 1.0 |
| `face_preservation` | Konuların yüz kimliğini korur. (varsayılan: True) | BOOLEAN | Evet | true<br>false |
| `color_preservation` | Özgün renkleri korur. (varsayılan: True) | BOOLEAN | Evet | true<br>false |
| `crop_to_fill` | Varsayılan olarak, çıktı en-boy oranı farklı olduğunda görüntüye letterbox uygulanır. Çıktı boyutlarını dolduracak şekilde görüntüyü kırpmak için etkinleştirin. (varsayılan: False) | BOOLEAN | Evet | true<br>false |

### Bloom 2 Girdileri

Bu ayarlar `model` parametresi `"Bloom 2"` olarak ayarlandığında geçerlidir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Üretim için isteğe bağlı metin istemi. Giriş görüntüsünden otomatik olarak istem oluşturmak için boş bırakın. (varsayılan: "") | STRING | Evet | Herhangi bir metin |
| `creativity` | 1 ölçülü iyileştirme, 9 yeni üretilmiş ayrıntılarla belirgin yeniden yorumlamadır. (varsayılan: 3) | INT | Evet | 1 - 9 |
| `seed` | Yeniden üretilebilir oluşturma için tohum. (varsayılan: 2) | INT | Evet | 1 - 2000 |
| `color_preservation` | Özgün renkleri korur. (varsayılan: True) | BOOLEAN | Evet | true<br>false |
| `grain` | Çıktı görüntüsüne gren ekler. (varsayılan: False) | BOOLEAN | Evet | true<br>false |
| `grain_model` | Kullanılacak gren modeli. `grain` devre dışıysa yok sayılır. | COMBO | Evet | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | Gren efektinin gücü. `grain` devre dışıysa yok sayılır. (varsayılan: 0.5) | FLOAT | Evet | 0.0 - 1.0 |
| `grain_size` | Gren parçacıklarının boyutu. `grain` devre dışıysa yok sayılır. (varsayılan: 1.0) | FLOAT | Evet | 1.0 - 5.0 |
| `grain_density` | Gren efektinin yoğunluğu. `grain` devre dışıysa yok sayılır. (varsayılan: 0.5) | FLOAT | Evet | 0.0 - 1.0 |

### Wonder 3.5 Girdileri

Bu ayarlar `model` parametresi `"Wonder 3.5"` olarak ayarlandığında geçerlidir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `enhancement_strength` | Değişen giriş koşulları için iyileştirme düzeyi. (varsayılan: "high") | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"` |
| `grain` | Çıktı görüntüsüne gren ekler. (varsayılan: False) | BOOLEAN | Evet | true<br>false |
| `grain_model` | Kullanılacak gren modeli. `grain` devre dışıysa yok sayılır. | COMBO | Evet | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | Gren efektinin gücü. `grain` devre dışıysa yok sayılır. (varsayılan: 0.5) | FLOAT | Evet | 0.0 - 1.0 |
| `grain_size` | Gren parçacıklarının boyutu. `grain` devre dışıysa yok sayılır. (varsayılan: 1.0) | FLOAT | Evet | 1.0 - 5.0 |
| `grain_density` | Gren efektinin yoğunluğu. `grain` devre dışıysa yok sayılır. (varsayılan: 0.5) | FLOAT | Evet | 0.0 - 1.0 |

**Not:** Yalnızca bir giriş görüntüsü desteklenir; giriş yığını birden fazla görüntü içeriyorsa düğüm hata verir. `grain` etkinleştirilmedikçe gren ayarları (`grain_model`, `grain_strength`, `grain_size`, `grain_density`) yok sayılır. Bloom 2 için `prompt` boş bırakılırsa giriş görüntüsünden otomatik olarak bir istem oluşturulur. Wonder 3.5 yalnızca 1x ile 6x arasındaki ölçek büyütme faktörlerini destekler; Bloom 2 ve Wonder 3.5 giriş en-boy oranını korur ve istenen boyutu hedef olarak değerlendirir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Topaz API tarafından döndürülen iyileştirilmiş ve ölçeklendirilmiş görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhanceV2/tr.md)

---
**Source fingerprint (SHA-256):** `19bb03ca7354f1b0d1e559b742b83939678fce6d5f490b1030717b846043e0e6`
