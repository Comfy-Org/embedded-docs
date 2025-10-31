> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncTextToVideoNode/tr.md)

Kling Lip Sync Text to Video Node, bir video dosyasındaki ağız hareketlerini bir metin istemine uyacak şekilde senkronize eder. Bir girdi videosu alır ve karakterin dudak hareketlerinin sağlanan metinle hizalandığı yeni bir video oluşturur. Düğüm, doğal görünümlü konuşma senkronizasyonu oluşturmak için ses sentezi kullanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Evet | - | Dudak senkronizasyonu için girdi video dosyası |
| `metin` | STRING | Evet | - | Dudak Senkronizasyonlu Video Üretimi için Metin İçeriği. Mod text2video olduğunda gereklidir. Maksimum uzunluk 120 karakterdir. |
| `ses` | COMBO | Hayır | "Melody"<br>"Bella"<br>"Aria"<br>"Ethan"<br>"Ryan"<br>"Dorothy"<br>"Nathan"<br>"Lily"<br>"Aaron"<br>"Emma"<br>"Grace"<br>"Henry"<br>"Isabella"<br>"James"<br>"Katherine"<br>"Liam"<br>"Mia"<br>"Noah"<br>"Olivia"<br>"Sophia" | Dudak senkronizasyonu sesi için ses seçimi (varsayılan: "Melody") |
| `ses_hızı` | FLOAT | Hayır | 0.8-2.0 | Konuşma Hızı. Geçerli aralık: 0.8~2.0, bir ondalık basamağa kadar hassas. (varsayılan: 1) |

**Video Gereksinimleri:**

- Video dosyası 100MB'tan büyük olmamalıdır
- Yükseklik/genişlik 720px ile 1920px arasında olmalıdır
- Süre 2s ile 10s arasında olmalıdır

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video_kimliği` | VIDEO | Dudak senkronizasyonlu ses ile oluşturulan video |
| `süre` | STRING | Oluşturulan video için benzersiz tanımlayıcı |
| `duration` | STRING | Oluşturulan video için süre bilgisi |