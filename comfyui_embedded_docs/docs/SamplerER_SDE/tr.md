> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerER_SDE/tr.md)

SamplerER_SDE düğümü, difüzyon modelleri için ER-SDE, Ters-zamanlı SDE ve ODE yaklaşımları dahil olmak üzere farklı çözücü türleri sunan özel örnekleme yöntemleri sağlar. Örnekleme sürecinin stokastik davranışı ve hesaplama aşamaları üzerinde kontrol sağlar. Düğüm, seçilen çözücü türüne göre parametreleri otomatik olarak ayarlayarak doğru işlevselliği sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `solver_type` | COMBO | Evet | "ER-SDE"<br>"Ters-zamanlı SDE"<br>"ODE" | Örnekleme için kullanılacak çözücü türü. Difüzyon süreci için matematiksel yaklaşımı belirler. |
| `max_stage` | INT | Hayır | 1-3 | Örnekleme süreci için maksimum aşama sayısı (varsayılan: 3). Hesaplama karmaşıklığını ve kalitesini kontrol eder. |
| `eta` | FLOAT | Hayır | 0.0-100.0 | Ters-zamanlı SDE'nin stokastik gücü (varsayılan: 1.0). eta=0 olduğunda deterministik ODE'ye indirgenir. Bu ayar ER-SDE çözücü türü için geçerli değildir. |
| `s_noise` | FLOAT | Hayır | 0.0-100.0 | Örnekleme süreci için gürültü ölçekleme faktörü (varsayılan: 1.0). Örnekleme sırasında uygulanan gürültü miktarını kontrol eder. |

**Parametre Kısıtlamaları:**

- `solver_type` "ODE" olarak ayarlandığında veya `eta`=0 ile "Ters-zamanlı SDE" kullanıldığında, kullanıcı giriş değerlerinden bağımsız olarak hem `eta` hem de `s_noise` otomatik olarak 0 olarak ayarlanır.
- `eta` parametresi yalnızca "Ters-zamanlı SDE" çözücü türünü etkiler ve "ER-SDE" çözücü türü üzerinde hiçbir etkisi yoktur.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Belirtilen çözücü ayarlarıyla örnekleme hattında kullanılabilen yapılandırılmış bir örnekleyici nesnesi. |

---
**Source fingerprint (SHA-256):** `bc24ec3c5dc645aebf55ef3392c5f4a40dcf0461b4b77731e8fe7ff397dcfadf`
