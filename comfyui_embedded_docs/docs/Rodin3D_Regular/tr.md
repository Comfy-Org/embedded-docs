**Genel Bakış**

Rodin 3D Regular düğümü, Rodin API'sini kullanarak 3D varlıklar üretir. Giriş görüntülerini alır ve bunları Rodin hizmeti aracılığıyla işleyerek 3D modeller oluşturur. Düğüm, görev oluşturmadan nihai 3D model dosyalarını indirmeye kadar tüm iş akışını yönetir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `Görseller` | 3D model oluşturma için kullanılan giriş görüntüleri. Birden fazla görüntü sağlanabilir. | IMAGE | Evet | - |
| `Tohum` | Tekrarlanabilir sonuçlar için rastgele tohum değeri. | INT | Evet | - |
| `Malzeme_Türü` | 3D modele uygulanacak malzeme türü. | STRING | Evet | - |
| `Poligon_sayısı` | Oluşturulan 3D model için hedef çokgen sayısı. Bu parametre, kalite modunu ve ağ karmaşıklığını belirler. | STRING | Evet | - |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `3D Model Yolu` | Oluşturulan 3D modelin dosya yolu (geriye dönük uyumluluk için korunmuştur). | STRING |
| `GLB` | GLB formatında oluşturulan 3D model. | FILE3DGLB |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Regular/tr.md)

---
**Source fingerprint (SHA-256):** `f937be3aa579baf4407434839e741141d6bd63c09b7e0bdc49a9e92a10d7a130`
