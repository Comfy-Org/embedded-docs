> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentImage/tr.md)

`EmptyLatentImage` düğümü, belirtilen boyutlarda ve toplu işlem sayısında boş bir gizli uzay temsili oluşturmak için tasarlanmıştır. Bu düğüm, görüntüleri gizli uzayda oluşturma veya işleme sürecinde temel bir adım olarak hizmet eder ve daha ileri düzey görüntü sentezi veya değiştirme işlemleri için bir başlangıç noktası sağlar.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `width`   | `INT`       | Oluşturulacak gizli görüntünün genişliğini belirtir. Bu parametre, elde edilen gizli temsilin uzamsal boyutlarını doğrudan etkiler. |
| `height`  | `INT`       | Oluşturulacak gizli görüntünün yüksekliğini belirler. Bu parametre, gizli uzay temsilinin uzamsal boyutlarını tanımlamak için çok önemlidir. |
| `batch_size` | `INT` | Tek bir toplu işlemde oluşturulacak gizli görüntü sayısını kontrol eder. Bu, aynı anda birden fazla gizli temsilin oluşturulmasına olanak tanıyarak toplu işlemeyi kolaylaştırır. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Çıktı, gizli uzayda daha ileri düzey görüntü oluşturma veya işleme için temel görevi gören bir dizi boş gizli görüntüyü temsil eden bir tensördür. |