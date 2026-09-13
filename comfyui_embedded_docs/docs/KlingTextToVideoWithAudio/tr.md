# Kling Metinden Videoya (Sesli)

Kling Text to Video with Audio düğümü, bir metin açıklamasından kısa bir video oluşturur. Kling AI hizmetine bir istek gönderir; hizmet istemi işler ve bir video dosyası döndürür. Düğüm ayrıca metne dayalı olarak video için eşlik eden ses de oluşturabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_name` | Video oluşturmak için kullanılacak belirli AI modeli. | COMBO | Evet | `"kling-v2-6"` |
| `prompt` | Pozitif metin istemi. Videoyu oluşturmak için kullanılan açıklama. 1 ile 2500 karakter arasında olmalıdır. | STRING | Evet | - |
| `mode` | Video oluşturma için çalışma modu. | COMBO | Evet | `"pro"` |
| `aspect_ratio` | Oluşturulan video için istenen genişlik-yükseklik oranı. | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | Videonun saniye cinsinden uzunluğu. | COMBO | Evet | `5`<br>`10` |
| `generate_audio` | Video için ses oluşturulup oluşturulmayacağını kontrol eder. Etkinleştirildiğinde, AI isteme dayalı olarak ses oluşturur (varsayılan: `True`). | BOOLEAN | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoWithAudio/tr.md)

---
**Source fingerprint (SHA-256):** `ddd2f3c1799abac067a05f3f5d6442ad4fe023d2f4f9afbde2894ca66854977e`
