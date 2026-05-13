> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBlur/tr.md)

`ImageBlur` düğümü, bir görüntüye Gauss bulanıklığı uygulayarak kenarların yumuşatılmasını, detay ve gürültünün azaltılmasını sağlar. Parametreler aracılığıyla bulanıklığın yoğunluğu ve yayılımı üzerinde kontrol imkanı sunar.

## Girişler

| Alan           | Veri Türü | Açıklama                                                                 |
|----------------|-----------|--------------------------------------------------------------------------|
| `image`        | `IMAGE`   | Bulanıklaştırılacak giriş görüntüsü. Bulanıklık efektinin ana hedefidir. |
| `blur_radius`  | `INT`     | Bulanıklık efektinin yarıçapını belirler. Daha büyük bir yarıçap, daha belirgin bir bulanıklıkla sonuçlanır. |
| `sigma`        | `FLOAT`   | Bulanıklığın yayılımını kontrol eder. Daha yüksek bir sigma değeri, bulanıklığın her piksel etrafında daha geniş bir alanı etkileyeceği anlamına gelir. |

## Çıkışlar

| Alan   | Veri Türü | Açıklama                                                              |
|--------|-----------|--------------------------------------------------------------------------|
| `image`| `IMAGE`   | Çıktı, giriş parametreleri tarafından belirlenen bulanıklık derecesine sahip, giriş görüntüsünün bulanıklaştırılmış halidir. |