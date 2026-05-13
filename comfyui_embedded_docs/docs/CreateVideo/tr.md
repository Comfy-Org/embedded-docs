> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/tr.md)

Video Oluştur düğümü, bir dizi görüntüden video dosyası oluşturur. Saniyedeki kare sayısını kullanarak oynatma hızını belirleyebilir ve isteğe bağlı olarak videoya ses ekleyebilirsiniz. Düğüm, görüntülerinizi belirtilen kare hızında oynatılabilen bir video formatında birleştirir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `images` | IMAGE | Evet | - | Video oluşturulacak görüntüler. |
| `fps` | FLOAT | Evet | 1,0 - 120,0 | Video oynatma hızı için saniyedeki kare sayısı (varsayılan: 30,0). |
| `audio` | AUDIO | Hayır | - | Videoya eklenecek ses. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | VIDEO | Giriş görüntülerini ve isteğe bağlı sesi içeren oluşturulan video dosyası. |

---
**Source fingerprint (SHA-256):** `6da9a09542b5e357c0180c30018ec10facf06d1bdd3e4edee8172b8426802e3d`
