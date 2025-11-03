> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExponentialScheduler/tr.md)

`ExponentialScheduler` düğümü, difüzyon örnekleme süreçleri için üstel bir programa uygun bir sigma değerleri dizisi oluşturmak üzere tasarlanmıştır. Örnekleme davranışının hassas ayarını sağlamak amacıyla, difüzyon sürecinin her adımında uygulanan gürültü seviyelerini kontrol etmek için özelleştirilebilir bir yaklaşım sunar.

## Girdiler

| Parametre   | Veri Türü | Açıklama                                                                                   |
|-------------|-------------|---------------------------------------------------------------------------------------------|
| `adımlar`     | INT         | Difüzyon sürecindeki adım sayısını belirtir. Oluşturulan sigma dizisinin uzunluğunu ve dolayısıyla gürültü uygulamasının ayrıntı düzeyini etkiler. |
| `sigma_maks` | FLOAT       | Maksimum sigma değerini tanımlayarak difüzyon sürecindeki gürültü yoğunluğunun üst sınırını belirler. Uygulanan gürültü seviyelerinin aralığını belirlemede kritik bir rol oynar. |
| `sigma_min` | FLOAT       | Minimum sigma değerini ayarlayarak gürültü yoğunluğunun alt sınırını oluşturur. Bu parametre, gürültü uygulamasının başlangıç noktasının hassas ayarlanmasına yardımcı olur. |

## Çıktılar

| Parametre | Veri Türü | Açıklama                                                                                   |
|-----------|-------------|---------------------------------------------------------------------------------------------|
| `sigmas`  | SIGMAS      | Üstel programa göre oluşturulmuş bir sigma değerleri dizisi. Bu değerler, difüzyon sürecinin her adımındaki gürültü seviyelerini kontrol etmek için kullanılır. |