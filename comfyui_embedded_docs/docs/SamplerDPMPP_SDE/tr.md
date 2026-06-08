SamplerDPMPP_SDE düğümü, örnekleme sürecinde kullanılmak üzere bir DPM++ SDE (Stokastik Diferansiyel Denklem) örnekleyicisi oluşturur. Bu örnekleyici, yapılandırılabilir gürültü parametreleri ve cihaz seçimi ile stokastik bir örnekleme yöntemi sağlar. Örnekleme hattında kullanılabilecek bir örnekleyici nesnesi döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `eta` | Örnekleme sürecinin stokastikliğini kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 100.0 |
| `s_gürültü` | Örnekleme sırasında eklenen gürültü miktarını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 100.0 |
| `r` | Örnekleme davranışını etkileyen bir parametre (varsayılan: 0.5) | FLOAT | Evet | 0.0 - 100.0 |
| `gürültü_cihazı` | Gürültü hesaplamalarının yapıldığı cihazı seçer (varsayılan: "gpu") | COMBO | Evet | "gpu"<br>"cpu" |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sampler` | Örnekleme hatlarında kullanılmak üzere yapılandırılmış bir DPM++ SDE örnekleyici nesnesi döndürür | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_SDE/tr.md)

---
**Source fingerprint (SHA-256):** `43b3b3c4b2756a6e7979c12418de1dba79e3e0c0fde2a06505cf0a6825e6ebbf`
