# Flux Sanal Deneme

Bu düğüm, bir kişiyi sağlanan giysi görüntüsüyle giydirerek sanal deneme gerçekleştirir. Kişinin belirtilen giysiyi giydiği gerçekçi bir görüntü oluşturmak için BFL Flux VTO API'sini kullanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `kişi` | Giydirilecek kişinin görüntüsü. | IMAGE | Evet | - |
| `giysi` | Uygulanacak giysinin görüntüsü. | IMAGE | Evet | - |
| `istem` | İsteğe bağlı doğal dil stil talimatı (ör. giysinin nasıl oturması gerektiği). | STRING | Hayır | - |
| `tohum` | Gürültü oluşturmak için kullanılan rastgele tohum değeri. | INT | Hayır | 0 ile 18446744073709551615 arası |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `image` | Kişinin sağlanan giysiyi giydiğini gösteren sonuç görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVTONode/tr.md)

---
**Source fingerprint (SHA-256):** `137c4cf91a539605ade93a428567619fea9e6a71459dd92354878fa2f2ea4afa`
