> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointSave/tr.md)

`Save Checkpoint` düğümü, eksiksiz bir Stable Diffusion modelini (UNet, CLIP ve VAE bileşenleri dahil) **.safetensors** formatında bir kontrol noktası dosyası olarak kaydetmek için tasarlanmıştır.

Save Checkpoint, öncelikle model birleştirme iş akışlarında kullanılır. `ModelMergeSimple`, `ModelMergeBlocks` gibi düğümler aracılığıyla yeni bir birleştirilmiş model oluşturduktan sonra, bu düğümü kullanarak sonucu yeniden kullanılabilir bir kontrol noktası dosyası olarak kaydedebilirsiniz.

## Girişler

| Parametre | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `model` | MODEL | Model parametresi, durumu kaydedilecek olan ana modeli temsil eder. Gelecekte geri yükleme veya analiz için modelin mevcut durumunu yakalamak açısından önemlidir. |
| `clip` | CLIP | Clip parametresi, ana modelle ilişkili CLIP modeli içindir ve durumunun ana modelle birlikte kaydedilmesini sağlar. |
| `vae` | VAE | Vae parametresi, Varyasyonel Otomatik Kodlayıcı (VAE) modeli içindir ve durumunun ana model ve CLIP ile birlikte gelecekte kullanım veya analiz için kaydedilmesini sağlar. |
| `dosyaadı_öneki` | STRING | Bu parametre, kontrol noktasının kaydedileceği dosya adı için ön eki belirtir. |

Ayrıca düğüm, meta veriler için iki gizli girişe sahiptir:

**prompt (PROMPT)**: İş akışı prompt bilgisi
**extra_pnginfo (EXTRA_PNGINFO)**: Ek PNG bilgisi

## Çıktılar

Bu düğüm bir kontrol noktası dosyası çıktısı verecektir ve ilgili çıktı dosyası yolu `output/checkpoints/` dizinidir.

## Mimari Uyumluluğu

- **Tam desteklenenler**: SDXL, SD3, SVD ve diğer ana akım mimariler. Bkz. [kaynak kod](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L176-L189)
- **Temel destek**: Diğer mimariler kaydedilebilir ancak standartlaştırılmış meta veri bilgisi içermez.

## İlgili Bağlantılar

İlgili kaynak kodu: [nodes_model_merging.py#L227](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L227)