> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeHunyuan3D/tr.md)

VAEDecodeHunyuan3D düğümü, gizli temsilleri bir VAE kod çözücü kullanarak 3B voksel verilerine dönüştürür. Gizli örnekleri, 3B uygulamalar için uygun hacimsel veri üretmek üzere yapılandırılabilir parçalama ve çözünürlük ayarlarıyla VAE modeli üzerinden işler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `örnekler` | LATENT | Evet | - | 3B voksel verisine dönüştürülecek gizli temsil |
| `vae` | VAE | Evet | - | Gizli örnekleri çözmek için kullanılan VAE modeli |
| `parça_sayısı` | INT | Evet | 1000-500000 | Bellek yönetimi için işlemi bölmek üzere kullanılan parça sayısı (varsayılan: 8000) |
| `sekizli_ağaç_çözünürlüğü` | INT | Evet | 16-512 | 3B voksel oluşturma için kullanılan sekizli ağaç yapısının çözünürlüğü (varsayılan: 256) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `voxels` | VOXEL | Çözülen gizli temsilden üretilen 3B voksel verisi |