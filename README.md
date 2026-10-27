# Wonka Bilbao — Una Marca · Tres Experiencias

> **Experiencia web cinematográfica y gastronómica de Wonka Bilbao.**  
> Demo interactiva que une hospitalidad vasca contemporánea, tres identidades complementarias (*Wonka House*, *Wonka Lounge*, *Wonka Bar*) y dirección artística inspirada en el universo cinematográfico de Willy Wonka y técnicas avanzadas de Codrops.

🌐 **Demo en vivo (GitHub Pages):** [https://baituman420.github.io/wonka/](https://baituman420.github.io/wonka/)

---

## 🎩 El Concepto

Arraigado en el pulso gastronómico y social de Bilbao, **Wonka** reúne en un mismo espacio tres atmósferas complementarias:

1. **Wonka House (Verde Botella `#2D4739`):** Comida reposada, sobremesa cálida, cocina con producto seleccionado y ambiente hogareño.
2. **Wonka Lounge (Púrpura Imperial `#2E1050`):** Luces tenues, coctelería de autor, música cuidada y el pulso nocturno de la noche bilbaína.
3. **Wonka Bar (Dorado Mostaza / Cacao `#C49A45`):** Pintxos recién hechos, raciones de corte tradicional, vinos de calidad y ambiente tabernero cercano.

---

## ✨ Características Técnicas y Dirección Artística

### 1. Animaciones y Coreografía con GSAP
- **GSAP 3 + ScrollTrigger + MorphSVGPlugin:**
  - **Separadores de Onda Elásticos (Codrops On-Scroll Path Animations):** Cuatro transiciones fluidas entre secciones mediante siluetas SVG Bézier animadas según el desplazamiento.
  - **Estrechamiento Orgánico de Fotografías:** Máscaras `<clipPath>` Bézier isomórficas que se pellizcan lateralmente («cintura de avispa») al pasar por el centro del viewport sin deformar las proporciones de las imágenes.
  - **Golosina Mágica Líquida (Codrops Morphing Background Shapes):** Escultura 3D paramétrica de 320px que recorre la página con inercia viscosa (`scrub: 2.2`), combinando el vector de desplazamiento con estiramiento cinético (*kinetic squash & stretch*) al cruzar las ondas divisorias.
  - **Sombrero Mágico Wonka en el Hero:** Ilustración SVG original con respiración flotante, inclinación reactiva al cursor y destellos dorados.

### 2. Microinteracciones y Sistema de Diseño
- **Selector Interactivo «¿Qué plan buscas hoy?»:** Píldoras interactivas con estados activos diferenciados cromáticamente por experiencia.
- **Formulario Demostrativo de Celebraciones:** Selector de número de comensales, fecha y espacio preferido, con toasts de feedback accesibles.
- **Arquitectura de Capas Segura:** Jerarquía de `z-index` estricta que mantiene las animaciones de fondo en `z-index: 5` con `pointer-events: none`, garantizando accesibilidad y respuesta inmediata en textos, botones y formularios.
- **Accesibilidad y Responsive:** Detección de `@media (prefers-reduced-motion: reduce)` y escalado armónico para viewports móviles (390px).

---

## 🚀 Estructura del Proyecto

```
wonka/
├── index.html                   # Página principal interactiva
├── .nojekyll                    # Configuración estática para GitHub Pages
├── .github/
│   └── workflows/
│       └── deploy.yml           # GitHub Actions workflow de despliegue automático
├── DESIGN.md                    # Manual de identidad y tokens de diseño
├── PRODUCT.md                   # Definición de producto y narrativa
└── public/
    └── assets/
        ├── brand/               # Patrones geométricos art decó y posters
        ├── images/              # Fotografía gastronómica real de Wonka
        ├── js/                  # MorphSVGPlugin y dependencias locales
        └── logos/               # Logotipos oficiales vectoriales y adaptaciones
```

---

## 🛠️ Tecnologías

- **HTML5 Semántico / SVG Nativo**
- **Tailwind CSS (CDN con plugins de formularios y container queries)**
- **GSAP 3.12.5 (GreenSock Animation Platform)**
- **GSAP ScrollTrigger & MorphSVGPlugin**
- **GitHub Pages & GitHub Actions**

---

© 2026 Wonka Bilbao. Todos los derechos reservados.
