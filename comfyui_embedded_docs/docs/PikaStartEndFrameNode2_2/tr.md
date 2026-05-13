> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaStartEndFrameNode2_2/tr.md)

PikaFrames v2.2 Düğümü, ilk ve son karenizi birleştirerek bir video oluşturur. Başlangıç ve bitiş noktalarını tanımlamak için iki resim yüklersiniz ve yapay zeka, bunlar arasında yumuşak bir geçiş oluşturarak eksiksiz bir video üretir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `image_start` | IMAGE | Evet | - | Birleştirilecek ilk resim. |
| `image_end` | IMAGE | Evet | - | Birleştirilecek son resim. |
| `prompt_text` | STRING | Evet | - | İstenen video içeriğini tanımlayan metin istemi. |
| `negative_prompt` | STRING | Evet | - | Videoda kaçınılması gerekenleri tanımlayan metin. |
| `seed` | INT | Evet | - | Oluşturma tutarlılığı için rastgele tohum değeri. |
| `resolution` | STRING | Evet | - | Çıktı videosu çözünürlüğü. |
| `duration` | INT | Evet | - | Oluşturulan videonun süresi. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | VIDEO | Başlangıç ve bitiş karelerini yapay zeka geçişleriyle birleştiren oluşturulmuş video. |

---
**Source fingerprint (SHA-256):** `0a26f6db754c61d1f35e3fd9faceb631a8103ce9ff38190a5dd637991914e238`
