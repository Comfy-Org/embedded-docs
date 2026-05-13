> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceText/tr.md)

Metin Değiştir düğümü, basit bir metin değiştirme işlemi gerçekleştirir. Giriş metni içinde belirtilen bir metin parçasını arar ve her bulduğu yeri yeni bir metin parçasıyla değiştirir. Bu işlem, düğüme sağlanan tüm metin girdilerine uygulanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `text` | STRING | Evet | - | İşlenecek metin. |
| `find` | STRING | Evet | - | Bulunacak metin (varsayılan: boş dize). |
| `replace` | STRING | Evet | - | Değiştirilecek metin (varsayılan: boş dize). |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `text` | STRING | `find` metninin tüm geçtiği yerlerin `replace` metni ile değiştirildiği işlenmiş metin. |

---
**Source fingerprint (SHA-256):** `e9d4681e638c5ca2732ec254282243e9e9cdd01cc985af8bbfa41dea208cb7dd`
