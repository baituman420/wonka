import re

with open('public/assets/logos/wonka-top-hat.svg', 'r', encoding='utf-8') as f:
    svg_hat_raw = f.read().strip()

svg_hat = re.sub(r'<\?xml[^>]*\?>', '', svg_hat_raw).strip()

html_content = f'''<!DOCTYPE html>
<html class="scroll-smooth" lang="es">
<head>
  <meta charset="utf-8" />
  <meta content="width=device-width, initial-scale=1.0" name="viewport" />
  <meta content="Wonka Bilbao · Una marca. Tres experiencias gastronómicas en Bilbao: Wonka House, Wonka Lounge y Wonka Bar." name="description" />
  <title>Wonka Bilbao — Una Marca. Tres Experiencias.</title>
  
  <!-- Favicon with Wonka Hat SVG -->
  <link rel="icon" type="image/svg+xml" href="public/assets/logos/wonka-top-hat.svg" />
  
  <!-- Typography -->
  <link href="https://fonts.googleapis.com" rel="preconnect" />
  <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect" />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet" />
  
  <!-- GSAP 3 (GreenSock Animation Platform) & ScrollTrigger CDN -->
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js"></script>
  
  <style>
    /* ==========================================================================
       THEATRICAL SCENIC & DESIGN ENGINEERING TOKENS
       ========================================================================== */
    :root {{
      --ease-out: cubic-bezier(0.23, 1, 0.32, 1);
      --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);
      --ease-spring: cubic-bezier(0.175, 0.885, 0.32, 1.275);
      --ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);
      --duration-press: 160ms;
      --duration-ui: 240ms;
      --gold-primary: #8D6A2A;
      --gold-light: #D4A349;
      --purple-primary: #2E1050;
      --green-primary: #4E5B3F;
    }}

    @layer base {{
      html, body {{
        margin: 0;
        padding: 0;
        background-color: #FDF9F0;
        color: #1E1A17;
      }}
      body {{
        overscroll-behavior-y: none;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
      }}
    }}

    /* Theatrical Scenic Wallpaper (Art Déco Arcade Pattern & Soft Texture) */
    .theatrical-wallpaper {{
      background-color: #FDF9F0;
      background-image: 
        radial-gradient(ellipse at 50% -10%, rgba(212, 163, 73, 0.22) 0%, rgba(253, 249, 240, 0) 65%),
        radial-gradient(circle at 90% 25%, rgba(46, 16, 80, 0.10) 0%, transparent 45%),
        radial-gradient(circle at 10% 75%, rgba(78, 91, 63, 0.09) 0%, transparent 45%),
        url('public/assets/brand/art-deco-arcade-pattern.svg');
      background-repeat: repeat;
      background-size: auto, auto, auto, 120px 120px;
    }}

    /* Browser Surfaces Theming (Impeccable Craft Floor) */
    ::selection {{
      background: #2E1050;
      color: #FAF3E3;
    }}
    ::-moz-selection {{
      background: #2E1050;
      color: #FAF3E3;
    }}

    /* Custom Subtle Scrollbar */
    ::-webkit-scrollbar {{
      width: 8px;
      height: 8px;
    }}
    ::-webkit-scrollbar-track {{
      background: #F4EFE6;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #D5CEBF;
      border-radius: 4px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #8D6A2A;
    }}

    /* Focus States */
    :focus-visible {{
      outline: 2px solid #2E1050;
      outline-offset: 3px;
    }}

    /* Emil Kowalski Press Feedback (:active scale) */
    .btn-press, button, a[role="button"], .chip-interactive {{
      transition: transform var(--duration-press) var(--ease-out), 
                  box-shadow var(--duration-ui) var(--ease-out),
                  background-color var(--duration-ui) var(--ease-out),
                  color var(--duration-ui) var(--ease-out),
                  border-color var(--duration-ui) var(--ease-out);
      user-select: none;
      -webkit-user-select: none;
    }}
    .btn-press:active, button:active, a[role="button"]:active, .chip-interactive:active {{
      transform: scale(0.97) !important;
    }}

    /* Theatrical Proscenium Arched Frames */
    .proscenium-frame {{
      position: relative;
      border-radius: 28px;
      border: 1px solid rgba(212, 163, 73, 0.35);
      box-shadow: 0 16px 36px -10px rgba(46, 16, 80, 0.12), 
                  inset 0 0 0 1px rgba(255, 255, 255, 0.6);
      transition: box-shadow 0.4s var(--ease-out), border-color 0.4s var(--ease-out), transform 0.4s var(--ease-out);
    }}
    .proscenium-frame:hover {{
      border-color: rgba(212, 163, 73, 0.7);
      box-shadow: 0 24px 50px -12px rgba(141, 106, 42, 0.22),
                  inset 0 0 0 1px rgba(255, 255, 255, 0.85);
    }}

    /* Ambient Stage Dynamic Glow */
    #ambient-stage-glow {{
      position: absolute;
      inset: 0;
      pointer-events: none;
      opacity: 0.85;
      transition: background 0.8s var(--ease-in-out);
      z-index: 1;
    }}

    /* Focused Experience Card Glow */
    .card-active-experience {{
      transform: translateY(-8px) scale(1.02);
      box-shadow: 0 24px 45px -12px rgba(46, 16, 80, 0.22), 0 0 0 3px var(--exp-accent, #2E1050) !important;
    }}

    /* Sparkles & Dust Canvas Overlay */
    #theatrical-canvas {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 30;
    }}

    /* Mobile Drawer Transitions */
    #mobile-drawer {{
      transition: transform 0.35s var(--ease-drawer);
    }}
    #mobile-drawer-backdrop {{
      transition: opacity 0.3s var(--ease-out);
    }}

    /* Reduced Motion Accessibility */
    @media (prefers-reduced-motion: reduce) {{
      * {{
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
      }}
    }}
  </style>

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
  <script id="tailwind-config">
    tailwind.config = {{
      darkMode: "class",
      theme: {{
        extend: {{
          colors: {{
            "surface": "#FDF9F0",
            "surface-container": "#F4EFE6",
            "surface-container-low": "#FAF6ED",
            "surface-container-high": "#ECE5D8",
            "surface-container-highest": "#E4DDD0",
            "primary": "#2E1050",
            "on-surface": "#1E1A17",
            "on-surface-variant": "#59544B",
            "outline-variant": "#DED7C8",
            // The Three Wonka Brand Experiences:
            "wonka-house": "#4E5B3F",
            "wonka-house-light": "#EEF2E8",
            "wonka-house-dark": "#37412C",
            "wonka-lounge": "#2E1050",
            "wonka-lounge-light": "#F4EEFA",
            "wonka-lounge-dark": "#1A072E",
            "wonka-bar": "#8D6A2A",
            "wonka-bar-light": "#FAF3E3",
            "wonka-bar-dark": "#5E4416",
            "gold-accent": "#D4A349"
          }},
          fontFamily: {{
            "display-hero": ["Playfair Display", "serif"],
            "headline-lg": ["Playfair Display", "serif"],
            "headline-md": ["Playfair Display", "serif"],
            "headline-sm": ["Playfair Display", "serif"],
            "body-lg": ["Plus Jakarta Sans", "sans-serif"],
            "body-md": ["Plus Jakarta Sans", "sans-serif"],
            "body-sm": ["Plus Jakarta Sans", "sans-serif"],
            "label-uppercase": ["Plus Jakarta Sans", "sans-serif"],
            "label-md": ["Plus Jakarta Sans", "sans-serif"]
          }},
          spacing: {{
            "margin-mobile": "1.25rem",
            "margin-desktop": "4rem",
            "space-xs": "0.25rem",
            "space-sm": "0.5rem",
            "space-md": "1rem",
            "space-lg": "1.75rem",
            "space-xl": "3rem",
            "gutter-desktop": "2.5rem"
          }}
        }}
      }}
    }};
  </script>
</head>

<body class="theatrical-wallpaper font-body-md text-on-surface antialiased min-h-screen">

  <!-- ==================== DEMO COMMERCIAL CONTROLLER ==================== -->
  <aside aria-label="Controlador de Demo" class="fixed bottom-5 right-5 z-50 flex items-center gap-2.5 bg-[#1E1A17]/95 text-white backdrop-blur-md px-4 py-2.5 rounded-full shadow-2xl border border-[#D4A349]/40 text-xs">
    <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
    <span class="font-label-uppercase font-bold tracking-wider text-[#FAF0D4] hidden sm:inline">Demo Comercial</span>
    <span class="text-white/30 hidden sm:inline">|</span>
    <div class="flex items-center gap-1.5">
      <button onclick="selectPlan('bar')" class="chip-interactive px-2.5 py-1 rounded-full bg-wonka-bar text-white text-[10px] font-bold uppercase hover:brightness-110" title="Ver Wonka Bar">Bar</button>
      <button onclick="selectPlan('house')" class="chip-interactive px-2.5 py-1 rounded-full bg-wonka-house text-white text-[10px] font-bold uppercase hover:brightness-110" title="Ver Wonka House">House</button>
      <button onclick="selectPlan('lounge')" class="chip-interactive px-2.5 py-1 rounded-full bg-wonka-lounge text-white text-[10px] font-bold uppercase hover:brightness-110" title="Ver Wonka Lounge">Lounge</button>
    </div>
  </aside>

  <!-- ==================== HEADER (AUTHENTIC WONKA BILBAO BRANDMARK) ==================== -->
  <header class="fixed top-0 left-0 right-0 z-40 bg-[#FDF9F0]/92 backdrop-blur-md border-b border-[#E7DFD0] transition-all duration-300" id="main-header">
    <div class="h-20 sm:h-22 w-full px-margin-mobile lg:px-margin-desktop flex items-center justify-between max-w-[1440px] mx-auto">
      
      <!-- Brand Identity: Authentic Wonka Bilbao Wordmark with Top Hat -->
      <a class="group flex items-center gap-3 focus-visible:ring-2 focus-visible:ring-wonka-lounge rounded-xl py-1 px-2 -ml-2 transition-transform duration-300 hover:scale-[1.02]" href="#" title="Wonka Bilbao — Inicio">
        <img 
          src="public/assets/logos/wonka-bilbao-logo-purple.png" 
          alt="Wonka Bilbao — Logotipo Oficial" 
          class="h-10 sm:h-12 w-auto object-contain filter drop-shadow-sm group-hover:drop-shadow transition-all"
        />
        <div class="hidden xl:flex flex-col border-l border-[#D5CEBF] pl-3 ml-1">
          <span class="font-label-uppercase text-[10px] tracking-[0.24em] text-wonka-bar uppercase font-bold">
            Una marca · Tres experiencias
          </span>
          <span class="font-body-sm text-[11px] text-on-surface-variant">
            Bilbao, Bizkaia
          </span>
        </div>
      </a>

      <!-- Desktop Navigation Links -->
      <nav class="hidden lg:flex items-center gap-8" aria-label="Navegación principal">
        <a class="font-label-uppercase text-[12px] tracking-[0.16em] text-on-surface-variant hover:text-wonka-lounge transition-colors uppercase py-1 relative group" href="#experiencias">
          Experiencias
          <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-wonka-lounge transition-all duration-300 group-hover:w-full"></span>
        </a>
        <a class="font-label-uppercase text-[12px] tracking-[0.16em] text-on-surface-variant hover:text-wonka-house transition-colors uppercase py-1 relative group" href="#gastronomia">
          Gastronomía
          <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-wonka-house transition-all duration-300 group-hover:w-full"></span>
        </a>
        <a class="font-label-uppercase text-[12px] tracking-[0.16em] text-on-surface-variant hover:text-wonka-bar transition-colors uppercase py-1 relative group" href="#celebraciones">
          Celebraciones
          <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-wonka-bar transition-all duration-300 group-hover:w-full"></span>
        </a>
        <a class="font-label-uppercase text-[12px] tracking-[0.16em] text-on-surface-variant hover:text-wonka-lounge transition-colors uppercase py-1 relative group" href="#celebraciones">
          Contacto
          <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-wonka-lounge transition-all duration-300 group-hover:w-full"></span>
        </a>
      </nav>

      <!-- Action Buttons & Mobile Hamburger -->
      <div class="flex items-center gap-3">
        <a class="btn-press hidden sm:inline-flex items-center justify-center font-label-uppercase text-[11px] uppercase tracking-[0.18em] font-bold px-6 py-3 border-2 border-wonka-bar text-wonka-bar hover:bg-wonka-bar hover:text-white rounded-full shadow-sm" href="#celebraciones">
          Reservas &amp; Eventos
        </a>
        <a class="btn-press hidden md:inline-flex items-center justify-center font-label-uppercase text-[11px] uppercase tracking-[0.18em] font-bold px-6 py-3 bg-wonka-lounge text-white rounded-full hover:bg-[#3D1768] hover:shadow-lg" href="#experiencias">
          Explorar
        </a>
        
        <!-- Mobile Hamburger Toggle -->
        <button 
          id="mobile-menu-btn"
          onclick="toggleMobileMenu()"
          aria-label="Abrir menú" 
          class="btn-press lg:hidden p-2 rounded-xl text-on-surface hover:bg-[#F4EFE6] focus-visible:ring-2 focus-visible:ring-wonka-lounge"
        >
          <span class="material-symbols-outlined text-2xl" id="menu-icon">menu</span>
        </button>
      </div>
    </div>
  </header>

  <!-- ==================== MOBILE SLIDE-OUT DRAWER ==================== -->
  <div id="mobile-drawer-backdrop" class="fixed inset-0 bg-black/60 z-50 backdrop-blur-xs opacity-0 pointer-events-none transition-opacity duration-300" onclick="toggleMobileMenu()"></div>
  <aside id="mobile-drawer" class="fixed top-0 right-0 bottom-0 w-[84vw] max-w-sm bg-surface z-50 p-6 shadow-2xl flex flex-col justify-between transform translate-x-full border-l border-[#E6DFD0]">
    <div>
      <div class="flex items-center justify-between pb-6 border-b border-[#E6DFD0]">
        <img 
          src="public/assets/logos/wonka-bilbao-logo-purple.png" 
          alt="Wonka Bilbao" 
          class="h-9 w-auto object-contain"
        />
        <button onclick="toggleMobileMenu()" class="btn-press p-2 rounded-full hover:bg-[#F4EFE6] text-on-surface" aria-label="Cerrar menú">
          <span class="material-symbols-outlined">close</span>
        </button>
      </div>

      <nav class="flex flex-col gap-5 pt-8" aria-label="Navegación móvil">
        <a onclick="toggleMobileMenu()" href="#experiencias" class="font-headline-sm text-2xl text-on-surface hover:text-wonka-lounge transition-colors">Experiencias</a>
        <a onclick="toggleMobileMenu()" href="#gastronomia" class="font-headline-sm text-2xl text-on-surface hover:text-wonka-house transition-colors">Gastronomía</a>
        <a onclick="toggleMobileMenu()" href="#celebraciones" class="font-headline-sm text-2xl text-on-surface hover:text-wonka-bar transition-colors">Celebraciones &amp; Eventos</a>
        <a onclick="toggleMobileMenu()" href="#selector-plan" class="font-headline-sm text-2xl text-on-surface hover:text-wonka-lounge transition-colors">¿Qué plan buscas hoy?</a>
      </nav>

      <div class="pt-8 mt-6 border-t border-[#E6DFD0]">
        <span class="font-label-uppercase text-[11px] font-bold text-wonka-bar uppercase tracking-widest block mb-3">Accesos directos</span>
        <div class="grid grid-cols-3 gap-2">
          <button onclick="toggleMobileMenu(); selectPlan('house')" class="p-2 rounded-xl bg-wonka-house-light text-wonka-house text-center text-xs font-bold font-label-uppercase">House</button>
          <button onclick="toggleMobileMenu(); selectPlan('lounge')" class="p-2 rounded-xl bg-wonka-lounge-light text-wonka-lounge text-center text-xs font-bold font-label-uppercase">Lounge</button>
          <button onclick="toggleMobileMenu(); selectPlan('bar')" class="p-2 rounded-xl bg-wonka-bar-light text-wonka-bar text-center text-xs font-bold font-label-uppercase">Bar</button>
        </div>
      </div>
    </div>

    <div class="pt-6 border-t border-[#E6DFD0]">
      <a onclick="toggleMobileMenu()" href="#celebraciones" class="btn-press w-full py-3.5 bg-wonka-lounge text-white rounded-full font-label-uppercase text-xs uppercase tracking-widest font-bold flex items-center justify-center gap-2">
        <span>Reservar espacio (Demo)</span>
        <span class="material-symbols-outlined text-sm">arrow_forward</span>
      </a>
    </div>
  </aside>

  <!-- ==================== MAIN CONTENT ==================== -->
  <main class="w-full pt-20 sm:pt-24 relative overflow-hidden">
    <!-- Atmospheric Canvas for Ambient Gold Dust & Hat Sparkles -->
    <canvas id="theatrical-canvas"></canvas>

    <!-- ==================== HERO SECTION (BELLE ÉPOQUE ARCADE THEATRICALITY) ==================== -->
    <section class="w-full pt-10 pb-16 lg:pt-16 lg:pb-20 px-margin-mobile lg:px-margin-desktop relative" id="hero-section">
      
      <!-- Theatrical Arch Light Header Banner -->
      <div class="max-w-[1440px] mx-auto relative z-10">
        
        <!-- Micro Strip: Three Spheres & City Identity -->
        <div class="flex flex-wrap items-center justify-between gap-4 mb-8 pb-4 border-b border-[#E6DFD0]/80">
          <div class="flex items-center gap-2.5">
            <span class="w-2.5 h-2.5 rounded-full bg-wonka-house ring-2 ring-wonka-house/30" title="Wonka House"></span>
            <span class="w-2.5 h-2.5 rounded-full bg-wonka-lounge ring-2 ring-wonka-lounge/30" title="Wonka Lounge"></span>
            <span class="w-2.5 h-2.5 rounded-full bg-wonka-bar ring-2 ring-wonka-bar/30" title="Wonka Bar"></span>
            <span class="font-label-uppercase text-[11px] uppercase tracking-[0.24em] text-wonka-lounge font-bold ml-1">
              Bilbao · Sabores, Encuentros &amp; Carácter Propio
            </span>
          </div>

          <div class="flex items-center gap-2">
            <button onclick="selectPlan('house')" class="chip-interactive px-3 py-1 rounded-full text-[11px] font-label-uppercase font-semibold tracking-wider bg-wonka-house-light text-wonka-house border border-wonka-house/30">
              House
            </button>
            <button onclick="selectPlan('lounge')" class="chip-interactive px-3 py-1 rounded-full text-[11px] font-label-uppercase font-semibold tracking-wider bg-wonka-lounge-light text-wonka-lounge border border-wonka-lounge/30">
              Lounge
            </button>
            <button onclick="selectPlan('bar')" class="chip-interactive px-3 py-1 rounded-full text-[11px] font-label-uppercase font-semibold tracking-wider bg-wonka-bar-light text-wonka-bar border border-wonka-bar/30">
              Bar
            </button>
          </div>
        </div>

        <!-- Editorial Hero Headline with GSAP Interactive Centerpiece Hat -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-gutter-desktop items-end mb-12">
          <div class="lg:col-span-8">
            <h1 class="font-display-hero text-[42px] sm:text-[62px] lg:text-[78px] text-on-surface tracking-[-0.025em] leading-[1.03] uppercase font-normal select-none">
              UNA MARCA.<br />
              <span class="italic font-normal lowercase tracking-tight text-wonka-lounge font-display-hero inline-flex items-center gap-3 relative">
                <span>tres</span>
                
                <!-- HERO BESPOKE TOP HAT (GSAP Choreographed Centerpiece) -->
                <span 
                  class="inline-block -mt-5 -ml-1 cursor-pointer select-none" 
                  title="Toca o haz clic para inclinar el sombrero de Wonka" 
                  id="hat-interactive-trigger"
                >
                  <div class="w-16 h-16 sm:w-20 sm:h-20 lg:w-24 lg:h-24 filter drop-shadow-md" id="hero-wonka-hat">
                    {svg_hat}
                  </div>
                </span>
              </span> 
              EXPERIENCIAS.
            </h1>
          </div>

          <div class="lg:col-span-4 flex flex-col justify-end">
            <p class="font-body-lg text-[16px] lg:text-[17px] text-on-surface-variant font-light leading-relaxed mb-6">
              Arraigado en el pulso gastronómico y social de Bilbao, Wonka reúne en una sola casa tres espacios complementarios para comer bien, brindar con ganas y compartir sin prisas.
            </p>
            <div class="flex flex-wrap items-center gap-4">
              <a class="btn-press inline-flex items-center justify-center font-label-uppercase text-[12px] uppercase tracking-[0.18em] font-bold px-7 py-4 bg-wonka-lounge text-white rounded-full hover:bg-[#3E166C] hover:shadow-xl" href="#experiencias">
                Descubre los espacios
              </a>
              <a class="btn-press inline-flex items-center gap-2 font-label-md text-[14px] font-semibold text-wonka-bar hover:text-wonka-lounge transition-colors group" href="#gastronomia">
                <span>Ver gastronomía</span>
                <span class="material-symbols-outlined text-[18px] group-hover:translate-x-1.5 transition-transform">east</span>
              </a>
            </div>
          </div>
        </div>

        <!-- Hero Visual: Shared Table Feast in Grand Proscenium Arch Frame -->
        <div class="relative w-full aspect-[16/9] lg:aspect-[21/9] min-h-[380px] bg-surface-container rounded-[32px] overflow-hidden proscenium-frame group">
          <img 
            alt="Mesa gastronómica compartida en Wonka Bilbao con pulpo, raciones, ibéricos, ensalada y vino" 
            class="w-full h-full object-cover object-center transform group-hover:scale-[1.02] transition-transform duration-1000 ease-out" 
            src="public/assets/images/mesa-compartida-hero.jpg"
            loading="eager"
            fetchpriority="high"
          />
          <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/25 to-transparent pointer-events-none"></div>

          <!-- Theatrical Floating Badge -->
          <div class="absolute top-5 right-5 hidden sm:flex items-center gap-2 bg-[#FDF9F0]/92 backdrop-blur-md px-4 py-2 rounded-full border border-wonka-bar/40 shadow-lg">
            <span class="w-2.5 h-2.5 rounded-full bg-wonka-bar animate-ping"></span>
            <span class="font-label-uppercase text-[11px] font-bold text-wonka-lounge tracking-wider">Sabor &amp; Vida Bilbaína</span>
          </div>

          <!-- Bottom Narrative Ribbon -->
          <div class="absolute bottom-6 left-6 right-6 flex flex-wrap items-center justify-between text-white gap-3">
            <div class="flex items-center gap-3">
              <span class="font-label-uppercase text-[11px] tracking-[0.2em] uppercase backdrop-blur-md bg-wonka-lounge/90 px-4 py-2 rounded-full border border-wonka-bar/40 text-[#FAF3E3] font-bold shadow-md">
                Mesa Compartida · El placer de quedarse sin prisas
              </span>
              <span class="font-body-sm text-[13px] tracking-wide text-white/90 hidden sm:inline-block">
                Raciones generosas, buen producto y brindis espontáneos
              </span>
            </div>
            <span class="font-label-uppercase text-[11px] tracking-widest text-[#F5E6CC] font-bold flex items-center gap-1.5">
              <span class="material-symbols-outlined text-[16px] text-wonka-bar">location_on</span>
              Bilbao, Bizkaia
            </span>
          </div>
        </div>

      </div>
    </section>

    <!-- Art Déco Filigree Divider -->
    <div class="w-full flex justify-center py-2 opacity-70">
      <img src="public/assets/brand/art-deco-filigree.svg" alt="Adorno Art Déco" class="max-w-md w-full px-4 h-auto" />
    </div>

    <!-- ==================== DISCOVERY SELECTOR: ¿QUÉ PLAN BUSCAS HOY? ==================== -->
    <section class="w-full py-10 px-margin-mobile lg:px-margin-desktop relative z-10" id="selector-plan">
      <div class="max-w-[1400px] mx-auto">
        <div class="p-6 sm:p-8 bg-surface/90 backdrop-blur-md rounded-3xl border border-[#D4A349]/40 shadow-md flex flex-col md:flex-row items-center justify-between gap-6">
          <div class="flex items-center gap-4">
            <div class="w-12 h-12 rounded-2xl bg-wonka-bar-light border border-wonka-bar/30 flex items-center justify-center text-wonka-bar shrink-0 shadow-xs">
              <span class="material-symbols-outlined text-2xl">magic_button</span>
            </div>
            <div>
              <h2 class="font-headline-sm text-2xl text-on-surface font-normal">¿Qué plan buscas hoy en Bilbao?</h2>
              <p class="font-body-sm text-on-surface-variant text-xs mt-0.5">Elige tu momento y descubre el espacio ideal para ti</p>
            </div>
          </div>

          <!-- Interactive Plan Chips -->
          <div class="flex flex-wrap items-center gap-3 w-full md:w-auto" role="tablist">
            <button 
              id="plan-btn-house" 
              onclick="selectPlan('house')"
              role="tab"
              aria-selected="false"
              class="chip-interactive flex-1 sm:flex-initial inline-flex items-center justify-center gap-2 px-5 py-3 rounded-full text-xs font-label-uppercase font-bold tracking-wider bg-surface border-2 border-wonka-house/30 text-wonka-house hover:bg-wonka-house hover:text-white shadow-sm"
            >
              <span class="w-2.5 h-2.5 rounded-full bg-wonka-house"></span>
              Comida &amp; Sobremesa
            </button>
            
            <button 
              id="plan-btn-lounge" 
              onclick="selectPlan('lounge')"
              role="tab"
              aria-selected="false"
              class="chip-interactive flex-1 sm:flex-initial inline-flex items-center justify-center gap-2 px-5 py-3 rounded-full text-xs font-label-uppercase font-bold tracking-wider bg-surface border-2 border-wonka-lounge/30 text-wonka-lounge hover:bg-wonka-lounge hover:text-white shadow-sm"
            >
              <span class="w-2.5 h-2.5 rounded-full bg-wonka-lounge"></span>
              Cócteles &amp; Noche
            </button>

            <button 
              id="plan-btn-bar" 
              onclick="selectPlan('bar')"
              role="tab"
              aria-selected="false"
              class="chip-interactive flex-1 sm:flex-initial inline-flex items-center justify-center gap-2 px-5 py-3 rounded-full text-xs font-label-uppercase font-bold tracking-wider bg-surface border-2 border-wonka-bar/30 text-wonka-bar hover:bg-wonka-bar hover:text-white shadow-sm"
            >
              <span class="w-2.5 h-2.5 rounded-full bg-wonka-bar"></span>
              Pintxos &amp; Barra Viva
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================== TRES EXPERIENCIAS (CHROMATIC GSAP STAGE) ==================== -->
    <section class="w-full py-20 px-margin-mobile lg:px-margin-desktop relative border-b border-[#E6DFD0]" id="experiencias" style="background-color: #FAF6ED;">
      <!-- Ambient Stage Lighting Halo -->
      <div id="ambient-stage-glow"></div>

      <div class="max-w-[1400px] mx-auto relative z-10">
        <!-- Section Header -->
        <div class="flex flex-col md:flex-row md:items-end justify-between mb-16 pb-6 border-b border-[#E6DFD0]/70">
          <div>
            <h2 class="font-headline-lg text-[36px] lg:text-[48px] text-on-surface tracking-tight font-normal">
              Tres atmósferas complementarias
            </h2>
          </div>
          <p class="font-body-md text-on-surface-variant max-w-md mt-4 md:mt-0 font-light leading-relaxed">
            Una misma identidad acogedora con tres expresiones para cada momento del día: mesa reposada, coctelería nocturna y el pulso vibrante de barra.
          </p>
        </div>

        <!-- The 3 Cards Grid (Theatrical Proscenium Architecture) -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
          
          <!-- CARD 1: WONKA HOUSE (Olive Green Theme) -->
          <article 
            id="card-house"
            class="theatrical-card flex flex-col bg-surface/95 backdrop-blur-md rounded-3xl overflow-hidden border-2 border-wonka-house/30 shadow-md hover:shadow-2xl transition-all duration-300 group hover:-translate-y-1.5"
          >
            <!-- Card Header Banner -->
            <div class="p-6 bg-gradient-to-r from-wonka-house to-[#333D29] text-white flex items-center justify-between">
              <div class="flex items-center gap-3.5">
                <div class="w-14 h-14 rounded-2xl overflow-hidden shadow-md shrink-0 border-2 border-white/20 bg-wonka-house">
                  <img alt="Logo Wonka House" class="w-full h-full object-cover" src="public/assets/logos/wonka-house-green.jpg" loading="lazy" />
                </div>
                <div>
                  <span class="font-label-uppercase text-[10px] tracking-[0.24em] uppercase font-bold text-[#DDE7D3] block">Mesa &amp; Sobremesa</span>
                  <h3 class="font-headline-sm text-[24px] tracking-wide text-white font-semibold">Wonka House</h3>
                </div>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-white/15 text-[11px] font-label-uppercase text-white border border-white/20">Calma</span>
            </div>

            <!-- Imagery in Grand Proscenium Arch Frame -->
            <div class="relative aspect-[4/3] w-full overflow-hidden bg-surface-container">
              <img 
                alt="Gastronomía Wonka para compartir en mesa reposada" 
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out" 
                src="public/assets/images/ensalada-fresca.jpg" 
                loading="lazy"
              />
              <div class="absolute bottom-3 left-3 bg-wonka-house/90 backdrop-blur-md px-3.5 py-1.5 rounded-full text-white text-[11px] font-label-uppercase uppercase tracking-wider font-semibold shadow-sm">
                Comida reposada &amp; Sobremesa
              </div>
            </div>

            <!-- Body Content -->
            <div class="p-7 flex flex-col flex-1 justify-between bg-surface">
              <div>
                <p class="font-body-md text-on-surface-variant leading-relaxed mb-6">
                  Una atmósfera acogedora concebida para sentarse sin mirar el reloj, disfrutar de producto seleccionado y dejar que la sobremesa fluya de forma natural en buena compañía.
                </p>
              </div>
              <div class="pt-4 border-t border-wonka-house/15">
                <a class="btn-press inline-flex items-center justify-between w-full font-label-uppercase text-[12px] uppercase tracking-[0.18em] font-bold px-4 py-3 rounded-full text-wonka-house bg-wonka-house-light hover:bg-wonka-house hover:text-white transition-all group/btn" href="#celebraciones">
                  <span>Conocer Wonka House</span>
                  <span class="material-symbols-outlined text-[18px] group-hover/btn:translate-x-1 transition-transform">arrow_forward</span>
                </a>
              </div>
            </div>
          </article>

          <!-- CARD 2: WONKA LOUNGE (Deep Purple Theme) -->
          <article 
            id="card-lounge"
            class="theatrical-card flex flex-col bg-surface/95 backdrop-blur-md rounded-3xl overflow-hidden border-2 border-wonka-lounge/30 shadow-md hover:shadow-2xl transition-all duration-300 group hover:-translate-y-1.5"
          >
            <!-- Card Header Banner -->
            <div class="p-6 bg-gradient-to-r from-wonka-lounge to-[#1C0633] text-white flex items-center justify-between">
              <div class="flex items-center gap-3.5">
                <div class="w-14 h-14 rounded-2xl overflow-hidden shadow-md shrink-0 border-2 border-white/20 bg-wonka-lounge">
                  <img alt="Logo Wonka Lounge" class="w-full h-full object-cover" src="public/assets/logos/wonka-lounge-purple.jpg" loading="lazy" />
                </div>
                <div>
                  <span class="font-label-uppercase text-[10px] tracking-[0.24em] uppercase font-bold text-[#DEC6F5] block">Nocturno &amp; Cóctel</span>
                  <h3 class="font-headline-sm text-[24px] tracking-wide text-white font-semibold">Wonka Lounge</h3>
                </div>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-white/15 text-[11px] font-label-uppercase text-white border border-white/20">Coctelería</span>
            </div>

            <!-- Imagery -->
            <div class="relative aspect-[4/3] w-full overflow-hidden bg-surface-container">
              <img 
                alt="Ambiente sofisticado y bocados en Wonka Lounge Bilbao" 
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out" 
                src="public/assets/images/gambas-plancha.jpg" 
                loading="lazy"
              />
              <div class="absolute bottom-3 left-3 bg-wonka-lounge/90 backdrop-blur-md px-3.5 py-1.5 rounded-full text-[#FAF3E3] text-[11px] font-label-uppercase uppercase tracking-wider font-semibold shadow-sm">
                Cócteles de autor &amp; Noche
              </div>
            </div>

            <!-- Body Content -->
            <div class="p-7 flex flex-col flex-1 justify-between bg-surface">
              <div>
                <p class="font-body-md text-on-surface-variant leading-relaxed mb-6">
                  Luces tenues, copas preparadas con mimo y una selección musical que acompaña cada conversación. El rincón idóneo para alargar la noche bilbaína con estilo.
                </p>
              </div>
              <div class="pt-4 border-t border-wonka-lounge/15">
                <a class="btn-press inline-flex items-center justify-between w-full font-label-uppercase text-[12px] uppercase tracking-[0.18em] font-bold px-4 py-3 rounded-full text-wonka-lounge bg-wonka-lounge-light hover:bg-wonka-lounge hover:text-white transition-all group/btn" href="#celebraciones">
                  <span>Conocer Wonka Lounge</span>
                  <span class="material-symbols-outlined text-[18px] group-hover/btn:translate-x-1 transition-transform">arrow_forward</span>
                </a>
              </div>
            </div>
          </article>

          <!-- CARD 3: WONKA BAR (Warm Amber / Gold Theme) -->
          <article 
            id="card-bar"
            class="theatrical-card flex flex-col bg-surface/95 backdrop-blur-md rounded-3xl overflow-hidden border-2 border-wonka-bar/30 shadow-md hover:shadow-2xl transition-all duration-300 group hover:-translate-y-1.5"
          >
            <!-- Card Header Banner -->
            <div class="p-6 bg-gradient-to-r from-wonka-bar to-[#664917] text-white flex items-center justify-between">
              <div class="flex items-center gap-3.5">
                <div class="w-14 h-14 rounded-2xl overflow-hidden shadow-md shrink-0 border-2 border-white/20 bg-wonka-bar">
                  <img alt="Logo Wonka Bar" class="w-full h-full object-cover" src="public/assets/logos/wonka-bar-gold.jpg" loading="lazy" />
                </div>
                <div>
                  <span class="font-label-uppercase text-[10px] tracking-[0.24em] uppercase font-bold text-[#FCEAC4] block">Pintxos &amp; Barra Viva</span>
                  <h3 class="font-headline-sm text-[24px] tracking-wide text-white font-semibold">Wonka Bar</h3>
                </div>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-white/15 text-[11px] font-label-uppercase text-white border border-white/20">Tradición</span>
            </div>

            <!-- Imagery -->
            <div class="relative aspect-[4/3] w-full overflow-hidden bg-surface-container">
              <img 
                alt="Pintxos y raciones de barra en Wonka Bar Bilbao" 
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out" 
                src="public/assets/images/vieiras-horno.jpg" 
                loading="lazy"
              />
              <div class="absolute bottom-3 left-3 bg-wonka-bar/90 backdrop-blur-md px-3.5 py-1.5 rounded-full text-white text-[11px] font-label-uppercase uppercase tracking-wider font-semibold shadow-sm">
                Pintxos, Vinos &amp; Celebraciones
              </div>
            </div>

            <!-- Body Content -->
            <div class="p-7 flex flex-col flex-1 justify-between bg-surface">
              <div>
                <p class="font-body-md text-on-surface-variant leading-relaxed mb-6">
                  La barra donde empieza todo. Pintxos recién hechos, raciones de corte tradicional, vinos de calidad y ese murmullo inconfundible de taberna viva y cercana.
                </p>
              </div>
              <div class="pt-4 border-t border-wonka-bar/15">
                <a class="btn-press inline-flex items-center justify-between w-full font-label-uppercase text-[12px] uppercase tracking-[0.18em] font-bold px-4 py-3 rounded-full text-wonka-bar bg-wonka-bar-light hover:bg-wonka-bar hover:text-white transition-all group/btn" href="#celebraciones">
                  <span>Conocer Wonka Bar</span>
                  <span class="material-symbols-outlined text-[18px] group-hover/btn:translate-x-1 transition-transform">arrow_forward</span>
                </a>
              </div>
            </div>
          </article>

        </div>
      </div>
    </section>

    <!-- Art Déco Filigree Divider -->
    <div class="w-full flex justify-center py-6 opacity-70">
      <img src="public/assets/brand/art-deco-filigree.svg" alt="Adorno Art Déco" class="max-w-md w-full px-4 h-auto" />
    </div>

    <!-- ==================== GASTRONOMIA BENTO (EMPORIUM SHOWCASE) ==================== -->
    <section class="w-full py-20 px-margin-mobile lg:px-margin-desktop relative" id="gastronomia">
      <div class="max-w-[1400px] mx-auto relative z-10">
        <!-- Section Header -->
        <div class="flex flex-col md:flex-row md:items-end justify-between mb-16 pb-6 border-b border-[#E6DFD0]/70">
          <div>
            <h2 class="font-headline-lg text-[36px] lg:text-[48px] text-on-surface tracking-tight font-normal">
              Platos honestos, raciones para compartir
            </h2>
          </div>
          <p class="font-body-md text-on-surface-variant max-w-md mt-4 md:mt-0 font-light leading-relaxed">
            Fotografías reales de nuestra cocina en Bilbao: pulpo a la brasa, vieiras gratinadas, ibéricos selectos, hamburguesas de autor y bocados calientes de barra.
          </p>
        </div>

        <!-- Bento Grid of Real Gastronomy with Proscenium Arch Frames -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 mb-16">
          
          <!-- Left Column: Octopus & Classics -->
          <div class="lg:col-span-7 space-y-8">
            <!-- Featured: Pulpo a la Gallega -->
            <div class="theatrical-card bg-surface-container-low/95 rounded-3xl overflow-hidden proscenium-frame group">
              <div class="relative aspect-[16/10] w-full overflow-hidden bg-surface-container">
                <img 
                  alt="Pulpo a la gallega sobre plato de madera y pimentón" 
                  class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" 
                  src="public/assets/images/pulpo-gallega.jpg" 
                  loading="lazy"
                />
                <div class="absolute top-4 left-4 bg-wonka-lounge/90 backdrop-blur-md text-[#FAF3E3] px-3.5 py-1.5 rounded-full text-[11px] font-label-uppercase tracking-wider uppercase font-bold shadow-md">
                  Plato Estrella
                </div>
              </div>
              <div class="p-8">
                <h3 class="font-headline-sm text-2xl text-on-surface font-semibold mb-2">Clásicos al centro de la mesa</h3>
                <p class="font-body-md text-on-surface-variant leading-relaxed">
                  Pulpo tierno cocido en su punto justo, aliñado con aceite de oliva virgen extra, pimentón de la Vera y patata cocida suave. Servido en tabla tradicional de madera para compartir.
                </p>
              </div>
            </div>

            <!-- Mini 2-col: Croquetas & Gambas -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
              <!-- Croquetas -->
              <div class="theatrical-card bg-surface-container-low/95 rounded-3xl overflow-hidden proscenium-frame p-4">
                <div class="relative aspect-square w-full rounded-2xl overflow-hidden mb-4 bg-surface-container">
                  <img 
                    alt="Croqueta crujiente recién hecha" 
                    class="w-full h-full object-cover hover:scale-105 transition-transform duration-500" 
                    src="public/assets/images/croqueta-crujiente.jpg" 
                    loading="lazy"
                  />
                  <span class="absolute top-2.5 right-2.5 bg-black/60 backdrop-blur-md text-white px-2.5 py-1 rounded-full text-[10px] font-label-uppercase tracking-wider font-semibold">
                    Receta Casera
                  </span>
                </div>
                <h4 class="font-headline-sm text-[18px] font-semibold text-on-surface mb-1">Croquetas crujientes</h4>
                <p class="font-body-sm text-on-surface-variant leading-relaxed">
                  Bechamel melosa, rebozado dorado y crujiente para disfrutar de un bocado caliente en cualquier momento.
                </p>
              </div>

              <!-- Gambas con limón -->
              <div class="theatrical-card bg-surface-container-low/95 rounded-3xl overflow-hidden proscenium-frame p-4">
                <div class="relative aspect-square w-full rounded-2xl overflow-hidden mb-4 bg-surface-container">
                  <img 
                    alt="Gambas a la plancha recién hechas con limón" 
                    class="w-full h-full object-cover hover:scale-105 transition-transform duration-500" 
                    src="public/assets/images/gambas-plancha.jpg" 
                    loading="lazy"
                  />
                  <span class="absolute top-2.5 right-2.5 bg-black/60 backdrop-blur-md text-white px-2.5 py-1 rounded-full text-[10px] font-label-uppercase tracking-wider font-semibold">
                    A la Plancha
                  </span>
                </div>
                <h4 class="font-headline-sm text-[18px] font-semibold text-on-surface mb-1">Gambas con limón</h4>
                <p class="font-body-sm text-on-surface-variant leading-relaxed">
                  Punto jugoso, toque de cítrico recién exprimido y el aroma inconfundible de marisco fresco.
                </p>
              </div>
            </div>
          </div>

          <!-- Right Column: Burger & Tablas de Ibéricos -->
          <div class="lg:col-span-5 space-y-8">
            <!-- Burger Feature -->
            <div class="theatrical-card bg-surface-container-low/95 rounded-3xl overflow-hidden proscenium-frame group">
              <div class="relative aspect-[4/3] w-full overflow-hidden bg-surface-container">
                <img 
                  alt="Hamburguesa Wonka con huevo campero y patatas caseras" 
                  class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" 
                  src="public/assets/images/hamburguesa-completa.jpg" 
                  loading="lazy"
                />
                <div class="absolute top-3 right-3 bg-wonka-bar text-white px-3.5 py-1 rounded-full text-[11px] font-label-uppercase tracking-wider uppercase font-bold shadow-md flex items-center gap-1.5">
                  <span>★ Favorito de la casa</span>
                </div>
              </div>
              <div class="p-7">
                <h3 class="font-headline-sm text-2xl text-on-surface font-semibold mb-2">Hamburguesas &amp; Bocados</h3>
                <p class="font-body-md text-on-surface-variant leading-relaxed">
                  Carne seleccionada a la parrilla, pan artesanal tierno, queso fundente, huevo campero y patatas fritas caseras. Un bocado reconfortante y rotundo.
                </p>
              </div>
            </div>

            <!-- Tabla de Ibéricos Feature -->
            <div class="theatrical-card bg-surface-container-low/95 rounded-3xl p-6 proscenium-frame">
              <div class="relative aspect-[16/10] w-full rounded-2xl overflow-hidden mb-5">
                <img 
                  alt="Tabla de embutidos ibéricos y quesos artesanos" 
                  class="w-full h-full object-cover hover:scale-105 transition-transform duration-700" 
                  src="public/assets/images/tabla-ibericos.jpg" 
                  loading="lazy"
                />
                <div class="absolute bottom-2.5 left-2.5 bg-wonka-house/90 backdrop-blur-md px-3 py-1 rounded-full text-white text-[10px] font-label-uppercase uppercase tracking-wider font-bold">
                  Corte Tradicional
                </div>
              </div>
              <div class="flex items-center justify-between mb-2">
                <h4 class="font-headline-sm text-[19px] font-semibold text-on-surface">Tablas de Ibéricos y Quesos</h4>
                <span class="font-label-uppercase text-[11px] text-wonka-house font-bold tracking-wider px-2.5 py-0.5 rounded-full bg-wonka-house-light">Para Compartir</span>
              </div>
              <p class="font-body-sm text-on-surface-variant leading-relaxed">
                Jamón ibérico cortado con esmero, lomo curado, chorizo de bellota y quesos de caserío con rebanadas de pan tostado.
              </p>
            </div>
          </div>
        </div>

        <!-- Real Gallery Additions: Gyozas & Tequeños -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-16">
          <div class="theatrical-card bg-surface-container-low/95 rounded-3xl p-6 proscenium-frame flex flex-col sm:flex-row items-center gap-6">
            <div class="w-full sm:w-44 h-44 rounded-2xl overflow-hidden shrink-0 bg-surface-container">
              <img alt="Gyozas al vapor en bambú" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500" src="public/assets/images/gyozas-vapor.jpg" loading="lazy" />
            </div>
            <div>
              <span class="font-label-uppercase text-[10px] tracking-wider text-wonka-bar font-bold uppercase">Toque de Fusión</span>
              <h4 class="font-headline-sm text-xl text-on-surface font-semibold mb-1">Gyozas al vapor</h4>
              <p class="font-body-sm text-on-surface-variant leading-relaxed">
                Masa fina cocida al vapor en bambú tradicional, relleno sabroso y salsa de soja para acompañar con un buen vino tinto.
              </p>
            </div>
          </div>

          <div class="theatrical-card bg-surface-container-low/95 rounded-3xl p-6 proscenium-frame flex flex-col sm:flex-row items-center gap-6">
            <div class="w-full sm:w-44 h-44 rounded-2xl overflow-hidden shrink-0 bg-surface-container">
              <img alt="Tequeños dorados en tabla de madera" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500" src="public/assets/images/tequenos-tabla.jpg" loading="lazy" />
            </div>
            <div>
              <span class="font-label-uppercase text-[10px] tracking-wider text-wonka-bar font-bold uppercase">Imprescindible de Barra</span>
              <h4 class="font-headline-sm text-xl text-on-surface font-semibold mb-1">Tequeños artesanos</h4>
              <p class="font-body-sm text-on-surface-variant leading-relaxed">
                Queso blanco fundido envuelto en masa dorada crujiente, servidos con salsa para untar y disfrutar en ronda de amigos.
              </p>
            </div>
          </div>
        </div>

        <!-- Manifesto Strip with Brand Colors -->
        <div class="p-8 md:p-12 bg-gradient-to-br from-surface-container via-[#FAF5EB] to-surface-container rounded-3xl proscenium-frame grid grid-cols-1 md:grid-cols-3 gap-8 shadow-sm">
          <div class="flex flex-col space-y-2">
            <span class="font-headline-sm text-[21px] text-wonka-house font-semibold flex items-center gap-2.5">
              <span class="w-3.5 h-3.5 rounded-full bg-wonka-house ring-4 ring-wonka-house/20"></span>
              Producto Fresco
            </span>
            <p class="font-body-sm text-on-surface-variant leading-relaxed">
              Ingredientes frescos y elaboración diaria. Platos honestos que honran el recetario de Bilbao sin adornos innecesarios.
            </p>
          </div>
          <div class="flex flex-col space-y-2">
            <span class="font-headline-sm text-[21px] text-wonka-lounge font-semibold flex items-center gap-2.5">
              <span class="w-3.5 h-3.5 rounded-full bg-wonka-lounge ring-4 ring-wonka-lounge/20"></span>
              Encuentro &amp; Charla
            </span>
            <p class="font-body-sm text-on-surface-variant leading-relaxed">
              Espacios concebidos para demorarse, pedir otra ronda y convertir cualquier merienda o cena en una buena conversación.
            </p>
          </div>
          <div class="flex flex-col space-y-2">
            <span class="font-headline-sm text-[21px] text-wonka-bar font-semibold flex items-center gap-2.5">
              <span class="w-3.5 h-3.5 rounded-full bg-wonka-bar ring-4 ring-wonka-bar/20"></span>
              El Pulso de Bilbao
            </span>
            <p class="font-body-sm text-on-surface-variant leading-relaxed">
              Cercanía, generosidad en cada ración y un trato cómplice para que siempre te sientas como en casa al cruzar la puerta.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Art Déco Filigree Divider -->
    <div class="w-full flex justify-center py-6 opacity-70">
      <img src="public/assets/brand/art-deco-filigree.svg" alt="Adorno Art Déco" class="max-w-md w-full px-4 h-auto" />
    </div>

    <!-- ==================== CELEBRACIONES & ENCUENTROS ==================== -->
    <section class="w-full py-20 px-margin-mobile lg:px-margin-desktop relative" id="celebraciones">
      <div class="max-w-[1400px] mx-auto relative z-10">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
          
          <!-- Left Column: Celebra en Wonka Proposition -->
          <div class="lg:col-span-6 flex flex-col">
            <h2 class="font-headline-lg text-[38px] sm:text-[48px] text-on-surface tracking-tight font-normal leading-[1.1] mb-5">
              Celebra en Wonka.<br />
              <span class="italic font-display-hero text-wonka-lounge font-normal text-[32px] sm:text-[40px]">
                Cualquier excusa es buena para brindar.
              </span>
            </h2>
            <p class="font-body-lg text-[16px] text-on-surface-variant font-light leading-relaxed mb-6">
              Cumpleaños, reuniones de amigos, cenas de empresa o encuentros de cuadrilla. Ponemos a tu disposición nuestros tres espacios para diseñar una experiencia a tu medida.
            </p>

            <!-- Featured Brand Artwork: Poster Tres Experiencias -->
            <div class="bg-surface rounded-3xl p-6 proscenium-frame mb-8 flex items-center gap-5">
              <div class="w-24 h-32 rounded-2xl overflow-hidden shrink-0 shadow-md border border-[#D4A349]/40">
                <img alt="Póster oficial Wonka Bilbao: Una marca, tres experiencias" class="w-full h-full object-cover" src="public/assets/brand/poster-tres-experiencias.jpg" loading="lazy" />
              </div>
              <div>
                <span class="font-label-uppercase text-[10px] tracking-[0.24em] text-wonka-bar font-bold uppercase block mb-1">Concepto Integral</span>
                <h4 class="font-headline-sm text-lg text-wonka-lounge font-semibold mb-1">Una marca. Tres experiencias.</h4>
                <p class="font-body-sm text-on-surface-variant leading-relaxed">
                  El diseño oficial que une Wonka House, Wonka Lounge y Wonka Bar bajo una misma visión culinaria y social.
                </p>
              </div>
            </div>

            <!-- Key Features -->
            <div class="grid grid-cols-2 gap-4">
              <div class="p-4 rounded-2xl bg-surface/90 border border-[#D4A349]/30">
                <span class="font-headline-sm text-xl text-wonka-lounge font-semibold block mb-1">Flexibilidad</span>
                <p class="font-body-sm text-on-surface-variant">Menús para grupos y opciones adaptadas a tus gustos.</p>
              </div>
              <div class="p-4 rounded-2xl bg-surface/90 border border-[#D4A349]/30">
                <span class="font-headline-sm text-xl text-wonka-bar font-semibold block mb-1">Tres Ambientes</span>
                <p class="font-body-sm text-on-surface-variant">Pasa de la comida a las copas sin cambiar de casa.</p>
              </div>
            </div>
          </div>

          <!-- Right Column: Interactive Commercial Demo Form -->
          <div class="lg:col-span-6">
            <div class="bg-surface/95 backdrop-blur-md rounded-[32px] p-8 sm:p-10 proscenium-frame relative overflow-hidden">
              <div class="absolute top-0 right-0 w-32 h-32 bg-wonka-bar/10 rounded-full blur-2xl pointer-events-none"></div>
              
              <div class="mb-6">
                <h3 class="font-headline-sm text-2xl text-on-surface font-semibold">Planea tu visita o celebración</h3>
                <p class="font-body-sm text-on-surface-variant mt-1">
                  Pruébalo libremente en esta demo interactiva: selecciona tu espacio y número de personas.
                </p>
              </div>

              <form class="space-y-4" onsubmit="handleDemoSubmit(event)">
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div class="flex flex-col space-y-1.5">
                    <label class="font-label-uppercase text-[11px] uppercase tracking-wider text-on-surface font-bold">Tu nombre</label>
                    <input id="demo-name" required class="w-full bg-[#FAF6EE] px-4 py-3 rounded-xl border border-[#D5CEBF] text-on-surface text-body-md focus:outline-none focus:border-wonka-lounge focus:ring-2 focus:ring-wonka-lounge/20 transition-all" placeholder="Ej: Mikel, Ane..." type="text" />
                  </div>
                  <div class="flex flex-col space-y-1.5">
                    <label class="font-label-uppercase text-[11px] uppercase tracking-wider text-on-surface font-bold">Email o Teléfono</label>
                    <input required class="w-full bg-[#FAF6EE] px-4 py-3 rounded-xl border border-[#D5CEBF] text-on-surface text-body-md focus:outline-none focus:border-wonka-lounge focus:ring-2 focus:ring-wonka-lounge/20 transition-all" placeholder="ejemplo@wonka.eus" type="text" />
                  </div>
                </div>

                <div class="flex flex-col space-y-1.5">
                  <label class="font-label-uppercase text-[11px] uppercase tracking-wider text-on-surface font-bold">Espacio preferido</label>
                  <select id="demo-space" class="w-full bg-[#FAF6EE] px-4 py-3 rounded-xl border border-[#D5CEBF] text-on-surface text-body-md focus:outline-none focus:border-wonka-lounge focus:ring-2 focus:ring-wonka-lounge/20 transition-all">
                    <option value="Wonka Bar (Pintxos & Raciones de barra)">Wonka Bar (Pintxos &amp; Raciones de barra)</option>
                    <option value="Wonka House (Comida reposada en mesa)">Wonka House (Comida reposada en mesa)</option>
                    <option value="Wonka Lounge (Copas & Cócteles de noche)">Wonka Lounge (Copas &amp; Cócteles de noche)</option>
                    <option value="Celebración Combinada (Varios espacios)">Celebración Combinada (Varios espacios)</option>
                  </select>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div class="flex flex-col space-y-1.5">
                    <label class="font-label-uppercase text-[11px] uppercase tracking-wider text-on-surface font-bold">Fecha orientativa</label>
                    <input class="w-full bg-[#FAF6EE] px-4 py-3 rounded-xl border border-[#D5CEBF] text-on-surface text-body-md focus:outline-none focus:border-wonka-lounge focus:ring-2 focus:ring-wonka-lounge/20 transition-all" type="date" id="demo-date" />
                  </div>
                  <div class="flex flex-col space-y-1.5">
                    <label class="font-label-uppercase text-[11px] uppercase tracking-wider text-on-surface font-bold">Número de personas</label>
                    <select id="demo-guests" class="w-full bg-[#FAF6EE] px-4 py-3 rounded-xl border border-[#D5CEBF] text-on-surface text-body-md focus:outline-none focus:border-wonka-lounge focus:ring-2 focus:ring-wonka-lounge/20 transition-all">
                      <option>2 a 4 personas</option>
                      <option>5 a 8 personas</option>
                      <option>9 a 15 personas</option>
                      <option>Más de 15 personas (Grupo grande)</option>
                    </select>
                  </div>
                </div>

                <div class="flex flex-col space-y-1.5">
                  <label class="font-label-uppercase text-[11px] uppercase tracking-wider text-on-surface font-bold">Comentarios o preferencia</label>
                  <textarea class="w-full bg-[#FAF6EE] px-4 py-3 rounded-xl border border-[#D5CEBF] text-on-surface text-body-md focus:outline-none focus:border-wonka-lounge focus:ring-2 focus:ring-wonka-lounge/20 transition-all resize-none" placeholder="¿Tienes algún detalle o preferencia especial?" rows="2"></textarea>
                </div>

                <button class="btn-press w-full inline-flex items-center justify-center gap-2 font-label-uppercase text-[12px] uppercase tracking-[0.2em] font-bold px-8 py-4 bg-wonka-lounge text-white rounded-full hover:bg-[#3D1768] hover:shadow-[0_6px_20px_rgba(46,16,80,0.3)] transition-all duration-300 mt-2" type="submit">
                  <span>Consultar disponibilidad (Demo)</span>
                  <span class="material-symbols-outlined text-[18px]">send</span>
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- ==================== DEMONSTRATIVE MODAL ==================== -->
  <div id="demo-modal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-xs hidden opacity-0 transition-opacity duration-300 p-4" onclick="handleBackdropClick(event)">
    <div class="bg-surface rounded-3xl max-w-md w-full p-8 border-2 border-wonka-bar shadow-2xl transform scale-95 transition-transform duration-300 relative text-center" id="demo-modal-box">
      <div class="w-16 h-16 rounded-full bg-wonka-bar-light border border-wonka-bar/30 flex items-center justify-center mx-auto mb-4 text-wonka-bar">
        <span class="material-symbols-outlined text-3xl">celebration</span>
      </div>
      <h3 class="font-headline-sm text-2xl text-on-surface font-semibold mb-2" id="modal-title">¡Solicitud Demostrativa!</h3>
      <p class="font-body-md text-on-surface-variant mb-6" id="modal-message">
        Tu consulta ha sido simulada correctamente para Wonka Bilbao.
      </p>
      <button onclick="closeDemoModal()" class="btn-press inline-flex items-center justify-center font-label-uppercase text-[12px] uppercase tracking-widest font-bold px-8 py-3.5 bg-wonka-lounge text-white rounded-full hover:bg-wonka-lounge-dark transition-all">
        Entendido
      </button>
    </div>
  </div>

  <!-- ==================== TOAST NOTIFICATION (EASTER EGG) ==================== -->
  <div id="hat-toast" class="fixed bottom-6 left-1/2 -translate-x-1/2 z-50 bg-[#1E1A17] text-white px-5 py-3 rounded-full shadow-2xl border border-wonka-bar/50 flex items-center gap-3 opacity-0 pointer-events-none transform translate-y-4 transition-all duration-300">
    <span class="text-wonka-bar text-lg">🎩</span>
    <span class="font-body-sm text-xs text-[#FAF0D4]" id="hat-toast-text">«El secreto no está en el truco, sino en cómo se comparte en la mesa.» — Wonka Bilbao</span>
  </div>

  <!-- ==================== FOOTER (PROMINENT OFFICIAL LOGO) ==================== -->
  <footer class="w-full bg-[#F5EFE3] border-t border-[#E6DFD0] pt-16 pb-12 relative z-10">
    <div class="w-full px-margin-mobile lg:px-margin-desktop max-w-[1400px] mx-auto">
      <div class="grid grid-cols-1 md:grid-cols-12 gap-10 pb-12 border-b border-[#E6DFD0]">
        
        <!-- Brand Summary -->
        <div class="md:col-span-5 flex flex-col justify-between space-y-4">
          <div>
            <div class="mb-3">
              <img 
                src="public/assets/logos/wonka-bilbao-logo-purple.png" 
                alt="Wonka Bilbao" 
                class="h-11 w-auto object-contain"
              />
            </div>
            <span class="font-label-uppercase text-[10px] tracking-[0.26em] text-wonka-bar uppercase block mb-3 font-bold">
              Una marca · Tres experiencias
            </span>
            <p class="font-body-sm text-on-surface-variant max-w-sm leading-relaxed">
              Hospitalidad, raciones honestas y el placer de compartir buenos momentos en Bilbao. Wonka House, Wonka Lounge y Wonka Bar reunidos bajo un mismo espíritu acogedor.
            </p>
          </div>
          <div>
            <span class="font-label-uppercase text-[11px] text-wonka-bar tracking-[0.18em] uppercase font-bold block mb-1">Ubicación</span>
            <p class="font-body-md text-on-surface font-medium">Bilbao, Bizkaia · País Vasco</p>
          </div>
        </div>

        <!-- The 3 Spaces Links -->
        <div class="md:col-span-4 flex flex-col justify-between space-y-4">
          <div>
            <span class="font-label-uppercase text-[11px] text-wonka-lounge tracking-[0.18em] uppercase font-bold block mb-3">
              Nuestros Espacios
            </span>
            <ul class="space-y-2.5 font-body-sm text-on-surface">
              <li class="flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-wonka-house"></span>
                <a class="hover:text-wonka-house hover:underline transition-all" href="#experiencias" onclick="selectPlan('house')">Wonka House — Comida &amp; Sobremesa</a>
              </li>
              <li class="flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-wonka-lounge"></span>
                <a class="hover:text-wonka-lounge hover:underline transition-all" href="#experiencias" onclick="selectPlan('lounge')">Wonka Lounge — Noche &amp; Coctelería</a>
              </li>
              <li class="flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-wonka-bar"></span>
                <a class="hover:text-wonka-bar hover:underline transition-all" href="#experiencias" onclick="selectPlan('bar')">Wonka Bar — Pintxos &amp; Barra informal</a>
              </li>
            </ul>
          </div>
          <div>
            <span class="font-label-uppercase text-[11px] text-wonka-lounge tracking-[0.18em] uppercase font-bold block mb-2">Comunidad</span>
            <div class="flex items-center gap-4 text-on-surface font-body-sm">
              <a class="hover:text-wonka-lounge font-medium transition-colors flex items-center gap-1" href="https://instagram.com" rel="noopener" target="_blank">
                <span>@wonkabilbao</span>
                <span class="material-symbols-outlined text-[15px]">arrow_outward</span>
              </a>
              <span class="text-[#D5CEBF]">·</span>
              <a class="hover:text-wonka-house transition-colors" href="#gastronomia">Gastronomía</a>
              <span class="text-[#D5CEBF]">·</span>
              <a class="hover:text-wonka-bar transition-colors" href="#celebraciones">Celebraciones</a>
            </div>
          </div>
        </div>

        <!-- Social & Welcome Note -->
        <div class="md:col-span-3 flex flex-col justify-between space-y-4">
          <div>
            <span class="font-label-uppercase text-[11px] text-wonka-bar tracking-[0.18em] uppercase font-bold block mb-2">
              Te esperamos
            </span>
            <p class="font-body-sm text-on-surface-variant leading-relaxed">
              Pásate por nuestra barra a tomar un vino y un pintxo o ven a celebrar con nosotros tu próxima reunión de amigos en Bilbao.
            </p>
          </div>
          <div class="pt-2">
            <a class="btn-press inline-flex items-center gap-2 font-label-uppercase text-[11px] uppercase tracking-[0.16em] font-bold px-5 py-2.5 rounded-full border-2 border-wonka-lounge text-wonka-lounge hover:bg-wonka-lounge hover:text-white transition-all shadow-sm" href="#celebraciones">
              <span>Contactar</span>
              <span class="material-symbols-outlined text-[15px]">arrow_forward</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Copyright & Bottom notes -->
      <div class="pt-8 flex flex-col sm:flex-row items-center justify-between gap-4 font-body-sm text-on-surface-variant text-[13px]">
        <p>© Wonka Bilbao · Una marca. Tres experiencias. Todos los derechos reservados.</p>
        <div class="flex items-center gap-6 font-label-uppercase text-[11px] font-medium">
          <a class="hover:text-wonka-lounge transition-colors" href="#">Aviso Legal</a>
          <a class="hover:text-wonka-lounge transition-colors" href="#">Privacidad</a>
          <a class="hover:text-wonka-lounge transition-colors" href="#">Cookies</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- ==================== JAVASCRIPT & GSAP THEATRICAL ENGINE ==================== -->
  <script>
    // Register GSAP plugins
    if (typeof gsap !== 'undefined') {{
      gsap.registerPlugin(ScrollTrigger);
    }}

    // 1. Mobile Drawer Controller
    let isMobileOpen = false;
    function toggleMobileMenu() {{
      const drawer = document.getElementById('mobile-drawer');
      const backdrop = document.getElementById('mobile-drawer-backdrop');
      const icon = document.getElementById('menu-icon');
      
      isMobileOpen = !isMobileOpen;
      if (isMobileOpen) {{
        drawer.classList.remove('translate-x-full');
        backdrop.classList.remove('opacity-0', 'pointer-events-none');
        backdrop.classList.add('opacity-100');
        if (icon) icon.innerText = 'close';
        document.body.style.overflow = 'hidden';
      }} else {{
        drawer.classList.add('translate-x-full');
        backdrop.classList.remove('opacity-100');
        backdrop.classList.add('opacity-0', 'pointer-events-none');
        if (icon) icon.innerText = 'menu';
        document.body.style.overflow = '';
      }}
    }}

    // 2. GSAP Choreographed Top Hat Physics & Timeline
    const hat = document.getElementById('hero-wonka-hat');
    const hatTrigger = document.getElementById('hat-interactive-trigger');
    let idleTween = null;
    let isTipping = false;

    if (hat && typeof gsap !== 'undefined') {{
      // Subtle idle breathing float
      idleTween = gsap.to(hat, {{
        y: -9,
        rotation: -3,
        duration: 2.8,
        ease: "sine.inOut",
        yoyo: true,
        repeat: -1
      }});

      // Mouse tracking parallax in Hero area
      const heroSec = document.getElementById('hero-section');
      if (heroSec) {{
        heroSec.addEventListener('mousemove', (e) => {{
          if (isTipping) return;
          const rect = heroSec.getBoundingClientRect();
          const relX = (e.clientX - rect.left) / rect.width - 0.5;
          const relY = (e.clientY - rect.top) / rect.height - 0.5;
          gsap.to(hat, {{
            rotation: -6 + relX * 12,
            x: relX * 10,
            duration: 0.8,
            ease: "power1.out",
            overwrite: "auto"
          }});
        }});
      }}

      // Interactive Click/Tap Tip with GSAP Timeline
      if (hatTrigger) {{
        hatTrigger.addEventListener('click', (e) => {{
          if (isTipping) return;
          isTipping = true;
          if (idleTween) idleTween.pause();

          const tl = gsap.timeline({{
            onComplete: () => {{
              isTipping = false;
              if (idleTween) idleTween.resume();
            }}
          }});

          // Coordinated Tip + Golden Burst
          tl.to(hat, {{
            y: -22,
            rotation: -24,
            scale: 1.25,
            duration: 0.35,
            ease: "back.out(2)"
          }})
          .to(hat, {{
            y: 0,
            rotation: -6,
            scale: 1,
            duration: 0.75,
            ease: "elastic.out(1, 0.35)"
          }});

          // Particle burst
          const rect = hat.getBoundingClientRect();
          spawnGoldSparkles(rect.left + rect.width / 2, rect.top + rect.height / 2);
          showHatToast();
        }});
      }}
    }}

    function showHatToast() {{
      const toast = document.getElementById('hat-toast');
      if (!toast) return;
      toast.classList.remove('opacity-0', 'pointer-events-none', 'translate-y-4');
      toast.classList.add('opacity-100', 'translate-y-0');
      setTimeout(() => {{
        toast.classList.remove('opacity-100', 'translate-y-0');
        toast.classList.add('opacity-0', 'pointer-events-none', 'translate-y-4');
      }}, 3200);
    }}

    // 3. Canvas Ambient Gold Dust & Hat Shimmer Particle System
    const canvas = document.getElementById('theatrical-canvas');
    const ctx = canvas ? canvas.getContext('2d') : null;
    let particles = [];
    let dustMotes = [];

    function resizeCanvas() {{
      if (!canvas) return;
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    }}
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    // Initialize floating ambient dust motes
    function initDustMotes() {{
      dustMotes = [];
      const count = window.innerWidth < 768 ? 20 : 45;
      for (let i = 0; i < count; i++) {{
        dustMotes.push({{
          x: Math.random() * window.innerWidth,
          y: Math.random() * window.innerHeight,
          size: 1 + Math.random() * 2.2,
          vx: (Math.random() - 0.5) * 0.4,
          vy: -0.2 - Math.random() * 0.3,
          alpha: 0.15 + Math.random() * 0.35,
          color: Math.random() > 0.4 ? '#D4A349' : '#FAF0D4'
        }});
      }}
    }}
    initDustMotes();

    function spawnGoldSparkles(x, y) {{
      if (!ctx) return;
      const colors = ['#D4A349', '#FAF3E3', '#8D6A2A', '#E4C381', '#FFFFFF'];
      for (let i = 0; i < 35; i++) {{
        const angle = Math.random() * Math.PI * 2;
        const speed = 2.8 + Math.random() * 6.2;
        particles.push({{
          x: x,
          y: y,
          vx: Math.cos(angle) * speed,
          vy: Math.sin(angle) * speed - 1.8,
          size: 2.5 + Math.random() * 3.8,
          color: colors[Math.floor(Math.random() * colors.length)],
          alpha: 1,
          decay: 0.016 + Math.random() * 0.02
        }});
      }}
    }}

    function animateParticles() {{
      if (!ctx) return;
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // 1. Render ambient floating dust motes
      for (let i = 0; i < dustMotes.length; i++) {{
        const d = dustMotes[i];
        d.x += d.vx;
        d.y += d.vy;
        if (d.y < -10) d.y = canvas.height + 10;
        if (d.x < -10) d.x = canvas.width + 10;
        if (d.x > canvas.width + 10) d.x = -10;

        ctx.save();
        ctx.globalAlpha = d.alpha;
        ctx.fillStyle = d.color;
        ctx.beginPath();
        ctx.arc(d.x, d.y, d.size, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
      }}

      // 2. Render sparkle burst
      for (let i = particles.length - 1; i >= 0; i--) {{
        const p = particles[i];
        p.x += p.vx;
        p.y += p.vy;
        p.vy += 0.14; // gravity
        p.alpha -= p.decay;

        if (p.alpha <= 0) {{
          particles.splice(i, 1);
          continue;
        }}

        ctx.save();
        ctx.globalAlpha = p.alpha;
        ctx.fillStyle = p.color;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
      }}

      requestAnimationFrame(animateParticles);
    }}
    requestAnimationFrame(animateParticles);

    // 4. GSAP Chromatic Experience Stage Lighting Transitions
    const colorThemes = {{
      'house': {{ 
        bg: '#EEF4E8', 
        border: '#4E5B3F',
        glow: 'radial-gradient(ellipse at 50% 30%, rgba(78, 91, 63, 0.22) 0%, transparent 70%)'
      }},
      'lounge': {{ 
        bg: '#F3ECF8', 
        border: '#2E1050',
        glow: 'radial-gradient(ellipse at 50% 30%, rgba(46, 16, 80, 0.24) 0%, transparent 70%)'
      }},
      'bar': {{ 
        bg: '#FAF3E3', 
        border: '#8D6A2A',
        glow: 'radial-gradient(ellipse at 50% 30%, rgba(141, 106, 42, 0.24) 0%, transparent 70%)'
      }},
      'default': {{ 
        bg: '#FAF6ED', 
        border: '#E6DFD0',
        glow: 'radial-gradient(ellipse at 50% 30%, rgba(212, 163, 73, 0.14) 0%, transparent 70%)'
      }}
    }};

    function toggleColorExperience(experience) {{
      const sec = document.getElementById('experiencias');
      const glow = document.getElementById('ambient-stage-glow');
      if (!sec) return;
      
      const theme = colorThemes[experience] || colorThemes['default'];

      if (typeof gsap !== 'undefined') {{
        gsap.to(sec, {{
          backgroundColor: theme.bg,
          duration: 0.85,
          ease: "power2.inOut"
        }});
      }} else {{
        sec.style.backgroundColor = theme.bg;
      }}

      if (glow) glow.style.background = theme.glow;

      // Focus matching experience card
      ['house', 'lounge', 'bar'].forEach(exp => {{
        const card = document.getElementById('card-' + exp);
        if (card) {{
          if (exp === experience) {{
            card.classList.add('card-active-experience');
            card.style.setProperty('--exp-accent', theme.border);
            if (typeof gsap !== 'undefined') {{
              gsap.fromTo(card, {{ scale: 1 }}, {{ scale: 1.025, duration: 0.45, ease: "back.out(1.7)" }});
            }}
          }} else {{
            card.classList.remove('card-active-experience');
            if (typeof gsap !== 'undefined') {{
              gsap.to(card, {{ scale: 1, duration: 0.4, ease: "power2.out" }});
            }}
          }}
        }}
      }});
    }}

    // 5. Plan Discovery Selection with GSAP Smooth Scroll
    function selectPlan(plan) {{
      toggleColorExperience(plan);

      const expSec = document.getElementById('experiencias');
      if (expSec) {{
        expSec.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
      }}

      // Highlight corresponding discovery chip
      ['house', 'lounge', 'bar'].forEach(p => {{
        const btn = document.getElementById('plan-btn-' + p);
        if (btn) {{
          if (p === plan) {{
            btn.classList.add('ring-2', 'ring-offset-2', 'ring-wonka-' + p);
            btn.setAttribute('aria-selected', 'true');
          }} else {{
            btn.classList.remove('ring-2', 'ring-offset-2', 'ring-wonka-house', 'ring-wonka-lounge', 'ring-wonka-bar');
            btn.setAttribute('aria-selected', 'false');
          }}
        }}
      }});
    }}

    // 6. GSAP ScrollTrigger Staggered Entrance for Cards
    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {{
      gsap.utils.toArray('.theatrical-card').forEach((card, i) => {{
        gsap.from(card, {{
          scrollTrigger: {{
            trigger: card,
            start: "top 88%",
            toggleActions: "play none none none"
          }},
          y: 28,
          opacity: 0,
          duration: 0.75,
          ease: "power2.out",
          delay: (i % 3) * 0.1
        }});
      }});
    }}

    // 7. Demonstrative Form Handler (Emil Scale 0.95 -> 1.0 Entrance)
    function handleDemoSubmit(e) {{
      e.preventDefault();
      const name = document.getElementById('demo-name')?.value || 'Amigo';
      const space = document.getElementById('demo-space')?.value || 'Wonka';
      
      const modal = document.getElementById('demo-modal');
      const modalBox = document.getElementById('demo-modal-box');
      const title = document.getElementById('modal-title');
      const msg = document.getElementById('modal-message');

      if (title) title.innerText = '¡Solicitud Recibida, ' + name + '!';
      if (msg) msg.innerHTML = 'En esta <strong>demo comercial</strong>, tu consulta para <strong>' + space + '</strong> ha sido simulada con éxito.<br/><br/>Wonka Bilbao: <em>Una marca. Tres experiencias.</em>';

      if (modal && modalBox) {{
        modal.classList.remove('hidden');
        if (typeof gsap !== 'undefined') {{
          gsap.fromTo(modal, {{ opacity: 0 }}, {{ opacity: 1, duration: 0.25 }});
          gsap.fromTo(modalBox, {{ scale: 0.92, y: 15 }}, {{ scale: 1, y: 0, duration: 0.35, ease: "back.out(1.5)" }});
        }} else {{
          setTimeout(() => {{
            modal.classList.remove('opacity-0');
            modalBox.classList.remove('scale-95');
            modalBox.classList.add('scale-100');
          }}, 10);
        }}
      }}
    }}

    function closeDemoModal() {{
      const modal = document.getElementById('demo-modal');
      const modalBox = document.getElementById('demo-modal-box');
      if (modal && modalBox) {{
        if (typeof gsap !== 'undefined') {{
          gsap.to(modalBox, {{ scale: 0.94, opacity: 0, duration: 0.2, ease: "power2.in" }});
          gsap.to(modal, {{ opacity: 0, duration: 0.25, onComplete: () => {{
            modal.classList.add('hidden');
            gsap.set([modal, modalBox], {{ clearProps: "all" }});
          }} }});
        }} else {{
          modal.classList.add('opacity-0');
          modalBox.classList.remove('scale-100');
          modalBox.classList.add('scale-95');
          setTimeout(() => {{
            modal.classList.add('hidden');
          }}, 280);
        }}
      }}
    }}

    function handleBackdropClick(e) {{
      if (e.target.id === 'demo-modal') closeDemoModal();
    }}
  </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully generated theatrical index.html with {len(html_content)} characters")
