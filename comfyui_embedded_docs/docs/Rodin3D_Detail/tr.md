> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Detail/tr.md)

Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme öneriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Detail/en.md)

Rodin 3D Detay düğümü, Rodin API'sini kullanarak detaylı 3D varlıklar üretir. Girdi görüntülerini alır ve bunları Rodin hizmeti aracılığıyla işleyerek detaylı geometri ve malzemelere sahip yüksek kaliteli 3D modeller oluşturur. Düğüm, görev oluşturmadan nihai 3D model dosyasını indirmeye kadar tüm iş akışını yönetir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `Görseller` | IMAGE | Evet | - | 3D model oluşturma için kullanılan girdi görüntüleri. Birden fazla görüntü sağlanabilir. |
| `Tohum` | INT | Evet | - | Tekrarlanabilir sonuçlar için rastgele tohum değeri |
| `Malzeme_Türü` | STRING | Evet | - | 3D modele uygulanacak malzeme türü |
| `Poligon_sayısı` | STRING | Evet | - | Oluşturulan 3D model için hedef çokgen sayısı. Ağ kalite seviyesini belirler. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `GLB` | STRING | Oluşturulan 3D modelin dosya yolu (yalnızca geriye dönük uyumluluk için) |
| `GLB` | FILE3DGLB | GLB formatında oluşturulan 3D model |

---
**Source fingerprint (SHA-256):** `ed9ed2c8a55ca80d18da88ee2703c66057a09beeac7163fc270d81a492417b0a`
