> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CenterCropImages/tr.md)

Merkezi Kırpma Görselleri düğümü, bir görseli merkezinden belirtilen genişlik ve yüksekliğe kırpar. Giriş görselinin merkez bölgesini hesaplar ve tanımlanan boyutlarda dikdörtgen bir alan çıkarır. İstenen kırpma boyutu görselden büyükse, kırpma işlemi görselin sınırlarıyla kısıtlanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `image` | IMAGE | Evet | - | Kırpılacak giriş görseli. |
| `genişlik` | INT | Evet | 1 ila 8192 | Kırpma alanının genişliği (varsayılan: 512). |
| `yükseklik` | INT | Evet | 1 ila 8192 | Kırpma alanının yüksekliği (varsayılan: 512). |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `image` | IMAGE | Merkezi kırpma işlemi sonucunda elde edilen görsel. |

---
**Source fingerprint (SHA-256):** `4361b6630ab1833e035d6ab04a130fb36fff33cddc36b54ff5a2d8e04534a555`
