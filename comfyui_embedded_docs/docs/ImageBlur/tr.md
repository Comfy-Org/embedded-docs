> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBlur/tr.md)

`ImageBlur` düğümü, bir görüntüye Gauss bulanıklığı uygulayarak kenarların yumuşatılmasını, detay ve gürültünün azaltılmasını sağlar. Bulanıklığın yoğunluğu ve yayılımı üzerinde parametreler aracılığıyla kontrol imkanı sunar.

## Girdiler

| Alan          | Veri Türü | Açıklama                                                                   |
|----------------|-------------|-------------------------------------------------------------------------------|
| `görüntü`        | `IMAGE`     | Bulanıklaştırılacak girdi görüntüsü. Bu, bulanıklık efektinin temel hedefidir. |
| `bulanıklık_yarıçapı`  | `INT`       | Bulanıklık efektinin yarıçapını belirler. Daha büyük bir yarıçap, daha belirgin bir bulanıklık ile sonuçlanır. |
| `sigma`        | `FLOAT`     | Bulanıklığın yayılımını kontrol eder. Daha yüksek bir sigma değeri, bulanıklığın her piksel etrafında daha geniş bir alanı etkileyeceği anlamına gelir. |

## Çıktılar

| Alan | Veri Türü | Açıklama                                                              |
|-------|-------------|--------------------------------------------------------------------------|
| `görüntü`| `IMAGE`     | Çıktı, girdi parametreleri tarafından belirlenen bulanıklık derecesine sahip, girdi görüntüsünün bulanıklaştırılmış halidir. |