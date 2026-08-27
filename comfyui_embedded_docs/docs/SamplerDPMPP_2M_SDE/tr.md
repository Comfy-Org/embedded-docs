# ÖrnekleyiciDPMPP_2M_SDE

The SamplerDPMPP_2M_SDE düğümü, difüzyon modelleri için bir DPM++ 2M SDE örnekleyici oluşturur. Bu örnekleyici, örnekler üretmek için ikinci dereceden diferansiyel denklem çözücülerini stokastik diferansiyel denklemlerle birlikte kullanır. Örnekleme sürecini kontrol etmek için farklı çözücü türleri ve gürültü işleme seçenekleri sunar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `çözücü_türü` | Örnekleme süreci için kullanılacak diferansiyel denklem çözücüsünün türü (varsayılan: "midpoint") | COMBO | Evet | `"midpoint"`<br>`"heun"` |
| `eta` | Örnekleme sürecinin stokastikliğini kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 100.0 |
| `s_gürültü` | Örnekleme sırasında eklenen gürültü miktarını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 100.0 |
| `gürültü_cihazı` | Gürültü hesaplamalarının yapıldığı cihaz. "cpu" olarak ayarlandığında örnekleyici CPU tabanlı gürültü üretimi kullanır; "gpu" olarak ayarlandığında ise potansiyel olarak daha hızlı performans için GPU tabanlı gürültü üretimini kullanır (varsayılan: "gpu") | COMBO | Evet | `"gpu"`<br>`"cpu"` |

Not: `eta`, `s_noise` ve `noise_device` gelişmiş parametreler olarak işaretlenmiştir ve düğümün kullanıcı arayüzünün gelişmiş bölümünde görünür.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sampler` | Örnekleme hattında kullanıma hazır yapılandırılmış bir örnekleyici nesnesi | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2M_SDE/tr.md)

---
**Source fingerprint (SHA-256):** `42f5f098fa7573ca8a1a6085b72675ee6cb0ae8e7865c5793a815a6ef2495f82`
