# Üstel Zamanlayıcı

`ExponentialScheduler` düğümü, difüzyon örnekleme süreçleri için üstel bir program izleyen bir sigma değerleri dizisi oluşturmak üzere tasarlanmıştır. Difüzyon sürecinin her adımında uygulanan gürültü seviyelerini kontrol etmek için özelleştirilebilir bir yaklaşım sunarak örnekleme davranışının ince ayarını yapmaya olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `adımlar` | Difüzyon sürecindeki adım sayısını belirtir. Oluşturulan sigma dizisinin uzunluğunu ve dolayısıyla gürültü uygulamasının ayrıntı düzeyini etkiler. | INT |
| `sigma_maks` | Maksimum sigma değerini tanımlayarak difüzyon sürecindeki gürültü yoğunluğunun üst sınırını belirler. Uygulanan gürültü seviyelerinin aralığının belirlenmesinde önemli bir rol oynar. | FLOAT |
| `sigma_min` | Minimum sigma değerini ayarlayarak gürültü yoğunluğunun alt sınırını oluşturur. Bu parametre, gürültü uygulamasının başlangıç noktasının ince ayarının yapılmasına yardımcı olur. | FLOAT |

## Çıktılar

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigmas` | Üstel programa göre oluşturulan bir sigma değerleri dizisi. Bu değerler, difüzyon sürecinin her adımında gürültü seviyelerini kontrol etmek için kullanılır. | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExponentialScheduler/tr.md)
