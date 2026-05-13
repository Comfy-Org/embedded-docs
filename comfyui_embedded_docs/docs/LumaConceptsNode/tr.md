> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaConceptsNode/tr.md)

Luma Metinden Videoya ve Luma Görüntüden Videoya düğümleriyle kullanılmak üzere bir veya daha fazla Kamera Konseptini tutar. Bu düğüm, en fazla dört kamera konsepti seçmenize ve isteğe bağlı olarak bunları mevcut konsept zincirleriyle birleştirmenize olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `concept1` | STRING | Evet | Birden çok seçenek mevcut<br>"Yok" seçeneğini içerir | Mevcut Luma konseptlerinden ilk kamera konsepti seçimi |
| `concept2` | STRING | Evet | Birden çok seçenek mevcut<br>"Yok" seçeneğini içerir | Mevcut Luma konseptlerinden ikinci kamera konsepti seçimi |
| `concept3` | STRING | Evet | Birden çok seçenek mevcut<br>"Yok" seçeneğini içerir | Mevcut Luma konseptlerinden üçüncü kamera konsepti seçimi |
| `concept4` | STRING | Evet | Birden çok seçenek mevcut<br>"Yok" seçeneğini içerir | Mevcut Luma konseptlerinden dördüncü kamera konsepti seçimi |
| `luma_concepts` | LUMA_CONCEPTS | Hayır | Yok | Burada seçilenlere eklenecek isteğe bağlı Kamera Konseptleri |

**Not:** Dört konsept yuvasının tamamını kullanmak istemiyorsanız, tüm konsept parametreleri (`concept1` ile `concept4` arası) "Yok" olarak ayarlanabilir. Düğüm, sağlanan `luma_concepts` değerlerini seçilen konseptlerle birleştirerek birleşik bir konsept zinciri oluşturacaktır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `luma_concepts` | LUMA_CONCEPTS | Seçilen tüm konseptleri içeren birleşik kamera konsept zinciri |

---
**Source fingerprint (SHA-256):** `d0e334104884eadab86987f188dff079e11ee4a3de05d2537d88fa9d2a30534a`
