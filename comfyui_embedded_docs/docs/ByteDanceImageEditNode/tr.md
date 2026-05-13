> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageEditNode/tr.md)

ByteDance Image Edit düğümü, ByteDance'in yapay zeka modellerini bir API aracılığıyla kullanarak görselleri değiştirmenize olanak tanır. Bir giriş görseli ve istenen değişiklikleri açıklayan bir metin istemi sağlarsınız; düğüm, görseli talimatlarınıza göre işler. Düğüm, API iletişimini otomatik olarak yönetir ve düzenlenmiş görseli döndürür.

## Girişler

| Parametre | Veri Türü | Giriş Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | seededit_3 | Image2ImageModelName seçenekleri | Model adı |
| `image` | GÖRSEL | GÖRSEL | - | - | Düzenlenecek temel görsel |
| `prompt` | METİN | METİN | "" | - | Görseli düzenleme talimatı |
| `seed` | TAMSAYI | TAMSAYI | 0 | 0-2147483647 | Üretim için kullanılacak tohum değeri |
| `guidance_scale` | ONDALIK | ONDALIK | 5.5 | 1.0-10.0 | Daha yüksek değer, görselin istemi daha yakından takip etmesini sağlar |
| `watermark` | MANTIKSAL | MANTIKSAL | True | - | Görsele "AI tarafından oluşturuldu" filigranı eklenip eklenmeyeceği |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `GÖRSEL` | GÖRSEL | ByteDance API'sinden döndürülen düzenlenmiş görsel |

---
**Source fingerprint (SHA-256):** `9dc13d89f84756b545120efb5535e08ada163d4534975809f5056bdf7d8bfb73`
