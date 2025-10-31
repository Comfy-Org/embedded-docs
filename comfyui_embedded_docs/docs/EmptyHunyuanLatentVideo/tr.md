> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanLatentVideo/tr.md)

`EmptyHunyuanLatentVideo` düğümü, `EmptyLatentImage` düğümüne benzer. Bu düğümü video üretimi için boş bir tuval olarak düşünebilirsiniz; burada genişlik, yükseklik ve uzunluk tuvalin özelliklerini tanımlar, ve toplu iş boyutu da oluşturulacak tuval sayısını belirler. Bu düğüm, sonraki video üretimi görevleri için hazır boş tuvaller oluşturur.

## Girdiler

| Parametre    | Comfy Türü | Açıklama                                                                                |
| ----------- | ---------- | ------------------------------------------------------------------------------------------ |
| `genişlik`     | `INT`      | Video genişliği, varsayılan 848, minimum 16, maksimum `nodes.MAX_RESOLUTION`, artış miktarı 16. |
| `yükseklik`    | `INT`      | Video yüksekliği, varsayılan 480, minimum 16, maksimum `nodes.MAX_RESOLUTION`, artış miktarı 16. |
| `uzunluk`    | `INT`      | Video uzunluğu, varsayılan 25, minimum 1, maksimum `nodes.MAX_RESOLUTION`, artış miktarı 4.     |
| `toplu_boyut`| `INT`      | Toplu iş boyutu, varsayılan 1, minimum 1, maksimum 4096.                                           |

## Çıktılar

| Parametre | Comfy Türü | Açıklama                                                                               |
| --------- | ---------- | ----------------------------------------------------------------------------------------- |
| `samples` | `LATENT`   | İşleme ve üretim görevleri için hazır, sıfır tensörleri içeren üretilmiş gizli video örnekleri. |