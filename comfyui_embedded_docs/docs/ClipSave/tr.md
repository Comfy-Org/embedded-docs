> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSave/tr.md)

`CLIPSave` düğümü, CLIP metin kodlayıcı modellerini SafeTensors formatında kaydetmek için tasarlanmıştır. Bu düğüm, gelişmiş model birleştirme iş akışlarının bir parçasıdır ve genellikle `CLIPMergeSimple` ve `CLIPMergeAdd` gibi düğümlerle birlikte kullanılır. Kaydedilen dosyalar, güvenlik ve uyumluluğu sağlamak için SafeTensors formatını kullanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Varsayılan Değer | Açıklama |
|-----------|-----------|----------|---------------|-------------|
| clip | CLIP | Evet | - | Kaydedilecek CLIP modeli |
| filename_prefix | STRING | Evet | "clip/ComfyUI" | Kaydedilen dosya için ön ek yolu |
| prompt | PROMPT | Gizli | - | İş akışı istem bilgileri (üst veri için) |
| extra_pnginfo | EXTRA_PNGINFO | Gizli | - | Ek PNG bilgileri (üst veri için) |

## Çıktılar

Bu düğümün tanımlanmış çıktı türü yoktur. İşlenmiş dosyaları `ComfyUI/output/` klasörüne kaydeder.

### Çoklu Dosya Kaydetme Stratejisi

Düğüm, CLIP model türüne göre farklı bileşenleri kaydeder:

| Ön Ek Türü | Dosya Son Eki | Açıklama |
|------------|-------------|-------------|
| `clip_l.` | `_clip_l` | CLIP-L metin kodlayıcı |
| `clip_g.` | `_clip_g` | CLIP-G metin kodlayıcı |
| Boş ön ek | Son ek yok | Diğer CLIP bileşenleri |

## Kullanım Notları

1. **Dosya Konumu**: Tüm dosyalar `ComfyUI/output/` dizininde kaydedilir
2. **Dosya Formatı**: Modeller güvenlik için SafeTensors formatında kaydedilir
3. **Üst Veri**: Mevcutsa iş akışı bilgilerini ve PNG üst verilerini içerir
4. **İsimlendirme Kuralı**: Belirtilen ön ek artı model türüne göre uygun son ekler kullanır