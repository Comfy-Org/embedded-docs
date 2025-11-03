> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerCFGpp/tr.md)

SamplerEulerCFGpp düğümü, çıktılar oluşturmak için bir Euler CFG++ örnekleme yöntemi sağlar. Bu düğüm, kullanıcı tercihine göre seçilebilen iki farklı Euler CFG++ örnekleyici uygulama versiyonu sunar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `sürüm` | STRING | Evet | `"regular"`<br>`"alternative"` | Kullanılacak Euler CFG++ örnekleyicinin uygulama versiyonu |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Yapılandırılmış bir Euler CFG++ örnekleyici örneği döndürür |