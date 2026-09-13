# 3D Kaydet (Gelişmiş)

Bir 3D modeli ComfyUI çıktı dizinindeki bir dosyaya kaydeder ve kaydedilen sahnenin önizlemesini oluşturur. Ayrıca 3D modeli, sahnedeki yerleşimini, kamera bilgilerini ve görüntü alanı boyutlarını aşağı akış düğümlerine iletir. Model yerleşimi veya kamera bilgisi bağlı olmadığında, düğüm görüntü alanı durumunda saklanan değerleri kullanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `model_3d` | Yukarı akış 3D düğümünden gelen 3D model dosyası. | FILE3D | Evet | GLB<br>GLTF<br>FBX<br>OBJ<br>STL<br>USDZ<br>Any |
| `filename_prefix` | Kaydedilen dosya adı için kullanılan ön ek (varsayılan: "3d/ComfyUI"). | STRING | Evet | Serbest metin |
| `viewport_state` | Kamera ve model yerleşim bilgilerini içeren görüntü alanı durumu; genellikle bir Load 3D düğümünden gelir. | LOAD3D | Evet | - |
| `model_3d_info` | Sahnede her modelin yerleşimi: konum, dönüş ve ölçek (Y-up dünya uzayı). Bağlandığında `viewport_state` içinde saklanan model yerleşiminin yerine geçer. | LOAD3DMODELINFO | Hayır | - |
| `camera_info` | Görüntü alanı kamera bilgileri: konum, bakış hedefi, yakınlaştırma ve tür. Bağlandığında `viewport_state` içinde saklanan kamera bilgilerinin yerine geçer. | LOAD3DCAMERA | Hayır | - |
| `width` | Görüntü alanının piksel cinsinden render genişliği (varsayılan: 1024). | INT | Evet | 1 ila 4096 |
| `height` | Görüntü alanının piksel cinsinden render yüksekliği (varsayılan: 1024). | INT | Evet | 1 ila 4096 |

Not: `model_3d_info` ve `camera_info` isteğe bağlıdır. Girdilerden biri bağlı olmadığında, düğüm `viewport_state` içinde saklanan karşılık gelen değerlere geri döner.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `model_3d` | Girdiden iletilen 3D model dosyası. | FILE3D |
| `model_3d_info` | Sahnede her modelin yerleşimi: konum, dönüş ve ölçek (Y-up dünya uzayı). | LOAD3DMODELINFO |
| `camera_info` | Görüntü alanı kamera bilgileri: konum, bakış hedefi, yakınlaştırma ve tür. | LOAD3DCAMERA |
| `width` | Girdiden iletilen render genişliği değeri. | INT |
| `height` | Girdiden iletilen render yüksekliği değeri. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Save3DAdvanced/tr.md)

---
**Source fingerprint (SHA-256):** `27cb15c5cf382e6e5b8164cfd456993404222c61d59edff2d51f9f1c8e47b25f`
