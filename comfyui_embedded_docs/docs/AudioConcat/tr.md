AudioConcat düğümü, iki ses girişini birleştirerek tek bir ses dosyası oluşturur. İki ses girişini alır ve belirttiğiniz sıraya göre, ikinci sesi birincinin önüne veya arkasına ekleyerek birleştirir. Düğüm, mono sesi stereo'ya dönüştürerek ve iki giriş arasındaki örnekleme hızlarını eşleştirerek farklı ses formatlarını otomatik olarak işler.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `ses1` | Birleştirilecek ilk ses girişi | AUDIO | Evet | - |
| `ses2` | Birleştirilecek ikinci ses girişi | AUDIO | Evet | - |
| `direction` | audio2'nin audio1'den sonra mı yoksa önce mi ekleneceği (varsayılan: "after") | COMBO | Evet | `"after"`<br>`"before"` |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `AUDIO` | Her iki ses giriş dosyasını da içeren birleştirilmiş ses | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioConcat/tr.md)

---
**Source fingerprint (SHA-256):** `b54046e29761cf27bc5b1c065dac87846613afc0b5cbb296632628bf7d4527b7`
