# RecraftStyleV3VectorIllustrationNode

Bu düğüm, Recraft API'si için bir stil seçer; özellikle vektör illüstrasyon stil kategorisini. Bu kategori içinde isteğe bağlı olarak daha belirli bir alt stil seçebilirsiniz. Düğüm, diğer Recraft düğümlerine aktarılabilecek bir stil yapılandırma nesnesi çıkarır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `substyle` | Vektör illüstrasyon kategorisi içinde daha belirli bir stil. Kullanılabilir seçenekler, Recraft API tarafından `vector_illustration` stili için tanımlanmış alt stillerdir. Eğer alt stil seçilmezse, temel `vector_illustration` stili kullanılır. | COMBO | Evet | Birden çok seçenek mevcuttur (`vector_illustration` stili için dinamik olarak yüklenen alt stil listesi) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `recraft_style` | Seçilen vektör illüstrasyon stilini ve isteğe bağlı alt stili içeren bir Recraft stil yapılandırma nesnesi. Bu, diğer Recraft düğümlerine bağlanabilir. | STYLEV3 |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3VectorIllustrationNode/tr.md)

---
**Source fingerprint (SHA-256):** `e88e7ea35b18acb55ec59814981cb36451d922d3287d23dcdb504289ea9f541b`
