# Kling Virtual Try-On

Connectez une photo d’une personne et une photo du vêtement, et le nœud renvoie une nouvelle image de cette personne portant le vêtement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `person_image` | Photo d’une personne, idéalement de face ou en vue de trois-quarts. Les images dont un côté dépasse 2048 pixels sont d’abord réduites. | IMAGE | Oui | N/A |
| `garment_image` | Le vêtement à enfiler : photo produit, à plat, sur mannequin ou portée par un modèle. Une photo portée par un modèle peut conserver le reste de cette tenue. Vêtements uniquement ; les chaussures, sacs et accessoires ne sont pas pris en charge. | IMAGE | Oui | N/A |
| `keep_pose` | Désactivez cette option pour permettre à la pose de changer afin de mieux présenter la tenue. Paramètre avancé (par défaut : True). | BOOLEAN | Oui | `True`<br>`False` |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. Ce paramètre dispose de la fonctionnalité « contrôle après génération » (par défaut : 42). | INT | Oui | 0 à 2147483647 |

**Note :** Le résultat a la même taille que `person_image`, plafonnée à 2048 pixels sur le côté le plus long. Les deux entrées sont téléversées vers l’API de Kling, ce qui peut prendre un moment.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | La personne portant le vêtement. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTryOnNode/fr.md)

---
**Source fingerprint (SHA-256):** `03c2f9f1169ec2de3dd58162f9a7718a9c1f9af584aa63f280a0c4feefb70478`
