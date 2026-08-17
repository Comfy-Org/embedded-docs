# SamplerSASolver

SamplerSASolver düğümü, difüzyon modelleri için özel bir örnekleme algoritması uygular. Girdi modelinden örnekler üretmek için yapılandırılabilir mertebe ayarları ve stokastik diferansiyel denklem (SDE) parametreleriyle bir tahminci-düzeltici yaklaşımı kullanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Örnekleme için kullanılacak difüzyon modeli | MODEL | Evet | - |
| `eta` | Adım boyutu ölçekleme faktörünü kontrol eder (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 10.0 |
| `sde_start_percent` | SDE örneklemesinin başladığı gürültü giderme işleminin başlangıç yüzdesi; modelin örnekleme çizelgesi kullanılarak sigma değerine dönüştürülür (varsayılan: 0.2) | FLOAT | Hayır | 0.0 - 1.0 |
| `sde_end_percent` | SDE örneklemesinin durduğu gürültü giderme işleminin bitiş yüzdesi; modelin örnekleme çizelgesi kullanılarak sigma değerine dönüştürülür (varsayılan: 0.8) | FLOAT | Hayır | 0.0 - 1.0 |
| `s_noise` | Örnekleme sırasında eklenen gürültü miktarını kontrol eder (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 100.0 |
| `predictor_order` | Çözücüdeki tahminci bileşeninin mertebesi (varsayılan: 3) | INT | Hayır | 1 - 6 |
| `corrector_order` | Çözücüdeki düzeltici bileşeninin mertebesi (varsayılan: 4) | INT | Hayır | 0 - 6 |
| `use_pece` | PECE (Tahmin Et-Değerlendir-Düzelt-Değerlendir) yöntemini etkinleştirir veya devre dışı bırakır | BOOLEAN | Hayır | - |
| `simple_order_2` | Basitleştirilmiş ikinci mertebe hesaplamalarını etkinleştirir veya devre dışı bırakır | BOOLEAN | Hayır | - |

Not: `model` dışındaki tüm girdiler, düğümün arayüzünde varsayılan olarak gizlenen gelişmiş parametrelerdir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `sampler` | Difüzyon modelleriyle kullanılabilen yapılandırılmış bir örnekleyici nesnesi | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/tr.md)

---
**Source fingerprint (SHA-256):** `31da2d436665bf533c28b32248f632edab8f6d92372402904702ae954230f98d`
