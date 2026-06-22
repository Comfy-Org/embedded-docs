# LTXVÖnİşleme

LTXVPreprocess düğümü, görüntülere sıkıştırma ön işleme uygular. Giriş görüntülerini alır ve belirtilen sıkıştırma seviyesiyle işleyerek, uygulanan sıkıştırma ayarlarıyla birlikte işlenmiş görüntüleri çıktı olarak verir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | İşlenecek giriş görüntüsü | IMAGE | Evet | - |
| `görüntü_sıkıştırma` | Görüntüye uygulanacak sıkıştırma miktarı (varsayılan: 35) | INT | Hayır | 0-100 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output_image` | Uygulanan sıkıştırma ile işlenmiş çıkış görüntüsü | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVPreprocess/tr.md)

---
**Source fingerprint (SHA-256):** `2c5fbde5d011bdf3313ca05508f58a13eaae0bdff12f3659fef281c0045e480d`
