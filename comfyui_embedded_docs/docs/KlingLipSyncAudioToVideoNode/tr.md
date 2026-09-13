# Kling Dudak Senkronizasyonu Video ile Ses

Kling Lip Sync Audio to Video Düğümü, bir video dosyasındaki ağız hareketlerini bir ses dosyasının ses içeriğiyle eşleşecek şekilde senkronize eder. Bu düğüm, sesteki vokal desenlerini analiz eder ve gerçekçi dudak senkronizasyonu oluşturmak için videodaki yüz hareketlerini ayarlar. Bu işlem, belirgin bir yüz içeren bir video ve açıkça ayırt edilebilir vokaller içeren bir ses dosyası gerektirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | Dudak senkronizasyonu yapılacak yüzü içeren video dosyası | VIDEO | Evet | - |
| `ses` | Video ile senkronize edilecek vokalleri içeren ses dosyası | AUDIO | Evet | - |
| `ses_dili` | Ses dosyasındaki sesin dili (varsayılan: "en") | COMBO | Evet | `"en"`<br>`"zh"`<br>`"es"`<br>`"fr"`<br>`"de"`<br>`"it"`<br>`"pt"`<br>`"pl"`<br>`"tr"`<br>`"ru"`<br>`"nl"`<br>`"cs"`<br>`"ar"`<br>`"ja"`<br>`"hu"`<br>`"ko"` |

**Önemli Kısıtlamalar:**

- Ses dosyası 5MB'den büyük olmamalıdır
- Video dosyası 100MB'den büyük olmamalıdır
- Video boyutları yükseklik/genişlik olarak 720px ile 1920px arasında olmalıdır
- Video süresi 2 saniye ile 10 saniye arasında olmalıdır
- Ses, açıkça ayırt edilebilir vokaller içermelidir
- Video, belirgin bir yüz içermelidir

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Dudak senkronize ağız hareketlerine sahip işlenmiş video | VIDEO |
| `video_id` | İşlenmiş video için benzersiz tanımlayıcı | STRING |
| `duration` | İşlenmiş videonun süresi | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncAudioToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `2f88af3191ac4f9c5c9fa1aaa5b744a12620b66e55a1fe0ab16b8b3b61110128`
