> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/tr.md)

## Genel Bakış

SamplerSASolver düğümü, difüzyon modelleri için özel bir örnekleme algoritması uygular. Giriş modelinden örnekler üretmek için yapılandırılabilir sıra ayarları ve stokastik diferansiyel denklem (SDE) parametreleriyle bir tahminci-düzeltici yaklaşımı kullanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Örnekleme için kullanılacak difüzyon modeli |
| `eta` | FLOAT | Hayır | 0.0 - 10.0 | Adım boyutu ölçekleme faktörünü kontrol eder (varsayılan: 1.0) |
| `sde_start_percent` | FLOAT | Hayır | 0.0 - 1.0 | SDE örneklemesi için başlangıç yüzdesi (varsayılan: 0.2) |
| `sde_end_percent` | FLOAT | Hayır | 0.0 - 1.0 | SDE örneklemesi için bitiş yüzdesi (varsayılan: 0.8) |
| `s_noise` | FLOAT | Hayır | 0.0 - 100.0 | Örnekleme sırasında eklenen gürültü miktarını kontrol eder (varsayılan: 1.0) |
| `predictor_order` | INT | Hayır | 1 - 6 | Çözücüdeki tahminci bileşeninin sırası (varsayılan: 3) |
| `corrector_order` | INT | Hayır | 0 - 6 | Çözücüdeki düzeltici bileşeninin sırası (varsayılan: 4) |
| `use_pece` | BOOLEAN | Hayır | - | PECE (Tahmin-Değerlendir-Düzelt-Değerlendir) yöntemini etkinleştirir veya devre dışı bırakır |
| `simple_order_2` | BOOLEAN | Hayır | - | Basitleştirilmiş ikinci derece hesaplamaları etkinleştirir veya devre dışı bırakır |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Difüzyon modelleriyle kullanılabilen yapılandırılmış bir örnekleyici nesnesi |

---
**Source fingerprint (SHA-256):** `3de8834281c09d0bd1435e29f0c9ae540a2ea42db142277d07cb655ccf814873`
