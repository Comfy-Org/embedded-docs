The VAESave node is designed for saving VAE models along with their metadata, including prompts and additional PNG information, to a specified output directory. It encapsulates the functionality to serialize the model state and associated information into a file, facilitating the preservation and sharing of trained models.

## Girişler

| Parametre | Açıklama | Veri Türü |
| --- | --- | --- |
| `vae` | Kaydedilecek VAE modeli. Bu parametre, durumu serileştirilip depolanacak modeli temsil ettiği için kritik öneme sahiptir. | VAE |
| `dosyaadı_öneki` | Modelin ve meta verilerinin kaydedileceği dosya adı için bir ön ek. Bu, düzenli depolama ve modellerin kolayca bulunmasını sağlar. | STRING |

## Çıktılar

Düğümün çıktı türü bulunmamaktadır.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAESave/tr.md)
