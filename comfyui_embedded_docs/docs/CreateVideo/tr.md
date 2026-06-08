Video Oluştur düğümü, bir dizi görüntüden video dosyası oluşturur. Saniyedeki kare sayısını kullanarak oynatma hızını belirleyebilir ve isteğe bağlı olarak videoya ses ekleyebilirsiniz. Düğüm, görüntülerinizi belirtilen kare hızında oynatılabilen bir video formatında birleştirir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntüler` | Video oluşturulacak görüntüler. | IMAGE | Evet | - |
| `fps` | Video oynatma hızı için saniyedeki kare sayısı (varsayılan: 30,0). | FLOAT | Evet | 1,0 - 120,0 |
| `ses` | Videoya eklenecek ses. | AUDIO | Hayır | - |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Giriş görüntülerini ve isteğe bağlı sesi içeren oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/tr.md)

---
**Source fingerprint (SHA-256):** `6da9a09542b5e357c0180c30018ec10facf06d1bdd3e4edee8172b8426802e3d`
