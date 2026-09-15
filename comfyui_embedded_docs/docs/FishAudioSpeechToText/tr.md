# Fish Audio Konuşmadan Metne

Bu düğüm, Fish Audio konuşmadan metne hizmetini kullanarak sesi metne dönüştürür. Sesin dilini otomatik olarak algılar ve isteğe bağlı olarak JSON biçiminde kelime düzeyinde zaman damgalı segmentler döndürebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `ses` | Metne dönüştürülecek ses. | AUDIO | Evet | — |
| `dil` | ISO 639-1 dil ipucu (örn. 'en', 'zh'). Dil, ipucundan bağımsız olarak otomatik algılanır. Varsayılan: "" (boş dize). | STRING | Hayır | Herhangi bir ISO 639-1 dil kodu, örn. `en`, `zh`; otomatik algılama için boş dize |
| `precise_timestamps` | Kelime düzeyinde zaman damgalı segmentler döndürür. Varsayılan: false. | BOOLEAN | Hayır | true veya false |

Not: `language` parametresi yalnızca bir ipucudur — dil her zaman sesten otomatik olarak algılanır. `precise_timestamps` false (varsayılan) olduğunda, kelime düzeyinde zaman damgaları döndürülmez; true olduğunda, çıktı segmentleri kelime düzeyinde zaman damgaları içerir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `text` | Transkripsiyonu yapılan metin. | STRING |
| `language_code` | Ses için algılanan ISO 639-1 dil kodu. | STRING |
| `segments_json` | Transkripsiyon segmentlerini içeren JSON dizesi. `precise_timestamps` etkinleştirildiğinde kelime düzeyinde zaman damgalarını içerir. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioSpeechToText/tr.md)

---
**Source fingerprint (SHA-256):** `eaf1c9a9d2b90ec962a408615cc417b552864354c3f272144b8e239b23961920`
