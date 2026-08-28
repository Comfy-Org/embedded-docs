# RenderUVAtlas

Bir mesh'in UV yerleşimini görüntü olarak render eder. Birbirine bağlı her UV bölgesi (chart) farklı bir renkle doldurulur ve chart sınırları, koyu gri bir arka plan üzerinde siyah çizgilerle çevrelenir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `ağ` | UV yerleşimi render edilecek 3D mesh. Mesh'in UV koordinatlarına sahip olması gerekir; aksi takdirde bir hata verilir. | MESH | Evet | - |
| `çözünürlük` | Render edilen görüntünün piksel cinsinden genişliği ve yüksekliği (varsayılan: 1024). | INT | Evet | 64 ila 4096 (adım 64) |

Not: Mesh'in UV koordinatları yoksa, düğüm "mesh has no UVs to render. Run UnwrapMesh first." hatasını verir. Mesh bir batch boyutu içeriyorsa (3D UV veya yüz dizileri), batch içindeki yalnızca ilk öğe render edilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `görüntü` | Her chart'ın renklendirildiği ve chart sınır kenarlarının siyah çizgilerle çevrelendiği render edilmiş UV atlas görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderUVAtlas/tr.md)

---
**Source fingerprint (SHA-256):** `b462101036418350390ffed621e583c6de14d5ea34d1e427342dc44ec3fd1922`
