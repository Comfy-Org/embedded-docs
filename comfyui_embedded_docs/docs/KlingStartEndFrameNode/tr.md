# Kling Başlangıç-Bitiş Karesinden Videoya

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

Kling Başlangıç-Bitiş Karesinden Video düğümü, sağladığınız başlangıç ve bitiş görselleri arasında geçiş yapan bir video dizisi oluşturur. İlk kareden son kareye kadar yumuşak bir dönüşüm üretmek için aradaki tüm kareleri oluşturur. Bu düğüm, görselden videoya API'sini çağırır ancak yalnızca `image_tail` istek alanıyla çalışan giriş seçeneklerini destekler.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `başlangıç_karesi` | Referans Görsel - URL veya Base64 kodlu dize, 10MB'ı geçemez, çözünürlük en az 300*300 piksel olmalıdır, en-boy oranı 1:2,5 ~ 2,5:1 arasında olmalıdır. Base64, data:image ön ekini içermemelidir. | IMAGE | Evet | - |
| `bitiş_karesi` | Referans Görsel - Bitiş karesi kontrolü. URL veya Base64 kodlu dize, 10MB'ı geçemez, çözünürlük en az 300*300 piksel olmalıdır. Base64, data:image ön ekini içermemelidir. | IMAGE | Evet | - |
| `istem` | Pozitif metin istemi | STRING | Evet | - |
| `negatif_istem` | Negatif metin istemi | STRING | Evet | - |
| `cfg_ölçeği` | İstem yönlendirmesinin gücünü kontrol eder (varsayılan: 0.5) | FLOAT | Hayır | 0.0-1.0 |
| `en_boy_oranı` | Oluşturulan video için en-boy oranı (varsayılan: "16:9") | COMBO | Hayır | "16:9"<br>"9:16"<br>"1:1" |
| `mod` | Video oluşturma için kullanılacak yapılandırma, şu formatta: mod / süre / model_adı. (varsayılan: mevcut modlardan yedinci seçenek) | COMBO | Hayır | Birden çok seçenek mevcut |

**Görsel Kısıtlamaları:**

- Hem `start_frame` hem de `end_frame` sağlanmalıdır ve dosya boyutu 10MB'ı geçemez
- Her iki görsel için minimum çözünürlük: 300×300 piksel
- `start_frame` en-boy oranı 1:2,5 ile 2,5:1 arasında olmalıdır
- Base64 kodlu görseller "data:image" ön ekini içermemelidir

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video_kimliği` | Oluşturulan video dizisi | VIDEO |
| `video_kimliği` | Oluşturulan video için benzersiz tanımlayıcı | STRING |
| `süre` | Oluşturulan videonun süresi | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/tr.md)

---
**Source fingerprint (SHA-256):** `1df5820b4f41ccd5afec8e2701888d90c940f164c433c7f81397b41e8fc333c6`
