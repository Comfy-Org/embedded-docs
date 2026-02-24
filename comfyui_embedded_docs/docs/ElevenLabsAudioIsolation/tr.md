> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsAudioIsolation/tr.md)

ElevenLabs Ses İzolasyon düğümü, bir ses dosyasından arka plan gürültüsünü kaldırarak vokalleri veya konuşmayı izole eder. İşlem için sesi ElevenLabs API'sine gönderir ve temizlenmiş sesi döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Evet | | Arka plan gürültüsünün kaldırılması için işlenecek ses. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `audio` | AUDIO | Arka plan gürültüsü kaldırılmış işlenmiş ses. |