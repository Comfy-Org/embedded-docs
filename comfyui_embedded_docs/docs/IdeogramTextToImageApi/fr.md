# Ideogram 4.5 Text to Image

Générez des images à partir d'un prompt textuel avec Ideogram 4.5. Le prompt accepte également une légende JSON structurée d'Ideogram, par exemple le `final_prompt` renvoyé par une exécution précédente, ce qui permet un contrôle exact des chaînes de texte, des couleurs et de la mise en page. Le nœud renvoie la ou les images générées ainsi que la légende à partir de laquelle l'image a réellement été générée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Modèle à utiliser. (par défaut : `"ideogram-4.5"`) | DYNAMIC_COMBO | Oui | `"ideogram-4.5"` |
| `prompt` | Prompt textuel, ou une légende JSON structurée d'Ideogram telle qu'un `final_prompt` précédent. (par défaut : chaîne vide) | STRING | Oui | 1 à 10000 caractères |
| `size` | Taille de sortie. `"auto"` laisse le modèle choisir un canevas adapté au prompt. Un préréglage `(2K)` ou `(1K)` fixe à la fois la taille en pixels et le rapport d'aspect. (par défaut : `"auto"`) | COMBO | Oui | `"auto"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1296x3168 (9:22)"`<br>`"(2K) 3168x1296 (22:9)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"(1K) 720x1280 (9:16)"`<br>`"(1K) 1280x720 (16:9)"`<br>`"(1K) 720x1440 (1:2)"`<br>`"(1K) 1440x720 (2:1)"` |
| `quality` | Niveau de qualité. Les niveaux supérieurs coûtent plus cher et prennent plus de temps. (par défaut : `"medium"`) | COMBO | Oui | `"low"`<br>`"medium"`<br>`"high"` |
| `magic_prompt` | Réécrit le prompt sous forme de légende structurée détaillée avant la génération ; `"off"` conserve votre formulation aussi littérale que possible. La légende est renvoyée sous le nom `final_prompt`. (par défaut : `"auto"`) Il s'agit d'un paramètre avancé. | COMBO | Oui | `"auto"`<br>`"on"`<br>`"off"` |
| `seed` | Graine pour la génération. La génération texte-image n'est pas reproductible à partir de la graine seule, car le prompt est réécrit à chaque exécution ; pour reproduire une image, réutilisez son `final_prompt` avec `magic_prompt` défini sur `"off"` et la même graine. (par défaut : 42) | INT | Oui | 0 à 2147483647 |

### Contraintes des paramètres

- **Prompt requis :** le prompt doit contenir au moins un caractère autre qu'un espace blanc et au plus 10000 caractères. Définissez `magic_prompt` sur `"off"` lorsque vous fournissez votre propre légende JSON ou une formulation exacte.
- **Taille :** `"auto"` laisse le modèle choisir. Les préréglages `(2K)` font environ 3 à 4 mégapixels et les préréglages `(1K)` environ 1 mégapixel : l'étiquette du niveau décrit le budget de pixels et non un grand côté fixe ; le rapport d'aspect du préréglage est respecté. Seule la partie correspondant à la taille en pixels du préréglage est envoyée à l'API.
- **Reproductibilité :** avec `magic_prompt` défini sur `"auto"` ou `"on"`, le prompt est réécrit à chaque exécution, donc la même graine peut tout de même produire une image différente. Pour reproduire une image, réinjectez son `final_prompt` avec `magic_prompt` défini sur `"off"` et la même graine.
- **Sécurité du contenu :** si le filtre de sécurité du contenu d'Ideogram bloque la génération, le nœud lève une erreur au lieu de renvoyer une image.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | La ou les images générées sous forme de lot. | IMAGE |
| `final_prompt` | La légende structurée à partir de laquelle l'image a été générée. Réinjectez-la avec `magic_prompt` défini sur `"off"` et la même graine pour reproduire l'image. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramTextToImageApi/fr.md)

---
**Source fingerprint (SHA-256):** `a21f1faed9ca7a7bc63dae74003cc7599f11013075f718af9e5860d2cd666828`
