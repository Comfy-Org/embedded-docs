SaveAudioOpus düğümü, ses verilerini Opus formatında bir dosyaya kaydeder. Ses girişini alır ve yapılandırılabilir kalite ayarlarıyla sıkıştırılmış bir Opus dosyası olarak dışa aktarır. Düğüm, dosya adlandırmayı otomatik olarak yönetir ve çıktıyı belirlenen çıktı dizinine kaydeder.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `ses` | Opus dosyası olarak kaydedilecek ses verisi | AUDIO | Evet | - |
| `dosya_adı_ön_eki` | Çıktı dosya adı için ön ek (varsayılan: "audio/ComfyUI") | STRING | Hayır | - |
| `kalite` | Opus dosyası için ses kalitesi ayarı (varsayılan: "128k") | COMBO | Hayır | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| - | Bu düğüm herhangi bir çıktı değeri döndürmez. Temel işlevi olarak ses dosyasını diske kaydeder. | - |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/tr.md)

---
**Source fingerprint (SHA-256):** `87c3b1b85ca51b79d43c8486eeb2de7b074faa11c4da2bff7b8931a3049560e2`
