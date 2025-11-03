> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointSave/tr.md)

`Save Checkpoint` düğümü, bir Stable Diffusion modelinin tamamını (UNet, CLIP ve VAE bileşenleri dahil) **.safetensors** formatında bir kontrol noktası dosyası olarak kaydetmek için tasarlanmıştır.

Save Checkpoint düğümü öncelikle model birleştirme iş akışlarında kullanılır. `ModelMergeSimple`, `ModelMergeBlocks` vb. düğümler aracılığıyla yeni bir birleştirilmiş model oluşturulduktan sonra, bu düğümü kullanarak sonucu yeniden kullanılabilir bir kontrol noktası dosyası olarak kaydedebilirsiniz.

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `model` | MODEL | model parametresi, durumu kaydedilecek olan birincil modeli temsil eder. Modelin mevcut durumunu gelecekteki geri yükleme veya analiz için yakalamak için gereklidir. |
| `clip` | CLIP | clip parametresi, birincil model ile ilişkili CLIP modeli içindir ve bu modelin durumunun ana modelle birlikte kaydedilmesine olanak tanır. |
| `vae` | VAE | vae parametresi, Varyasyonel Otokodlayıcı (VAE) modeli içindir; bu modelin durumunun ana model ve CLIP ile birlikte gelecekteki kullanım veya analiz için kaydedilmesini sağlar. |
| `dosyaadı_öneki` | STRING | Bu parametre, kontrol noktasının kaydedileceği dosya adı için ön eki belirtir. |

Ek olarak, düğümün meta veriler için iki gizli girdisi vardır:

**prompt (PROMPT)**: İş akışı prompt bilgisi
**extra_pnginfo (EXTRA_PNGINFO)**: Ek PNG bilgisi

## Çıktılar

Bu düğüm bir kontrol noktası dosyası çıktılayacaktır ve ilgili çıktı dosya yolu `output/checkpoints/` dizinidir.

## Mimari Uyumluluğu

- Şu anda tam desteklenenler: SDXL, SD3, SVD ve diğer ana akım mimariler, bkz. [kaynak kodu](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L176-L189)
- Temel destek: Diğer mimariler kaydedilebilir ancak standart meta veri bilgisi olmadan

## İlgili Bağlantılar

İlgili kaynak kodu: [nodes_model_merging.py#L227](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L227)