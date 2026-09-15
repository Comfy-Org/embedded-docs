# SheetSage2 Sesi ABC'ye Dönüştür

Bu düğüm, müzikteki vokal ve enstrümantal melodileri, müzikal partisyonları yazmak için metin tabanlı bir format olan ABC notasyonuna dönüştürür. Bağlı sesi analiz eder ve ortaya çıkan notasyonu metin olarak döndürür; bu metin daha sonra eşleşen mod kullanılarak YuE2 Generate Music düğümüne beslenebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `audio_encoder` | Sesi analiz etmek ve ABC notasyonunu üretmek için kullanılan ses kodlayıcı modeli. | AUDIO_ENCODER | Evet | - |
| `audio` | ABC notasyonuna dönüştürülecek müzik sesi. | AUDIO | Evet | - |
| `mode` | Neyin notaya döküleceğini kontrol eder. "full" melodi ve akorları üretir; "melody" yalnızca melodi üretir, cover'lar için önerilir. | COMBO | Evet | `"melody"`<br>`"full"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `abc` | ABC notasyonunda dönüştürülmüş müzik, bir string listesi olarak döndürülür. Bunu YuE2 Generate Music düğümüne bağlayın ve eşleşen modu kullanın. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SheetSage2AudioToABC/tr.md)

---
**Source fingerprint (SHA-256):** `612d18dedd09b64210087c340b8f304ace8cd7b30b1a6e8e8ba7c749b355a497`
