> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Sketch/tr.md)

Bu düğüm, Rodin API'sini kullanarak 3D varlıklar oluşturur. Giriş görüntülerini alır ve bunları harici bir hizmet aracılığıyla 3D modellere dönüştürür. Düğüm, görev oluşturmadan nihai 3D model dosyalarını indirmeye kadar tüm süreci yönetir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | Evet | - | 3D modellere dönüştürülecek giriş görüntüleri. Birden fazla görüntü sağlanabilir. |
| `Seed` | INT | Hayır | 0-65535 | Oluşturma için rastgele tohum değeri (varsayılan: 0). Rastgele tohum için 0 olarak ayarlayın. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `3D Model Yolu` | STRING | Oluşturulan 3D modelin dosya yolu (yalnızca geriye dönük uyumluluk için) |
| `GLB` | FILE3DGLB | GLB formatında oluşturulan 3D model |

---
**Source fingerprint (SHA-256):** `d3bc71e6a44c11cbeff25351d561e99a7f09ed8ce3544d2968a873b6796512da`
