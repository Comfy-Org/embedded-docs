> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV1/tr.md)

IdeogramV1 düğümü, bir API aracılığıyla Ideogram V1 modelini kullanarak görüntüler oluşturur. Girdilerinize dayalı olarak bir veya daha fazla görüntü oluşturmak için metin istemlerini ve çeşitli oluşturma ayarlarını alır. Düğüm, çıktıyı özelleştirmek için farklı en-boy oranlarını ve oluşturma modlarını destekler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `istem` | STRING | Evet | - | Görüntü oluşturma için istem (varsayılan: boş) |
| `turbo` | BOOLEAN | Evet | - | Turbo modunun kullanılıp kullanılmayacağı (daha hızlı oluşturma, potansiyel olarak daha düşük kalite) (varsayılan: False) |
| `en_boy_oranı` | COMBO | Hayır | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" | Görüntü oluşturma için en-boy oranı (varsayılan: "1:1") |
| `sihirli_istem_seçeneği` | COMBO | Hayır | "AUTO"<br>"ON"<br>"OFF" | Oluşturmada MagicPrompt'un kullanılıp kullanılmayacağını belirleme (varsayılan: "AUTO") |
| `tohum` | INT | Hayır | 0-2147483647 | Oluşturma için rastgele tohum değeri (varsayılan: 0) |
| `negatif_istem` | STRING | Hayır | - | Görüntüden neyin hariç tutulacağının açıklaması (varsayılan: boş) |
| `görüntü_sayısı` | INT | Hayır | 1-8 | Oluşturulacak görüntü sayısı (varsayılan: 1) |

**Not:** `num_images` parametresinin, oluşturma isteği başına maksimum 8 görüntü sınırı vardır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | IMAGE | Ideogram V1 modelinden oluşturulan görüntü(ler) |