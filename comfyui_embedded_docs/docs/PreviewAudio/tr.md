# Sesi Önizle

PreviewAudio düğümü, sesi ComfyUI çıktı dizinine kaydetmeden doğrudan arayüzde önizlemenize olanak tanır. Girdi olarak ses verisi alır ve sonucu dinlemek için kullanabileceğiniz bir ses oynatıcı bileşeni görüntüler. Girdi sesi None ise, düğüm bir hata verir; bu, kaynak videoda ses parçası olmadığında gerçekleşebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `audio` | Önizlenecek ses verisi. Ses None ise düğüm bir hata verir; bu, kaynak videoda ses parçası olmadığında gerçekleşebilir. | AUDIO | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `audio` | Düğümden geçirilen ses verisi. Sesi önizlemek için arayüzde bir ses oynatıcı bileşeni görüntülenir. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/tr.md)

---
**Source fingerprint (SHA-256):** `ccbf9873a16bf1578fe25d178454d782f4f9b37ad5721721bef0aee3ff374f9f`
