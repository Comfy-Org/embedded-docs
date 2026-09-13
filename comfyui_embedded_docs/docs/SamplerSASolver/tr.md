# SamplerSASolver

The SamplerSASolver düğümü, difüzyon modelleri için özel bir örnekleyici oluşturur ve yapılandırır. Yapılandırılabilir bir tahmin edici-düzeltici şeması ve stokastik diferansiyel denklem (SDE) ayarlarıyla "sa_solver" örnekleme algoritmasını kullanır; bir örnekleme düğümüne takılabilecek bir örnekleyici nesnesi döndürür. `sde_start_percent` ve `sde_end_percent` değerleri, stokastik bileşenin uygulandığı aralığı tanımlamak için bağlı modelin örnekleme çizelgesi kullanılarak sigma değerlerine dönüştürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Örnekleyiciyi oluşturmak için örnekleme çizelgesi kullanılan difüzyon modeli | MODEL | Evet | - |
| `eta` | SDE çözücüsünün adım boyutu ölçekleme faktörünü kontrol eder (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 10.0 |
| `sde_start_percent` | Stokastik (SDE) bileşeninin başladığı örnekleme sürecinin başlangıç yüzdesi; modelin çizelgesi kullanılarak bir sigma değerine dönüştürülür (varsayılan: 0.2) | FLOAT | Hayır | 0.0 - 1.0 |
| `sde_end_percent` | Stokastik (SDE) bileşeninin durduğu örnekleme sürecinin bitiş yüzdesi; modelin çizelgesi kullanılarak bir sigma değerine dönüştürülür (varsayılan: 0.8) | FLOAT | Hayır | 0.0 - 1.0 |
| `s_noise` | Örnekleme sırasında eklenen gürültü miktarını kontrol eder (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 100.0 |
| `predictor_order` | Çözücüdeki tahmin edici bileşenin mertebesi (varsayılan: 3) | INT | Hayır | 1 - 6 |
| `corrector_order` | Çözücüdeki düzeltici bileşenin mertebesi (varsayılan: 4) | INT | Hayır | 0 - 6 |
| `use_pece` | PECE (Predict-Evaluate-Correct-Evaluate) yöntemini etkinleştirir (varsayılan: devre dışı) | BOOLEAN | Hayır | - |
| `simple_order_2` | Basitleştirilmiş ikinci mertebe hesaplamalarını etkinleştirir (varsayılan: devre dışı) | BOOLEAN | Hayır | - |

Tüm isteğe bağlı girdiler arayüzde gelişmiş olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sampler` | Örnekleme düğümleri tarafından kullanılabilecek, yapılandırılmış bir örnekleyici nesnesi (`sa_solver` algoritmasını kullanır) | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/tr.md)

---
**Source fingerprint (SHA-256):** `31da2d436665bf533c28b32248f632edab8f6d92372402904702ae954230f98d`
