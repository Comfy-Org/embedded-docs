> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_TrackPreview/tr.md)

## Genel Bakış

Bu düğüm, izlenen nesnelerin bir video önizlemesini oluşturur; her izlenen nesneyi farklı bir renk katmanı ve bir numara etiketiyle çizer. Herhangi bir görüntü veya video tensörü çıktısı vermez; bunun yerine, ortaya çıkan önizleme videosunu doğrudan geçici bir dosyaya kaydeder.

## Girdiler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|---------|--------|-----------|
| `track_data` | TRACK_DATA | Evet | - | Bir SAM3 izleme düğümünden paketlenmiş maskeler ve nesne bilgilerini içeren izleme verileri. |
| `images` | IMAGE | Hayır | - | Önizleme için arka plan olarak kullanılacak isteğe bağlı giriş görüntüleri. Sağlanmazsa siyah bir arka plan kullanılır. |
| `opacity` | FLOAT | Hayır | 0.0 ile 1.0 arası (adım: 0.05) | İzlenen nesnelere uygulanan renk katmanının opaklığı (varsayılan: 0.5). |
| `fps` | FLOAT | Hayır | 1.0 ile 120.0 arası (adım: 1.0) | Çıktı videosunun kare hızı (varsayılan: 24.0). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-----------|
| `ui` | PREVIEW_VIDEO | Oluşturulan önizleme videosunu görüntüleyen bir kullanıcı arayüzü öğesi. Herhangi bir tensör verisi döndürülmez. |