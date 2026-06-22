# Kling Görüntüden Videoya (Kamera Kontrolü)

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

Kling Görüntüden Videoya Kamera Kontrol Düğümü, hareketsiz görüntüleri profesyonel kamera hareketleriyle sinematik videolara dönüştürür. Bu özel görüntüden videoya düğümü, orijinal görüntünüze odaklanmayı korurken yakınlaştırma, döndürme, kaydırma, eğme ve birinci şahıs görüşü dahil olmak üzere sanal kamera eylemlerini kontrol etmenizi sağlar. Kamera kontrolü şu anda yalnızca kling-v1-5 modeliyle 5 saniyelik sürede pro modunda desteklenmektedir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `başlangıç_karesi` | Referans Görüntü - URL veya Base64 kodlanmış dize, 10MB'ı geçemez, çözünürlük 300x300 pikselden az olamaz, en boy oranı 1:2,5 ile 2,5:1 arasında olmalıdır. Base64, data:image önekini içermemelidir. | IMAGE | Evet | - |
| `istem` | İstenen video içeriğini tanımlayan olumlu metin istemi | STRING | Evet | - |
| `negatif_istem` | Oluşturulan videoda nelerden kaçınılacağını tanımlayan olumsuz metin istemi | STRING | Evet | - |
| `cfg_ölçeği` | Metin yönlendirmesinin gücünü kontrol eder. Daha yüksek değerler, çıktının istemi daha yakından takip etmesini sağlar (varsayılan: 0,75) | FLOAT | Hayır | 0,0 ile 1,0 |
| `en_boy_oranı` | Oluşturulan videonun en boy oranı (varsayılan: "16:9") | COMBO | Hayır | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `kamera_kontrolü` | Kling Kamera Kontrolleri düğümü kullanılarak oluşturulabilir. Video oluşturma sırasında kamera hareketini ve hareketliliği kontrol eder. | CAMERA_CONTROL | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video_kimliği` | Oluşturulan video çıktısı | VIDEO |
| `süre` | Oluşturulan video için benzersiz tanımlayıcı | STRING |
| `duration` | Oluşturulan videonun süresi | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlI2VNode/tr.md)

---
**Source fingerprint (SHA-256):** `a2965975cd484768298f4c7e504423f782ea032dfb5ef304579715be9c27cb79`
