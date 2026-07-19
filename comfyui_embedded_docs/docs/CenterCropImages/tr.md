# Ortadan Kırp Görseller

Merkezi Kırpma Görselleri düğümü, bir görseli merkezinden belirtilen genişlik ve yüksekliğe kırpar. Giriş görselinin merkez bölgesini hesaplar ve tanımlanan boyutlarda dikdörtgen bir alan çıkarır. İstenen kırpma boyutu görselden büyükse, kırpma işlemi görselin sınırlarıyla kısıtlanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Kırpılacak giriş görseli. | IMAGE | Evet | - |
| `genişlik` | Kırpma alanının genişliği (varsayılan: 512). | INT | Evet | 1 ila 8192 |
| `yükseklik` | Kırpma alanının yüksekliği (varsayılan: 512). | INT | Evet | 1 ila 8192 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Merkezi kırpma işlemi sonucunda elde edilen görsel. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CenterCropImages/tr.md)

---
**Source fingerprint (SHA-256):** `4361b6630ab1833e035d6ab04a130fb36fff33cddc36b54ff5a2d8e04534a555`
