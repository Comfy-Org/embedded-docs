> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyVideo2VideoNode/tr.md)

Moonvalley Marey Video'dan Video'ya düğümü, bir girdi videosunu metin açıklamasına dayalı olarak yeni bir videoya dönüştürür. Orijinal videodaki hareket veya poz özelliklerini korurken, isteminize uygun videolar oluşturmak için Moonvalley API'sini kullanır. Çıktı videosunun stilini ve içeriğini metin istemleri ve çeşitli oluşturma parametreleri aracılığıyla kontrol edebilirsiniz.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `prompt` | STRING | Evet | - | Oluşturulacak videoyu tanımlar (çok satırlı girdi) |
| `negative_prompt` | STRING | Hayır | - | Olumsuz istem metni (varsayılan: kapsamlı olumsuz tanımlayıcı listesi) |
| `seed` | INT | Evet | 0 ile 4294967295 arası | Rastgele tohum değeri (varsayılan: 9) |
| `video` | VIDEO | Evet | - | Çıktı videosunu oluşturmak için kullanılan referans videosu. En az 5 saniye uzunluğunda olmalıdır. 5 saniyeden uzun videolar otomatik olarak kırpılır. Yalnızca MP4 formatı desteklenir. |
| `control_type` | COMBO | Hayır | "Motion Transfer"<br>"Pose Transfer" | Kontrol türü seçimi (varsayılan: "Motion Transfer") |
| `motion_intensity` | INT | Hayır | 0 ile 100 arası | Yalnızca control_type "Motion Transfer" ise kullanılır (varsayılan: 100) |
| `steps` | INT | Evet | 1 ile 100 arası | Çıkarım adım sayısı (varsayılan: 33) |

**Not:** `motion_intensity` parametresi yalnızca `control_type` "Motion Transfer" olarak ayarlandığında uygulanır. "Pose Transfer" kullanıldığında bu parametre dikkate alınmaz.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | VIDEO | Oluşturulan video çıktısı |

---
**Source fingerprint (SHA-256):** `8202a4be469afa16d77b9e0287c290b9c3f390347fc60f23878f50fd95a758e0`
