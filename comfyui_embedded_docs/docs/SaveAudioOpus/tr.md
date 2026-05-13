> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/tr.md)

SaveAudioOpus düğümü, ses verilerini Opus formatında bir dosyaya kaydeder. Ses girişini alır ve yapılandırılabilir kalite ayarlarıyla sıkıştırılmış bir Opus dosyası olarak dışa aktarır. Düğüm, dosya adlandırmayı otomatik olarak yönetir ve çıktıyı belirlenen çıktı dizinine kaydeder.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `ses` | AUDIO | Evet | - | Opus dosyası olarak kaydedilecek ses verisi |
| `dosya_adı_ön_eki` | STRING | Hayır | - | Çıktı dosya adı için ön ek (varsayılan: "audio/ComfyUI") |
| `kalite` | COMBO | Hayır | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" | Opus dosyası için ses kalitesi ayarı (varsayılan: "128k") |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| - | - | Bu düğüm herhangi bir çıktı değeri döndürmez. Temel işlevi olarak ses dosyasını diske kaydeder. |

---
**Source fingerprint (SHA-256):** `87c3b1b85ca51b79d43c8486eeb2de7b074faa11c4da2bff7b8931a3049560e2`
