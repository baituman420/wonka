# DESIGN.md — Wonka Bilbao Design System

## Modos y Dirección Artística
- **Modo Primario**: Persuade + Experience (Landing editorial de alta cocina y vida urbana).
- **Inspiración**: Google Stitch export 'Portada Editorial con Carácter y Color', refinado con Impeccable (pbakaus) y Emil Design Engineering (emilkowalski).

## Paleta de Color & Tokens
- **Canvas / Superficie**: `#FDF9F0` (Marfil cálido Bilbao)
- **Contenedores de Superficie**: `#F4EFE6` (Arena suave), `#FAF6ED` (Crema claro), `#ECE5D8` (Piedra)
- **Texto Principal**: `#1E1A17` (Casi negro cálido, contraste > 10:1)
- **Texto Secundario**: `#59544B` (Pardo neutro cálido, contraste > 5.5:1)
- **Bordes & Separadores**: `#E6DFD0`, `#DED7C8`
- **Experiencias Wonka**:
  - **Wonka Bar**: `#8D6A2A` (Ámbar dorado) | Fondo claro: `#FAF3E3`
  - **Wonka House**: `#4E5B3F` (Verde oliva bosque) | Fondo claro: `#EEF2E8`
  - **Wonka Lounge**: `#2E1050` (Violeta nocturno regio) | Fondo claro: `#F4EEFA`

## Tipografía
- **Display / Titulares**: *Playfair Display* (Serif editorial, tracking -0.02em, pesos 400 y 600 cursiva).
- **Lectura / UI**: *Plus Jakarta Sans* (Sans geométrica de alta legibilidad, pesos 400, 500, 600, 700).

## Filosofía de Animación & Microinteracciones (Emil Kowalski)
- **Curvas de Aceleración Personalizadas**:
  - `--ease-out: cubic-bezier(0.23, 1, 0.32, 1)` (UI reactiva)
  - `--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1)` (Transiciones cromáticas de página)
  - `--ease-spring: cubic-bezier(0.175, 0.885, 0.32, 1.275)` (Física de rebote para el sombrero y selector)
- **Feedback Háptico Visual**:
  - `:active` con `transform: scale(0.97)` en 160ms ease-out en todos los botones y selectores.
- **Entradas Orgánicas**:
  - Jamás animar desde `scale(0)`; siempre desde `scale(0.95)` con opacidad.
- **Transición de Color sin Saltos**:
  - Desenfoque sutil (`filter: blur(2px)`) en capas de cambio de ambiente para fusionar la paleta de las tres experiencias.
