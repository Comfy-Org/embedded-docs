> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/tr.md)

**Node Function:** `Save Image` düğümü, temel olarak görüntüleri ComfyUI'daki **output** klasörüne kaydetmek için kullanılır. Ara işlem sırasında görüntüyü kaydetmek yerine yalnızca önizlemek istiyorsanız, `Preview Image` düğümünü kullanabilirsiniz.
Varsayılan kayıt konumu: `ComfyUI/output/`

## Girdiler

| Parametre | Veri Türü | Açıklama |
|-----------|-------------|-------------|
| `görüntüler` | `IMAGE` | Kaydedilecek görüntüler. Bu parametre, doğrudan işlenecek ve diske kaydedilecek görüntü verilerini içerdiği için çok önemlidir. |
| `dosyaadı_öneki` | STRING   | `ComfyUI/output/` klasörüne kaydedilen görüntüler için dosya adı öneki. Varsayılan değer `ComfyUI`'dır, ancak özelleştirebilirsiniz. |

## Sağ Tıklama Menü Seçenekleri

Görüntü oluşturma tamamlandıktan sonra, ilgili menüye sağ tıklamak aşağıdaki düğüme özel seçenekleri ve işlevleri sağlar:

| Seçenek Adı | İşlev |
|-------------|----------|
| `Save Image` | Görüntüyü yerel olarak kaydeder |
| `Copy Image` | Görüntüyü panoya kopyalar |
| `Open Image` | Görüntüyü yeni bir tarayıcı sekmesinde açar |

Kaydedilen görüntüler genellikle PNG formatındadır ve tüm görüntü oluşturma verilerini içerir. İlgili iş akışını yeniden oluşturmak için kullanmak isterseniz, ilgili görüntüyü ComfyUI'ya yükleyerek iş akışını yükleyebilirsiniz.