Voici la traduction en français de la documentation du nœud ComfyUI :

Ce nœud supprime les images en double ou très similaires d'un lot. Il fonctionne en créant un hachage perceptuel pour chaque image — une simple empreinte numérique basée sur son contenu visuel — puis en les comparant. Les images dont les hachages sont plus similaires qu'un seuil défini sont considérées comme des doublons et filtrées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `images` | Le lot d'images à traiter pour la déduplication. | IMAGE | Oui | - |
| `seuil_de_similarité` | Seuil de similarité (0-1). Plus la valeur est élevée, plus les images sont similaires. Les images au-dessus de ce seuil sont considérées comme des doublons. (par défaut : 0.95) | FLOAT | Non | 0.0 - 1.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `images` | La liste filtrée des images dont les doublons ont été supprimés. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageDeduplication/fr.md)

---
**Source fingerprint (SHA-256):** `8904f9dee4ca911821e76d2317983cbc230c4821a9ee7876180bd7dbe42b9a54`
