> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioMerge/tr.md)

AudioMerge düğümü, iki ses parçasını dalga formlarını üst üste bindirerek birleştirir. Her iki ses girişinin örnekleme hızlarını otomatik olarak eşleştirir ve birleştirmeden önce uzunluklarını eşit olacak şekilde ayarlar. Düğüm, ses sinyallerini birleştirmek için çeşitli matematiksel yöntemler sunar ve çıktının kabul edilebilir ses seviyelerinde kalmasını sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `ses1` | AUDIO | Evet | - | Birleştirilecek ilk ses girişi |
| `ses2` | AUDIO | Evet | - | Birleştirilecek ikinci ses girişi |
| `merge_method` | COMBO | Evet | `"add"`<br>`"mean"`<br>`"subtract"`<br>`"multiply"` | Ses dalga formlarını birleştirmek için kullanılan yöntem. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `AUDIO` | AUDIO | Birleştirilmiş dalga formu ve örnekleme hızını içeren birleştirilmiş ses çıktısı |

---
**Source fingerprint (SHA-256):** `2a4a7da42835efd03cc67002e617a70c0514524a0ac0ed61d57e499c1283be95`
