> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DTextureEditNode/tr.md)

Bu düğüm, bir 3B modelin dokularını düzenlemek için Tencent Hunyuan3D API'sini kullanır. Bir 3B model ve istenen değişikliklerin metin açıklamasını sağlarsınız; düğüm de, verdiğiniz komuta göre dokuları yeniden çizilmiş yeni bir model sürümünü döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model_3d` | FILE3D | Evet | FBX, Herhangi | FBX formatında 3B model. Modelin 100.000'den az yüzü olmalıdır. |
| `prompt` | STRING | Evet | | Doku düzenlemesini açıklar. En fazla 1024 UTF-8 karakteri destekler. |
| `seed` | INT | Hayır | 0 ile 2147483647 arası | Düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. (varsayılan: 0) |

**Not:** `model_3d` girişi FBX formatında bir dosya olmalıdır. Diğer 3B dosya formatları bu düğüm tarafından desteklenmez.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `GLB` | FILE3D | İşlenmiş 3B model, GLB formatında. |
| `FBX` | FILE3D | İşlenmiş 3B model, FBX formatında. |
