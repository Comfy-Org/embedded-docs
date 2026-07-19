# BoşHunyuanGizliVideo

`EmptyHunyuanLatentVideo` düğümü, `EmptyLatentImage` düğümüne benzer. Bunu, video oluşturma için boş bir tuval olarak düşünebilirsiniz; burada genişlik, yükseklik ve uzunluk tuvallerin özelliklerini tanımlar ve toplu iş boyutu oluşturulacak tuval sayısını belirler. Bu düğüm, sonraki video oluşturma görevleri için hazır boş tuvaller oluşturur.

## Girişler

| Parametre | Açıklama | Comfy Türü |
| --- | --- | --- |
| `genişlik` | Video genişliği, varsayılan 848, minimum 16, maksimum `nodes.MAX_RESOLUTION`, adım boyutu 16. | `INT` |
| `yükseklik` | Video yüksekliği, varsayılan 480, minimum 16, maksimum `nodes.MAX_RESOLUTION`, adım boyutu 16. | `INT` |
| `uzunluk` | Video uzunluğu, varsayılan 25, minimum 1, maksimum `nodes.MAX_RESOLUTION`, adım boyutu 4. | `INT` |
| `toplu_boyut` | Toplu iş boyutu, varsayılan 1, minimum 1, maksimum 4096. | `INT` |

## Çıkışlar

| Parametre | Açıklama | Comfy Türü |
| --- | --- | --- |
| `samples` | İşleme ve oluşturma görevleri için hazır, sıfır tensörleri içeren oluşturulmuş gizli video örnekleri. | `LATENT` |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanLatentVideo/tr.md)
