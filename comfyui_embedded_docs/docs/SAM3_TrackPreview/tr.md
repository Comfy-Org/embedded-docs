# SAM3 İz Önizleme

Lütfen aşağıdaki belgeyi Türkçeye çevirin (belgenin başlangıç notunu dahil etmeyin):

## Genel Bakış

Bu düğüm, izlenen nesnelerin bir video önizlemesini oluşturur; her izlenen nesneyi farklı bir renk katmanı ve bir numara etiketiyle çizer. Herhangi bir görüntü veya video tensörü çıktısı vermez — bunun yerine, ortaya çıkan önizleme videosunu doğrudan geçici bir dosyaya kaydeder.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `iz_verisi` | Bir SAM3 izleme düğümünden paketlenmiş maskeler ve nesne bilgilerini içeren izleme verileri. | TRACK_DATA | Evet | - |
| `görüntüler` | Önizleme için arka plan olarak kullanılacak isteğe bağlı giriş görüntüleri. Sağlanmazsa siyah bir arka plan kullanılır. | IMAGE | Hayır | - |
| `opaklık` | İzlenen nesnelere uygulanan renk katmanının opaklığı (varsayılan: 0,5). | FLOAT | Hayır | 0,0 ile 1,0 arası (adım: 0,05) |
| `fps` | Çıktı videosunun kare hızı (varsayılan: 24,0). | FLOAT | Hayır | 1,0 ile 120,0 arası (adım: 1,0) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `ui` | Oluşturulan önizleme videosunu görüntüleyen bir kullanıcı arayüzü öğesi. Herhangi bir tensör verisi döndürülmez. | PREVIEW_VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_TrackPreview/tr.md)

---
**Source fingerprint (SHA-256):** `8300d4fa89c7bbc481ac9a59868ede0e3c9413faa63d56c16a4f603ef878e877`
