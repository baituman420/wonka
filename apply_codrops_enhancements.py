import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add MorphSVGPlugin script in head
if "MorphSVGPlugin.min.js" not in content:
    content = content.replace(
        '<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js"></script>',
        '<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js"></script>\n  <script src="public/assets/js/MorphSVGPlugin.min.js"></script>'
    )

# 2. Add Codrops styles
codrops_css = '''
    /* ==========================================================================
       CODROPS MORPHING SHAPES & ON-SCROLL PATH ANIMATIONS STYLES
       ========================================================================== */
    .morph-bg-container {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;
      z-index: 0;
      overflow: hidden;
    }

    .morph-svg-canvas {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
    }

    .morph-blob {
      will-change: transform, d, fill;
      transform-origin: center center;
    }

    /* On-Scroll Path Wave Separators (Codrops Reference 2) */
    .scroll-separator-wrap {
      position: relative;
      width: 100%;
      overflow: hidden;
      line-height: 0;
      z-index: 20;
      pointer-events: none;
    }

    .scroll-wave-svg {
      display: block;
      width: 100%;
      height: 64px;
    }
    @media (min-width: 640px) {
      .scroll-wave-svg {
        height: 96px;
      }
    }
    @media (min-width: 1024px) {
      .scroll-wave-svg {
        height: 128px;
      }
    }

    .scroll-wave-path {
      will-change: d;
      transition: fill 0.6s ease;
    }
    .scroll-wave-accent {
      will-change: d;
    }
'''

if "morph-bg-container" not in content:
    content = content.replace("</style>", codrops_css + "\n  </style>")

# 3. Add Morphing Background Shapes Markup after body tag
morph_bg_html = '''
  <!-- ==================== CODORPS MORPHING BACKGROUND SHAPES ==================== -->
  <aside class="morph-bg-container" aria-hidden="true" id="morph-bg">
    <svg class="morph-svg-canvas" viewBox="0 0 1600 1200" preserveAspectRatio="xMidYMid slice">
      <defs>
        <!-- Atmospheric Gaussian Filters -->
        <filter id="morph-blur-primary" x="-40%" y="-40%" width="180%" height="180%">
          <feGaussianBlur stdDeviation="80" result="blur" />
        </filter>
        <filter id="morph-blur-secondary" x="-40%" y="-40%" width="180%" height="180%">
          <feGaussianBlur stdDeviation="95" result="blur" />
        </filter>
        <filter id="morph-blur-tertiary" x="-40%" y="-40%" width="180%" height="180%">
          <feGaussianBlur stdDeviation="110" result="blur" />
        </filter>
      </defs>

      <!-- Shape 1: Primary Morphing Organic Mass (Wonka Purple / Sage Green / Warm Ochre) -->
      <path id="morph-shape-primary"
            class="morph-blob"
            filter="url(#morph-blur-primary)"
            fill="#2E1050"
            opacity="0.32"
            d="M 1050,150 C 1380,120 1560,340 1500,620 C 1440,900 1240,1080 960,1040 C 680,1000 520,840 560,580 C 600,320 720,180 1050,150 Z" />

      <!-- Shape 2: Secondary Organic Harmonizer (Warm Amber Gold / Soft Wheat Crema) -->
      <path id="morph-shape-secondary"
            class="morph-blob"
            filter="url(#morph-blur-secondary)"
            fill="#D4A349"
            opacity="0.34"
            d="M 450,220 C 760,180 940,380 900,660 C 860,940 680,1050 420,1020 C 160,990 60,820 90,560 C 120,300 200,260 450,220 Z" />

      <!-- Shape 3: Tertiary Ethereal Aura (Drifting Ambient Light) -->
      <path id="morph-shape-tertiary"
            class="morph-blob"
            filter="url(#morph-blur-tertiary)"
            fill="#FAF0D4"
            opacity="0.25"
            d="M 850,300 C 1120,260 1280,440 1240,680 C 1200,920 1040,1020 820,1000 C 600,980 500,840 530,620 C 560,400 640,340 850,300 Z" />
    </svg>
  </aside>
'''

if "morph-bg" not in content:
    content = content.replace(
        '<body class="theatrical-wallpaper font-body-md text-on-surface antialiased min-h-screen">',
        '<body class="theatrical-wallpaper font-body-md text-on-surface antialiased min-h-screen">\n' + morph_bg_html
    )

# 4. Separator 1: Hero / Selector -> Experiencias
sep1 = '''
    <!-- ==================== CODROPS ON-SCROLL PATH SEPARATOR 1: HERO -> EXPERIENCIAS ==================== -->
    <div class="scroll-separator-wrap -mb-[1px]" aria-hidden="true">
      <svg class="scroll-wave-svg text-[#FAF6ED]" id="svg-wave-exp" viewBox="0 0 1440 120" preserveAspectRatio="none">
        <path class="scroll-wave-path"
              id="wave-path-1"
              fill="currentColor"
              d="M 0,60 C 380,105 1060,15 1440,60 L 1440,120 L 0,120 Z"
              data-path-to="M 0,20 C 440,135 980,-25 1440,85 L 1440,120 L 0,120 Z" />
        <path class="scroll-wave-accent"
              id="wave-accent-1"
              fill="none"
              stroke="#D4A349"
              stroke-width="2"
              stroke-opacity="0.5"
              d="M 0,60 C 380,105 1060,15 1440,60"
              data-path-to="M 0,20 C 440,135 980,-25 1440,85" />
      </svg>
    </div>
'''

if "wave-path-1" not in content:
    content = content.replace("<!-- ==================== TRES EXPERIENCIAS", sep1 + "\n    <!-- ==================== TRES EXPERIENCIAS")

# 5. Separator 2: Experiencias -> Gastronomía
sep2 = '''
    <!-- ==================== CODROPS ON-SCROLL PATH SEPARATOR 2: EXPERIENCIAS -> GASTRONOMIA ==================== -->
    <div class="scroll-separator-wrap -mt-[1px] -mb-[1px]" aria-hidden="true">
      <svg class="scroll-wave-svg text-[#FAF6ED]" id="svg-wave-gastro" viewBox="0 0 1440 120" preserveAspectRatio="none">
        <path class="scroll-wave-path"
              id="wave-path-2"
              fill="currentColor"
              d="M 0,0 L 1440,0 L 1440,60 C 1040,105 380,15 0,60 Z"
              data-path-to="M 0,0 L 1440,0 L 1440,90 C 960,-20 460,130 0,25 Z" />
        <path class="scroll-wave-accent"
              id="wave-accent-2"
              fill="none"
              stroke="#4E5B3F"
              stroke-width="2"
              stroke-opacity="0.45"
              d="M 1440,60 C 1040,105 380,15 0,60"
              data-path-to="M 1440,90 C 960,-20 460,130 0,25" />
      </svg>
    </div>
'''

if "wave-path-2" not in content:
    content = content.replace("<!-- ==================== GASTRONOMIA BENTO", sep2 + "\n    <!-- ==================== GASTRONOMIA BENTO")

# 6. Separator 3: Gastronomía -> Celebraciones
sep3 = '''
    <!-- ==================== CODROPS ON-SCROLL PATH SEPARATOR 3: GASTRONOMIA -> CELEBRACIONES ==================== -->
    <div class="scroll-separator-wrap -mb-[1px]" aria-hidden="true">
      <svg class="scroll-wave-svg text-[#FBF5EA]" id="svg-wave-celeb" viewBox="0 0 1440 120" preserveAspectRatio="none">
        <path class="scroll-wave-path"
              id="wave-path-3"
              fill="currentColor"
              d="M 0,65 C 440,25 1040,105 1440,55 L 1440,120 L 0,120 Z"
              data-path-to="M 0,25 C 520,125 920,-15 1440,85 L 1440,120 L 0,120 Z" />
        <path class="scroll-wave-accent"
              id="wave-accent-3"
              fill="none"
              stroke="#8D6A2A"
              stroke-width="2"
              stroke-opacity="0.5"
              d="M 0,65 C 440,25 1040,105 1440,55"
              data-path-to="M 0,25 C 520,125 920,-15 1440,85" />
      </svg>
    </div>
'''

if "wave-path-3" not in content:
    content = content.replace("<!-- ==================== CELEBRACIONES & ENCUENTROS", sep3 + "\n    <!-- ==================== CELEBRACIONES & ENCUENTROS")

# 7. Separator 4: Celebraciones -> Footer
sep4 = '''
    <!-- ==================== CODROPS ON-SCROLL PATH SEPARATOR 4: CELEBRACIONES -> FOOTER ==================== -->
    <div class="scroll-separator-wrap -mb-[1px]" aria-hidden="true">
      <svg class="scroll-wave-svg text-[#F5EFE3]" id="svg-wave-footer" viewBox="0 0 1440 120" preserveAspectRatio="none">
        <path class="scroll-wave-path"
              id="wave-path-4"
              fill="currentColor"
              d="M 0,55 C 460,95 980,15 1440,60 L 1440,120 L 0,120 Z"
              data-path-to="M 0,20 C 380,115 1040,-15 1440,75 L 1440,120 L 0,120 Z" />
        <path class="scroll-wave-accent"
              id="wave-accent-4"
              fill="none"
              stroke="#D4A349"
              stroke-width="2"
              stroke-opacity="0.5"
              d="M 0,55 C 460,95 980,15 1440,60"
              data-path-to="M 0,20 C 380,115 1040,-15 1440,75" />
      </svg>
    </div>
'''

if "wave-path-4" not in content:
    content = content.replace("<!-- ==================== FOOTER (PROMINENT OFFICIAL LOGO)", sep4 + "\n  <!-- ==================== FOOTER (PROMINENT OFFICIAL LOGO)")

# 8. Script enhancements: Register MorphSVGPlugin, add toggleColorExperience morph updates, and add full Codrops scroll timeline
old_register = "gsap.registerPlugin(ScrollTrigger);"
new_register = """gsap.registerPlugin(ScrollTrigger);
    if (typeof MorphSVGPlugin !== 'undefined') {
      gsap.registerPlugin(MorphSVGPlugin);
    }"""
content = content.replace(old_register, new_register, 1)

# Enhance toggleColorExperience to update Morphing Background Shapes and wave colors
old_toggle_start = "function toggleColorExperience(experience) {"
new_toggle_start = """function toggleColorExperience(experience) {
      // Update wave separators to blend with active atmosphere
      const waveExp = document.getElementById('svg-wave-exp');
      const waveGastro = document.getElementById('svg-wave-gastro');
      if (waveExp && colorThemes[experience]) waveExp.style.color = colorThemes[experience].bg;
      if (waveGastro && colorThemes[experience]) waveGastro.style.color = colorThemes[experience].bg;

      // Update Morphing Background Shapes in real time
      if (typeof gsap !== 'undefined') {
        const prim = document.getElementById('morph-shape-primary');
        const sec = document.getElementById('morph-shape-secondary');
        const tert = document.getElementById('morph-shape-tertiary');
        
        if (experience === 'house') {
          if (prim) gsap.to(prim, { fill: '#4E5B3F', duration: 1.1, ease: 'power2.out', overwrite: 'auto' });
          if (sec) gsap.to(sec, { fill: '#D4A349', duration: 1.1, ease: 'power2.out', overwrite: 'auto' });
          if (tert) gsap.to(tert, { fill: '#FAF0D4', duration: 1.1, ease: 'power2.out', overwrite: 'auto' });
        } else if (experience === 'lounge') {
          if (prim) gsap.to(prim, { fill: '#2E1050', duration: 1.1, ease: 'power2.out', overwrite: 'auto' });
          if (sec) gsap.to(sec, { fill: '#8D6A2A', duration: 1.1, ease: 'power2.out', overwrite: 'auto' });
          if (tert) gsap.to(tert, { fill: '#D4A349', duration: 1.1, ease: 'power2.out', overwrite: 'auto' });
        } else if (experience === 'bar') {
          if (prim) gsap.to(prim, { fill: '#8D6A2A', duration: 1.1, ease: 'power2.out', overwrite: 'auto' });
          if (sec) gsap.to(sec, { fill: '#4E5B3F', duration: 1.1, ease: 'power2.out', overwrite: 'auto' });
          if (tert) gsap.to(tert, { fill: '#2E1050', duration: 1.1, ease: 'power2.out', overwrite: 'auto' });
        }
      }"""
content = content.replace(old_toggle_start, new_toggle_start, 1)

# Add Codrops engine at the end of the script before </script>
codrops_js = """
    // -------------------------------------------------------------------------
    // CODROPS COMBINED ENGINE: MORPHING BACKGROUND SHAPES + ON-SCROLL PATH ANIMATIONS
    // -------------------------------------------------------------------------
    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
      const mm = gsap.matchMedia();

      mm.add({
        isMotionOK: "(prefers-reduced-motion: no-preference)",
        reduceMotion: "(prefers-reduced-motion: reduce)",
        isMobile: "(max-width: 768px)",
        isDesktop: "(min-width: 769px)"
      }, (context) => {
        const { isMotionOK, reduceMotion, isMobile } = context.conditions;

        if (!isMotionOK || typeof MorphSVGPlugin === 'undefined') {
          return;
        }

        // 1. CODROPS ON-SCROLL PATH ANIMATIONS (Separadores ondulados animados)
        gsap.utils.toArray('.scroll-wave-path').forEach(path => {
          const svg = path.closest('svg');
          const targetD = path.getAttribute('data-path-to');
          if (targetD && svg) {
            gsap.to(path, {
              morphSVG: targetD,
              ease: "none",
              scrollTrigger: {
                trigger: svg,
                start: "top bottom",
                end: "bottom top",
                scrub: 1.2
              }
            });
          }
        });

        gsap.utils.toArray('.scroll-wave-accent').forEach(line => {
          const svg = line.closest('svg');
          const targetD = line.getAttribute('data-path-to');
          if (targetD && svg) {
            gsap.to(line, {
              morphSVG: targetD,
              ease: "none",
              scrollTrigger: {
                trigger: svg,
                start: "top bottom",
                end: "bottom top",
                scrub: 1.2
              }
            });
          }
        });

        // 2. CODROPS MORPHING BACKGROUND SHAPES (Fondos orgánicos con morphing)
        const morphShapes = {
          hero: {
            p: "M 1050,150 C 1380,120 1560,340 1500,620 C 1440,900 1240,1080 960,1040 C 680,1000 520,840 560,580 C 600,320 720,180 1050,150 Z",
            s: "M 450,220 C 760,180 940,380 900,660 C 860,940 680,1050 420,1020 C 160,990 60,820 90,560 C 120,300 200,260 450,220 Z",
            t: "M 850,300 C 1120,260 1280,440 1240,680 C 1200,920 1040,1020 820,1000 C 600,980 500,840 530,620 C 560,400 640,340 850,300 Z"
          },
          experiencias: {
            p: "M 920,120 C 1280,160 1520,440 1460,740 C 1400,1040 1140,1120 840,1060 C 540,1000 440,780 480,520 C 520,260 620,100 920,120 Z",
            s: "M 520,140 C 840,180 1020,440 960,760 C 900,1080 660,1120 380,1040 C 100,960 40,700 80,420 C 120,140 220,100 520,140 Z",
            t: "M 980,260 C 1240,220 1400,420 1350,680 C 1300,940 1100,1060 880,1020 C 660,980 620,800 650,560 C 680,320 740,280 980,260 Z"
          },
          gastronomia: {
            p: "M 1120,160 C 1440,140 1580,420 1520,700 C 1460,980 1280,1100 980,1080 C 680,1060 480,880 500,600 C 520,320 720,200 1120,160 Z",
            s: "M 420,180 C 740,140 920,380 880,680 C 840,980 680,1080 400,1040 C 120,1000 60,780 80,480 C 100,180 180,140 420,180 Z",
            t: "M 760,220 C 1040,180 1220,380 1180,640 C 1140,900 960,1020 720,980 C 480,940 440,760 470,520 C 500,280 560,240 760,220 Z"
          },
          celebraciones: {
            p: "M 980,140 C 1300,180 1500,420 1440,720 C 1380,1020 1160,1100 860,1040 C 560,980 460,760 500,480 C 540,200 680,120 980,140 Z",
            s: "M 500,160 C 800,140 980,400 920,700 C 860,1000 660,1100 380,1040 C 100,980 40,740 70,440 C 100,140 220,100 500,160 Z",
            t: "M 880,240 C 1160,200 1340,400 1280,680 C 1220,960 1020,1060 780,1020 C 540,980 500,780 530,520 C 560,260 640,240 880,240 Z"
          },
          footer: {
            p: "M 1020,180 C 1320,160 1480,380 1420,660 C 1360,940 1180,1060 920,1020 C 660,980 540,820 560,560 C 580,300 740,220 1020,180 Z",
            s: "M 480,200 C 760,180 920,400 880,680 C 840,960 680,1050 420,1000 C 160,950 80,780 110,500 C 140,220 220,180 480,200 Z",
            t: "M 820,280 C 1080,240 1240,440 1200,680 C 1160,920 1000,1020 780,980 C 560,940 520,780 550,560 C 580,340 640,300 820,280 Z"
          }
        };

        // ScrollTrigger Transition 1: Hero -> Experiencias
        gsap.timeline({
          scrollTrigger: {
            trigger: '#experiencias',
            start: 'top 85%',
            end: 'top 20%',
            scrub: 1.4
          }
        })
        .to('#morph-shape-primary', {
          morphSVG: morphShapes.experiencias.p,
          fill: '#4E5B3F',
          x: isMobile ? -20 : -60,
          y: isMobile ? 30 : 70,
          scale: 1.05,
          ease: 'none'
        }, 0)
        .to('#morph-shape-secondary', {
          morphSVG: morphShapes.experiencias.s,
          fill: '#8D6A2A',
          x: isMobile ? 20 : 60,
          y: isMobile ? -20 : -40,
          scale: 1.08,
          ease: 'none'
        }, 0)
        .to('#morph-shape-tertiary', {
          morphSVG: morphShapes.experiencias.t,
          fill: '#2E1050',
          opacity: 0.20,
          ease: 'none'
        }, 0);

        // ScrollTrigger Transition 2: Experiencias -> Gastronomía
        gsap.timeline({
          scrollTrigger: {
            trigger: '#gastronomia',
            start: 'top 85%',
            end: 'top 20%',
            scrub: 1.4
          }
        })
        .to('#morph-shape-primary', {
          morphSVG: morphShapes.gastronomia.p,
          fill: '#4E5B3F',
          x: isMobile ? -40 : -120,
          y: isMobile ? 40 : 90,
          scale: 1.12,
          ease: 'none'
        }, 0)
        .to('#morph-shape-secondary', {
          morphSVG: morphShapes.gastronomia.s,
          fill: '#D4A349',
          x: isMobile ? 40 : 100,
          y: isMobile ? 30 : 60,
          scale: 1.15,
          ease: 'none'
        }, 0)
        .to('#morph-shape-tertiary', {
          morphSVG: morphShapes.gastronomia.t,
          fill: '#EBD8B8',
          opacity: 0.28,
          ease: 'none'
        }, 0);

        // ScrollTrigger Transition 3: Gastronomía -> Celebraciones
        gsap.timeline({
          scrollTrigger: {
            trigger: '#celebraciones',
            start: 'top 85%',
            end: 'top 20%',
            scrub: 1.4
          }
        })
        .to('#morph-shape-primary', {
          morphSVG: morphShapes.celebraciones.p,
          fill: '#2E1050',
          x: isMobile ? 20 : 50,
          y: isMobile ? -20 : -40,
          scale: 1.18,
          ease: 'none'
        }, 0)
        .to('#morph-shape-secondary', {
          morphSVG: morphShapes.celebraciones.s,
          fill: '#D4A349',
          x: isMobile ? -30 : -80,
          y: isMobile ? 30 : 50,
          scale: 1.22,
          ease: 'none'
        }, 0)
        .to('#morph-shape-tertiary', {
          morphSVG: morphShapes.celebraciones.t,
          fill: '#8D6A2A',
          opacity: 0.26,
          ease: 'none'
        }, 0);

        // ScrollTrigger Transition 4: Celebraciones -> Footer
        gsap.timeline({
          scrollTrigger: {
            trigger: '#contacto',
            start: 'top 90%',
            end: 'top 30%',
            scrub: 1.4
          }
        })
        .to('#morph-shape-primary', {
          morphSVG: morphShapes.footer.p,
          fill: '#8D6A2A',
          x: 0,
          y: 60,
          scale: 0.95,
          ease: 'none'
        }, 0)
        .to('#morph-shape-secondary', {
          morphSVG: morphShapes.footer.s,
          fill: '#2E1050',
          x: 0,
          y: -30,
          scale: 0.98,
          ease: 'none'
        }, 0);
      });
    }
"""

content = content.replace("</script>\n</body>", codrops_js + "\n  </script>\n</body>")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("index.html updated successfully with Codrops Morphing Shapes & On-Scroll Path Animations!")
