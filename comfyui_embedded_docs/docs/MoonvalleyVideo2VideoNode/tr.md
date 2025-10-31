> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyVideo2VideoNode/tr.md)

Moonvalley Marey Video'dan Video'ya düğümü, bir giriş videosunu metin açıklamasına dayalı olarak yeni bir videoya dönüştürür. Orijinal videodan hareket veya poz özelliklerini korurken, sizin isteminizle eşleşen videolar oluşturmak için Moonvalley API'sini kullanır. Metin istemleri ve çeşitli oluşturma parametreleri aracılığıyla çıktı videosunun stilini ve içeriğini kontrol edebilirsiniz.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | - | Oluşturulacak videoyu tanımlar (çok satırlı giriş) |
| `negative_prompt` | STRING | Hayır | - | Olumsuz istem metni (varsayılan: kapsamlı olumsuz tanımlayıcı listesi) |
| `seed` | INT | Evet | 0-4294967295 | Rastgele tohum değeri (varsayılan: 9) |
| `video` | VIDEO | Evet | - | Çıktı videosunu oluşturmak için kullanılan referans videosu. En az 5 saniye uzunluğunda olmalıdır. 5 saniyeden uzun videolar otomatik olarak kırpılacaktır. Sadece MP4 formatı desteklenir. |
| `control_type` | COMBO | Hayır | "Motion Transfer"<br>"Pose Transfer" | Kontrol tipi seçimi (varsayılan: "Motion Transfer") |
| `motion_intensity` | INT | Hayır | 0-100 | Sadece control_type 'Motion Transfer' olduğunda kullanılır (varsayılan: 100) |
| `steps` | INT | Evet | 1-100 | Çıkarım adım sayısı (varsayılan: 33) |

**Not:** `motion_intensity` parametresi sadece `control_type` "Motion Transfer" olarak ayarlandığında uygulanır. "Pose Transfer" kullanılırken bu parametre dikkate alınmaz.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Oluşturulan video çıktısı |