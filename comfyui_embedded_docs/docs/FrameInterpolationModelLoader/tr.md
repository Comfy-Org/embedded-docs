> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolationModelLoader/tr.md)

Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme öneriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolationModelLoader/en.md)

## Genel Bakış

Bu düğüm, bir dosyadan kare enterpolasyon modeli yükler ve iş akışında kullanıma hazır hale getirir. Model türünü (FILM veya RIFE) otomatik olarak algılar ve modeli donanımınızda en iyi performans için yapılandırır.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `model_name` | STRING | Evet | `frame_interpolation` klasöründeki model dosyalarının listesi | Yüklenecek kare enterpolasyon modelini seçin. Modeller 'frame_interpolation' klasörüne yerleştirilmelidir. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `FRAME_INTERPOLATION_MODEL` | MODEL | Yüklenmiş ve yapılandırılmış, diğer düğümlerde kullanıma hazır kare enterpolasyon modeli. |