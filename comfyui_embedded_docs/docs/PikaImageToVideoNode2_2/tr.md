> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaImageToVideoNode2_2/tr.md)

Pika Görüntüden Videoya düğümü, bir video oluşturmak için Pika API sürüm 2.2'ye bir görüntü ve metin istemi gönderir. Sağlanan açıklama ve ayarlara dayanarak giriş görüntünüzü video formatına dönüştürür. Düğüm, API iletişimini yönetir ve oluşturulan videoyu çıktı olarak döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `image` | IMAGE | Evet | - | Videoya dönüştürülecek görüntü |
| `prompt_text` | STRING | Evet | - | Video oluşturmayı yönlendiren metin açıklaması |
| `negative_prompt` | STRING | Evet | - | Videoda kaçınılması gerekenleri açıklayan metin |
| `seed` | INT | Evet | - | Tekrarlanabilir sonuçlar için rastgele tohum değeri |
| `resolution` | STRING | Evet | - | Çıktı videosu çözünürlük ayarı |
| `duration` | INT | Evet | - | Oluşturulan videonun saniye cinsinden uzunluğu |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | VIDEO | Oluşturulan video dosyası |

---
**Source fingerprint (SHA-256):** `aaa8dc49b94f0fae2010a3b61a3fb41e212fa9d2946a934a1a7c651fdced81b3`
