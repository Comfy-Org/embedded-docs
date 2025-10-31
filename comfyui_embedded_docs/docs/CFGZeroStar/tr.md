> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGZeroStar/tr.md)

CFGZeroStar düğümü, difüzyon modellerine özel bir rehberlik ölçeklendirme tekniği uygular. Koşullu ve koşulsuz tahminler arasındaki farka dayalı olarak optimize edilmiş bir ölçek faktörü hesaplayarak, sınıflandırıcısız rehberlik sürecini değiştirir. Bu yaklaşım, model kararlılığını korurken, oluşturma süreci üzerinde gelişmiş kontrol sağlamak için son çıktıyı ayarlar.

## Girdiler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | gerekli | - | - | CFGZeroStar rehberlik ölçeklendirme tekniği ile değiştirilecek difüzyon modeli |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `patched_model` | MODEL | CFGZeroStar rehberlik ölçeklendirmesi uygulanmış değiştirilmiş model |