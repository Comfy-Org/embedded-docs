> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_SDE/tr.md)

SamplerDPMPP_SDE düğümü, örnekleme sürecinde kullanılmak üzere bir DPM++ SDE (Stokastik Diferansiyel Denklem) örnekleyicisi oluşturur. Bu örnekleyici, yapılandırılabilir gürültü parametreleri ve cihaz seçimi ile stokastik bir örnekleme yöntemi sağlar. Örnekleme hattında kullanılabilecek bir örnekleyici nesnesi döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `eta` | FLOAT | Evet | 0.0 - 100.0 | Örnekleme sürecinin stokastikliğini kontrol eder (varsayılan: 1.0) |
| `s_gürültü` | FLOAT | Evet | 0.0 - 100.0 | Örnekleme sırasında eklenen gürültü miktarını kontrol eder (varsayılan: 1.0) |
| `r` | FLOAT | Evet | 0.0 - 100.0 | Örnekleme davranışını etkileyen bir parametre (varsayılan: 0.5) |
| `gürültü_cihazı` | COMBO | Evet | "gpu"<br>"cpu" | Gürültü hesaplamalarının yapıldığı cihazı seçer (varsayılan: "gpu") |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Örnekleme hatlarında kullanılmak üzere yapılandırılmış bir DPM++ SDE örnekleyici nesnesi döndürür |

---
**Source fingerprint (SHA-256):** `43b3b3c4b2756a6e7979c12418de1dba79e3e0c0fde2a06505cf0a6825e6ebbf`
