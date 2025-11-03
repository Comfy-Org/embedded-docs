> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2M_SDE/tr.md)

SamplerDPMPP_2M_SDE düğümü, difüzyon modelleri için bir DPM++ 2M SDE örnekleyici oluşturur. Bu örnekleyici, örnekler oluşturmak için stokastik diferansiyel denklemlerle ikinci dereceden diferansiyel denklem çözücüleri kullanır. Örnekleme sürecini kontrol etmek için farklı çözücü türleri ve gürültü yönetimi seçenekleri sunar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `çözücü_türü` | STRING | Evet | `"midpoint"`<br>`"heun"` | Örnekleme süreci için kullanılacak diferansiyel denklem çözücüsünün türü |
| `eta` | FLOAT | Evet | 0.0 - 100.0 | Örnekleme sürecinin stokastikliğini kontrol eder (varsayılan: 1.0) |
| `s_gürültü` | FLOAT | Evet | 0.0 - 100.0 | Örnekleme sırasında eklenen gürültü miktarını kontrol eder (varsayılan: 1.0) |
| `gürültü_cihazı` | STRING | Evet | `"gpu"`<br>`"cpu"` | Gürültü hesaplamalarının gerçekleştirildiği aygıt |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Örnekleme işlem hattında kullanıma hazır yapılandırılmış bir örnekleyici nesnesi |