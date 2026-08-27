# RenderUVAtlas

Bir mesh'in UV yerleşimini bir görüntü olarak işler. Birbirine bağlı her UV bölgesi (chart) farklı bir renkle doldurulur ve chart sınırları koyu gri bir arka plan üzerinde siyah renkle çerçevelenir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | UV yerleşimi işlenecek 3B mesh. Mesh'in UV koordinatlarına sahip olması gerekir; aksi takdirde bir hata verilir. | MESH | Evet | - |
| `resolution` | İşlenen görüntünün piksel cinsinden genişliği ve yüksekliği (varsayılan: 1024). | INT | Evet | 64 ila 4096 (adım 64) |

Not: Mesh'in UV koordinatları yoksa düğüm "mesh has no UVs to render. Run UnwrapMesh first." hatasını verir. Mesh bir batch boyutu içeriyorsa (3B UV veya yüz dizileri), batch içindeki yalnızca ilk öğe işlenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | İşlenmiş UV atlas görüntüsü; her chart renklendirilmiş ve chart sınır kenarları siyahla çerçevelenmiştir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderUVAtlas/tr.md)

---
**Source fingerprint (SHA-256):** `b462101036418350390ffed621e583c6de14d5ea34d1e427342dc44ec3fd1922`
