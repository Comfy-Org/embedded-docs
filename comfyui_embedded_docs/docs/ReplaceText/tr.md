> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceText/tr.md)

Replace Text düğümü basit bir metin değiştirme işlemi gerçekleştirir. Girdi içinde belirtilen bir metin parçasını arar ve her bir geçtiği yeri yeni bir metin parçasıyla değiştirir. Bu işlem, düğüme sağlanan tüm metin girdilerine uygulanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `text` | STRING | Evet | - | İşlenecek metin. |
| `find` | STRING | Hayır | - | Bulunacak ve değiştirilecek metin (varsayılan: boş dize). |
| `replace` | STRING | Hayır | - | Bulunan metnin yerine konulacak metin (varsayılan: boş dize). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `text` | STRING | `find` metninin tüm geçtiği yerlerin `replace` metniyle değiştirildiği işlenmiş metin. |
