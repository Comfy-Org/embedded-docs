> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/tr.md)

PreviewAudio düğümü, arayüzde görüntülenebilen geçici bir ses önizleme dosyası oluşturur. SaveAudio düğümünden türetilmiştir ancak dosyaları rastgele bir dosya adı öneki ile geçici bir dizine kaydeder. Bu, kullanıcıların kalıcı dosyalar oluşturmadan ses çıktılarını hızlıca önizlemesine olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `ses` | AUDIO | Evet | - | Önizlenecek ses verisi |
| `prompt` | PROMPT | Hayır | - | Dahili kullanım için gizli parametre |
| `extra_pnginfo` | EXTRA_PNGINFO | Hayır | - | Dahili kullanım için gizli parametre |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `ui` | UI | Ses önizlemesini arayüzde görüntüler |