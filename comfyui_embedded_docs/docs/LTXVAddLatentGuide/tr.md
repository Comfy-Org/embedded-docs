# LTXV Latent Kılavuzu Ekle

LTXV Add Latent Guide düğümü, önceden kodlanmış bir latentı kılavuz olarak sabitler; bu, kılavuz bir görüntüden değil de daha erken bir aşamadan geldiğinde kullanılır. VAE çözme/kodlama gidiş-dönüşü olmadan LTXV Add Guide ile aynı etkiye sahiptir. Hedeften uzamsal olarak daha küçük olan bir kılavuz (bir IC-LoRA veya ayrıntılandırma referansı) seyrek bir ızgara üzerine genişletilir ve RoPE bitiş konumları aynı oranda genişletilir; böylece yalnızca sol üst köşesini adreslemek yerine hedef tuvalin tamamını kaplar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `positive` | Pozitif koşullandırma girdisi. | CONDITIONING | Evet | Yok |
| `negative` | Negatif koşullandırma girdisi. | CONDITIONING | Evet | Yok |
| `vae` | Kare yerleşimi için küçültme indeksi formülünü okumak üzere kullanılan VAE modeli. | VAE | Evet | Yok |
| `latent` | Kılavuzun üzerine sabitlendiği hedef video latentı. | LATENT | Evet | Yok |
| `guiding_latent` | Kılavuz latentı. Uzamsal boyutu, hedefin uzamsal boyutunu her iki eksende de aynı tam sayıya bölmelidir; eşit boyut olduğu gibi sabitlenir, yarım boyut x2 IC-LoRA referansı olarak değerlendirilir. | LATENT | Evet | Yok |
| `latent_idx` | Kılavuzun başlatılacağı latent kare indeksi; piksel kareleri yerine latent kareleriyle sayılır. Negatif değerler kılavuzu latentin başlangıcından önceki karelere yerleştirir, sonundan geriye doğru sayılmaz. Varsayılan: 0. | INT | Evet | -9999 ile 9999 |
| `strength` | 1.0 ile sınırlandırılmıştır. Genişletilmiş bir kılavuz, dolgu konumlarını negatif bir gürültü giderme maskesiyle işaretler, böylece model onları atar; 1.0'ın üzerinde tutulan konumlar da negatife düşer ve kılavuzun tamamı atılırdı. 1.0'ın ötesine çıkarmak için bunun yerine `attention_mask` kullanın. Varsayılan: 1.0. | FLOAT | Evet | 0.0 ile 1.0, adım 0.01 |
| `attention_mask` | İsteğe bağlı piksel uzayı uzamsal maskesi. Bölge başına koşullandırma etkisini öz-dikkat yoluyla kontrol eder, `strength` ile çarpılır. | MASK | Hayır | Yok |

### Notlar

- Hem `latent` hem de `guiding_latent`, (batch, channels, frames, height, width) şeklinde 5 boyutlu video latentları olmalıdır.
- Kılavuz hedef latentın içine sığmalıdır: kılavuzun kare sayısı ile `latent_idx` toplamı hedef latentın sonunu geçmemelidir. Negatif `latent_idx` değerlerine izin verilir ve kılavuzu latentin başlangıcından önceye yerleştirir.
- Kılavuzun uzamsal boyutu, hedefin uzamsal boyutunu hem yükseklik hem de genişlik ekseninde bir tam sayıya bölmelidir.
- Yükseklik oranı ve genişlik oranı aynı değer olmalıdır (kare oran). Kare olmayan oran bir hata verir, çünkü genişletme ve RoPE yerleşimi her iki eksen için tek bir küçültme faktörü kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | Kılavuzun eklendiği pozitif koşullandırma. | CONDITIONING |
| `negative` | Kılavuzun eklendiği negatif koşullandırma. | CONDITIONING |
| `latent` | Kılavuzun uygulandığı, güncellenmiş `noise_mask` dahil latent çıktısı. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddLatentGuide/tr.md)

---
**Source fingerprint (SHA-256):** `19542500484dbc57fdbeeab8ba05bc2978246b3be5decc413825f616cab46f73`
