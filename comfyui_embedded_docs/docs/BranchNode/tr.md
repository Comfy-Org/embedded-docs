# Branch

Branch, bağlı birkaç girdiden birini ada göre seçer ve çıktıya aktarır. Tembel bir anahtar gibi çalışır: yalnızca seçili dal değerlendirilir; böylece diğer dallar bağlantısız kalabilir veya hesaplanmasını istemediğiniz çıktıları tutabilir. Her yeni bağlantı yeni bir dal girdisi ekler, girdiler çift tıklanarak yeniden adlandırılabilir ve etkin dal `branch` seçicisinden seçilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `autogrow` | Bağlı dallar. Her bağlantı yeni bir dal girdisi ekler, en fazla 32'ye kadar; tüm dallar aynı veri türünü kullanmalıdır ve bu tür çıktı türü olur. | AUTOGROW | Evet | 1 ile 32 dal arası |
| `branch` | Çıktıya aktarılan dalın adı. Seçenekler bağlı dal girdilerinin adlarıdır ve bir girdi çift tıklanarak yeniden adlandırılabilir. | STRING | Evet | Bağlı dalların adları |
| `branch_names` | Bağlı dal adlarının dahili listesi; frontend tarafından eşitlenmiş tutulur. Seçili adı ilgili dala eşler ve elle düzenlenmemelidir. | ARRAY | Evet | - |

**Not:** Yalnızca seçili dal istenir; bu nedenle diğer dallar değerlendirilmez. Seçili ad bağlı değilse düğüm hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Seçili dalın değeri, değiştirilmeden aktarılır. | MATCH_TYPE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BranchNode/tr.md)

---
**Source fingerprint (SHA-256):** `2b4dca360c1b459a9f05eb54fedb7cdea6842fb0c606ee6f937ed00f715ee23a`
