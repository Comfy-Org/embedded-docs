# TopazImageEnhanceV2

Topaz Image Enhance, Topaz modellerini kullanarak tek bir girdi görüntüsüne endüstri standardı yükseltme (upscaling) ve görüntü iyileştirme uygular. Görüntüyü Topaz API'sine gönderir, seçilen modelle işler ve iyileştirilmiş sonucu döndürür. Üç model arasından seçim yapabilirsiniz: Reimagine, Bloom 2 ve Wonder 3.5.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Geliştirilecek girdi görüntüsü. Yalnızca bir girdi görüntüsü desteklenir. | IMAGE | Evet | Single image |
| `model` | Kullanılacak Topaz iyileştirme modeli. Seçilen model, hangi modele özgü ayarların görüneceğini belirler. | STRING | Evet | `"Reimagine"`<br>`"Bloom 2"`<br>`"Wonder 3.5"` |
| `output_width` | Sıfır değeri otomatik hesaplama anlamına gelir (genellikle orijinal boyut veya belirtilmişse `output_height` ile orantılı olarak ölçeklenir). Wonder 3.5 yalnızca 1x ile 6x arası büyütme faktörlerini destekler. Bloom 2 ve Wonder 3.5 girdi en-boy oranını korur ve istenen boyutu bir hedef olarak ele alır. (varsayılan: 0) | INT | Hayır | 0 to 32000 |
| `output_height` | Sıfır değeri, orijinal yükseklikte çıktı alma veya belirtilmişse `output_width` ile orantılı olarak ölçekleme anlamına gelir. Wonder 3.5 yalnızca 1x ile 6x arası büyütme faktörlerini destekler. Bloom 2 ve Wonder 3.5 girdi en-boy oranını korur ve istenen boyutu bir hedef olarak ele alır. (varsayılan: 0) | INT | Hayır | 0 to 32000 |

### Reimagine ayarları

Bu ayarlar, `model` `"Reimagine"` olarak ayarlandığında geçerlidir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Yaratıcı büyütme için isteğe bağlı metin istemi. (varsayılan: "") | STRING | Evet | Any text |
| `creativity` | İyileştirme için yaratıcılık seviyesi. (varsayılan: 3) | INT | Evet | 1 to 9 |
| `subject_detection` | Nesne algılama modu. | STRING | Evet | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `face_enhancement` | İşleme sırasında yüzleri (varsa) iyileştirir. (varsayılan: True) | BOOLEAN | Evet | true<br>false |
| `face_enhancement_creativity` | Yüz iyileştirme için yaratıcılık seviyesini ayarlar. (varsayılan: 0.0) | FLOAT | Evet | 0.0 to 1.0 |
| `face_enhancement_strength` | İyileştirilmiş yüzlerin arka plana göre ne kadar keskin olduğunu kontrol eder. (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |
| `face_preservation` | Kişilerin yüz kimliğini korur. (varsayılan: True) | BOOLEAN | Evet | true<br>false |
| `color_preservation` | Orijinal renkleri korur. (varsayılan: True) | BOOLEAN | Evet | true<br>false |
| `crop_to_fill` | Varsayılan olarak, çıktı en-boy oranı farklı olduğunda görüntüye mektup kutusu (letterbox) uygulanır. Görüntüyü kırpıp çıktı boyutlarını doldurmak için etkinleştirin. (varsayılan: False) | BOOLEAN | Evet | true<br>false |

### Bloom 2 ayarları

Bu ayarlar, `model` `"Bloom 2"` olarak ayarlandığında geçerlidir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Üretim için isteğe bağlı metin istemi. Boş bırakılırsa girdi görüntüsünden otomatik bir istem oluşturulur. (varsayılan: "") | STRING | Evet | Any text |
| `creativity` | 1 sınırlı iyileştirme, 9 yeni oluşturulmuş ayrıntılarla belirgin bir yeniden yorumlamadır. (varsayılan: 3) | INT | Evet | 1 to 9 |
| `seed` | Tekrarlanabilir üretim için tohum. (varsayılan: 2) | INT | Evet | 1 to 2000 |
| `color_preservation` | Orijinal renkleri korur. (varsayılan: True) | BOOLEAN | Evet | true<br>false |
| `grain` | Çıktı görüntüsüne gren (grain) ekler. (varsayılan: False) | BOOLEAN | Evet | true<br>false |
| `grain_model` | Kullanılacak gren modeli. Gren devre dışıysa yok sayılır. | STRING | Evet | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | Gren efektinin şiddeti. Gren devre dışıysa yok sayılır. (varsayılan: 0.5) | FLOAT | Evet | 0.0 to 1.0 |
| `grain_size` | Gren parçacıklarının boyutu. Gren devre dışıysa yok sayılır. (varsayılan: 1.0) | FLOAT | Evet | 1.0 to 5.0 |
| `grain_density` | Gren efektinin yoğunluğu. Gren devre dışıysa yok sayılır. (varsayılan: 0.5) | FLOAT | Evet | 0.0 to 1.0 |

### Wonder 3.5 ayarları

Bu ayarlar, `model` `"Wonder 3.5"` olarak ayarlandığında geçerlidir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `enhancement_strength` | Değişken girdi koşulları için iyileştirme seviyesi. (varsayılan: "high") | STRING | Evet | `"low"`<br>`"medium"`<br>`"high"` |
| `grain` | Çıktı görüntüsüne gren ekler. (varsayılan: False) | BOOLEAN | Evet | true<br>false |
| `grain_model` | Kullanılacak gren modeli. Gren devre dışıysa yok sayılır. | STRING | Evet | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | Gren efektinin şiddeti. Gren devre dışıysa yok sayılır. (varsayılan: 0.5) | FLOAT | Evet | 0.0 to 1.0 |
| `grain_size` | Gren parçacıklarının boyutu. Gren devre dışıysa yok sayılır. (varsayılan: 1.0) | FLOAT | Evet | 1.0 to 5.0 |
| `grain_density` | Gren efektinin yoğunluğu. Gren devre dışıysa yok sayılır. (varsayılan: 0.5) | FLOAT | Evet | 0.0 to 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Topaz API tarafından döndürülen iyileştirilmiş ve büyütülmüş görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhanceV2/tr.md)

---
**Source fingerprint (SHA-256):** `4301abb7cbab5122490b2ed3b328b199a29409da0dcc5ea5201570c2acbc2a58`
