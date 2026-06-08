`ImageBlur` düğümü, bir görüntüye Gauss bulanıklığı uygulayarak kenarların yumuşatılmasını, detay ve gürültünün azaltılmasını sağlar. Parametreler aracılığıyla bulanıklığın yoğunluğu ve yayılımı üzerinde kontrol imkanı sunar.

## Girişler

| Alan | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | Bulanıklaştırılacak giriş görüntüsü. Bulanıklık efektinin ana hedefidir. | `IMAGE` |
| `bulanıklık_yarıçapı` | Bulanıklık efektinin yarıçapını belirler. Daha büyük bir yarıçap, daha belirgin bir bulanıklıkla sonuçlanır. | `INT` |
| `sigma` | Bulanıklığın yayılımını kontrol eder. Daha yüksek bir sigma değeri, bulanıklığın her piksel etrafında daha geniş bir alanı etkileyeceği anlamına gelir. | `FLOAT` |

## Çıkışlar

| Alan | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | Çıktı, giriş parametreleri tarafından belirlenen bulanıklık derecesine sahip, giriş görüntüsünün bulanıklaştırılmış halidir. | `IMAGE` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBlur/tr.md)
