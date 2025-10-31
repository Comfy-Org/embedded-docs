> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncAudioToVideoNode/tr.md)

Kling Lip Sync Audio to Video Node, bir video dosyasındaki ağız hareketlerini bir ses dosyasının ses içeriğiyle senkronize eder. Bu düğüm, ses içindeki vokal kalıplarını analiz eder ve gerçekçi dudak senkronizasyonu oluşturmak için videodaki yüz hareketlerini ayarlar. Süreç, belirgin bir yüz içeren bir video ve net bir şekilde ayırt edilebilir vokallere sahip bir ses dosyası gerektirir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Evet | - | Dudak senkronizasyonu uygulanacak bir yüz içeren video dosyası |
| `audio` | AUDIO | Evet | - | Video ile senkronize edilecek vokaller içeren ses dosyası |
| `voice_language` | COMBO | Hayır | `"en"`<br>`"zh"`<br>`"es"`<br>`"fr"`<br>`"de"`<br>`"it"`<br>`"pt"`<br>`"pl"`<br>`"tr"`<br>`"ru"`<br>`"nl"`<br>`"cs"`<br>`"ar"`<br>`"ja"`<br>`"hu"`<br>`"ko"` | Ses dosyasındaki konuşmanın dili (varsayılan: "en") |

**Önemli Kısıtlamalar:**

- Ses dosyası 5MB'tan büyük olmamalıdır
- Video dosyası 100MB'tan büyük olmamalıdır
- Video boyutları yükseklik/genişlik olarak 720px ile 1920px arasında olmalıdır
- Video süresi 2 saniye ile 10 saniye arasında olmalıdır
- Ses, net bir şekilde ayırt edilebilir vokaller içermelidir
- Video, belirgin bir yüz içermelidir

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Dudak senkronizasyonu uygulanmış ağız hareketlerine sahip işlenmiş video |
| `video_id` | STRING | İşlenmiş video için benzersiz tanımlayıcı |
| `duration` | STRING | İşlenmiş videonun süresi |