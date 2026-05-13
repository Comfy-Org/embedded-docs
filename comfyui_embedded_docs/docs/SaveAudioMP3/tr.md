> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioMP3/tr.md)

SaveAudioMP3 düğümü, ses verilerini MP3 dosyası olarak kaydeder. Ses girişini alır ve özelleştirilebilir dosya adı ve kalite ayarlarıyla belirtilen çıktı dizinine aktarır. Düğüm, oynatılabilir bir MP3 dosyası oluşturmak için dosya adlandırma ve format dönüşümünü otomatik olarak yönetir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `ses` | AUDIO | Evet | - | MP3 dosyası olarak kaydedilecek ses verisi |
| `dosya_adı_ön_eki` | STRING | Hayır | - | Çıktı dosya adı için ön ek (varsayılan: "audio/ComfyUI") |
| `kalite` | STRING | Hayır | "V0"<br>"128k"<br>"320k" | MP3 dosyası için ses kalite ayarı (varsayılan: "V0") |
| `prompt` | PROMPT | Hayır | - | Dahili istem verisi (sistem tarafından otomatik sağlanır) |
| `extra_pnginfo` | EXTRA_PNGINFO | Hayır | - | Ek PNG bilgisi (sistem tarafından otomatik sağlanır) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| *Yok* | - | Bu düğüm herhangi bir çıktı verisi döndürmez, ancak ses dosyasını çıktı dizinine kaydeder |

---
**Source fingerprint (SHA-256):** `70b960cc9c86ad9a4c98e643f40e6caaafdeb9840ac72a5f8e59533fd6120e3e`
