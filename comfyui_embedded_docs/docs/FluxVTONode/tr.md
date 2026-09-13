# Flux Sanal Deneme

Bu düğüm, sağlanan bir giysi görselini bir kişiye giydirerek sanal prova gerçekleştirir. Kişi ve giysi görsellerini BFL Flux VTO hizmetine gönderir; hizmet, kişinin giysiyi giydiği gerçekçi bir görsel üretir. İsteğe bağlı bir metin talimatı, giysinin nasıl oturması veya görünmesi gerektiğini açıklayabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `kişi` | Giydirilecek kişinin görseli. | IMAGE | Evet | - |
| `giysi` | Uygulanacak giysinin görseli. | IMAGE | Evet | - |
| `istem` | İsteğe bağlı doğal dilde stil talimatı (örn. giysinin nasıl oturması gerektiği). Varsayılan boş bir dizedir. | STRING | Hayır | - |
| `tohum` | Gürültüyü oluşturmak için kullanılan rastgele tohum. Varsayılan: 0. | INT | Hayır | 0 ile 18446744073709551615 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Kişinin sağlanan giysiyi giydiğini gösteren sonuç görseli. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVTONode/tr.md)

---
**Source fingerprint (SHA-256):** `5e0777dedcbd6275e31a16f6f5d78f4166147266c0c88531c5843a027702e594`
