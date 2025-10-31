> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerER_SDE/tr.md)

SamplerER_SDE düğümü, difüzyon modelleri için özel örnekleme yöntemleri sağlar ve ER-SDE, Ters-zamanlı SDE ve ODE yaklaşımları dahil olmak üzere farklı çözücü türleri sunar. Örnekleme sürecinin stokastik davranışını ve hesaplama aşamalarını kontrol etme olanağı tanır. Düğüm, uygun işlevselliği sağlamak için seçilen çözücü türüne bağlı olarak parametreleri otomatik olarak ayarlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `solver_type` | COMBO | Evet | "ER-SDE"<br>"Ters-zamanlı SDE"<br>"ODE" | Örnekleme için kullanılacak çözücü türü. Difüzyon süreci için matematiksel yaklaşımı belirler. |
| `max_stage` | INT | Evet | 1-3 | Örnekleme süreci için maksimum aşama sayısı (varsayılan: 3). Hesaplama karmaşıklığını ve kalitesini kontrol eder. |
| `eta` | FLOAT | Evet | 0.0-100.0 | Ters-zamanlı SDE'nin stokastik gücü (varsayılan: 1.0). Eta=0 olduğunda, deterministik ODE'ye indirgenir. Bu ayar ER-SDE çözücü türü için geçerli değildir. |
| `s_noise` | FLOAT | Evet | 0.0-100.0 | Örnekleme süreci için gürültü ölçeklendirme faktörü (varsayılan: 1.0). Örnekleme sırasında uygulanan gürültü miktarını kontrol eder. |

**Parametre Kısıtlamaları:**

- `solver_type` "ODE" olarak ayarlandığında veya "Ters-zamanlı SDE" `eta`=0 ile kullanıldığında, hem `eta` hem de `s_noise` kullanıcı girdi değerlerinden bağımsız olarak otomatik olarak 0'a ayarlanır.
- `eta` parametresi yalnızca "Ters-zamanlı SDE" çözücü türünü etkiler ve "ER-SDE" çözücü türü üzerinde hiçbir etkisi yoktur.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Belirtilen çözücü ayarlarıyla örnekleme işlem hattında kullanılabilecek yapılandırılmış bir örnekleyici nesnesi. |