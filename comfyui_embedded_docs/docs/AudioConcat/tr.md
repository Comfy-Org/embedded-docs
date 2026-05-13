> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioConcat/tr.md)

AudioConcat düğümü, iki ses girişini birleştirerek tek bir ses dosyası oluşturur. İki ses girişini alır ve belirttiğiniz sıraya göre, ikinci sesi birincinin önüne veya arkasına ekleyerek birleştirir. Düğüm, mono sesi stereo'ya dönüştürerek ve iki giriş arasındaki örnekleme hızlarını eşleştirerek farklı ses formatlarını otomatik olarak işler.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `audio1` | AUDIO | Evet | - | Birleştirilecek ilk ses girişi |
| `audio2` | AUDIO | Evet | - | Birleştirilecek ikinci ses girişi |
| `direction` | COMBO | Evet | `"after"`<br>`"before"` | audio2'nin audio1'den sonra mı yoksa önce mi ekleneceği (varsayılan: "after") |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `AUDIO` | AUDIO | Her iki ses giriş dosyasını da içeren birleştirilmiş ses |

---
**Source fingerprint (SHA-256):** `b54046e29761cf27bc5b1c065dac87846613afc0b5cbb296632628bf7d4527b7`
