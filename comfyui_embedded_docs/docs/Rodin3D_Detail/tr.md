Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme öneriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Detail/en.md)

Rodin 3D Detay düğümü, Rodin API'sini kullanarak detaylı 3D varlıklar üretir. Girdi görüntülerini alır ve bunları Rodin hizmeti aracılığıyla işleyerek detaylı geometri ve malzemelere sahip yüksek kaliteli 3D modeller oluşturur. Düğüm, görev oluşturmadan nihai 3D model dosyasını indirmeye kadar tüm iş akışını yönetir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `Görseller` | 3D model oluşturma için kullanılan girdi görüntüleri. Birden fazla görüntü sağlanabilir. | IMAGE | Evet | - |
| `Tohum` | Tekrarlanabilir sonuçlar için rastgele tohum değeri | INT | Evet | - |
| `Malzeme_Türü` | 3D modele uygulanacak malzeme türü | STRING | Evet | - |
| `Poligon_sayısı` | Oluşturulan 3D model için hedef çokgen sayısı. Ağ kalite seviyesini belirler. | STRING | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `GLB` | Oluşturulan 3D modelin dosya yolu (yalnızca geriye dönük uyumluluk için) | STRING |
| `GLB` | GLB formatında oluşturulan 3D model | FILE3DGLB |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Detail/tr.md)

---
**Source fingerprint (SHA-256):** `ed9ed2c8a55ca80d18da88ee2703c66057a09beeac7163fc270d81a492417b0a`
