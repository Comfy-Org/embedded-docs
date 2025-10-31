> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentRotate/tr.md)

LatentRotate düğümü, görüntülerin gizli temsillerini belirtilen açılarla döndürmek için tasarlanmıştır. Döndürme efektleri elde etmek için gizli uzayın manipülasyonunun karmaşıklığını soyutlar ve kullanıcıların bir üretken modelin gizli uzayındaki görüntüleri kolayca dönüştürmesine olanak tanır.

## Girdiler

| Parametre | Veri Tipi | Açıklama |
|-----------|-------------|-------------|
| `samples` | `LATENT`    | 'samples' parametresi, döndürülecek görüntülerin gizli temsillerini temsil eder. Döndürme işleminin başlangıç noktasını belirlemede çok önemlidir. |
| `rotation` | COMBO[STRING] | 'rotation' parametresi, gizli görüntülerin hangi açıyla döndürüleceğini belirtir. Ortaya çıkan görüntülerin yönelimi üzerinde doğrudan etkiye sahiptir. |

## Çıktılar

| Parametre | Veri Tipi | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Çıktı, girdi olarak verilen gizli temsillerin, belirtilen açıyla döndürülmüş halidir. |