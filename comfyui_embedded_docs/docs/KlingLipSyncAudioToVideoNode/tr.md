# Kling Dudak Senkronizasyonu Video ile Ses

ComfyUI düğüm belgelerini İngilizceden Türkçeye çevirmede uzmanlaşmış teknik çeviri uzmanısınız.

## Çeviri Kuralları

1. **Çevrilmemesi gereken içerik:**
   - Ters tırnak içindeki parametre adları: `image`, `seed`, `model`
   - BÜYÜK harflerle veri türleri: IMAGE, STRING, INT, FLOAT, MODEL, CONDITIONING, vb.
   - Range sütunundaki değerler: sayılar, "auto", seçenek adları
   - Kod, dosya yolları

2. **Çevrilmesi gereken içerik:**
   - Bölüm başlıkları: ## Genel Bakış, ## Girdiler, ## Çıktılar
   - Tüm açıklayıcı metinler
   - Parametre açıklamaları

3. **Çeviri kalitesi:**
   - Standart Türkçe kullanın
   - Profesyonel ama anlaşılır bir üslup koruyun
   - Teknik doğruluğu sağlayın
   - Standart Türkçe teknik terminolojiyi kullanın

4. **Format:**
   - Tüm Markdown biçimlendirmesini koruyun
   - Tablo yapısını koruyun
   - Belgenin başına herhangi bir not veya bağlantı eklemeyin (otomatik olarak eklenecektir)

Lütfen aşağıdaki belgeyi Türkçeye çevirin (belgenin başlangıç notunu dahil etmeyin):

Kling Lip Sync Audio to Video Node, bir video dosyasındaki ağız hareketlerini, bir ses dosyasının ses içeriğiyle eşleşecek şekilde senkronize eder. Bu düğüm, sesteki ses kalıplarını analiz eder ve gerçekçi dudak senkronizasyonu oluşturmak için videodaki yüz hareketlerini ayarlar. İşlem, belirgin bir yüz içeren bir video ve net bir şekilde ayırt edilebilir sesler içeren bir ses dosyası gerektirir.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `video` | Dudak senkronizasyonu yapılacak yüzü içeren video dosyası | VIDEO | Evet | - |
| `ses` | Video ile senkronize edilecek sesleri içeren ses dosyası | AUDIO | Evet | - |
| `ses_dili` | Ses dosyasındaki sesin dili (varsayılan: "en") | COMBO | Evet | `"en"`<br>`"zh"`<br>`"es"`<br>`"fr"`<br>`"de"`<br>`"it"`<br>`"pt"`<br>`"pl"`<br>`"tr"`<br>`"ru"`<br>`"nl"`<br>`"cs"`<br>`"ar"`<br>`"ja"`<br>`"hu"`<br>`"ko"` |

**Önemli Kısıtlamalar:**

- Ses dosyası 5MB'tan büyük olmamalıdır
- Video dosyası 100MB'tan büyük olmamalıdır
- Video boyutları yükseklik/genişlik olarak 720px ile 1920px arasında olmalıdır
- Video süresi 2 saniye ile 10 saniye arasında olmalıdır
- Ses, net bir şekilde ayırt edilebilir sesler içermelidir
- Video, belirgin bir yüz içermelidir

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video_kimliği` | Dudak senkronizasyonu yapılmış ağız hareketlerini içeren işlenmiş video | VIDEO |
| `süre` | İşlenmiş video için benzersiz tanımlayıcı | STRING |
| `duration` | İşlenmiş videonun süresi | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncAudioToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `92b8a7a4f9508632155a5f69707ffc4a14f2f44c04e4d01bf46476a972465592`
