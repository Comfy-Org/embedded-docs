# UV Atlasını Renderla

Bir mesh'in UV düzenini görüntü olarak render eder. Bağlı her UV bölgesi (chart) farklı bir renkle doldurulur ve chart sınır kenarları koyu gri arka plan üzerinde siyahla çerçevelenir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `ağ` | UV düzeninin render edileceği 3D mesh. Mesh'in UV koordinatları olmalıdır; aksi takdirde düğüm "mesh has no UVs to render. Run UnwrapMesh first." hatasını verir. | MESH | Evet | - |
| `çözünürlük` | Render edilen kare görüntünün piksel cinsinden genişliği ve yüksekliği (varsayılan: 1024). | INT | Evet | 64 ile 4096 arası (adım 64) |

Not: Mesh bir batch boyutu içeriyorsa (3D UV veya yüz dizileri), batch içindeki yalnızca ilk öğe render edilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Render edilen UV atlas görüntüsü, tek görüntülük batch olarak döndürülür. Her UV chart'ı renklendirilir ve chart sınır kenarları siyahla çerçevelenir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderUVAtlas/tr.md)

---
**Source fingerprint (SHA-256):** `b462101036418350390ffed621e583c6de14d5ea34d1e427342dc44ec3fd1922`
