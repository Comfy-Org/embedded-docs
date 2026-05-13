> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentComposite/tr.md)

LatentComposite düğümü, iki gizli temsili tek bir çıktıda birleştirmek veya harmanlamak için tasarlanmıştır. Bu işlem, girdi gizli temsillerinin özelliklerini kontrollü bir şekilde birleştirerek kompozit görüntüler veya özellikler oluşturmak için gereklidir.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|--------------|-------------|-------------|
| `samples_to` | `LATENT` | 'samples_from' gizli temsilinin üzerine yerleştirileceği 'samples_to' gizli temsilidir. Kompozit işlemi için temel görevi görür. |
| `samples_from` | `LATENT` | 'samples_to' üzerine yerleştirilecek 'samples_from' gizli temsilidir. Nihai kompozit çıktıya kendi özelliklerini veya karakteristiklerini katar. |
| `x` | `INT` | 'samples_from' gizli temsilinin 'samples_to' üzerine yerleştirileceği x koordinatıdır (yatay konum). Kompozitin yatay hizalamasını belirler. |
| `y` | `INT` | 'samples_from' gizli temsilinin 'samples_to' üzerine yerleştirileceği y koordinatıdır (dikey konum). Kompozitin dikey hizalamasını belirler. |
| `feather` | `INT` | 'samples_from' gizli temsilinin, kompozit işleminden önce 'samples_to' ile eşleşecek şekilde yeniden boyutlandırılıp boyutlandırılmayacağını belirten bir boole değeridir. Bu, kompozit sonucunun ölçeğini ve oranını etkileyebilir. |

## Çıktılar

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `latent` | `LATENT` | Çıktı, hem 'samples_to' hem de 'samples_from' gizli temsillerinin özelliklerini belirtilen koordinatlara ve yeniden boyutlandırma seçeneğine göre harmanlayan bir kompozit gizli temsildir. |