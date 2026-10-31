# MiniMax H3 Max Insert Video

Bu düğüm, bir videonun başlangıç ve devam etme zamanları arasındaki bölümünü, bir istem ile isteğe bağlı referans görselleri ve videolarıyla yönlendirilen yeni oluşturulmuş bir sahneyle değiştirir. Kaynak video `start_time` noktasında kesilir ve `resume_time` noktasında devam eder; çıkarılan aralık yeniden oluşturulur ve geri yerleştirilir. Bir çekimi düzeltmek, bir eylemi değiştirmek veya bir klibin iki bölümünü birbirine bağlamak için kullanın.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video oluşturma için kullanılacak model. | DYNAMIC_COMBO | Evet | "MiniMax H3 Max" |

### MiniMax H3 Max Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `video` | Kaynak video, en fazla 60 saniye uzunluğunda. En-boy oranı 0.4 ile 2.5 arasında olmalıdır. | VIDEO | Evet | 0 ile 60 arası saniye |
| `reference_images` | Büyütülebilir yuva: yeni sahne için en fazla 9 isteğe bağlı referans görseli (`image_1`...`image_9`) bağlayın; her biri en az 256x256 piksel olmalıdır. İstemde bağlantı sırasına göre `@Image1`..`@Image9` olarak anılırlar. | IMAGE | Hayır | 0 ile 9 arası görüntü |
| `reference_videos` | Büyütülebilir yuva: yeni sahne için en fazla 3 isteğe bağlı referans videosu (`video_1`...`video_3`) bağlayın; her biri 2 ila 15 saniye ve toplamda 15 saniye olmalıdır. İstemde bağlantı sırasına göre `@Video1`..`@Video3` olarak anılırlar. | VIDEO | Hayır | 0 ile 3 arası video |
| `prompt` | Yeni sahne. Bir istem veya en az bir referans gereklidir; istem olmadan referanslar genellikle yok sayılır. | STRING | Evet | 0 ile 50000 arası karakter |
| `start_time` | Kaynak videonun durduğu ve yeni sahnenin başladığı saniye (varsayılan: 2.0). | FLOAT | Evet | 1.625 ile 60.0 arası |
| `resume_time` | Yeni sahneden sonra kaynak videonun devam ettiği saniye (varsayılan: 3.0). `start_time` değerinden sonra olmalı ve videonun sonundan en az 1.375 saniye önce olmalıdır. `start_time` ile `resume_time` arasındaki kaynak kaldırılır. | FLOAT | Evet | 1.625 ile 60.0 arası |
| `duration` | Yeni sahnenin saniye cinsinden uzunluğu (varsayılan: 5). | INT | Evet | 5 ile 13 arası |
| `resolution` | Çıktı videosunun çözünürlüğü (varsayılan: "768P"). | COMBO | Evet | "480P"<br>"768P" |
| `color_match` | Yeni sahnenin renklerini kaynak videoyla eşleştirin (varsayılan: true). | BOOLEAN | Hayır | true<br>false |
| `prompt_expansion` | İstemi kaynak videoyu kullanarak yeniden yazın. Aynı `seed` için tekrarlanabilir sonuçlar almak üzere kapatın (varsayılan: true). | BOOLEAN | Hayır | true<br>false |
| `seed` | Rastgele tohum. Aynı `seed` ile yapılan aynı istek benzer, ancak birebir aynı olduğu garanti edilmeyen sonuçlar verir (varsayılan: 42). | INT | Evet | 0 ile 2147483647 arası |

### Parametre Kısıtlamaları

- `resume_time`, `start_time` değerinden büyük olmalı ve videonun sonundan en az 1.375 saniye önce olmalıdır; aksi takdirde istek reddedilir.
- Her referans video 2 ila 15 saniye uzunluğunda olmalıdır ve hepsi birlikte 15 saniyeyi aşamaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Başlangıç ve devam etme zamanları arasına yeni sahnenin yerleştirildiği kaynak video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxInsertVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `623ad0b37f51ce4640c0058676e008697e31563c2a77a3da79ba7936af2d3f99`
