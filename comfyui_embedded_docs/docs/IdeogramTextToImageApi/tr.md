# Ideogram 4.5 Text to Image

Ideogram 4.5 ile bir metin isteminden görüntüler oluşturun. `prompt` ayrıca, önceki bir çalıştırmada döndürülen `final_prompt` gibi bir Ideogram yapılandırılmış JSON açıklamasını da kabul eder; bu, metin dizeleri, renkler ve yerleşim üzerinde tam kontrol sağlar. Düğüm, oluşturulan görüntüyü/görüntüleri, görüntünün gerçekte üretildiği açıklamayla birlikte döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model. (varsayılan: `"ideogram-4.5"`) | DYNAMIC_COMBO | Evet | `"ideogram-4.5"` |
| `prompt` | Metin istemi veya önceki bir `final_prompt` gibi Ideogram yapılandırılmış JSON açıklaması. (varsayılan: boş dize) | STRING | Evet | 1 ile 10000 arası characters |
| `size` | Çıktı boyutu. `"auto"` modelin isteme uygun bir tuval seçmesini sağlar. Bir `(2K)` veya `(1K)` ön ayarı hem piksel boyutunu hem de en-boy oranını sabitler. (varsayılan: `"auto"`) | COMBO | Evet | `"auto"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1296x3168 (9:22)"`<br>`"(2K) 3168x1296 (22:9)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"(1K) 720x1280 (9:16)"`<br>`"(1K) 1280x720 (16:9)"`<br>`"(1K) 720x1440 (1:2)"`<br>`"(1K) 1440x720 (2:1)"` |
| `quality` | Kalite kademesi. Daha yüksek kademeler daha pahalıdır ve daha uzun sürer. (varsayılan: `"medium"`) | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"` |
| `magic_prompt` | Oluşturmadan önce istemi ayrıntılı, yapılandırılmış bir açıklamaya dönüştürür; `"off"` ifadenizi olabildiğince birebir korur. Açıklama `final_prompt` olarak döndürülür. (varsayılan: `"auto"`) Bu gelişmiş bir ayardır. | COMBO | Evet | `"auto"`<br>`"on"`<br>`"off"` |
| `seed` | Üretim için tohum. Metinden görüntüye üretim yalnızca tohumla yeniden üretilemez çünkü istem her çalıştırmada yeniden yazılır; bir görüntüyü yeniden üretmek için `final_prompt` değerini `magic_prompt` `"off"` olarak ayarlanmış ve aynı tohumla yeniden kullanın. (varsayılan: 42) | INT | Evet | 0 ile 2147483647 arası |

### Parametre Kısıtları

- **İstem gerekli:** istem en az bir boşluk olmayan karakter içermeli ve en fazla 10000 karakter olmalıdır. Kendi JSON açıklamanızı veya tam ifadenizi sağlarken `magic_prompt` değerini `"off"` olarak ayarlayın.
- **Boyut:** `"auto"` modelin seçmesini sağlar. `(2K)` ön ayarları uzun kenarda yaklaşık 2048 piksel, `(1K)` ön ayarları ise yaklaşık 1024 pikseldir; ön ayarın en-boy oranına uyulur. Ön ayarın yalnızca piksel boyutu kısmı API'ye gönderilir.
- **Yeniden üretilebilirlik:** `magic_prompt` `"auto"` veya `"on"` olarak ayarlandığında istem her çalıştırmada yeniden yazılır, bu nedenle aynı tohum yine de farklı bir görüntü üretebilir. Bir görüntüyü yeniden üretmek için `final_prompt` değerini `magic_prompt` `"off"` olarak ayarlanmış ve aynı tohumla geri besleyin.
- **İçerik güvenliği:** Ideogram'ın içerik güvenliği filtresi üretimi engellerse, düğüm görüntü döndürmek yerine bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Oluşturulan görüntüyü/görüntüleri toplu olarak. | IMAGE |
| `final_prompt` | Görüntünün üretildiği yapılandırılmış açıklama. Görüntüyü yeniden üretmek için `magic_prompt` `"off"` olarak ayarlanmış ve aynı tohumla bunu geri besleyin. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramTextToImageApi/tr.md)

---
**Source fingerprint (SHA-256):** `a21f1faed9ca7a7bc63dae74003cc7599f11013075f718af9e5860d2cd666828`
