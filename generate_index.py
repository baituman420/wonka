import re

with open('public/assets/logos/wonka-top-hat.svg', 'r') as f:
    svg_hat_raw = f.read().strip()

# Clean XML declaration if present
svg_hat = re.sub(r'<\?xml[^>]*\?>', '', svg_hat_raw).strip()

html_content = f'''<!DOCTYPE html>
<html class="scroll-smooth" lang="es">
<head>
  <meta charset="utf-8" />
  <meta content="width=device-width, initial-scale=1.0" name="viewport" />
  <meta content="Wonka Bilbao · Una marca. Tres experiencias gastronómicas." name="description" />
  <title>Wonka Bilbao · Una Marca. Tres Experiencias.</title>
  
  <!-- Favicon with Wonka Hat SVG -->
  <link rel="icon" type="image/svg+xml" href="public/assets/logos/wonka-top-hat.svg" />
  
  <!-- Fonts -->
  <link href="https://fonts.googleapis.com" rel="preconnect" />
  <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect" />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet" />
  
  <style>
    @layer base {{
      html, body {{ margin: 0; padding: 0; }}
      body {{ overscroll-behavior: none; }}
      main > :first-child {{ margin-top: 0 !important; }}
      main > :last-child {{ margin-bottom: 0 !important; }}
    }}
    ::-webkit-scrollbar {{ display: none; }}

    /* Keyframe animations for the bespoke Wonka top hat */
    @keyframes wonkaHatFloat {{
      0%, 100% {{
        transform: translateY(0px) rotate(-7deg);
      }}
      50% {{
        transform: translateY(-8px) rotate(-3deg);
      }}
    }}

    @keyframes softPulse {{
      0%, 100% {{ opacity: 0.7; transform: scale(1); }}
      50% {{ opacity: 1; transform: scale(1.04); }}
    }}

    .animate-wonka-hat {{
      animation: wonkaHatFloat 5s ease-in-out infinite;
      transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1), filter 0.3s ease;
      transform-origin: 30% 90%;
    }}

    .animate-wonka-hat:hover {{
      animation-play-state: paused;
      transform: translateY(-16px) rotate(-14deg) scale(1.18) !important;
      filter: drop-shadow(0 14px 20px rgba(46, 16, 80, 0.45));
    }}

    /* Smooth color transition engine for experiential cards */
    .experiencia-ambient-transition {{
      transition: background-color 0.7s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.5s ease, box-shadow 0.7s ease;
    }}

    /* Card active focus styles */
    .card-focused {{
      transform: translateY(-6px) scale(1.015);
      box-shadow: 0 20px 35px -10px rgba(46, 16, 80, 0.18), 0 0 0 3px var(--focus-color, #2E1050) !important;
    }}

    /* Glassmorphic navigation & panels */
    .glass-nav {{
      background: rgba(253, 249, 240, 0.88);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
    }}

    /* Respect reduced motion */
    @media (prefers-reduced-motion: reduce) {{
      .animate-wonka-hat, .animate-bounce, .animate-pulse {{
        animation: none !important;
        transform: none !important;
      }}
      * {{
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

<body class="bg-surface font-body-md text-on-surface antialiased selection:bg-[#E8DECE] selection:text-wonka-lounge">

  <!-- ==================== DEMO COMMERCIAL CONTROLLER (TOP PILL) ==================== -->
  <aside aria-label="Demo Controller" class="hidden sm:flex fixed bottom-5 right-5 z-50 items-center gap-2.5 bg-[#1E1A17]/95 text-white backdrop-blur-md px-4 py-2.5 rounded-full shadow-2xl border border-white/20 text-xs transition-all hover:scale-105">
    <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
    <span class="font-label-uppercase font-semibold tracking-wider text-[#FAF0D4]">Demo Comercial</span>
    <span class="text-white/40">|</span>
    <span class="text-white/80">Recursos 100% Locales</span>
    <button onclick="toggleColorExperience('bar')" class="px-2 py-0.5 rounded bg-wonka-bar text-white text-[10px] font-bold uppercase hover:brightness-110 transition-all">Bar</button>
    <button onclick="toggleColorExperience('house')" class="px-2 py-0.5 rounded bg-wonka-house text-white text-[10px] font-bold uppercase hover:brightness-110 transition-all">House</button>
    <button onclick="toggleColorExperience('lounge')" class="px-2 py-0.5 rounded bg-wonka-lounge text-white text-[10px] font-bold uppercase hover:brightness-110 transition-all">Lounge</button>
  </aside>

  <!-- ==================== HEADER ==================== -->
  <header class="fixed top-0 left-0 right-0 z-50 glass-nav border-b border-[#E7DFD0] shadow-sm transition-all duration-300" id="main-header">
    <div class="h-20 w-full px-margin-mobile lg:px-margin-desktop flex items-center justify-between max-w-[1440px] mx-auto">
      <div class="flex items-center gap-space-xl">
        <a class="group flex items-center gap-3.5" href="#" title="Wonka Bilbao">
          <!-- Theatrical Mini Hat Emblem inside Badge -->
          <div class="w-11 h-11 rounded-2xl bg-gradient-to-br from-wonka-lounge to-[#1A072E] flex items-center justify-center p-1.5 shadow-md border border-white/20 group-hover:scale-105 transition-transform duration-300">
            <div class="w-7 h-7 transform -rotate-6">
              {svg_hat}
            </div>
          </div>
          <div class="flex flex-col">
            <span class="font-display-hero text-2xl tracking-[0.14em] uppercase text-wonka-lounge font-semibold group-hover:text-black transition-colors">
              Wonka Bilbao
            </span>
            <span class="font-label-uppercase text-[10px] tracking-[0.26em] text-wonka-bar uppercase -mt-0.5 font-bold">
              Una marca · Tres experiencias
            </span>
          </div>
        </a>

        <!-- Desktop Navigation Links -->
        <nav class="hidden lg:flex items-center gap-8">
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
          <a class="font-label-uppercase text-[12px] tracking-[0.16em] text-on-surface-variant hover:text-wonka-lounge transition-colors uppercase py-1 relative group" href="#contacto">
            Contacto
            <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-wonka-lounge transition-all duration-300 group-hover:w-full"></span>
          </a>
        </nav>
      </div>

      <!-- Action Buttons -->
      <div class="flex items-center gap-4">
        <a class="hidden sm:inline-flex items-center justify-center font-label-uppercase text-[11px] uppercase tracking-[0.18em] font-bold px-6 py-3 border-2 border-wonka-bar text-wonka-bar hover:bg-wonka-bar hover:text-white rounded-full transition-all duration-300 shadow-sm" href="#celebraciones">
          Reservas &amp; Eventos
        </a>
        <a class="inline-flex items-center justify-center font-label-uppercase text-[11px] uppercase tracking-[0.18em] font-bold px-6 py-3 bg-wonka-lounge text-white rounded-full hover:bg-[#3D1768] hover:shadow-lg transition-all duration-300" href="#experiencias">
          Explorar
        </a>
      </div>
    </div>
  </header>

  <!-- ==================== MAIN CONTENT ==================== -->
  <main class="w-full pt-20">

    <!-- ==================== HERO SECTION ==================== -->
    <section class="w-full pt-16 pb-12 lg:pt-24 lg:pb-16 px-margin-mobile lg:px-margin-desktop bg-surface relative overflow-hidden">
      <!-- Background subtle atmospheric gradients -->
      <div class="absolute -top-24 right-1/4 w-96 h-96 rounded-full bg-wonka-bar/5 blur-3xl pointer-events-none"></div>
      <div class="absolute top-1/3 -left-20 w-80 h-80 rounded-full bg-wonka-lounge/5 blur-3xl pointer-events-none"></div>

      <div class="max-w-[1440px] mx-auto">
        <!-- Top Micro Tagline Strip -->
        <div class="flex flex-wrap items-center justify-between gap-4 mb-6 pb-4 border-b border-[#E6DFD0]">
          <div class="flex items-center gap-2">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-wonka-house ring-2 ring-wonka-house/20"></span>
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-wonka-lounge ring-2 ring-wonka-lounge/20"></span>
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-wonka-bar ring-2 ring-wonka-bar/20"></span>
            <span class="font-label-uppercase text-[11px] uppercase tracking-[0.24em] text-wonka-lounge font-bold ml-1">
              Bilbao · Sabores, Encuentros &amp; Carácter Propio
            </span>
          </div>
          <div class="flex items-center gap-2">
            <button onclick="toggleColorExperience('house')" class="px-3 py-1 rounded-full text-[11px] font-label-uppercase font-semibold tracking-wider bg-wonka-house-light text-wonka-house border border-wonka-house/30 hover:scale-105 transition-transform">
              House
            </button>
            <button onclick="toggleColorExperience('lounge')" class="px-3 py-1 rounded-full text-[11px] font-label-uppercase font-semibold tracking-wider bg-wonka-lounge-light text-wonka-lounge border border-wonka-lounge/30 hover:scale-105 transition-transform">
              Lounge
            </button>
            <button onclick="toggleColorExperience('bar')" class="px-3 py-1 rounded-full text-[11px] font-label-uppercase font-semibold tracking-wider bg-wonka-bar-light text-wonka-bar border border-wonka-bar/30 hover:scale-105 transition-transform">
              Bar
            </button>
          </div>
        </div>

        <!-- Editorial Hero Headline with Bespoke Wonka Hat Centerpiece -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-gutter-desktop items-end mb-12">
          <div class="lg:col-span-8">
            <h1 class="font-display-hero text-[44px] sm:text-[62px] lg:text-[76px] text-on-surface tracking-[-0.02em] leading-[1.03] uppercase font-normal select-none">
              UNA MARCA.<br />
              <span class="italic font-normal lowercase tracking-tight text-wonka-lounge font-display-hero inline-flex items-center gap-3 relative">
                <span>tres</span>
                
                <!-- HERO BESPOKE TOP HAT (Primary Characteristic Graphic Element) -->
                <span class="inline-block -mt-4 -ml-1 cursor-pointer" title="Wonka Bilbao — Haz clic para inclinar el sombrero" onclick="tipTheHat()">
                  <div class="w-16 h-16 sm:w-20 sm:h-20 lg:w-24 lg:h-24 animate-wonka-hat" id="hero-wonka-hat">
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
              <a class="inline-flex items-center justify-center font-label-uppercase text-[12px] uppercase tracking-[0.18em] font-bold px-7 py-4 bg-wonka-lounge text-white rounded-full hover:bg-[#3E166C] hover:shadow-xl transition-all duration-300" href="#experiencias">
                Descubre los espacios
              </a>
              <a class="inline-flex items-center gap-2 font-label-md text-[14px] font-semibold text-wonka-bar hover:text-wonka-lounge transition-colors group" href="#gastronomia">
                <span>Ver gastronomía</span>
                <span class="material-symbols-outlined text-[18px] group-hover:translate-x-1.5 transition-transform">east</span>
              </a>
            </div>
          </div>
        </div>

        <!-- Hero Visual: Shared Table Feast (Local high-res photography) -->
        <div class="relative w-full aspect-[16/9] lg:aspect-[21/9] min-h-[380px] bg-surface-container rounded-[32px] overflow-hidden shadow-[0_12px_40px_rgba(46,16,80,0.1)] border-2 border-[#E7DEC8] group">
          <img 
            alt="Mesa gastronómica compartida en Wonka Bilbao con pulpo, raciones, ibéricos, ensalada y vino" 
            class="w-full h-full object-cover object-center transform group-hover:scale-[1.02] transition-transform duration-1000 ease-out" 
            src="public/assets/images/mesa-compartida-hero.jpg" 
          />
          <div class="absolute inset-0 bg-gradient-to-t from-black/75 via-black/15 to-transparent pointer-events-none"></div>

          <!-- Corner Floating Brand Badge -->
          <div class="absolute top-5 right-5 hidden sm:flex items-center gap-2 bg-[#FDF9F0]/90 backdrop-blur-md px-4 py-2 rounded-full border border-wonka-bar/30 shadow-md">
            <span class="w-2.5 h-2.5 rounded-full bg-wonka-bar animate-ping"></span>
            <span class="font-label-uppercase text-[11px] font-bold text-wonka-lounge tracking-wider">Sabor &amp; Vida Bilbaína</span>
          </div>

          <!-- Bottom Narrative Ribbon -->
          <div class="absolute bottom-6 left-6 right-6 flex flex-wrap items-center justify-between text-white gap-3">
            <div class="flex items-center gap-3">
              <span class="font-label-uppercase text-[11px] tracking-[0.2em] uppercase backdrop-blur-md bg-wonka-lounge/85 px-4 py-2 rounded-full border border-wonka-bar/40 text-[#FAF3E3] font-bold shadow-md">
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

    <!-- ==================== DISCOVERY SELECTOR: ¿QUÉ PLAN BUSCAS HOY? ==================== -->
    <section class="w-full py-10 px-margin-mobile lg:px-margin-desktop bg-[#FAF6ED] border-y border-[#E6DFD0]" id="selector-plan">
      <div class="max-w-[1400px] mx-auto">
        <div class="p-6 sm:p-8 bg-surface rounded-3xl border border-[#DFD8C9] shadow-sm flex flex-col md:flex-row items-center justify-between gap-6">
          <div class="flex items-center gap-4">
            <div class="w-12 h-12 rounded-2xl bg-wonka-bar-light border border-wonka-bar/30 flex items-center justify-center text-wonka-bar shrink-0">
              <span class="material-symbols-outlined text-2xl">magic_button</span>
            </div>
            <div>
              <span class="font-label-uppercase text-[10px] tracking-[0.24em] text-wonka-bar uppercase font-bold block">Inspiración Wonka</span>
              <h2 class="font-headline-sm text-2xl text-on-surface font-normal">¿Qué plan buscas hoy en Bilbao?</h2>
            </div>
          </div>

          <!-- Interactive Plan Chips -->
          <div class="flex flex-wrap items-center gap-3 w-full md:w-auto">
            <button 
              id="plan-btn-house" 
              onclick="selectPlan('house')"
              class="flex-1 sm:flex-initial inline-flex items-center justify-center gap-2 px-5 py-3 rounded-full text-xs font-label-uppercase font-bold tracking-wider bg-surface border-2 border-wonka-house/30 text-wonka-house hover:bg-wonka-house hover:text-white transition-all shadow-sm"
            >
              <span class="w-2.5 h-2.5 rounded-full bg-wonka-house"></span>
              Comida &amp; Sobremesa
            </button>
            
            <button 
              id="plan-btn-lounge" 
              onclick="selectPlan('lounge')"
              class="flex-1 sm:flex-initial inline-flex items-center justify-center gap-2 px-5 py-3 rounded-full text-xs font-label-uppercase font-bold tracking-wider bg-surface border-2 border-wonka-lounge/30 text-wonka-lounge hover:bg-wonka-lounge hover:text-white transition-all shadow-sm"
            >
              <span class="w-2.5 h-2.5 rounded-full bg-wonka-lounge"></span>
              Cócteles &amp; Noche
            </button>

            <button 
              id="plan-btn-bar" 
              onclick="selectPlan('bar')"
              class="flex-1 sm:flex-initial inline-flex items-center justify-center gap-2 px-5 py-3 rounded-full text-xs font-label-uppercase font-bold tracking-wider bg-surface border-2 border-wonka-bar/30 text-wonka-bar hover:bg-wonka-bar hover:text-white transition-all shadow-sm"
            >
              <span class="w-2.5 h-2.5 rounded-full bg-wonka-bar"></span>
              Pintxos &amp; Barra Viva
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================== TRES EXPERIENCIAS ==================== -->
    <section class="w-full py-20 px-margin-mobile lg:px-margin-desktop experiencia-ambient-transition border-b border-[#E6DFD0]" id="experiencias" style="background-color: #FAF6ED;">
      <div class="max-w-[1400px] mx-auto">
        <!-- Section Header with Hat Watermark Motif -->
        <div class="flex flex-col md:flex-row md:items-end justify-between mb-16 pb-6 border-b border-[#E6DFD0] relative">
          <div>
            <div class="inline-flex items-center gap-2 mb-2">
              <span class="font-label-uppercase text-[11px] tracking-[0.26em] text-wonka-lounge uppercase font-bold">Universo Wonka Bilbao</span>
              <span class="text-wonka-bar font-bold">✦</span>
            </div>
            <h2 class="font-headline-lg text-[36px] lg:text-[48px] text-on-surface tracking-tight font-normal">
              Tres atmósferas complementarias
            </h2>
          </div>
          <p class="font-body-md text-on-surface-variant max-w-md mt-4 md:mt-0 font-light leading-relaxed">
            Una misma identidad acogedora con tres expresiones para cada momento del día: mesa reposada, coctelería nocturna y el pulso vibrante de barra.
          </p>
        </div>

        <!-- The 3 Cards Grid -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
          
          <!-- CARD 1: WONKA HOUSE (Olive Green Theme) -->
          <article 
            id="card-house"
            class="flex flex-col bg-surface rounded-3xl overflow-hidden border-2 border-wonka-house/30 shadow-sm hover:shadow-xl transition-all duration-300 group hover:-translate-y-1"
          >
            <!-- Colored Card Header Banner -->
            <div class="p-6 bg-gradient-to-r from-wonka-house to-[#333D29] text-white flex items-center justify-between">
              <div class="flex items-center gap-3.5">
                <div class="w-14 h-14 rounded-2xl overflow-hidden shadow-md shrink-0 border-2 border-white/20 bg-wonka-house">
                  <img alt="Logo Wonka House" class="w-full h-full object-cover" src="public/assets/logos/wonka-house-green.jpg" />
                </div>
                <div>
                  <span class="font-label-uppercase text-[10px] tracking-[0.24em] uppercase font-bold text-[#DDE7D3] block">01 · MESA &amp; SOBREMESA</span>
                  <h3 class="font-headline-sm text-[24px] tracking-wide text-white font-semibold">Wonka House</h3>
                </div>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-white/15 text-[11px] font-label-uppercase text-white border border-white/20">Calma</span>
            </div>

            <!-- Real Dish Imagery -->
            <div class="relative aspect-[4/3] w-full overflow-hidden bg-surface-container">
              <img 
                alt="Gastronomía Wonka para compartir en mesa" 
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out" 
                src="public/assets/images/ensalada-fresca.jpg" 
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
                <a class="inline-flex items-center justify-between w-full font-label-uppercase text-[12px] uppercase tracking-[0.18em] font-bold px-4 py-3 rounded-full text-wonka-house bg-wonka-house-light hover:bg-wonka-house hover:text-white transition-all group/btn" href="#celebraciones">
                  <span>Conocer Wonka House</span>
                  <span class="material-symbols-outlined text-[18px] group-hover/btn:translate-x-1 transition-transform">arrow_forward</span>
                </a>
              </div>
            </div>
          </article>

          <!-- CARD 2: WONKA LOUNGE (Deep Purple Theme) -->
          <article 
            id="card-lounge"
            class="flex flex-col bg-surface rounded-3xl overflow-hidden border-2 border-wonka-lounge/30 shadow-sm hover:shadow-xl transition-all duration-300 group hover:-translate-y-1"
          >
            <!-- Colored Card Header Banner -->
            <div class="p-6 bg-gradient-to-r from-wonka-lounge to-[#1C0633] text-white flex items-center justify-between">
              <div class="flex items-center gap-3.5">
                <div class="w-14 h-14 rounded-2xl overflow-hidden shadow-md shrink-0 border-2 border-white/20 bg-wonka-lounge">
                  <img alt="Logo Wonka Lounge" class="w-full h-full object-cover" src="public/assets/logos/wonka-lounge-purple.jpg" />
                </div>
                <div>
                  <span class="font-label-uppercase text-[10px] tracking-[0.24em] uppercase font-bold text-[#DEC6F5] block">02 · NOCTURNO &amp; CÓCTEL</span>
                  <h3 class="font-headline-sm text-[24px] tracking-wide text-white font-semibold">Wonka Lounge</h3>
                </div>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-white/15 text-[11px] font-label-uppercase text-white border border-white/20">Coctelería</span>
            </div>

            <!-- Real Dish Imagery -->
            <div class="relative aspect-[4/3] w-full overflow-hidden bg-surface-container">
              <img 
                alt="Gastronomía Wonka para veladas distendidas" 
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out" 
                src="public/assets/images/vieiras-horno.jpg" 
              />
              <div class="absolute bottom-3 left-3 bg-wonka-lounge/90 backdrop-blur-md px-3.5 py-1.5 rounded-full text-white text-[11px] font-label-uppercase uppercase tracking-wider font-semibold shadow-sm">
                Maridaje &amp; Copa Reposada
              </div>
            </div>

            <!-- Body Content -->
            <div class="p-7 flex flex-col flex-1 justify-between bg-surface">
              <div>
                <p class="font-body-md text-on-surface-variant leading-relaxed mb-6">
                  Atmósfera envolvente y distendida para alargar la tarde y la noche: cócteles de autor, copas reposadas y una acústica cuidada para conversar con calma.
                </p>
              </div>
              <div class="pt-4 border-t border-wonka-lounge/15">
                <a class="inline-flex items-center justify-between w-full font-label-uppercase text-[12px] uppercase tracking-[0.18em] font-bold px-4 py-3 rounded-full text-wonka-lounge bg-wonka-lounge-light hover:bg-wonka-lounge hover:text-white transition-all group/btn" href="#celebraciones">
                  <span>Conocer Wonka Lounge</span>
                  <span class="material-symbols-outlined text-[18px] group-hover/btn:translate-x-1 transition-transform">arrow_forward</span>
                </a>
              </div>
            </div>
          </article>

          <!-- CARD 3: WONKA BAR (Golden Ochre Theme) -->
          <article 
            id="card-bar"
            class="flex flex-col bg-surface rounded-3xl overflow-hidden border-2 border-wonka-bar/30 shadow-sm hover:shadow-xl transition-all duration-300 group hover:-translate-y-1"
          >
            <!-- Colored Card Header Banner -->
            <div class="p-6 bg-gradient-to-r from-wonka-bar to-[#664C1B] text-white flex items-center justify-between">
              <div class="flex items-center gap-3.5">
                <div class="w-14 h-14 rounded-2xl overflow-hidden shadow-md shrink-0 border-2 border-white/20 bg-wonka-bar">
                  <img alt="Logo Wonka Bar" class="w-full h-full object-cover" src="public/assets/logos/wonka-bar-gold.jpg" />
                </div>
                <div>
                  <span class="font-label-uppercase text-[10px] tracking-[0.24em] uppercase font-bold text-[#FDE5B5] block">03 · ORIGEN &amp; PICOTEO</span>
                  <h3 class="font-headline-sm text-[24px] tracking-wide text-white font-semibold">Wonka Bar</h3>
                </div>
              </div>
              <span class="px-2.5 py-1 rounded-full bg-white/15 text-[11px] font-label-uppercase text-white border border-white/20">Barra Viva</span>
            </div>

            <!-- Real Dish Imagery -->
            <div class="relative aspect-[4/3] w-full overflow-hidden bg-surface-container">
              <img 
                alt="Tequeños y raciones para picar en Wonka Bar" 
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out" 
                src="public/assets/images/tequenos-raciones.jpg" 
              />
              <div class="absolute bottom-3 left-3 bg-wonka-bar/90 backdrop-blur-md px-3.5 py-1.5 rounded-full text-white text-[11px] font-label-uppercase uppercase tracking-wider font-semibold shadow-sm">
                Pintxos, Raciones &amp; Encuentros
              </div>
            </div>

            <!-- Body Content -->
            <div class="p-7 flex flex-col flex-1 justify-between bg-surface">
              <div>
                <p class="font-body-md text-on-surface-variant leading-relaxed mb-6">
                  El pulso más vibrante y espontáneo: barra repleta de pintxos, tequeños dorados, raciones generosas para picar, comidas informales y celebraciones compartidas con amigos.
                </p>
              </div>
              <div class="pt-4 border-t border-wonka-bar/15">
                <a class="inline-flex items-center justify-between w-full font-label-uppercase text-[12px] uppercase tracking-[0.18em] font-bold px-4 py-3 rounded-full text-wonka-bar bg-wonka-bar-light hover:bg-wonka-bar hover:text-white transition-all group/btn" href="#celebraciones">
                  <span>Conocer Wonka Bar</span>
                  <span class="material-symbols-outlined text-[18px] group-hover/btn:translate-x-1 transition-transform">arrow_forward</span>
                </a>
              </div>
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- ==================== GASTRONOMÍA WONKA ==================== -->
    <section class="w-full py-24 px-margin-mobile lg:px-margin-desktop bg-surface" id="gastronomia">
      <div class="max-w-[1400px] mx-auto">
        <!-- Editorial Intro with Charismatic Flourish -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-end mb-16 pb-8 border-b border-[#E6DFD0]">
          <div class="lg:col-span-7">
            <div class="inline-flex items-center gap-2 mb-3 px-3 py-1 rounded-full bg-wonka-bar-light border border-wonka-bar/30 text-wonka-bar text-[11px] font-label-uppercase font-bold tracking-wider">
              <span>✦ Carta &amp; Tradición Compartida</span>
            </div>
            <h2 class="font-headline-lg text-[36px] sm:text-[46px] text-on-surface tracking-tight font-normal leading-[1.12]">
              Comida honesta, raciones generosas y sabor bilbaíno.
            </h2>
          </div>
          <div class="lg:col-span-5">
            <p class="font-body-lg text-[16px] text-on-surface-variant font-light leading-relaxed">
              Sin artificios ni recetas rebuscadas: producto seleccionado, platos recién cocinados y raciones generosas pensadas para poner al centro de la mesa y disfrutar.
            </p>
          </div>
        </div>

        <!-- Bento Grid of Real Gastronomy -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 mb-16">
          
          <!-- Left Column: Octopus & Classics -->
          <div class="lg:col-span-7 space-y-8">
            <!-- Featured: Pulpo a la Gallega -->
            <div class="bg-surface-container-low rounded-3xl overflow-hidden border border-[#E6DFD0] shadow-sm hover:shadow-md transition-shadow group">
              <div class="relative aspect-[16/10] w-full overflow-hidden bg-surface-container">
                <img 
                  alt="Pulpo a la gallega sobre plato de madera y pimentón" 
                  class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" 
                  src="public/assets/images/pulpo-gallega.jpg" 
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
              <div class="bg-surface-container-low rounded-3xl overflow-hidden border border-[#E6DFD0] shadow-sm p-4 hover:shadow-md transition-shadow">
                <div class="relative aspect-square w-full rounded-2xl overflow-hidden mb-4 bg-surface-container">
                  <img 
                    alt="Croqueta crujiente recién hecha" 
                    class="w-full h-full object-cover hover:scale-105 transition-transform duration-500" 
                    src="public/assets/images/croqueta-crujiente.jpg" 
                  />
                  <span class="absolute top-2.5 right-2.5 bg-black/60 backdrop-blur-md text-white px-2.5 py-1 rounded-full text-[10px] font-label-uppercase tracking-wider font-semibold">
                    Receta Casera
                  </span>
                </div>
                <h4 class="font-title-md text-[18px] font-semibold text-on-surface mb-1">Croquetas crujientes</h4>
                <p class="font-body-sm text-on-surface-variant leading-relaxed">
                  Bechamel melosa, rebozado dorado y crujiente para disfrutar de un bocado caliente en cualquier momento.
                </p>
              </div>

              <!-- Gambas con limón -->
              <div class="bg-surface-container-low rounded-3xl overflow-hidden border border-[#E6DFD0] shadow-sm p-4 hover:shadow-md transition-shadow">
                <div class="relative aspect-square w-full rounded-2xl overflow-hidden mb-4 bg-surface-container">
                  <img 
                    alt="Gambas a la plancha recién hechas con limón" 
                    class="w-full h-full object-cover hover:scale-105 transition-transform duration-500" 
                    src="public/assets/images/gambas-plancha.jpg" 
                  />
                  <span class="absolute top-2.5 right-2.5 bg-black/60 backdrop-blur-md text-white px-2.5 py-1 rounded-full text-[10px] font-label-uppercase tracking-wider font-semibold">
                    A la Plancha
                  </span>
                </div>
                <h4 class="font-title-md text-[18px] font-semibold text-on-surface mb-1">Gambas con limón</h4>
                <p class="font-body-sm text-on-surface-variant leading-relaxed">
                  Punto jugoso, toque de cítrico recién exprimido y el aroma inconfundible de marisco fresco.
                </p>
              </div>
            </div>
          </div>

          <!-- Right Column: Burguer & Tablas de Ibéricos -->
          <div class="lg:col-span-5 space-y-8">
            <!-- Burger Feature -->
            <div class="bg-surface-container-low rounded-3xl overflow-hidden border border-[#E6DFD0] shadow-sm hover:shadow-md transition-shadow group">
              <div class="relative aspect-[4/3] w-full overflow-hidden bg-surface-container">
                <img 
                  alt="Hamburguesa Wonka con huevo campero y patatas caseras" 
                  class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700" 
                  src="public/assets/images/hamburguesa-completa.jpg" 
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
            <div class="bg-surface-container-low rounded-3xl p-6 border-2 border-wonka-house/20 shadow-sm hover:shadow-md transition-shadow">
              <div class="relative aspect-[16/10] w-full rounded-2xl overflow-hidden mb-5">
                <img 
                  alt="Tabla de embutidos ibéricos y quesos artesanos" 
                  class="w-full h-full object-cover hover:scale-105 transition-transform duration-700" 
                  src="public/assets/images/tabla-ibericos.jpg" 
                />
                <div class="absolute bottom-2.5 left-2.5 bg-wonka-house/90 backdrop-blur-md px-3 py-1 rounded-full text-white text-[10px] font-label-uppercase uppercase tracking-wider font-bold">
                  Corte Tradicional
                </div>
              </div>
              <div class="flex items-center justify-between mb-2">
                <h4 class="font-title-md text-[19px] font-semibold text-on-surface">Tablas de Ibéricos y Quesos</h4>
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
          <div class="bg-surface-container-low rounded-3xl p-6 border border-[#E6DFD0] flex flex-col sm:flex-row items-center gap-6 shadow-sm">
            <div class="w-full sm:w-44 h-44 rounded-2xl overflow-hidden shrink-0 bg-surface-container">
              <img alt="Gyozas al vapor en bambú" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500" src="public/assets/images/gyozas-vapor.jpg" />
            </div>
            <div>
              <span class="font-label-uppercase text-[10px] tracking-wider text-wonka-bar font-bold uppercase">Toque de Fusión</span>
              <h4 class="font-headline-sm text-xl text-on-surface font-semibold mb-1">Gyozas al vapor</h4>
              <p class="font-body-sm text-on-surface-variant leading-relaxed">
                Masa fina cocida al vapor en bambú tradicional, relleno sabroso y salsa de soja para acompañar con un buen vino tinto.
              </p>
            </div>
          </div>

          <div class="bg-surface-container-low rounded-3xl p-6 border border-[#E6DFD0] flex flex-col sm:flex-row items-center gap-6 shadow-sm">
            <div class="w-full sm:w-44 h-44 rounded-2xl overflow-hidden shrink-0 bg-surface-container">
              <img alt="Tequeños dorados en tabla de madera" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500" src="public/assets/images/tequenos-tabla.jpg" />
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
        <div class="p-8 md:p-12 bg-gradient-to-br from-surface-container via-[#FAF5EB] to-surface-container rounded-3xl border-2 border-[#E6DFD0] grid grid-cols-1 md:grid-cols-3 gap-8 shadow-sm">
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

    <!-- ==================== CELEBRACIONES & ENCUENTROS ==================== -->
    <section class="w-full py-24 px-margin-mobile lg:px-margin-desktop bg-surface-container-low border-t border-[#E6DFD0]" id="celebraciones">
      <div class="max-w-[1400px] mx-auto">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
          
          <!-- Left Column: Celebra en Wonka Proposition -->
          <div class="lg:col-span-6 flex flex-col">
            <div class="inline-flex items-center gap-2 mb-2">
              <span class="font-label-uppercase text-[11px] tracking-[0.26em] text-wonka-bar uppercase font-bold">Grupos &amp; Momentos Especiales</span>
              <span class="text-wonka-lounge">★</span>
            </div>
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
            <div class="bg-surface rounded-3xl p-6 border-2 border-wonka-bar/30 shadow-md mb-8 flex items-center gap-5">
              <div class="w-24 h-32 rounded-2xl overflow-hidden shrink-0 shadow-sm border border-[#E6DFD0]">
                <img alt="Póster oficial Wonka Bilbao: Una marca, tres experiencias" class="w-full h-full object-cover" src="public/assets/brand/poster-tres-experiencias.jpg" />
              </div>
              <div>
                <span class="font-label-uppercase text-[10px] tracking-[0.24em] text-wonka-bar font-bold uppercase block mb-1">Concepto Integral</span>
                <h4 class="font-headline-sm text-lg text-wonka-lounge font-semibold mb-1">Una marca. Tres experiencias.</h4>
                <p class="font-body-sm text-on-surface-variant text-xs leading-relaxed">
                  Combina mesa en Wonka House, brindis en Wonka Bar o cócteles nocturnos en Wonka Lounge en una misma celebración.
                </p>
              </div>
            </div>

            <!-- Bullet points -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div class="flex items-start gap-3 p-3.5 rounded-2xl bg-surface border border-[#E6DFD0]">
                <span class="material-symbols-outlined text-wonka-house text-[22px] shrink-0 mt-0.5">restaurant</span>
                <div>
                  <h4 class="font-title-md text-[14px] font-semibold text-on-surface">Menús para Compartir</h4>
                  <p class="font-body-sm text-[12px] text-on-surface-variant">Raciones al centro para grupos.</p>
                </div>
              </div>
              <div class="flex items-start gap-3 p-3.5 rounded-2xl bg-surface border border-[#E6DFD0]">
                <span class="material-symbols-outlined text-wonka-lounge text-[22px] shrink-0 mt-0.5">local_bar</span>
                <div>
                  <h4 class="font-title-md text-[14px] font-semibold text-on-surface">Zonas Reservadas</h4>
                  <p class="font-body-sm text-[12px] text-on-surface-variant">Espacios adaptables a tu plan.</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Right Column: Demonstrative Booking Form -->
          <div class="lg:col-span-6" id="contacto">
            <div class="p-8 sm:p-10 bg-surface rounded-[32px] border-2 border-[#E6DFD0] shadow-xl relative overflow-hidden">
              <div class="mb-6">
                <span class="font-label-uppercase text-[11px] uppercase tracking-[0.22em] text-wonka-bar font-bold block mb-1">
                  Reserva Demostrativa
                </span>
                <h3 class="font-headline-sm text-2xl text-on-surface font-semibold">
                  Cuéntanos tu celebración
                </h3>
                <p class="font-body-sm text-on-surface-variant mt-1">
                  Prueba la experiencia de solicitud para comprobar la respuesta en esta demo comercial.
                </p>
              </div>

              <form id="wonka-demo-form" onsubmit="handleDemoSubmit(event)" class="space-y-4">
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div class="flex flex-col space-y-1.5">
                    <label class="font-label-uppercase text-[11px] uppercase tracking-wider text-on-surface font-bold">Nombre</label>
                    <input class="w-full bg-[#FAF6EE] px-4 py-3 rounded-xl border border-[#D5CEBF] text-on-surface text-body-md focus:outline-none focus:border-wonka-lounge focus:ring-2 focus:ring-wonka-lounge/10 transition-all" placeholder="Ej. Ainhoa García" required type="text" id="demo-name" />
                  </div>
                  <div class="flex flex-col space-y-1.5">
                    <label class="font-label-uppercase text-[11px] uppercase tracking-wider text-on-surface font-bold">Teléfono</label>
                    <input class="w-full bg-[#FAF6EE] px-4 py-3 rounded-xl border border-[#D5CEBF] text-on-surface text-body-md focus:outline-none focus:border-wonka-lounge focus:ring-2 focus:ring-wonka-lounge/10 transition-all" placeholder="Ej. 612 345 678" required type="tel" id="demo-phone" />
                  </div>
                </div>

                <div class="flex flex-col space-y-1.5">
                  <label class="font-label-uppercase text-[11px] uppercase tracking-wider text-on-surface font-bold">Espacio preferido</label>
                  <select id="demo-space" class="w-full bg-[#FAF6EE] px-4 py-3 rounded-xl border border-[#D5CEBF] text-on-surface text-body-md focus:outline-none focus:border-wonka-lounge focus:ring-2 focus:ring-wonka-lounge/10 transition-all">
                    <option value="Wonka Bar (Pintxos & Raciones de barra)">Wonka Bar (Pintxos &amp; Raciones de barra)</option>
                    <option value="Wonka House (Comida reposada en mesa)">Wonka House (Comida reposada en mesa)</option>
                    <option value="Wonka Lounge (Copas & Cócteles de noche)">Wonka Lounge (Copas &amp; Cócteles de noche)</option>
                    <option value="Celebración Combinada (Varios espacios)">Celebración Combinada (Varios espacios)</option>
                  </select>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div class="flex flex-col space-y-1.5">
                    <label class="font-label-uppercase text-[11px] uppercase tracking-wider text-on-surface font-bold">Fecha orientativa</label>
                    <input class="w-full bg-[#FAF6EE] px-4 py-3 rounded-xl border border-[#D5CEBF] text-on-surface text-body-md focus:outline-none focus:border-wonka-lounge focus:ring-2 focus:ring-wonka-lounge/10 transition-all" type="date" id="demo-date" />
                  </div>
                  <div class="flex flex-col space-y-1.5">
                    <label class="font-label-uppercase text-[11px] uppercase tracking-wider text-on-surface font-bold">Número de personas</label>
                    <select id="demo-guests" class="w-full bg-[#FAF6EE] px-4 py-3 rounded-xl border border-[#D5CEBF] text-on-surface text-body-md focus:outline-none focus:border-wonka-lounge focus:ring-2 focus:ring-wonka-lounge/10 transition-all">
                      <option>2 a 4 personas</option>
                      <option>5 a 8 personas</option>
                      <option>9 a 15 personas</option>
                      <option>Más de 15 personas (Grupo grande)</option>
                    </select>
                  </div>
                </div>

                <div class="flex flex-col space-y-1.5">
                  <label class="font-label-uppercase text-[11px] uppercase tracking-wider text-on-surface font-bold">Comentarios o preferencia</label>
                  <textarea class="w-full bg-[#FAF6EE] px-4 py-3 rounded-xl border border-[#D5CEBF] text-on-surface text-body-md focus:outline-none focus:border-wonka-lounge focus:ring-2 focus:ring-wonka-lounge/10 transition-all resize-none" placeholder="¿Tienes algún detalle o preferencia especial?" rows="2"></textarea>
                </div>

                <button class="w-full inline-flex items-center justify-center gap-2 font-label-uppercase text-[12px] uppercase tracking-[0.2em] font-bold px-8 py-4 bg-wonka-lounge text-white rounded-full hover:bg-[#3D1768] hover:shadow-[0_6px_20px_rgba(46,16,80,0.3)] transition-all duration-300 mt-2" type="submit">
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
  <div id="demo-modal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm hidden opacity-0 transition-opacity duration-300 p-4">
    <div class="bg-surface rounded-3xl max-w-md w-full p-8 border-2 border-wonka-bar shadow-2xl transform scale-95 transition-transform duration-300 relative text-center" id="demo-modal-box">
      <div class="w-16 h-16 rounded-full bg-wonka-bar-light border border-wonka-bar/30 flex items-center justify-center mx-auto mb-4 text-wonka-bar">
        <span class="material-symbols-outlined text-3xl">celebration</span>
      </div>
      <h3 class="font-headline-sm text-2xl text-on-surface font-semibold mb-2" id="modal-title">¡Solicitud Demostrativa!</h3>
      <p class="font-body-md text-on-surface-variant mb-6" id="modal-message">
        Tu consulta ha sido simulada correctamente para Wonka Bilbao.
      </p>
      <button onclick="closeDemoModal()" class="inline-flex items-center justify-center font-label-uppercase text-[12px] uppercase tracking-widest font-bold px-8 py-3.5 bg-wonka-lounge text-white rounded-full hover:bg-wonka-lounge-dark transition-all">
        Entendido
      </button>
    </div>
  </div>

  <!-- ==================== FOOTER ==================== -->
  <footer class="w-full bg-[#F5EFE3] border-t border-[#E6DFD0] pt-16 pb-12">
    <div class="w-full px-margin-mobile lg:px-margin-desktop max-w-[1400px] mx-auto">
      <div class="grid grid-cols-1 md:grid-cols-12 gap-10 pb-12 border-b border-[#E6DFD0]">
        
        <!-- Brand Summary -->
        <div class="md:col-span-5 flex flex-col justify-between space-y-4">
          <div>
            <div class="flex items-center gap-3 mb-2">
              <span class="font-display-hero text-2xl tracking-[0.12em] uppercase text-wonka-lounge font-bold">
                Wonka Bilbao
              </span>
              <div class="w-6 h-6 transform -rotate-6">
                {svg_hat}
              </div>
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
            <a class="inline-flex items-center gap-2 font-label-uppercase text-[11px] uppercase tracking-[0.16em] font-bold px-5 py-2.5 rounded-full border-2 border-wonka-lounge text-wonka-lounge hover:bg-wonka-lounge hover:text-white transition-all shadow-sm" href="#celebraciones">
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

  <!-- ==================== JAVASCRIPT INTERACTIONS ==================== -->
  <script>
    // 1. Hat Tilt Interaction
    function tipTheHat() {{
      const hat = document.getElementById('hero-wonka-hat');
      if (!hat) return;
      hat.style.transform = 'translateY(-22px) rotate(-18deg) scale(1.22)';
      setTimeout(() => {{
        hat.style.transform = '';
      }}, 700);
    }}

    // 2. Experiential Ambient Color Transitions
    const colorThemes = {{
      'house': {{ bg: '#EDF3E7', border: '#4E5B3F' }},
      'lounge': {{ bg: '#F2EBF7', border: '#2E1050' }},
      'bar': {{ bg: '#FAF2E1', border: '#8D6A2A' }},
      'default': {{ bg: '#FAF6ED', border: '#E6DFD0' }}
    }};

    function toggleColorExperience(experience) {{
      const sec = document.getElementById('experiencias');
      if (!sec) return;
      
      const theme = colorThemes[experience] || colorThemes['default'];
      sec.style.backgroundColor = theme.bg;

      // Focus card
      ['house', 'lounge', 'bar'].forEach(exp => {{
        const card = document.getElementById('card-' + exp);
        if (card) {{
          if (exp === experience) {{
            card.classList.add('card-focused');
            card.style.setProperty('--focus-color', theme.border);
          }} else {{
            card.classList.remove('card-focused');
          }}
        }}
      }});
    }}

    // 3. Plan Discovery Selection
    function selectPlan(plan) {{
      toggleColorExperience(plan);

      // Scroll to experiences section smoothly
      const expSec = document.getElementById('experiencias');
      if (expSec) {{
        expSec.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
      }}

      // Highlight corresponding discovery chip
      ['house', 'lounge', 'bar'].forEach(p => {{
        const btn = document.getElementById('plan-btn-' + p);
        if (btn) {{
          if (p === plan) {{
            btn.classList.add('ring-2', 'ring-offset-2');
          }} else {{
            btn.classList.remove('ring-2', 'ring-offset-2');
          }}
        }}
      }});
    }}

    // 4. Demonstrative Form Handler
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
        setTimeout(() => {{
          modal.classList.remove('opacity-0');
          modalBox.classList.remove('scale-95');
          modalBox.classList.add('scale-100');
        }}, 10);
      }}
    }}

    function closeDemoModal() {{
      const modal = document.getElementById('demo-modal');
      const modalBox = document.getElementById('demo-modal-box');
      if (modal && modalBox) {{
        modal.classList.add('opacity-0');
        modalBox.classList.remove('scale-100');
        modalBox.classList.add('scale-95');
        setTimeout(() => {{
          modal.classList.add('hidden');
        }}, 300);
      }}
    }}
  </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Successfully generated index.html with {len(html_content)} characters")
