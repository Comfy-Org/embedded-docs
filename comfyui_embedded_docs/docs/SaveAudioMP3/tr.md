SaveAudioMP3 düğümü, ses verilerini MP3 dosyası olarak kaydeder. Ses girişini alır ve özelleştirilebilir dosya adı ve kalite ayarlarıyla belirtilen çıktı dizinine aktarır. Düğüm, oynatılabilir bir MP3 dosyası oluşturmak için dosya adlandırma ve format dönüşümünü otomatik olarak yönetir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `ses` | MP3 dosyası olarak kaydedilecek ses verisi | AUDIO | Evet | - |
| `dosya_adı_ön_eki` | Çıktı dosya adı için ön ek (varsayılan: "audio/ComfyUI") | STRING | Hayır | - |
| `kalite` | MP3 dosyası için ses kalite ayarı (varsayılan: "V0") | STRING | Hayır | "V0"<br>"128k"<br>"320k" |
| `prompt` | Dahili istem verisi (sistem tarafından otomatik sağlanır) | PROMPT | Hayır | - |
| `extra_pnginfo` | Ek PNG bilgisi (sistem tarafından otomatik sağlanır) | EXTRA_PNGINFO | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| *Yok* | Bu düğüm herhangi bir çıktı verisi döndürmez, ancak ses dosyasını çıktı dizinine kaydeder | - |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioMP3/tr.md)

---
**Source fingerprint (SHA-256):** `70b960cc9c86ad9a4c98e643f40e6caaafdeb9840ac72a5f8e59533fd6120e3e`
