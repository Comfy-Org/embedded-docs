SamplerDPMPP_2M_SDE düğümü, difüzyon modelleri için bir DPM++ 2M SDE örnekleyicisi oluşturur. Bu örnekleyici, örnekler üretmek için stokastik diferansiyel denklemlerle birlikte ikinci dereceden diferansiyel denklem çözücüleri kullanır. Örnekleme sürecini kontrol etmek için farklı çözücü türleri ve gürültü işleme seçenekleri sunar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `çözücü_türü` | Örnekleme sürecinde kullanılacak diferansiyel denklem çözücüsünün türü | STRING | Evet | `"midpoint"`<br>`"heun"` |
| `eta` | Örnekleme sürecinin stokastikliğini kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 100.0 |
| `s_gürültü` | Örnekleme sırasında eklenen gürültü miktarını kontrol eder (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 100.0 |
| `gürültü_cihazı` | Gürültü hesaplamalarının yapıldığı cihaz. "cpu" olarak ayarlandığında, örnekleyici CPU tabanlı gürültü üretimi kullanır; "gpu" olarak ayarlandığında ise potansiyel olarak daha hızlı performans için GPU tabanlı gürültü üretimi kullanır | STRING | Evet | `"gpu"`<br>`"cpu"` |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sampler` | Örnekleme hattında kullanıma hazır, yapılandırılmış bir örnekleyici nesnesi | SAMPLER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2M_SDE/tr.md)

---
**Source fingerprint (SHA-256):** `4a6a16e3494e8270f3707e172f252e7fc4e1b65efbecd3dd086b1a1edc5ba23a`
