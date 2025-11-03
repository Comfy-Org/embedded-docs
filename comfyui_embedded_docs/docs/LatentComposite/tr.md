> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentComposite/tr.md)

LatentComposite düğümü, iki gizli temsili birleştirmek veya tek bir çıktıda birleştirmek için tasarlanmıştır. Bu işlem, girdi gizli temsillerin özelliklerini kontrollü bir şekilde birleştirerek kompozit görüntüler veya özellikler oluşturmak için gereklidir.

## Girdiler

| Parametre    | Veri Türü | Açıklama |
|--------------|-------------|-------------|
| `hedef_örnekler` | `LATENT`    | 'samples_from'in üzerine yerleştirileceği temel gizli temsildir. Kompozit işlemi için taban görevi görür. |
| `kaynak_örnekler` | `LATENT` | 'samples_to' üzerine yerleştirilecek olan gizli temsildir. Özelliklerini veya karakterini nihai kompozit çıktıya katkıda bulunur. |
| `x`          | `INT`      | 'samples_from' gizli temsilinin 'samples_to' üzerinde yerleştirileceği x-koordinatı (yatay konum). Kompozitin yatay hizalamasını belirler. |
| `y`          | `INT`      | 'samples_from' gizli temsilinin 'samples_to' üzerinde yerleştirileceği y-koordinatı (dikey konum). Kompozitin dikey hizalamasını belirler. |
| `yumuşatma`    | `INT`      | 'samples_from' gizli temsilinin, kompozit işleminden önce 'samples_to' ile eşleşecek şekilde yeniden boyutlandırılıp boyutlandırılmayacağını belirten bir boole değeri. Bu, kompozit sonucunun ölçeğini ve oranını etkileyebilir. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | Çıktı, belirtilen koordinatlara ve yeniden boyutlandırma seçeneğine dayanarak hem 'samples_to' hem de 'samples_from' gizli temsillerinin özelliklerini harmanlayan bir kompozit gizli temsildir. |