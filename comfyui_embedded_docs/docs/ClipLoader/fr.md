# Charger CLIP

Voici la traduction de la documentation du nœud CLIPLoader, conforme à vos règles :

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPLoader/en.md)

Le nœud CLIPLoader charge un modèle d'encodeur de texte (CLIP, T5 ou similaire) à partir d'un fichier, le rendant disponible pour d'autres nœuds qui doivent convertir des invites textuelles en représentations numériques. Il prend en charge une grande variété d'architectures de modèles, chacune nécessitant un type d'encodeur spécifique.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip_name` | Le nom du fichier du modèle d'encodeur de texte à charger. Ce fichier doit se trouver dans le répertoire `ComfyUI/models/text_encoders/` ou `ComfyUI/models/clip/`. | STRING | Oui | Liste des fichiers trouvés dans le dossier `text_encoders` |
| `type` | Le type d'architecture du modèle en cours de chargement. Cela détermine la variante d'encodeur spécifique à utiliser. La valeur par défaut est `"stable_diffusion"`. | STRING | Oui | `"stable_diffusion"`<br>`"stable_cascade"`<br>`"sd3"`<br>`"stable_audio"`<br>`"mochi"`<br>`"ltxv"`<br>`"pixart"`<br>`"cosmos"`<br>`"lumina2"`<br>`"wan"`<br>`"hidream"`<br>`"chroma"`<br>`"ace"`<br>`"omnigen2"`<br>`"qwen_image"`<br>`"hunyuan_image"`<br>`"flux2"`<br>`"ovis"`<br>`"longcat_image"`<br>`"cogvideox"` |
| `appareil` | Le périphérique sur lequel charger le modèle. `"default"` utilise le GPU s'il est disponible, tandis que `"cpu"` force le chargement sur le CPU. Il s'agit d'une option avancée (par défaut : `"default"`). | STRING | Non | `"default"`<br>`"cpu"` |

### Correspondances type-encodeur prises en charge

Le paramètre `type` sélectionne l'encodeur correct pour une architecture de modèle donnée. Voici les correspondances courantes :

| Type | Encodeur |
|------|----------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl / clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cogvideox | t5 xxl (remplissage à 226 jetons) |
| cosmos | old t5 xxl |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |
| hidream | llama-3.1 (recommandé) ou t5 |
| omnigen2 | qwen vl 2.5 3B |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `clip` | Le modèle d'encodeur de texte chargé, prêt à être connecté à d'autres nœuds pour l'encodage de texte et le conditionnement. | CLIP |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPLoader/fr.md)

---
**Source fingerprint (SHA-256):** `1051bfe5570dff81719682cb09938bae4c03e94e0e72f7a2be84867cccb48017`
