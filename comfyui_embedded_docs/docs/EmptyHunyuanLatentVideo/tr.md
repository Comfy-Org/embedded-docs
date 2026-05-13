> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanLatentVideo/tr.md)

`EmptyHunyuanLatentVideo` düğümü, `EmptyLatentImage` düğümüne benzer. Bunu, video oluşturma için boş bir tuval olarak düşünebilirsiniz; burada genişlik, yükseklik ve uzunluk tuvallerin özelliklerini tanımlar ve toplu iş boyutu oluşturulacak tuval sayısını belirler. Bu düğüm, sonraki video oluşturma görevleri için hazır boş tuvaller oluşturur.

## Girişler

| Parametre     | Comfy Türü | Açıklama                                                                                 |
| ------------ | ---------- | ---------------------------------------------------------------------------------------- |
| `width`      | `INT`      | Video genişliği, varsayılan 848, minimum 16, maksimum `nodes.MAX_RESOLUTION`, adım boyutu 16. |
| `height`     | `INT`      | Video yüksekliği, varsayılan 480, minimum 16, maksimum `nodes.MAX_RESOLUTION`, adım boyutu 16. |
| `length`     | `INT`      | Video uzunluğu, varsayılan 25, minimum 1, maksimum `nodes.MAX_RESOLUTION`, adım boyutu 4.    |
| `batch_size` | `INT`      | Toplu iş boyutu, varsayılan 1, minimum 1, maksimum 4096.                                          |

## Çıkışlar

| Parametre  | Comfy Türü | Açıklama                                                                                 |
| ---------- | ---------- | ---------------------------------------------------------------------------------------- |
| `samples`  | `LATENT`   | İşleme ve oluşturma görevleri için hazır, sıfır tensörleri içeren oluşturulmuş gizli video örnekleri. |