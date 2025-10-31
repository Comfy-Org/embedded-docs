> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingAuraFlow/tr.md)

ModelSamplingAuraFlow düğümü, difüzyon modellerine özel olarak AuraFlow model mimarileri için tasarlanmış özelleştirilmiş bir örnekleme yapılandırması uygular. Modelin örnekleme davranışını, örnekleme dağılımını ayarlayan bir kaydırma parametresi uygulayarak değiştirir. Bu düğüm, SD3 model örnekleme çerçevesinden türetilmiştir ve örnekleme süreci üzerinde hassas kontrol sağlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | AuraFlow örnekleme yapılandırmasının uygulanacağı difüzyon modeli |
| `shift` | FLOAT | Evet | 0.0 - 100.0 | Örnekleme dağılımına uygulanacak kaydırma değeri (varsayılan: 1.73) |

## Çıktılar

| Çıktı Adı | Veri Türı | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | AuraFlow örnekleme yapılandırması uygulanmış değiştirilmiş model |