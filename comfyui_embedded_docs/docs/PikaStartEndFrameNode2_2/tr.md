PikaFrames v2.2 Düğümü, ilk ve son karenizi birleştirerek bir video oluşturur. Başlangıç ve bitiş noktalarını tanımlamak için iki resim yüklersiniz ve yapay zeka, bunlar arasında yumuşak bir geçiş oluşturarak eksiksiz bir video üretir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `image_start` | Birleştirilecek ilk resim. | IMAGE | Evet | - |
| `image_end` | Birleştirilecek son resim. | IMAGE | Evet | - |
| `prompt_text` | İstenen video içeriğini tanımlayan metin istemi. | STRING | Evet | - |
| `negative_prompt` | Videoda kaçınılması gerekenleri tanımlayan metin. | STRING | Evet | - |
| `seed` | Oluşturma tutarlılığı için rastgele tohum değeri. | INT | Evet | - |
| `resolution` | Çıktı videosu çözünürlüğü. | STRING | Evet | - |
| `duration` | Oluşturulan videonun süresi. | INT | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Başlangıç ve bitiş karelerini yapay zeka geçişleriyle birleştiren oluşturulmuş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaStartEndFrameNode2_2/tr.md)

---
**Source fingerprint (SHA-256):** `0a26f6db754c61d1f35e3fd9faceb631a8103ce9ff38190a5dd637991914e238`
