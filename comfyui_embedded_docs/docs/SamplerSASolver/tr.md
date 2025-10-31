> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/tr.md)

SamplerSASolver düğümü, difüzyon modelleri için özel bir örnekleme algoritması uygular. Girdi modelinden örnekler oluşturmak üzere yapılandırılabilir sıra ayarları ve stokastik diferansiyel denklem (SDE) parametreleri ile bir tahminci-düzeltici yaklaşımı kullanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Örnekleme için kullanılacak difüzyon modeli |
| `eta` | FLOAT | Evet | 0.0 - 10.0 | Adım boyutu ölçeklendirme faktörünü kontrol eder (varsayılan: 1.0) |
| `sde_start_percent` | FLOAT | Evet | 0.0 - 1.0 | SDE örneklemesi için başlangıç yüzdesi (varsayılan: 0.2) |
| `sde_end_percent` | FLOAT | Evet | 0.0 - 1.0 | SDE örneklemesi için bitiş yüzdesi (varsayılan: 0.8) |
| `s_noise` | FLOAT | Evet | 0.0 - 100.0 | Örnekleme sırasında eklenen gürültü miktarını kontrol eder (varsayılan: 1.0) |
| `predictor_order` | INT | Evet | 1 - 6 | Çözücüdeki tahminci bileşeninin sırası (varsayılan: 3) |
| `corrector_order` | INT | Evet | 0 - 6 | Çözücüdeki düzeltici bileşeninin sırası (varsayılan: 4) |
| `use_pece` | BOOLEAN | Evet | - | PECE (Tahmin Et-Değerlendir-Düzelt-Değerlendir) yöntemini etkinleştirir veya devre dışı bırakır |
| `simple_order_2` | BOOLEAN | Evet | - | Basitleştirilmiş ikinci derece hesaplamaları etkinleştirir veya devre dışı bırakır |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Difüzyon modelleri ile kullanılabilecek yapılandırılmış bir örnekleyici nesnesi |