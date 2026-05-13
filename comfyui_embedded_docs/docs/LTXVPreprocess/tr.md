> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVPreprocess/tr.md)

LTXVPreprocess düğümü, görüntülere sıkıştırma ön işleme uygular. Giriş görüntülerini alır ve belirtilen sıkıştırma seviyesiyle işleyerek, uygulanan sıkıştırma ayarlarıyla birlikte işlenmiş görüntüleri çıktı olarak verir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `görüntü` | IMAGE | Evet | - | İşlenecek giriş görüntüsü |
| `görüntü_sıkıştırma` | INT | Hayır | 0-100 | Görüntüye uygulanacak sıkıştırma miktarı (varsayılan: 35) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output_image` | IMAGE | Uygulanan sıkıştırma ile işlenmiş çıkış görüntüsü |

---
**Source fingerprint (SHA-256):** `2c5fbde5d011bdf3313ca05508f58a13eaae0bdff12f3659fef281c0045e480d`
