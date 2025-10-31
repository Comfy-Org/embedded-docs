> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentImage/tr.md)

`EmptyLatentImage` düğümü, belirtilen boyutlarda ve toplu işlem boyutunda boş bir gizli uzay temsili oluşturmak için tasarlanmıştır. Bu düğüm, gizli uzayda görüntü oluşturma veya manipülasyon işlemlerinde temel bir adım olarak hizmet eder ve daha sonraki görüntü sentezi veya değiştirme süreçleri için bir başlangıç noktası sağlar.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `width`   | `INT`       | Oluşturulacak gizli görüntünün genişliğini belirtir. Bu parametre, ortaya çıkan gizli temsilin uzamsal boyutlarını doğrudan etkiler. |
| `height`  | `INT`       | Oluşturulacak gizli görüntünün yüksekliğini belirler. Bu parametre, gizli uzay temsilinin uzamsal boyutlarını tanımlamak için çok önemlidir. |
| `batch_size` | `INT` | Tek bir toplu işlemde oluşturulacak gizli görüntü sayısını kontrol eder. Bu, toplu işlemeyi kolaylaştırarak birden fazla gizli temsilin aynı anda oluşturulmasına olanak tanır. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Çıktı, gizli uzayda daha fazla görüntü oluşturma veya manipülasyon için temel oluşturan bir dizi boş gizli görüntüyü temsil eden bir tensördür. |