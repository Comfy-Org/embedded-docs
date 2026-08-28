# Topaz Görüntü İyileştirme

### Girdiler

#### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | İyileştirilecek girdi görüntüsü. Yalnızca bir girdi görüntüsü desteklenir. | IMAGE | Evet | Tek görüntü |
| `model` | Kullanılacak Topaz iyileştirme modeli. Seçilen model, hangi modele özel ayarların görüneceğini belirler. | DYNAMIC_COMBO | Evet | `"Reimagine"`<br>`"Bloom 2"`<br>`"Wonder 3.5"` |
| `output_width` | Sıfır değeri otomatik hesaplama anlamına gelir (genellikle orijinal boyut olur veya `output_height` belirtilmişse orantılı olarak ölçeklenir). Wonder 3.5 yalnızca 1x ila 6x arası büyütme faktörlerini destekler. Bloom 2 ve Wonder 3.5 girdi en-boy oranını korur ve istenen boyutu hedef olarak ele alır. (varsayılan: 0) | INT | Hayır | 0 ila 32000 |
| `output_height` | Sıfır değeri, orijinalle aynı yükseklikte çıktı vermek anlamına gelir veya `output_width` belirtilmişse orantılı olarak ölçeklenir. Wonder 3.5 yalnızca 1x ila 6x arası büyütme faktörlerini destekler. Bloom 2 ve Wonder 3.5 girdi en-boy oranını korur ve istenen boyutu hedef olarak ele alır. (varsayılan: 0) | INT | Hayır | 0 ila 32000 |

#### Reimagine Girdileri

Bu ayarlar, `model` `"Reimagine"` olarak ayarlandığında geçerlidir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Yaratıcı büyütme için isteğe bağlı metin istemi. (varsayılan: "") | STRING | Evet | Herhangi bir metin |
| `creativity` | İyileştirme için yaratıcılık düzeyi. (varsayılan: 3) | INT | Evet | 1 ila 9 |
| `subject_detection` | Özne algılama modu. | COMBO | Evet | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `face_enhancement` | İşleme sırasında yüzleri (varsa) iyileştir. (varsayılan: True) | BOOLEAN | Evet | true<br>false |
| `face_enhancement_creativity` | Yüz iyileştirme için yaratıcılık düzeyini ayarlar. (varsayılan: 0.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `face_enhancement_strength` | İyileştirilmiş yüzlerin arka plana göre ne kadar keskin olduğunu kontrol eder. (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `face_preservation` | Öznelerin yüz kimliğini korur. (varsayılan: True) | BOOLEAN | Evet | true<br>false |
| `color_preservation` | Orijinal renkleri korur. (varsayılan: True) | BOOLEAN | Evet | true<br>false |
| `crop_to_fill` | Varsayılan olarak, çıktı en-boy oranı farklı olduğunda görüntüye letterbox uygulanır. Etkinleştirildiğinde, çıktı boyutlarını doldurmak için görüntü kırpılır. (varsayılan: False) | BOOLEAN | Evet | true<br>false |

#### Bloom 2 Girdileri

Bu ayarlar, `model` `"Bloom 2"` olarak ayarlandığında geçerlidir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Üretim için isteğe bağlı metin istemi. Girdi görüntüsünden otomatik bir istem oluşturmak için boş bırakın. (varsayılan: "") | STRING | Evet | Herhangi bir metin |
| `creativity` | 1 ölçülü iyileştirme, 9 yeni oluşturulan ayrıntılarla belirgin yeniden yorumlamadır. (varsayılan: 3) | INT | Evet | 1 ila 9 |
| `seed` | Tekrarlanabilir üretim için tohum değeri. (varsayılan: 2) | INT | Evet | 1 ila 2000 |
| `color_preservation` | Orijinal renkleri korur. (varsayılan: True) | BOOLEAN | Evet | true<br>false |
| `grain` | Çıktı görüntüsüne gren ekler. (varsayılan: False) | BOOLEAN | Evet | true<br>false |
| `grain_model` | Kullanılacak gren modeli. Gren devre dışıysa yok sayılır. | COMBO | Evet | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | Gren efektinin gücü. Gren devre dışıysa yok sayılır. (varsayılan: 0.5) | FLOAT | Evet | 0.0 ila 1.0 |
| `grain_size` | Gren parçacıklarının boyutu. Gren devre dışıysa yok sayılır. (varsayılan: 1.0) | FLOAT | Evet | 1.0 ila 5.0 |
| `grain_density` | Gren efektinin yoğunluğu. Gren devre dışıysa yok sayılır. (varsayılan: 0.5) | FLOAT | Evet | 0.0 ila 1.0 |

#### Wonder 3.5 Girdileri

Bu ayarlar, `model` `"Wonder 3.5"` olarak ayarlandığında geçerlidir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `enhancement_strength` | Değişen girdi koşulları için iyileştirme düzeyi. (varsayılan: "high") | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"` |
| `grain` | Çıktı görüntüsüne gren ekler. (varsayılan: False) | BOOLEAN | Evet | true<br>false |
| `grain_model` | Kullanılacak gren modeli. Gren devre dışıysa yok sayılır. | COMBO | Evet | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | Gren efektinin gücü. Gren devre dışıysa yok sayılır. (varsayılan: 0.5) | FLOAT | Evet | 0.0 ila 1.0 |
| `grain_size` | Gren parçacıklarının boyutu. Gren devre dışıysa yok sayılır. (varsayılan: 1.0) | FLOAT | Evet | 1.0 ila 5.0 |
| `grain_density` | Gren efektinin yoğunluğu. Gren devre dışıysa yok sayılır. (varsayılan: 0.5) | FLOAT | Evet | 0.0 ila 1.0 |

**Not:** Yalnızca bir girdi görüntüsü desteklenir. `grain` etkinleştirilmediği sürece gren ayarları (`grain_model`, `grain_strength`, `grain_size`, `grain_density`) yok sayılır. Bloom 2 için `prompt` boş bırakılırsa girdi görüntüsünden otomatik olarak bir istem oluşturulur. Wonder 3.5 yalnızca 1x ila 6x arası büyütme faktörlerini destekler; Bloom 2 ve Wonder 3.5 girdi en-boy oranını korur ve istenen boyutu hedef olarak ele alır.

### Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Topaz API'si tarafından döndürülen iyileştirilmiş ve büyütülmüş görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhanceV2/tr.md)

---
**Source fingerprint (SHA-256):** `19bb03ca7354f1b0d1e559b742b83939678fce6d5f490b1030717b846043e0e6`
