# Recraft Stil Oluştur

Bu belge, yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme öneriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCreateStyleNode/en.md)

Bu düğüm, referans görseller yükleyerek görüntü oluşturma için özel bir stil oluşturur. Yeni stili tanımlamak için 1 ila 5 arasında görsel yükleyebilirsiniz; düğüm, diğer Recraft düğümleriyle kullanılabilecek benzersiz bir stil kimliği döndürür. Yüklenen tüm görsellerin toplam dosya boyutu 5 MB'ı geçmemelidir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `stil` | Oluşturulan görsellerin temel stili. | STRING | Evet | `"realistic_image"`<br>`"digital_illustration"` |
| `görseller` | Özel stili oluşturmak için kullanılan 1 ila 5 referans görselden oluşan bir küme. | IMAGE | Evet | 1 ila 5 görsel |

**Not:** `images` girişindeki tüm görsellerin toplam dosya boyutu 5 MB'tan az olmalıdır. Bu sınır aşılırsa düğüm başarısız olur.

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `style_id` | Yeni oluşturulan özel stil için benzersiz tanımlayıcı. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCreateStyleNode/tr.md)

---
**Source fingerprint (SHA-256):** `36340e64d90b3edbbecedf15ac123adaabb5bc0c950183d2df6627dc873da61c`
