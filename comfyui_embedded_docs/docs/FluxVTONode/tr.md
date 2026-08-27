# Flux Sanal Deneme

Bu düğüm, bir kişiyi sağlanan giysi görselindeki giysiyle giydirerek sanal giysi denemesi gerçekleştirir. Belirtilen giysiyi giyen kişinin gerçekçi bir görüntüsünü oluşturmak için BFL Flux VTO API'sini kullanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `kişi` | Giydirilecek kişinin görseli. | IMAGE | Evet | - |
| `giysi` | Uygulanacak giysinin görseli. | IMAGE | Evet | - |
| `istem` | İsteğe bağlı doğal dil stil talimatı (örn. giysinin nasıl oturması gerektiği). (varsayılan: boş) | STRING | Hayır | - |
| `tohum` | Gürültüyü oluşturmak için kullanılan rastgele tohum (seed). (varsayılan: 0) | INT | Hayır | 0 ile 18446744073709551615 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Sağlanan giysiyi giyen kişiyi gösteren sonuç görseli. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVTONode/tr.md)

---
**Source fingerprint (SHA-256):** `5e0777dedcbd6275e31a16f6f5d78f4166147266c0c88531c5843a027702e594`
