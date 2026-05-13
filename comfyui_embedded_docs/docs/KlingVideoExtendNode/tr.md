> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoExtendNode/tr.md)

ComfyUI Kling Video Uzatma Düğümü, diğer Kling düğümleri tarafından oluşturulan videoları uzatmanıza olanak tanır. Video kimliği ile tanımlanan mevcut bir videoyu alır ve metin istemlerinize dayanarak ek içerik oluşturur. Düğüm, uzatma isteğinizi Kling API'sine göndererek çalışır ve uzatılmış videoyu yeni kimliği ve süresiyle birlikte döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Hayır | - | Video uzatma işlemini yönlendiren olumlu metin istemi |
| `negative_prompt` | STRING | Hayır | - | Uzatılmış videoda kaçınılması gereken öğeler için olumsuz metin istemi |
| `cfg_scale` | FLOAT | Hayır | 0.0 - 1.0 | İstem yönlendirmesinin gücünü kontrol eder (varsayılan: 0.5) |
| `video_id` | STRING | Evet | - | Uzatılacak videonun kimliği. Metinden videoya, görüntüden videoya ve önceki video uzatma işlemleri tarafından oluşturulan videoları destekler. Uzatma sonrası toplam süre 3 dakikayı aşamaz. |

**Not:** `video_id` diğer Kling düğümleri tarafından oluşturulmuş bir videoya referans vermelidir ve uzatma sonrası toplam süre 3 dakikayı aşamaz.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Kling API'si tarafından oluşturulan uzatılmış video |
| `video_id` | STRING | Uzatılmış video için benzersiz tanımlayıcı |
| `duration` | STRING | Uzatılmış videonun süresi |

---
**Source fingerprint (SHA-256):** `ecef4aedffe83bf384f2f9c3d8840f3fcab4b8c21e6e9afb36e177abb6f069fd`
