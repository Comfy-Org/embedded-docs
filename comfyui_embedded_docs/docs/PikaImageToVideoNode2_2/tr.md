Pika Görüntüden Videoya düğümü, bir video oluşturmak için Pika API sürüm 2.2'ye bir görüntü ve metin istemi gönderir. Sağlanan açıklama ve ayarlara dayanarak giriş görüntünüzü video formatına dönüştürür. Düğüm, API iletişimini yönetir ve oluşturulan videoyu çıktı olarak döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Videoya dönüştürülecek görüntü | IMAGE | Evet | - |
| `prompt_text` | Video oluşturmayı yönlendiren metin açıklaması | STRING | Evet | - |
| `negative_prompt` | Videoda kaçınılması gerekenleri açıklayan metin | STRING | Evet | - |
| `seed` | Tekrarlanabilir sonuçlar için rastgele tohum değeri | INT | Evet | - |
| `resolution` | Çıktı videosu çözünürlük ayarı | STRING | Evet | - |
| `duration` | Oluşturulan videonun saniye cinsinden uzunluğu | INT | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video dosyası | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaImageToVideoNode2_2/tr.md)

---
**Source fingerprint (SHA-256):** `aaa8dc49b94f0fae2010a3b61a3fb41e212fa9d2946a934a1a7c651fdced81b3`
