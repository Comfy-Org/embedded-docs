# SamplerSASolver

## Genel Bakış

SamplerSASolver düğümü, difüzyon modelleri için özel bir örnekleme algoritması uygular. Giriş modelinden örnekler üretmek için yapılandırılabilir sıra ayarları ve stokastik diferansiyel denklem (SDE) parametreleriyle bir tahminci-düzeltici yaklaşımı kullanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Örnekleme için kullanılacak difüzyon modeli | MODEL | Evet | - |
| `eta` | Adım boyutu ölçekleme faktörünü kontrol eder (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 10.0 |
| `sde_başlangıç_yüzdesi` | SDE örneklemesi için başlangıç yüzdesi (varsayılan: 0.2) | FLOAT | Hayır | 0.0 - 1.0 |
| `sde_bitiş_yüzdesi` | SDE örneklemesi için bitiş yüzdesi (varsayılan: 0.8) | FLOAT | Hayır | 0.0 - 1.0 |
| `s_gürültü` | Örnekleme sırasında eklenen gürültü miktarını kontrol eder (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 100.0 |
| `tahminci_sırası` | Çözücüdeki tahminci bileşeninin sırası (varsayılan: 3) | INT | Hayır | 1 - 6 |
| `düzeltici_sırası` | Çözücüdeki düzeltici bileşeninin sırası (varsayılan: 4) | INT | Hayır | 0 - 6 |
| `pece_kullan` | PECE (Tahmin-Değerlendir-Düzelt-Değerlendir) yöntemini etkinleştirir veya devre dışı bırakır | BOOLEAN | Hayır | - |
| `basit_sıra_2` | Basitleştirilmiş ikinci derece hesaplamaları etkinleştirir veya devre dışı bırakır | BOOLEAN | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sampler` | Difüzyon modelleriyle kullanılabilen yapılandırılmış bir örnekleyici nesnesi | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/tr.md)

---
**Source fingerprint (SHA-256):** `3de8834281c09d0bd1435e29f0c9ae540a2ea42db142277d07cb655ccf814873`
