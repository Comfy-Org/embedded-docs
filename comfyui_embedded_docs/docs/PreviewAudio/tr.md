# Sesi Önizle

Preview Audio düğümü, sesi ComfyUI çıktı dizinine kaydetmeden, arayüzde doğrudan oynatılabilen geçici bir ses önizlemesi oluşturur. Girdi olarak ses verisini alır ve bir önizleme widget'ı üretir; böylece kullanıcılar kalıcı dosyalar kaydetmeden ses çıktılarını dinleyebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `ses` | Önizlenecek ses verisi. Bu düğüm, girdi sesi None ise hata verir; bu durum, kaynak videonun ses parçası olmadığında meydana gelebilir. | AUDIO | Evet | - |

**Not:** Girdi `audio` None ise düğüm bir ValueError hatası fırlatır. Bu durum, kaynak videonun ses parçası olmadığında meydana gelebilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `audio` | Önizleme için kullanılan, girdiden geçirilen ses verisi. | AUDIO |
| `ui` | Arayüzde sesi önizlemek için bir ses oynatıcı widget'ı görüntüler. | UI |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/tr.md)

---
**Source fingerprint (SHA-256):** `ccbf9873a16bf1578fe25d178454d782f4f9b37ad5721721bef0aee3ff374f9f`
