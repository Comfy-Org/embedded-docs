# Kling Video Uzatma

ComfyUI Kling Video Uzatma Düğümü, diğer Kling düğümleri tarafından oluşturulan videoları uzatmanıza olanak tanır. Video kimliği ile tanımlanan mevcut bir videoyu alır ve metin istemlerinize dayanarak ek içerik oluşturur. Düğüm, uzatma isteğinizi Kling API'sine göndererek çalışır ve uzatılmış videoyu yeni kimliği ve süresiyle birlikte döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `istem` | Video uzatma işlemini yönlendiren olumlu metin istemi | STRING | Hayır | - |
| `negatif_istem` | Uzatılmış videoda kaçınılması gereken öğeler için olumsuz metin istemi | STRING | Hayır | - |
| `cfg_ölçeği` | İstem yönlendirmesinin gücünü kontrol eder (varsayılan: 0.5) | FLOAT | Hayır | 0.0 - 1.0 |
| `video_kimliği` | Uzatılacak videonun kimliği. Metinden videoya, görüntüden videoya ve önceki video uzatma işlemleri tarafından oluşturulan videoları destekler. Uzatma sonrası toplam süre 3 dakikayı aşamaz. | STRING | Evet | - |

**Not:** `video_id` diğer Kling düğümleri tarafından oluşturulmuş bir videoya referans vermelidir ve uzatma sonrası toplam süre 3 dakikayı aşamaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video_kimliği` | Kling API'si tarafından oluşturulan uzatılmış video | VIDEO |
| `video_kimliği` | Uzatılmış video için benzersiz tanımlayıcı | STRING |
| `süre` | Uzatılmış videonun süresi | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoExtendNode/tr.md)

---
**Source fingerprint (SHA-256):** `ecef4aedffe83bf384f2f9c3d8840f3fcab4b8c21e6e9afb36e177abb6f069fd`
