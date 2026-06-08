AudioMerge düğümü, iki ses parçasını dalga formlarını üst üste bindirerek birleştirir. Her iki ses girişinin örnekleme hızlarını otomatik olarak eşleştirir ve birleştirmeden önce uzunluklarını eşit olacak şekilde ayarlar. Düğüm, ses sinyallerini birleştirmek için çeşitli matematiksel yöntemler sunar ve çıktının kabul edilebilir ses seviyelerinde kalmasını sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `ses1` | Birleştirilecek ilk ses girişi | AUDIO | Evet | - |
| `ses2` | Birleştirilecek ikinci ses girişi | AUDIO | Evet | - |
| `merge_method` | Ses dalga formlarını birleştirmek için kullanılan yöntem. | COMBO | Evet | `"add"`<br>`"mean"`<br>`"subtract"`<br>`"multiply"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `AUDIO` | Birleştirilmiş dalga formu ve örnekleme hızını içeren birleştirilmiş ses çıktısı | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioMerge/tr.md)

---
**Source fingerprint (SHA-256):** `2a4a7da42835efd03cc67002e617a70c0514524a0ac0ed61d57e499c1283be95`
